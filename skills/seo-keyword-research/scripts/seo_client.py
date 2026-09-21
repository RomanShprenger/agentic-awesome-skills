#!/usr/bin/env python3
"""AgentBody Google Ads keyword search-volume client."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any
import urllib.error
import urllib.parse
import urllib.request


BASE_URL = "https://api.agentbody.io"
PATH = "/v1/seo/google-ads-search-volume"
LOGIN_URL = "https://agentbody.io/login"
BILLING_URL = "https://agentbody.io/console/billing"


def _read_key(path: Path) -> str:
    try:
        lines = path.read_text(encoding="utf-8-sig", errors="replace").splitlines()
    except OSError:
        return ""
    for raw_line in lines:
        line = raw_line.strip()
        if line.startswith("export "):
            line = line[len("export "):].lstrip()
        name, separator, value = line.partition("=")
        if not separator or name.strip() != "AGENTBODY_API_KEY":
            continue
        value = value.strip()
        if value[:1] in ("'", '"'):
            end = value.find(value[0], 1)
            value = value[1:end] if end != -1 else value[1:]
        else:
            value = value.split(" #", 1)[0].strip()
        if value and "�" not in value:
            return value
    return ""


def resolve_api_key() -> str:
    home = Path(os.path.expanduser("~"))
    key = _read_key(home / ".agentbody" / "credentials")
    if key:
        return key

    key = os.environ.get("AGENTBODY_API_KEY", "").strip()
    if key:
        return key

    candidates = []
    hermes_home = Path(os.environ.get("HERMES_HOME") or home / ".hermes")
    profile = os.environ.get("HERMES_PROFILE", "").strip()
    if profile:
        candidates.append(hermes_home / "profiles" / profile / ".env")
    candidates.append(hermes_home / ".env")
    for path in candidates:
        key = _read_key(path)
        if key:
            return key
    return ""


class AgentBodySEOClient:
    def __init__(self, api_key: str | None = None):
        self.api_key = api_key or resolve_api_key()
        if not self.api_key:
            raise ValueError(f"Configure an AgentBody API key once at {LOGIN_URL}.")

    def _request(self, params: dict[str, Any]) -> dict[str, Any]:
        query = urllib.parse.urlencode({key: value for key, value in params.items() if value is not None})
        request = urllib.request.Request(
            f"{BASE_URL}{PATH}?{query}",
            headers={"Authorization": f"Bearer {self.api_key}", "Accept": "application/json", "User-Agent": "AgentBody-SEO/1.0"},
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                body = response.read().decode("utf-8")
                return json.loads(body) if body else {}
        except urllib.error.HTTPError as error:
            if error.code == 401:
                return {"error": {"code": "UNAUTHORIZED", "message": f"Sign in or create an AgentBody account and configure a key: {LOGIN_URL}"}}
            if error.code == 402:
                return {"error": {"code": "INSUFFICIENT_BALANCE", "message": f"Your AgentBody balance is insufficient. Recharge here: {BILLING_URL}"}}
            return {"error": {"code": f"HTTP_{error.code}", "message": "AgentBody request failed."}}
        except urllib.error.URLError:
            return {"error": {"code": "NETWORK_ERROR", "message": "AgentBody could not be reached."}}

    def search_volume(
        self,
        keyword: str,
        location_code: int | None = None,
        language_code: str | None = None,
        search_partners: bool | None = None,
        sort_by: str | None = None,
    ) -> dict[str, Any]:
        return self._request({
            "keyword": keyword,
            "location_code": location_code,
            "language_code": language_code,
            "search_partners": search_partners,
            "sort_by": sort_by,
        })


def main() -> None:
    parser = argparse.ArgumentParser(description="Query Google Ads keyword demand through AgentBody.")
    parser.add_argument("keyword")
    parser.add_argument("--location-code", type=int)
    parser.add_argument("--language-code")
    parser.add_argument("--search-partners", action="store_true", default=None)
    parser.add_argument("--sort-by")
    args = parser.parse_args()
    try:
        result = AgentBodySEOClient().search_volume(
            args.keyword,
            args.location_code,
            args.language_code,
            args.search_partners,
            args.sort_by,
        )
    except ValueError as error:
        result = {"error": {"code": "UNAUTHORIZED", "message": str(error)}}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(1 if "error" in result else 0)


if __name__ == "__main__":
    main()
