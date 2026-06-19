# Changelog

All notable changes to `solana-indexer-skill` are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Planned
- Golden test fixtures (real mainnet transactions, requires a Helius key)
- Animated demo / screenshots of `/build-indexer` in action
- Webhook secret rotation playbook
- Prometheus example config + Grafana dashboard JSON
- Litestream / pg-backup example for indexer DBs
- Chaos test suite as a separate npm script

## [0.1.0] - 2026-06-19

### Added
- 9 reference files in `skill/references/`:
  - `indexer-architecture.md` — decision tree for ingestion method
  - `geyser-plugins.md` — Yellowstone gRPC + Geyser plugin authoring
  - `postgres-schemas.md` — schemas for swaps, NFTs, pools, vaults
  - `backfill-strategies.md` — historical data replay + checkpointing
  - `real-time-streaming.md` — WebSocket + gRPC patterns, reconnect/dedup
  - `cost-optimization.md` — RPC cost reduction, provider comparison
  - `testing-indexers.md` — LiteSVM, Surfpool, golden tests, chaos
  - `production-ops.md` — health, metrics, alerts, on-call playbooks
  - `resources.md` — verified program IDs, official repos
- 3 working examples in `skill/examples/`:
  - `minimal-indexer-ts/` — 100-line Helius webhook → Postgres indexer (TypeScript, `tsc --noEmit` clean)
  - `geyser-plugin/skeleton/` — Rust Geyser plugin skeleton (Rust, `cargo check` clean)
  - `subgraph-template/` — The Graph on Solana (manifest + schema + mapping)
- 2 agents in `agents/`:
  - `indexer-architect` — design an indexer from a dApp description
  - `indexer-qa` — test an indexer for correctness, dedup, replay safety
- 2 commands in `commands/`:
  - `/build-indexer` — scaffold a complete indexer from a spec
  - `/backfill` — backfill historical data with checkpointing
- 1 rule in `rules/`:
  - `indexer-defaults.md` — auto-loads in `/indexer` folders
- `install.sh` — self-contained installer (downloads tarball, copies to `~/.claude/skills/` and `~/.codex/skills/`)
- `CLAUDE.md` — system personality + routing
- `README.md` — full skill description, install, quick start
- `LICENSE` — MIT
- `TODO.md` — v0.x → v1.0 roadmap
- `assets/indexer.webp` — banner (transparent background, blends with GitHub)
- `.github/workflows/validate.yml` — 6-job CI

[Unreleased]: https://github.com/srivtx/solana-indexer-skill/compare/main...HEAD
[0.1.0]: https://github.com/srivtx/solana-indexer-skill/releases/tag/v0.1.0
