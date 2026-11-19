#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_SOURCE="$REPO_ROOT/integrations/hermes/skills/question-understanding"
SKILL_TARGET="${HERMES_HOME:-$HOME/.hermes}/skills/question-understanding"

mkdir -p "$(dirname "$SKILL_TARGET")"
if [[ -e "$SKILL_TARGET" ]]; then
  echo "Refusing to overwrite existing skill: $SKILL_TARGET" >&2
  echo "Back it up or remove it manually, then rerun." >&2
  exit 1
fi
cp -R "$SKILL_SOURCE" "$SKILL_TARGET"
echo "Installed question-understanding skill at: $SKILL_TARGET"
echo "Start/restart Hermes Agent and run /question-understanding <your question>."
