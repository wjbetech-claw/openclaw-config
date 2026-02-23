---
name: openclaw-setup
description: Initialize and manage the OpenClaw infra repository skeleton, CI, and basic Terraform layout. Use when preparing a new infrastructure repo, generating safe .gitignore entries, and creating initial GitHub Actions workflows.
---

# openclaw-setup skill

This skill provides the minimal, repeatable steps and templates used when bootstrapping an OpenClaw infrastructure repository.

What it provides
- Templates: .gitignore, LICENSE (MIT), README, basic GitHub Actions workflow
- Terraform skeleton under infra/terraform
- Guidance for safe handling of secrets and tokens

When to use
- Use this skill when asked to create or update the repository skeleton for infrastructure (new repo bootstraps, CI plumbing, contributor guidance).

Resources
- scripts/push-setup.sh — one-way push procedure (do not change remotes or use gh; use this script to commit and push)
- infra/terraform/main.tf — placeholder Terraform layout

Usage notes
- Never commit private keys, .env files, or credential files. Ensure .gitignore contains patterns for .env, *.pem, *.key, and secret directories.
- Prefer GitHub Secrets or a secret manager for CI credentials.
