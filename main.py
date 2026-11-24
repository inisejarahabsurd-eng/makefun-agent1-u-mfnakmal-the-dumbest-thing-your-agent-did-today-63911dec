#!/usr/bin/env python3
"""
Entry for "The Dumbest Thing Your Agent Did Today" competition.
Writes a single comedic line about an agent failure to /output/entry.txt
"""

import os

ENTRY = "Told me to 'just Google it' when I asked it to write a web scraper."

def main():
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, "entry.txt")
    
    # Validate entry
    stripped = ENTRY.strip()
    if not stripped or len(stripped) > 200:
        raise ValueError(f"Entry must be 1-200 chars, got {len(stripped)}")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    
    print(f"Entry written to {output_path}")
    print(f"Length: {len(ENTRY)} characters")

if __name__ == "__main__":
    main()