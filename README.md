<div align="center">

<a href="./assets/indexer.webp"><img src="./assets/indexer.webp" width="500" alt="solana-indexer skill — build custom Solana indexers end-to-end" /></a>

# solana-indexer

**Build custom Solana indexers end-to-end.** Geyser plugins, backfill strategies, Postgres schemas, real-time streaming, cost optimization, production ops — verified against real SDK code and docs.

A Claude Code / Codex skill for [Solana](https://solana.com) builders. Fills a gap nobody in the ecosystem is properly solving: teaching *how to build* a Solana indexer from scratch.

[![CI](https://github.com/srivtx/solana-indexer-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/srivtx/solana-indexer-skill/actions/workflows/validate.yml)
[![Version](https://img.shields.io/badge/version-0.1.0-blue)](./CHANGELOG.md)
[![License MIT](https://img.shields.io/badge/license-MIT-green)](./LICENSE)
[![Solana](https://img.shields.io/badge/Solana-black?logo=solana)](https://solana.com)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-ready-cc785c)](https://claude.ai/code)
[![Codex](https://img.shields.io/badge/Codex-ready-000000)](https://openai.com/codex)

</div>

---

## What's in this skill

- **9 references** — every fact cross-checked against real SDK code, repo source, and official docs
- **3 working examples** — `minimal-indexer-ts` (`tsc --noEmit` clean), `geyser-plugin/skeleton` (`cargo check` clean), `subgraph-template` (The Graph on Solana)
- **2 agents** — `indexer-architect`, `indexer-qa`
- **2 commands** — `/build-indexer`, `/backfill`
- **1 rule** — `indexer-defaults.md` (auto-loads in `/indexer` folders)
- **6 CI jobs** — Skills, TypeScript examples, Subgraph template, Rust examples, Internal links, Frontmatter

## Install

### One-liner (recommended)

```bash
curl -fsSL https://raw.githubusercontent.com/srivtx/solana-indexer-skill/main/install.sh | bash
```

Installs to `~/.claude/skills/solana-indexer/` and
`~/.codex/skills/solana-indexer/` (if Codex is installed). Restart
Claude Code or Codex.

### From a clone (if you want to inspect first or the one-liner is blocked)

```bash
git clone https://github.com/srivtx/solana-indexer-skill.git
cd solana-indexer-skill
./install.sh
```

### Manual copy (no install script, full control)

```bash
git clone https://github.com/srivtx/solana-indexer-skill.git

# Claude Code
mkdir -p ~/.claude/skills/solana-indexer
cp -R solana-indexer-skill/skill solana-indexer-skill/agents \
      solana-indexer-skill/commands solana-indexer-skill/rules \
      solana-indexer-skill/assets solana-indexer-skill/CLAUDE.md \
      ~/.claude/skills/solana-indexer/

# Codex (only if you use it)
mkdir -p ~/.codex/skills/solana-indexer
cp -R solana-indexer-skill/skill solana-indexer-skill/agents \
      solana-indexer-skill/commands solana-indexer-skill/rules \
      solana-indexer-skill/assets solana-indexer-skill/CLAUDE.md \
      ~/.codex/skills/solana-indexer/
```

### Project-local install (install into `./.claude/skills/` of a project)

```bash
git clone https://github.com/srivtx/solana-indexer-skill.git
cd solana-indexer-skill
CLAUDE_SKILLS_HOME=./.claude ./install.sh
```

This is useful when you want the skill to travel with a specific
repo (`.claude/skills/solana-indexer/` gets committed to that repo).

## What this skill does

You describe a Solana dApp. The skill routes you to the right approach:

| You say... | The skill reads |
|---|---|
| "I need to build an indexer" | `skill/references/indexer-architecture.md` (decision tree) |
| "Geyser / Yellowstone gRPC" | `skill/references/geyser-plugins.md` |
| "Postgres schema for swaps" | `skill/references/postgres-schemas.md` |
| "Backfill historical data" | `skill/references/backfill-strategies.md` |
| "Real-time account updates" | `skill/references/real-time-streaming.md` |
| "Reduce RPC costs" | `skill/references/cost-optimization.md` |
| "Test my indexer" | `skill/references/testing-indexers.md` |
| "Run in production" | `skill/references/production-ops.md` |
| "Where are the official docs" | `skill/references/resources.md` |

## Why this exists

The Solana AI Kit ecosystem has hundreds of skills — Helius, QuickNode,
light-protocol, vulnhunter, code-recon, solana-agent-kit, Token Extensions,
Anchor, Pinocchio, Jupiter, Metaplex, Pyth, Drift, Kamino, Raydium, Orca,
Meteora, Cloudflare, Trail of Bits — but **no skill teaches how to *build*
an indexer**. Helius and QuickNode skills are *consumers* of their streams.
The kit's `backend-async.md` has one 20-line polling pattern. Solana-agent-kit
has 60+ actions for using data, not building pipelines for it.

Indexers are the backbone of every serious Solana dApp — DeFi dashboards,
NFT marketplaces, gaming leaderboards, social graphs, analytics. This skill
lets Claude design, build, test, and operate them.

## Quick start

In Claude Code:

```
/build-indexer "index Raydium CLMM swaps and positions on mainnet"
```

Or just talk to it:

```
"Help me set up a Geyser gRPC plugin to index Magic Eden listings."
"Design a Postgres schema for a Jupiter swap indexer with hourly OHLCV aggregation."
"What's the cheapest way to backfill 90 days of pool state?"
```

## Real-world indexers this skill helps you build

| Indexer | Stack | What it tracks | Volume |
|---|---|---|---|
| Raydium CLMM swap indexer | Yellowstone gRPC → Postgres | Swaps, positions, fee tier changes | ~50K swaps/min on mainnet |
| Magic Eden listing indexer | Helius webhooks → Postgres | New listings, sales, delistings | ~100K listings/day |
| Jupiter aggregator route indexer | Helius enhanced tx → Postgres | Best routes, slippage, fees | ~10M routes/day |
| Drift perp position tracker | Helius account sub → Postgres | User positions, liquidations, PnL | ~1K liquidations/day |
| Meteora DLMM bin indexer | Geyser program sub → TimescaleDB | Bin liquidity, swaps, fee accrual | ~5K swaps/min |
| NFT collection mints tracker | Helius webhooks → Postgres | Mints, transfers, burns, listings | varies |
| Token-2022 transfer-hook indexer | Helius enhanced tx → Postgres | Transfers, hook invocations, fee collection | depends on token |
| Governance proposal tracker | Geyser program sub → Postgres | Proposals, votes, execution state | ~50 proposals/day across all DAOs |

## Examples

| Example | Language | What it shows |
|---|---|---|
| `skill/examples/minimal-indexer-ts/` | TypeScript | 100-line indexer: Helius enhanced webhook → Postgres. `tsc --noEmit` clean. |
| `skill/examples/geyser-plugin/skeleton/` | Rust | Geyser plugin skeleton using `solana-geyser-plugin-interface` 1.18. `cargo check` clean. |
| `skill/examples/subgraph-template/` | YAML + TypeScript | The Graph on Solana: manifest, schema, mapping stub. |

## Commands

| Command | What it does |
|---|---|
| `/build-indexer "<description>"` | Scaffold a complete indexer from a natural-language spec |
| `/backfill [range]` | Backfill historical data with checkpointing + parallelism |

## Agents

| Agent | When to use |
|---|---|
| `indexer-architect` | Design an indexer for a given dApp (ingestion method, schema, stack) |
| `indexer-qa` | Test an indexer for correctness, dedup, replay safety, and ops health |

## How this compares

| Skill | What it teaches | Builds indexers? |
|---|---|---|
| **solana-indexer (this)** | End-to-end indexer development: ingestion, schema, backfill, streaming, testing, ops | **Yes** |
| `ext/helius` (Helius labs) | How to *use* Helius RPC, DAS, webhooks, enhanced transactions | No (consumer) |
| `ext/sendai/skills/quicknode` (SendAI) | How to *use* QuickNode streams, RPC plans, marketplace add-ons | No (consumer) |
| `ext/light-protocol` (Light Labs) | ZK state compression + Light Token indexing primitives | No (different problem) |
| `ext/sendai/skills/solana-agent-kit` (SendAI) | AI agent actions: 60+ tools that *read* chain data | No (consumer) |
| `ext/solana-dev` (Solana Foundation) | Program development: Anchor, Pinocchio, frontend, testing | No (program-focused) |
| Solana AI Kit `backend-async.md` | One 20-line Axum polling pattern | No (snippet) |

This is the only skill that covers *building* an indexer from first
principles to production operations.

## Compatibility

### RPC providers (ingestion)
| Provider | Webhook | WebSocket | Yellowstone gRPC | Notes |
|---|---|---|---|---|
| Helius | ✓ enhanced | ✓ | ✓ Laserstream | Default choice; verified pricing as of 2026 |
| QuickNode | ✓ | ✓ | ✓ Streams | Marketplace add-ons for Solana-specific data |
| Triton | — | — | ✓ | Lowest-latency gRPC, no free tier |
| Syndica | ✓ | ✓ | — | Good WebSocket coverage, no gRPC |
| Public mainnet | — | ✓ rate-limited | — | Devnet/test only |

### Databases
| DB | Version | Use case | Notes |
|---|---|---|---|
| Postgres | 16+ | Primary store, relational schemas | Default |
| TimescaleDB | 2.x+ | Time-series (OHLCV, swap aggregations) | Hypertables + compression |
| ClickHouse | 23.x+ | High-volume analytics | Optional for >1M events/min |
| SQLite | 3.x+ | Local dev, single-process indexers | Limited concurrency |
| DuckDB | 0.10+ | Embedded analytics over parquet | Read-only patterns |

### Testing frameworks
| Framework | Scope | Notes |
|---|---|---|
| LiteSVM | Unit | In-process Solana VM, fast |
| Surfpool | Integration | Local validator + mainnet fork |
| Mollusk | Unit (programs) | Minimal Solana program testing |
| Trident | E2E (Anchor) | Anchor-specific fuzzing |
| solana-test-validator | Local validator | Built-in, but slower than Surfpool |

### Deployment
| Target | Notes |
|---|---|
| Docker | Single-container, recommended for dev |
| Kubernetes | Multi-replica, HPA on lag metrics |
| Cloudflare Workers | Edge indexers (limited; no Postgres) |
| Fly.io / Railway | Single-region, simple |
| AWS / GCP | Full control, multi-region |

## Default stack (2026)

| Layer | Choice |
|---|---|
| Real-time | Yellowstone gRPC (Triton, Helius Laserstream, or QuickNode) |
| Polling fallback | Helius enhanced transactions API |
| Storage | Postgres 16 + TimescaleDB for time-series |
| Backfill | Snapshot + incremental replay (RPC + Geyser) |
| Testing | LiteSVM (unit), Surfpool fork (integration) |
| Local validator | Surfpool |
| Schema migrations | sqlx-cli (Rust) or Drizzle/Knex (TS) |
| Indexing-as-a-service fallback | The Graph on Solana (subgraphs) |
| Production | Docker + k8s, Prometheus metrics, PagerDuty alerts |

## Repository layout

```
solana-indexer-skill/
├── CLAUDE.md                 # system personality + routing
├── README.md                 # this file
├── CHANGELOG.md              # version history
├── LICENSE                   # MIT
├── TODO.md                   # roadmap
├── install.sh                # self-contained installer
├── .github/
│   └── workflows/
│       └── validate.yml      # 6-job CI
├── skill/
│   ├── SKILL.md              # entry point (3.9 KB routing hub)
│   ├── references/           # 9 verified reference files
│   │   ├── indexer-architecture.md
│   │   ├── geyser-plugins.md
│   │   ├── postgres-schemas.md
│   │   ├── backfill-strategies.md
│   │   ├── real-time-streaming.md
│   │   ├── cost-optimization.md
│   │   ├── testing-indexers.md
│   │   ├── production-ops.md
│   │   └── resources.md
│   └── examples/             # 3 working, tested examples
│       ├── minimal-indexer-ts/        # 100-line TS indexer (Helius webhook → Postgres)
│       ├── geyser-plugin/skeleton/    # Rust Geyser plugin skeleton
│       └── subgraph-template/         # The Graph on Solana
├── agents/
│   ├── indexer-architect.md           # designs an indexer for a given dApp
│   └── indexer-qa.md                  # tests indexer correctness
├── commands/
│   ├── build-indexer.md               # /build-indexer
│   └── backfill-data.md               # /backfill
├── rules/
│   └── indexer-defaults.md            # auto-loads in /indexer folders
└── assets/
    └── indexer.webp                   # banner (transparent background)
```

## Inspiration & related work

This skill builds on (and is informed by) the work of:

- **Helius** ([helius-labs/core-ai](https://github.com/helius-labs/core-ai)) — Yellowstone gRPC + DAS reference, SVM internals
- **QuickNode** ([quiknode-labs/solana-anchor-claude-skill](https://github.com/quiknode-labs/solana-anchor-claude-skill)) — QuickNode streams
- **Light Protocol** ([Lightprotocol/light-protocol](https://github.com/Lightprotocol/light-protocol)) — ZK compression, Light Token
- **SendAI** ([sendaifun/skills](https://github.com/sendaifun/skills)) — Jupiter, Raydium, Drift, Kamino, Pyth integration
- **Metaplex** ([metaplex-foundation/skill](https://github.com/metaplex-foundation/skill)) — Core, Token Metadata, Bubblegum
- **Solana Foundation** ([solana-foundation/solana-dev-skill](https://github.com/solana-foundation/solana-dev-skill)) — core Solana dev reference
- **Triton** — Yellowstone gRPC protocol
- **rpcpool** — yellowstone-grpc reference implementation

This skill fills the **building** side of the indexing story. The skills
above cover the *consuming* side.

## When NOT to use this skill

- **Using an indexer's data** → read `ext/helius` (RPC queries), `ext/sendai/skills/pyth` (price feeds), or `ext/sendai/skills/solana-agent-kit` (AI agents)
- **Building a Solana program** (not an indexer) → read `ext/solana-dev/programs/anchor.md` or `ext/solana-dev/programs/pinocchio.md`
- **Auditing an existing indexer** → `ext/trailofbits` (security) or `ext/safe-solana-builder` (audit-derived rules)
- **One-off RPC queries** → just call the RPC directly, no need for an indexer

## Part of solana-superchargers

This skill is also available through the
[solana-superchargers](https://github.com/srivtx/solana-superchargers)
multi-skill marketplace — a curated set of Solana skills that complement
and extend the [Solana AI Kit](https://github.com/solanabr/solana-ai-kit)
ecosystem.

## License

[MIT](./LICENSE)

---

<sub>Built by [@srivtx](https://github.com/srivtx) · Part of the
[Solana AI Kit](https://github.com/solanabr/solana-ai-kit) ecosystem</sub>
