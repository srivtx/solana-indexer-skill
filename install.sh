#!/usr/bin/env bash
#
# install.sh — standalone installer for solana-indexer-skill
#
# This skill ships in its own repo (https://github.com/srivtx/solana-indexer-skill)
# and is also distributed through the solana-superchargers marketplace
# (https://github.com/srivtx/solana-superchargers). Both install paths
# land at the same destination: ~/.claude/skills/solana-indexer/ and
# ~/.codex/skills/solana-indexer/.
#
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/srivtx/solana-indexer-skill/main/install.sh | bash
#   ./install.sh            # install (default)
#   ./install.sh remove     # uninstall
#   ./install.sh help       # show this message
#

set -eo pipefail
SKILL_NAME="solana-indexer"
REPO_RAW="https://raw.githubusercontent.com/srivtx/solana-indexer-skill/main"
REPO_TARBALL="https://codeload.github.com/srivtx/solana-indexer-skill/tar.gz/refs/heads/main"

# Where skills install. Override with CLAUDE_SKILLS_HOME=/path ./install.sh
: "${CLAUDE_SKILLS_HOME:=$HOME/.claude/skills}"
: "${CODEX_SKILLS_HOME:=$HOME/.codex/skills}"

ok()   { printf "  \033[32m✓\033[0m %s\n" "$*"; }
warn() { printf "  \033[33m!\033[0m %s\n" "$*"; }
err()  { printf "  \033[31m✗\033[0m %s\n" "$*" >&2; }
head() { printf "\n\033[1m\033[36m── %s ──\033[0m\n" "$*"; }

# SCRIPT_DIR is set when invoked as `./install.sh`. When piped from curl,
# stdin is not a tty and BASH_SOURCE[0] is unset — fall back to "".
SCRIPT_DIR=""
if [[ -t 0 ]]; then
  SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
fi
inside_repo=false
if [[ -n "$SCRIPT_DIR" ]] && [[ -f "${SCRIPT_DIR}/skill/SKILL.md" ]]; then
  inside_repo=true
fi

cmd="${1:-add}"
shift || true

case "$cmd" in
  help|--help|-h)
    head "solana-indexer — standalone installer"
    cat <<EOF

Install:

  curl -fsSL ${REPO_RAW}/install.sh | bash

Or from a clone:

  git clone https://github.com/srivtx/solana-indexer-skill.git
  cd solana-indexer-skill
  ./install.sh

Or manual copy (see README "Manual copy" section).

That copies the skill into:
  - \${CLAUDE_SKILLS_HOME:-~/.claude/skills}/solana-indexer/
  - \${CODEX_SKILLS_HOME:-~/.codex/skills}/solana-indexer/   (if codex is installed)

Commands:
  install.sh            Install (default)
  install.sh remove     Uninstall
  install.sh help       Show this message

Environment:
  CLAUDE_SKILLS_HOME    Override install location
  CODEX_SKILLS_HOME     Override codex install location
EOF
    exit 0
    ;;

  add|install|"")
    # Two-stage install: get the skill files into a temp dir, then copy to dest.
    head "Install ${SKILL_NAME}"
    TMP=$(mktemp -d)
    trap 'rm -rf "$TMP"' EXIT
    if [[ "$inside_repo" == "true" ]]; then
      cp -R "$SCRIPT_DIR/." "$TMP/"
    else
      curl -fsSL "$REPO_TARBALL" -o "$TMP/repo.tgz"
      tar -xzf "$TMP/repo.tgz" -C "$TMP" --strip-components=1
      rm -f "$TMP/repo.tgz"
    fi
    mkdir -p "$CLAUDE_SKILLS_HOME/$SKILL_NAME"
    cp -R "$TMP/." "$CLAUDE_SKILLS_HOME/$SKILL_NAME/"
    ok "installed ${SKILL_NAME} → $CLAUDE_SKILLS_HOME/$SKILL_NAME"
    if [[ -d "$CODEX_SKILLS_HOME" ]] || command -v codex >/dev/null 2>&1; then
      head "Mirror to Codex"
      mkdir -p "$CODEX_SKILLS_HOME/$SKILL_NAME"
      cp -R "$TMP/." "$CODEX_SKILLS_HOME/$SKILL_NAME/"
      ok "installed ${SKILL_NAME} → $CODEX_SKILLS_HOME/$SKILL_NAME"
    fi
    head "Done"
    echo "  Restart Claude Code or Codex to pick up the skill."
    ;;

  remove|rm|uninstall)
    head "Remove ${SKILL_NAME}"
    if [[ -d "$CLAUDE_SKILLS_HOME/$SKILL_NAME" ]]; then
      rm -rf "$CLAUDE_SKILLS_HOME/$SKILL_NAME"
      ok "removed ${SKILL_NAME} from $CLAUDE_SKILLS_HOME"
    fi
    if [[ -d "$CODEX_SKILLS_HOME/$SKILL_NAME" ]]; then
      rm -rf "$CODEX_SKILLS_HOME/$SKILL_NAME"
      ok "removed ${SKILL_NAME} from $CODEX_SKILLS_HOME"
    fi
    head "Done"
    echo "  Restart Claude Code or Codex to apply changes."
    ;;

  *)
    err "unknown command: $cmd"
    echo "  run: $0 help"
    exit 1
    ;;
esac
