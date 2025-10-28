#!/usr/bin/env python3
"""
Validate a Claude Agent Skill structure and content.
Checks naming conventions, frontmatter, and required fields.
"""

import os
import re
import sys
from pathlib import Path
from typing import List, Tuple

RESERVED_WORDS = ["anthropic", "claude"]

def validate_name(name: str) -> Tuple[bool, List[str]]:
    """Validate skill name against Claude requirements."""
    errors = []
    
    if len(name) > 64:
        errors.append(f"Name exceeds 64 characters (current: {len(name)})")
    
    if not re.match(r'^[a-z0-9-]+$', name):
        errors.append("Name must contain only lowercase letters, numbers, and hyphens")
    
    for word in RESERVED_WORDS:
        if word in name.lower():
            errors.append(f"Name cannot contain reserved word: '{word}'")
    
    if '<' in name or '>' in name:
        errors.append("Name cannot contain XML tags")
    
    return len(errors) == 0, errors

def validate_description(description: str) -> Tuple[bool, List[str]]:
    """Validate skill description against Claude requirements."""
    errors = []
    
    if not description or len(description.strip()) == 0:
        errors.append("Description cannot be empty")
    
    if len(description) > 1024:
        errors.append(f"Description exceeds 1024 characters (current: {len(description)})")
    
    if '<' in description and '>' in description:
        if re.search(r'<[^>]+>', description):
            errors.append("Description cannot contain XML tags")
    
    return len(errors) == 0, errors

def extract_frontmatter(content: str) -> Tuple[dict, str]:
    """Extract YAML frontmatter from SKILL.md content."""
    if not content.startswith('---'):
        return {}, content
    
    try:
        parts = content.split('---', 2)
        if len(parts) < 3:
            return {}, content
        
        frontmatter_lines = parts[1].strip().split('\n')
        frontmatter = {}
        
        for line in frontmatter_lines:
            if ':' in line:
                key, value = line.split(':', 1)
                frontmatter[key.strip()] = value.strip().strip('"').strip("'")
        
        body = parts[2]
        return frontmatter, body
    except Exception as e:
        return {}, content

def validate_skill(skill_dir: Path) -> Tuple[bool, List[str]]:
    """Validate a skill directory structure."""
    errors = []
    warnings = []
    
    skill_md = skill_dir / "SKILL.md"
    
    if not skill_md.exists():
        errors.append(f"SKILL.md not found in {skill_dir}")
        return False, errors
    
    # Read and validate SKILL.md
    content = skill_md.read_text(encoding='utf-8')
    frontmatter, body = extract_frontmatter(content)
    
    # Check required fields
    if 'name' not in frontmatter:
        errors.append("Missing required field: 'name' in frontmatter")
    else:
        name_valid, name_errors = validate_name(frontmatter['name'])
        if not name_valid:
            errors.extend([f"Name validation: {e}" for e in name_errors])
    
    if 'description' not in frontmatter:
        errors.append("Missing required field: 'description' in frontmatter")
    else:
        desc_valid, desc_errors = validate_description(frontmatter['description'])
        if not desc_valid:
            errors.extend([f"Description validation: {e}" for e in desc_errors])
    
    # Check if description includes "when to use"
    if 'description' in frontmatter:
        desc_lower = frontmatter['description'].lower()
        if 'use when' not in desc_lower and 'when' not in desc_lower:
            warnings.append("Consider adding 'when to use' guidance to description")
    
    # Check if body has content
    if len(body.strip()) < 100:
        warnings.append("SKILL.md body seems short - consider adding more detailed instructions")
    
    return len(errors) == 0, errors + [f"WARNING: {w}" for w in warnings]

def main():
    """Main validation function."""
    if len(sys.argv) < 2:
        print("Usage: python validate_skill.py <skill_directory>")
        sys.exit(1)
    
    skill_path = Path(sys.argv[1])
    
    if not skill_path.exists():
        print(f"Error: Directory {skill_path} does not exist")
        sys.exit(1)
    
    if not skill_path.is_dir():
        print(f"Error: {skill_path} is not a directory")
        sys.exit(1)
    
    is_valid, messages = validate_skill(skill_path)
    
    if is_valid and all("WARNING:" in m for m in messages):
        # Only warnings, no errors
        print("✓ Skill validation passed with warnings:")
        for msg in messages:
            print(f"  {msg}")
        sys.exit(0)
    elif is_valid:
        print("✓ Skill validation passed")
        if messages:
            for msg in messages:
                print(f"  {msg}")
        sys.exit(0)
    else:
        print("✗ Skill validation failed:")
        for msg in messages:
            print(f"  {msg}")
        sys.exit(1)

if __name__ == "__main__":
    main()

