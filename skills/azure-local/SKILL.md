---
name: azure-local
description: 'Plan, deploy, operate, and troubleshoot Azure Local (formerly Azure
  Stack HCI): sizing and prerequisites, Arc registration, lifecycle updates, workloads
  (Azure Local VMs, AKS on Azure Local, images,…'
license: MIT
metadata:
  author: Microsoft
  version: 1.0.1
source_repo: microsoft/skills
source_type: official
source: microsoft
date_added: '2026-09-21'
risk: unknown
---

# Azure Local

## Quick Reference

| Property | Value |
| --- | --- |
| Best for | Azure Local planning, deployment, operations, workloads |
| MCP Tools | Generic Azure MCP tools only; no Azure Local namespace |
| CLI | `az graph query`, `az resource show`, Azure Local PowerShell |
| Related skills | azure-compute (public VMs), azure-kubernetes (public AKS) |

## When to Use This Skill

Use for Azure Local, Azure Stack HCI, Azure Local VMs, AKS on Azure Local, AKS hybrid, SDN, lifecycle updates, disconnected sites, or troubleshooting. Covers standard deployments (1-16 node hyperconverged, up to 64 disaggregated) and rack-aware clusters.

Do not use for cloud VM or public AKS guidance, or for **multi-rack (rack scale)** deployments — those use a separate control plane and procedure set. Hand off to the `azure-local-multi-rack` skill.

## MCP Tools

Azure Local has no dedicated MCP namespace. Use generic Azure MCP tools: `mcp_azure_mcp_extension_cli_generate` (ARG/CLI inventory), `mcp_azure_mcp_monitor` (needs Log Analytics), `mcp_azure_mcp_resourcehealth` (partial; not local cluster health), `mcp_azure_mcp_documentation` (pass the user's version when known).

Scope and limitations: [mcp-and-cli-tools].

## Workflow

0. Confirm deployment scale. If the user mentions multi-rack, aggregation racks, Network Fabric Controller, Cluster Manager, or `Microsoft.NetworkCloud` resources, stop and use the `azure-local-multi-rack` skill instead.
1. Deploy -> [plan-and-deploy
2. Operate/update -> [operate-and-update
3. VMs, AKS, images, disks, networks -> [workload-management
4. SDN, NSG, load balancer, gateway -> [networking-and-security
5. Failures -> [troubleshooting

Read the matched workflow first and use [docs-map]. Start read-only. Ask before updates, deletes, reimages, network changes, VM power/delete operations, or Arc bridge/custom location changes.

## Error Handling

| Scenario | Remediation |
| --- | --- |
| Scale unknown | Ask whether the deployment is standard or multi-rack before giving procedures. |
| Multi-rack detected | Hand off to the `azure-local-multi-rack` skill; these procedures do not apply. |
| Version unknown | Ask for the Azure Local version, or use latest docs. |
| Risky change detected | Stop and follow [safety-rules]. |
| No local access | Stay with Azure control-plane checks only. |
| Doc URL 404/redirect | Search Learn for the article title with the user's version. |

## Limitations

- Imported upstream skill; verify credentials, permissions, and safety boundaries before execution.
- Does not replace environment-specific validation, testing, or maintainer review.
