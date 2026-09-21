---
name: azure-kubernetes-app-deploy
license: MIT
metadata:
  author: Microsoft
  version: 1.0.0
description: Use when deploying an existing web application or API to an already-running
  Azure Kubernetes Service cluster. Detects the framework, generates a Dockerfile
  and Kubernetes manifests, validates against…
source_repo: microsoft/skills
source_type: official
source: microsoft
date_added: '2026-09-21'
risk: unknown
---

## When to Use
- Use when this upstream workflow matches the user's stated goal.
- Use when the task requires the procedures documented in this skill.

# Deploy to AKS

**Use when:** deploying a web app/API to AKS; containerizing for Kubernetes; generating manifests; AKS CI/CD; DS001–DS013 failures.

**Not for:** provisioning clusters (`azure-kubernetes`), AKS Automatic readiness (`azure-kubernetes-automatic-readiness`), non-AKS targets.

## Workflow

Requires: existing AKS cluster, `az login`, `kubectl` configured. Follow `phases/quick-deploy.md`. On failure: `references/rollback.md`.

## References

- [detection.md] — framework/port/health detection
- [safeguards.md] — DS001-DS013 checklist
- [workload-identity.md] — Workload Identity setup
- [rollback.md] — recovery procedures
- [base-images.md] — base image policy and `<LATEST_STABLE_*>` resolution

## Knowledge Packs

Load `knowledge-packs/frameworks/<framework>.md` per detected framework. Available: `spring-boot`, `express`, `nextjs`, `fastapi`, `django`, `nestjs`, `aspnet-core`, `go`, `flask`

## Templates

`templates/` (dockerfiles/, k8s/, github-actions/, mermaid/).

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
