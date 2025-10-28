# Terraform Documentation Generator Skill

A comprehensive Claude Agent Skill for transforming Terraform code into user-friendly, professionally formatted documentation.

## What This Skill Does

Generates comprehensive documentation from Terraform configurations including:
- **Module READMEs** - Complete module documentation with inputs, outputs, and usage examples
- **Architecture Documentation** - High-level infrastructure overviews with diagrams and component descriptions
- **Operational Runbooks** - Step-by-step guides for deployment, maintenance, and troubleshooting
- **Quick Reference Guides** - Command cheat sheets and common tasks

## Installation

### Option 1: Project-Specific Installation

Place this skill in your project's `.claude/skills/` directory:

```bash
# From your project root
mkdir -p .claude/skills
cp -r terraform-docs .claude/skills/
```

### Option 2: Global Installation

Install globally to use across all projects:

```bash
# Create global skills directory if it doesn't exist
mkdir -p ~/.claude/skills

# Copy the skill
cp -r terraform-docs ~/.claude/skills/
```

## Usage

Once installed, Claude Code will automatically discover and use this skill when you work with Terraform files.

### Example Commands

**Generate Module Documentation:**
```
"Document this Terraform module"
"Create a README for this module"
"Generate module documentation from these .tf files"
```

**Generate Architecture Documentation:**
```
"Create architecture documentation for this infrastructure"
"Document the architecture of these Terraform files"
"Generate an architecture overview with diagrams"
```

**Generate Runbook:**
```
"Create an operations runbook for this infrastructure"
"Generate deployment and troubleshooting guide"
"Create a runbook for managing this Terraform configuration"
```

**Generate Quick Reference:**
```
"Create a quick reference guide"
"Generate a cheat sheet for this infrastructure"
"Create a quick reference with common commands"
```

### Providing Input

You can provide Terraform code in several ways:

1. **Reference files directly:**
   ```
   "Document the module in ./modules/vpc"
   "Create architecture docs from main.tf and variables.tf"
   ```

2. **Paste code:**
   ```
   "Document this Terraform code:

   resource \"aws_instance\" \"web\" {
     ami           = \"ami-12345678\"
     instance_type = \"t3.micro\"
   }"
   ```

3. **Current directory:**
   ```
   "Document the Terraform in this directory"
   ```

### Specifying Output Format

Tell Claude which documentation type you need:
- **Module README**: "Create a module README..."
- **Architecture**: "Generate architecture documentation..."
- **Runbook**: "Create an operational runbook..."
- **Quick Reference**: "Generate a quick reference..."

## What the Skill Will Do

1. **Analyze** your Terraform code
   - Parse resources, variables, outputs, providers
   - Identify infrastructure patterns
   - Extract metadata and configurations

2. **Transform** technical code into readable documentation
   - Convert resource names to human-friendly descriptions
   - Explain relationships between components
   - Add context and purpose

3. **Format** for the target documentation type
   - Apply appropriate templates
   - Include relevant sections
   - Add diagrams where helpful

4. **Enhance** with helpful information
   - Security considerations
   - Cost estimates
   - Best practices
   - Troubleshooting guides

## Output Examples

### Module README
```markdown
# VPC Module

## Overview
Creates a VPC with public and private subnets across multiple availability zones...

## Usage
[Basic and complete examples]

## Inputs
[Table of all variables]

## Outputs
[Table of all outputs]

## Resources Created
[List of resources with descriptions]
```

### Architecture Documentation
```markdown
# Production Infrastructure - Architecture

## Overview
Multi-tier web application with high availability...

## Architecture Diagram
[ASCII or Mermaid diagram]

## Components
[Detailed component descriptions]

## Security
[Security configurations and considerations]

## High Availability
[HA strategy and DR plan]
```

### Runbook
```markdown
# Operations Runbook

## Initial Deployment
[Step-by-step deployment instructions]

## Daily Operations
[Common operational tasks]

## Troubleshooting
[Common issues and solutions]

## Disaster Recovery
[Recovery procedures]
```

### Quick Reference
```markdown
# Quick Reference

## Terraform Commands
[Common terraform commands]

## Key Resources
[Resource inventory]

## Variables & Outputs
[Quick reference tables]

## Troubleshooting Quick Fixes
[Common fixes]
```

## Skill Structure

```
terraform-docs/
├── SKILL.md                          # Main skill instructions
├── README.md                         # This file
├── templates/
│   ├── MODULE_README_TEMPLATE.md     # Module README template
│   ├── ARCHITECTURE_TEMPLATE.md      # Architecture docs template
│   ├── RUNBOOK_TEMPLATE.md           # Operations runbook template
│   └── QUICK_REFERENCE_TEMPLATE.md   # Quick reference template
└── scripts/
    └── generate_docs.sh              # terraform-docs wrapper script
```

## Templates

The skill includes professional templates for all documentation types:

- **[Module README Template](templates/MODULE_README_TEMPLATE.md)** - Standard module documentation structure
- **[Architecture Template](templates/ARCHITECTURE_TEMPLATE.md)** - Infrastructure architecture overview
- **[Runbook Template](templates/RUNBOOK_TEMPLATE.md)** - Operational procedures and troubleshooting
- **[Quick Reference Template](templates/QUICK_REFERENCE_TEMPLATE.md)** - Command reference and cheat sheet

## Automated Documentation Script

The skill includes a script for automated documentation generation using terraform-docs:

```bash
# Install terraform-docs first
brew install terraform-docs  # macOS
# or download from https://terraform-docs.io

# Run the script
./terraform-docs/scripts/generate_docs.sh /path/to/terraform/module

# The script will:
# - Create a .terraform-docs.yml configuration
# - Generate README.md with proper sections
# - Use injection markers for easy updates
```

## Tips for Best Results

1. **Provide Complete Context**
   - Include all relevant .tf files (main.tf, variables.tf, outputs.tf)
   - Mention the cloud provider (AWS, Azure, GCP)
   - Specify the environment type (production, staging, dev)

2. **Specify Your Audience**
   - "For developers using this module..."
   - "For operations team managing production..."
   - "For architects reviewing the design..."

3. **Request Specific Sections**
   - "Include cost estimates"
   - "Add security considerations"
   - "Include troubleshooting for common issues"

4. **Iterate and Refine**
   - Ask Claude to add more detail
   - Request diagrams or examples
   - Ask for specific format changes

## Examples

### Basic Module Documentation
```
User: "Document this VPC module in ./modules/vpc"

Claude: [Analyzes the Terraform code and generates a complete
         module README with usage examples, input/output tables,
         security notes, and cost considerations]
```

### Complex Infrastructure
```
User: "Create architecture documentation for our production
       infrastructure. It's a containerized app on ECS with RDS.
       Include diagrams and focus on high availability."

Claude: [Generates comprehensive architecture docs with ASCII
         diagrams showing the component relationships, detailed
         HA strategy, security analysis, and operational notes]
```

### Operational Runbook
```
User: "Create a runbook for deploying and managing this
       Terraform infrastructure. Target audience is our
       DevOps team who will be on-call."

Claude: [Produces detailed runbook with deployment steps,
         daily operations guide, troubleshooting section,
         disaster recovery procedures, and emergency contacts]
```

## Use Cases

### For Development Teams
- Document reusable Terraform modules
- Create usage examples for shared infrastructure
- Generate API documentation for module inputs/outputs

### For Operations Teams
- Create deployment runbooks
- Document troubleshooting procedures
- Generate quick reference guides

### For Architecture Teams
- Document infrastructure designs
- Create architecture decision records
- Generate high-level system overviews

### For Compliance/Audit
- Document security configurations
- Create infrastructure inventory
- Generate compliance evidence

## Requirements

- Claude Code (claude.ai/code)
- This skill placed in `.claude/skills/` or `~/.claude/skills/`
- Terraform files (.tf) to document

### Optional
- `terraform-docs` for automated generation (scripts/generate_docs.sh)

## Validation

To validate the skill structure:

```bash
python3 ../claude-skill-creator/scripts/validate_skill.py terraform-docs
```

## Best Practices

1. **Keep Documentation Current**
   - Regenerate docs after significant Terraform changes
   - Update runbooks after operational changes
   - Review and update cost estimates periodically

2. **Tailor to Your Audience**
   - Module READMEs for developers
   - Architecture docs for architects and stakeholders
   - Runbooks for operations teams
   - Quick references for everyone

3. **Include Real Examples**
   - Use actual working code examples
   - Reference real resource names
   - Include actual commands that work

4. **Cross-Reference**
   - Link between related documentation
   - Reference external resources
   - Include links to provider documentation

## Troubleshooting

### Skill Not Activating

If Claude doesn't use the skill automatically:
- Verify the skill is in `.claude/skills/` or `~/.claude/skills/`
- Try explicitly mentioning "terraform" in your request
- Use phrases like "document this Terraform module"

### Incomplete Documentation

If the generated documentation is missing sections:
- Ensure all relevant .tf files are provided
- Ask Claude to "add [specific section]"
- Request more detail on specific areas

### Wrong Format

If Claude generates the wrong documentation type:
- Be explicit: "Create a MODULE README" vs "Create ARCHITECTURE docs"
- Reference the specific template you want
- Provide an example of what you're looking for

## Resources

- [Terraform Documentation](https://terraform.io/docs)
- [terraform-docs](https://terraform-docs.io)
- [Claude Agent Skills Documentation](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
- [Terraform Best Practices](https://www.terraform-best-practices.com/)

## Contributing

To improve this skill:
1. Update templates in the `templates/` directory
2. Enhance the main SKILL.md with better examples
3. Add more automation scripts to `scripts/`

## License

This skill is provided as-is for use with Claude Code.

## Support

For issues or questions about Claude Code skills:
- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [Agent Skills Guide](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)
