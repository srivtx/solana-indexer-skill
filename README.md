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

```bash
curl -fsSL https://raw.githubusercontent.com/srivtx/solana-indexer-skill/main/install.sh | bash
```

Installs to `~/.claude/skills/solana-indexer/` (and `~/.codex/skills/solana-indexer/`
if Codex is installed). Restart Claude Code or Codex.

For a clone + manual install:

```bash
git clone https://github.com/srivtx/solana-indexer-skill.git
cd solana-indexer-skill
./install.sh
```

For a manual copy (no install script, full control):

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

For a project-local install (skill lives in a specific repo instead of your home dir):

```bash
CLAUDE_SKILLS_HOME=./.claude ./install.sh
```

`CLAUDE_SKILLS_HOME` overrides the default `~/.claude/skills/` with the path you give it. `./.claude` resolves to a `solana-indexer/` subdirectory inside the current directory — so the skill gets installed to `./.claude/skills/solana-indexer/`. You'd then `git add` and commit that path yourself.

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

## Why this is needed

The Solana AI Kit ecosystem has hundreds of skills — Helius, QuickNode,
light-protocol, vulnhunter, code-recon, solana-agent-kit, Token Extensions,
Anchor, Pinocchio, Jupiter, Metaplex, Pyth, Drift, Kamino, Raydium, Orca,
Meteora, Cloudflare, Trail of Bits — but **no skill teaches how to *build*
an indexer**. Helius and QuickNode skills are *consumers* of their streams.
The kit's `backend-async.md` has one 20-line polling pattern. Solana-agent-kit
has 60+ actions for using data, not building pipelines for it.

Indexers are the backbone of every serious Solana dApp — DeFi dashboards,
NFT marketplaces, gaming leaderboards, social graphs, analytics. Every
founder building a "real" Solana product eventually needs one. Without a
custom indexer, you're stuck polling RPC every N seconds, which is
expensive, slow, and rate-limited.

## How this skill helps

Without this skill, every founder has to rediscover the same patterns.
With it, Claude gets them right on the first try:

- **Picks the right ingestion method** — Helius WebSocket, Yellowstone
  gRPC, account subs, polling, or subgraph. `indexer-architecture.md`
  is the decision tree.
- **Designs a Postgres schema that doesn't break** — `NUMERIC(40, 0)`
  for u128, `BYTEA(32)` for Pubkey, `(slot, signature)` dedup.
  Verified against Raydium CLMM's `PoolState` source.
- **Backfills in hours, not days** — 5 strategies with checkpointing
  + parallelism in `backfill-strategies.md`.
- **Cuts RPC costs** — Helius tier breakdown ($49 / $249 / $999) plus
  7 cost-reduction techniques in `cost-optimization.md`.
- **Tests with LiteSVM + Surfpool + golden + chaos** —
  `testing-indexers.md` covers all four.
- **Runs in production** — slot-lag SLOs, Prometheus, PagerDuty, and
  on-call playbooks for the 5 things that actually break.

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
| **solana-indexer (this)** | End-to-end indexer development | **Yes** |
| `ext/helius` | How to *use* Helius RPC, webhooks, enhanced tx | No (consumer) |
| `ext/sendai/skills/quicknode` | How to *use* QuickNode streams | No (consumer) |
| `ext/light-protocol` | ZK state compression + Light Token | No (different problem) |
| `ext/sendai/skills/solana-agent-kit` | 60+ AI agent actions that *read* chain data | No (consumer) |
| `ext/solana-dev` | Program development (Anchor, Pinocchio) | No (program-focused) |
| Kit's `backend-async.md` | One 20-line polling snippet | No (snippet) |

This is the only skill that covers *building* an indexer end-to-end.

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
├── README.md, CHANGELOG.md, TODO.md, LICENSE
├── install.sh                # self-contained installer
├── .github/workflows/validate.yml   # 6-job CI
├── skill/
│   ├── SKILL.md              # 3.9 KB routing hub
│   ├── references/           # 9 verified reference files
│   └── examples/             # 3 working, tested examples
├── agents/                   # 2 (architect, qa)
├── commands/                 # 2 (/build-indexer, /backfill)
├── rules/                    # 1 (indexer-defaults)
└── assets/indexer.webp       # banner
```

## Inspiration & related work

Built on top of Helius, QuickNode, Light Protocol, SendAI, Metaplex,
Solana Foundation, Triton, and rpcpool's work — see
[`skill/references/resources.md`](skill/references/resources.md) for
the full list of upstream repos. This skill fills the *building*
side of the indexing story; the listed sources cover the *consuming*
side.

## When NOT to use this skill

- **Using an indexer's data** → read `ext/helius` (RPC queries), `ext/sendai/skills/pyth` (price feeds), or `ext/sendai/skills/solana-agent-kit` (AI agents)
- **Building a Solana program** (not an indexer) → read `ext/solana-dev/programs/anchor.md` or `ext/solana-dev/programs/pinocchio.md`
- **Auditing an existing indexer** → `ext/trailofbits` (security) or `ext/safe-solana-builder` (audit-derived rules)
- **One-off RPC queries** → just call the RPC directly, no need for an indexer

## Extends the Solana AI Kit ecosystem

This skill fills a gap in the
[Solana AI Kit](https://github.com/solanabr/solana-ai-kit) ecosystem
— *how to build* a Solana indexer. The kit ships Helius, QuickNode,
light-protocol, solana-agent-kit, Jupiter, Metaplex, Anchor,
Pinocchio, Token Extensions, security skills, infra skills, GTM
skills. This is the indexer-builder skill that completes the picture.

It follows the kit's exact shape (`skill/` + `agents/` + `commands/`
+ `rules/` + `install.sh` + MIT LICENSE) so it can drop into
`ext/solana-indexer` with no restructuring.

It's also the first skill in
[solana-superchargers](https://github.com/srivtx/solana-superchargers),
a multi-skill marketplace extending the AI Kit with more skills
(observability, MEV, upgrades, E2E testing, wallet UX, and more in
the roadmap).

## License

[MIT](./LICENSE)

---

<sub>Built by [@srivtx](https://github.com/srivtx) · Part of the
[Solana AI Kit](https://github.com/solanabr/solana-ai-kit) ecosystem</sub>
