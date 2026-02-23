#!/usr/bin/env python3
"""
package_skill.py - basic validator and packager for a skill directory
Usage: ./scripts/package_skill.py <path/to/skill-folder> [outdir]
"""
import sys
from pathlib import Path
import zipfile

if len(sys.argv) < 2:
    print("Usage: package_skill.py <skill-folder> [outdir]")
    sys.exit(2)

skill = Path(sys.argv[1])
if not skill.exists() or not skill.is_dir():
    print("Skill folder not found")
    sys.exit(1)

skill_md = skill / 'SKILL.md'
if not skill_md.exists():
    print("SKILL.md missing")
    sys.exit(1)

out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('dist')
out.mkdir(parents=True, exist_ok=True)
zip_path = out / (skill.name + '.skill')
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
    for p in skill.rglob('*'):
        if p.is_file():
            z.write(p, p.relative_to(skill.parent))
print(f"Packaged skill to {zip_path}")
