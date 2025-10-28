#!/usr/bin/env bash
#
# Generate Terraform documentation using terraform-docs
# This script wraps terraform-docs to create consistent module documentation
#
# Usage: ./generate_docs.sh [path-to-module]
#
# Requirements:
# - terraform-docs (install: https://terraform-docs.io/user-guide/installation/)

set -euo pipefail

# Configuration
MODULE_PATH="${1:-.}"
OUTPUT_FILE="README.md"
CONFIG_FILE=".terraform-docs.yml"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if terraform-docs is installed
if ! command -v terraform-docs &> /dev/null; then
    echo -e "${RED}Error: terraform-docs is not installed${NC}"
    echo "Install it from: https://terraform-docs.io/user-guide/installation/"
    echo ""
    echo "Quick install:"
    echo "  macOS:   brew install terraform-docs"
    echo "  Linux:   Download from GitHub releases"
    exit 1
fi

# Check if module path exists
if [ ! -d "$MODULE_PATH" ]; then
    echo -e "${RED}Error: Module path does not exist: $MODULE_PATH${NC}"
    exit 1
fi

# Check if module has .tf files
if ! ls "$MODULE_PATH"/*.tf 1> /dev/null 2>&1; then
    echo -e "${RED}Error: No .tf files found in: $MODULE_PATH${NC}"
    exit 1
fi

echo -e "${GREEN}Generating documentation for: $MODULE_PATH${NC}"

# Create default config if it doesn't exist
if [ ! -f "$MODULE_PATH/$CONFIG_FILE" ]; then
    echo -e "${YELLOW}Creating default .terraform-docs.yml${NC}"
    cat > "$MODULE_PATH/$CONFIG_FILE" <<EOF
formatter: markdown table

header-from: main.tf

sections:
  hide: []
  show:
    - header
    - requirements
    - providers
    - inputs
    - outputs
    - resources

output:
  file: README.md
  mode: inject
  template: |-
    <!-- BEGIN_TF_DOCS -->
    {{ .Content }}
    <!-- END_TF_DOCS -->

sort:
  enabled: true
  by: required

settings:
  anchor: true
  color: true
  default: true
  description: true
  escape: true
  hide-empty: false
  html: true
  indent: 2
  lockfile: true
  read-comments: true
  required: true
  sensitive: true
  type: true
EOF
fi

# Generate documentation
echo -e "${GREEN}Running terraform-docs...${NC}"
if terraform-docs -c "$MODULE_PATH/$CONFIG_FILE" "$MODULE_PATH"; then
    echo -e "${GREEN}✓ Documentation generated successfully${NC}"
    echo -e "${GREEN}  Output: $MODULE_PATH/$OUTPUT_FILE${NC}"
else
    echo -e "${RED}✗ Failed to generate documentation${NC}"
    exit 1
fi

# Validate that README.md was created/updated
if [ -f "$MODULE_PATH/$OUTPUT_FILE" ]; then
    echo -e "${GREEN}✓ README.md exists${NC}"

    # Show file size
    SIZE=$(wc -c < "$MODULE_PATH/$OUTPUT_FILE" | tr -d ' ')
    echo -e "${GREEN}  File size: $SIZE bytes${NC}"

    # Check if it has the injection markers
    if grep -q "BEGIN_TF_DOCS" "$MODULE_PATH/$OUTPUT_FILE" && \
       grep -q "END_TF_DOCS" "$MODULE_PATH/$OUTPUT_FILE"; then
        echo -e "${GREEN}✓ Documentation markers found${NC}"
    else
        echo -e "${YELLOW}⚠ Warning: Documentation markers not found${NC}"
        echo -e "${YELLOW}  The file may not update correctly on subsequent runs${NC}"
    fi
else
    echo -e "${RED}✗ README.md was not created${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}Done!${NC}"
echo ""
echo "Next steps:"
echo "  1. Review the generated README.md"
echo "  2. Add any custom content before <!-- BEGIN_TF_DOCS --> marker"
echo "  3. Run this script again after changes to update docs"
