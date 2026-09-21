#!/usr/bin/env python3
"""Contract tests for AgentBody SEO search-volume client."""

import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import urllib.error


MODULE_PATH = Path(__file__).with_name("seo_client.py")
SPEC = importlib.util.spec_from_file_location("seo_client", MODULE_PATH)
assert SPEC and SPEC.loader
seo_client = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(seo_client)


class SEOClientContractTests(unittest.TestCase):
    def test_loads_persistent_agentbody_key(self):
        with tempfile.TemporaryDirectory() as home:
            credentials = Path(home) / ".agentbody" / "credentials"
            credentials.parent.mkdir()
            credentials.write_text("AGENTBODY_API_KEY=saved-key\n", encoding="utf-8")
            with patch.dict(os.environ, {}, clear=True), patch("os.path.expanduser", return_value=home):
                self.assertEqual(seo_client.resolve_api_key(), "saved-key")

    def test_local_credentials_override_process_environment(self):
        with tempfile.TemporaryDirectory() as home:
            credentials = Path(home) / ".agentbody" / "credentials"
            credentials.parent.mkdir()
            credentials.write_text("AGENTBODY_API_KEY=local-key\n", encoding="utf-8")
            with patch.dict(os.environ, {"AGENTBODY_API_KEY": "agent-key"}, clear=True), patch("os.path.expanduser", return_value=home):
                self.assertEqual(seo_client.resolve_api_key(), "local-key")

    def test_builds_agentbody_search_volume_query(self):
        client = seo_client.AgentBodySEOClient("key")
        captured = []
        client._request = lambda params: captured.append(params) or {"items": []}
        client.search_volume("ai agents", 2840, "en", True, "search_volume")
        self.assertEqual(captured, [{
            "keyword": "ai agents",
            "location_code": 2840,
            "language_code": "en",
            "search_partners": True,
            "sort_by": "search_volume",
        }])

    def test_maps_account_errors(self):
        client = seo_client.AgentBodySEOClient("key")
        with patch("urllib.request.urlopen", side_effect=urllib.error.HTTPError("url", 402, "Payment Required", {}, None)):
            result = client.search_volume("ai agents")
        self.assertEqual(result["error"]["code"], "INSUFFICIENT_BALANCE")
        self.assertIn("https://agentbody.io/console/billing", result["error"]["message"])


if __name__ == "__main__":
    unittest.main()
