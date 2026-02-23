#!/usr/bin/env python3
"""
init_skill.py - create a skill template directory with SKILL.md frontmatter
Usage:
  ./scripts/init_skill.py <skill-name> --path <output-dir>
"""
import os
import sys
from pathlib import Path

def usage():
    print("Usage: init_skill.py <skill-name> --path <output-dir>")
    sys.exit(2)

if len(sys.argv) < 4:
    usage()

skill_name = sys.argv[1]
if sys.argv[2] != "--path":
    usage()

out_dir = Path(sys.argv[3]) / skill_name
out_dir.mkdir(parents=True, exist_ok=True)

skill_md = out_dir / 'SKILL.md'
if skill_md.exists():
    print(f"SKILL.md already exists at {skill_md}")
    sys.exit(0)

front = f"---\nname: {skill_name}\ndescription: TODO: short description\n---\n\n# {skill_name} skill\n\nTODO: detail how/when to use this skill.\n"
skill_md.write_text(front)
print(f"Created skill template at {out_dir}")
