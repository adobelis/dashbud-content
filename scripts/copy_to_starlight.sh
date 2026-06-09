#!/bin/bash
# Copy a source markdown file into Starlight's docs dir with frontmatter added.
# Usage: ./copy_to_starlight.sh <source_file> <dest_slug> <title>
# Example: ./copy_to_starlight.sh wiki/dashbud/product_reality_june2026.md dashbud/product-reality "Product Reality — June 2026"

SRC="$1"
SLUG="$2"
TITLE="$3"
DEST="wiki/src/content/docs/${SLUG}.md"

mkdir -p "$(dirname "$DEST")"

# Extract content after the H1 line (Starlight renders title from frontmatter)
{
  echo "---"
  echo "title: \"${TITLE}\""
  echo "---"
  echo ""
  # Skip the first H1 line and any blank line after it
  awk 'BEGIN{skip=1} /^# /{if(skip){skip=0; next}} /^$/{if(!found){found=1; next}} {found=1; print}' "$SRC"
} > "$DEST"

echo "Copied $SRC -> $DEST"
