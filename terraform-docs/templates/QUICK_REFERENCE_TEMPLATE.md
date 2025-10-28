# [Infrastructure Name] - Quick Reference

## Terraform Commands

### Initialize
```bash
terraform init                    # Initialize working directory
terraform init -upgrade          # Upgrade providers
terraform init -reconfigure      # Reconfigure backend
```

### Plan
```bash
terraform plan                   # Show execution plan
terraform plan -out=tfplan      # Save plan to file
terraform plan -destroy         # Plan destruction
terraform plan -target=[addr]   # Plan specific resource
terraform plan -var="key=value" # Override variable
```

### Apply
```bash
terraform apply                  # Apply changes
terraform apply tfplan          # Apply saved plan
terraform apply -auto-approve   # Skip confirmation (use carefully!)
terraform apply -target=[addr]  # Apply to specific resource
```

### Destroy
```bash
terraform destroy               # Destroy all resources
terraform destroy -target=[addr] # Destroy specific resource
terraform destroy -auto-approve # Skip confirmation (dangerous!)
```

### State Management
```bash
terraform state list            # List all resources
terraform state show [addr]     # Show resource details
terraform state pull            # Download state
terraform state push [file]     # Upload state
terraform state mv [src] [dst]  # Move resource
terraform state rm [addr]       # Remove from state
terraform state replace-provider # Replace provider
```

### Import
```bash
terraform import [addr] [id]    # Import existing resource
```

### Output
```bash
terraform output                # Show all outputs
terraform output [name]         # Show specific output
terraform output -json          # JSON format
```

### Workspace
```bash
terraform workspace list        # List workspaces
terraform workspace show        # Show current workspace
terraform workspace new [name]  # Create workspace
terraform workspace select [name] # Switch workspace
terraform workspace delete [name] # Delete workspace
```

### Validation & Formatting
```bash
terraform validate              # Validate configuration
terraform fmt                   # Format files
terraform fmt -recursive        # Format all files
terraform fmt -check            # Check if formatted
```

### Other
```bash
terraform refresh               # Refresh state
terraform graph                 # Generate dependency graph
terraform force-unlock [id]     # Unlock state
terraform taint [addr]          # Mark for recreation (deprecated)
terraform untaint [addr]        # Remove taint mark (deprecated)
terraform apply -replace=[addr] # Force replacement (new way)
```

## Key Resources

### [Resource Category 1]

| Resource | Type | Address | Description |
|----------|------|---------|-------------|
| [Name] | [Type] | `[resource_address]` | [What it does] |
| [Name] | [Type] | `[resource_address]` | [What it does] |

### [Resource Category 2]

| Resource | Type | Address | Description |
|----------|------|---------|-------------|
| [Name] | [Type] | `[resource_address]` | [What it does] |
| [Name] | [Type] | `[resource_address]` | [What it does] |

## Variables

### Required Variables

| Variable | Type | Description | Example |
|----------|------|-------------|---------|
| `[var_name]` | `string` | [Description] | `"example"` |
| `[var_name]` | `number` | [Description] | `5` |
| `[var_name]` | `list(string)` | [Description] | `["a", "b"]` |

### Optional Variables

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `[var_name]` | `string` | `"default"` | [Description] |
| `[var_name]` | `bool` | `true` | [Description] |
| `[var_name]` | `map(string)` | `{}` | [Description] |

### Setting Variables

```bash
# Command line
terraform apply -var="key=value"

# Variable file
terraform apply -var-file="prod.tfvars"

# Environment variable
export TF_VAR_[name]=[value]
terraform apply
```

## Outputs

| Output | Type | Description | Usage Example |
|--------|------|-------------|---------------|
| `[output_name]` | `string` | [Description] | `terraform output [name]` |
| `[output_name]` | `list` | [Description] | `terraform output -json [name]` |

## File Structure

```
.
├── main.tf                 # Main resource definitions
├── variables.tf            # Input variable declarations
├── outputs.tf              # Output value declarations
├── providers.tf            # Provider configurations
├── versions.tf             # Version constraints
├── terraform.tfvars        # Variable values (gitignored)
├── terraform.tfvars.example # Example variables
├── backend.tf              # Backend configuration (optional)
└── modules/
    └── [module-name]/
        ├── main.tf
        ├── variables.tf
        ├── outputs.tf
        └── README.md
```

## Common Patterns

### Get Resource ID/ARN
```bash
# Show full resource
terraform state show [resource_address]

# Extract specific attribute
terraform state show [resource_address] | grep [attribute]

# Using outputs
terraform output [output_name]
```

### Find Resources by Type
```bash
terraform state list | grep [resource_type]

# Example:
terraform state list | grep aws_instance
```

### Refresh State
```bash
# Check for drift
terraform plan -refresh-only

# Apply drift to state
terraform apply -refresh-only
```

### Target Specific Resource
```bash
# Plan
terraform plan -target=[resource_address]

# Apply
terraform apply -target=[resource_address]

# Destroy
terraform destroy -target=[resource_address]
```

### Force Resource Replacement
```bash
# New method (recommended)
terraform apply -replace=[resource_address]

# Old method (deprecated)
terraform taint [resource_address]
terraform apply
```

### Working with Modules
```bash
# Initialize with modules
terraform init

# Update modules
terraform get -update

# Show module tree
terraform providers
```

## Cloud Provider CLI Commands

### [AWS/Azure/GCP] Basics

```bash
# Verify authentication
[provider auth command]

# List resources
[list resources command]

# Get resource details
[get resource command]

# Common queries
[useful query commands]
```

### Resource Verification

```bash
# Verify specific resources exist
[verification commands]

# Get resource IDs
[ID retrieval commands]

# Check resource status
[status commands]
```

## Troubleshooting Quick Fixes

### State Lock
```bash
# Check lock
[provider-specific command]

# Force unlock (careful!)
terraform force-unlock [lock-id]
```

### Provider Issues
```bash
# Re-initialize
terraform init -upgrade

# Clear cache
rm -rf .terraform
terraform init
```

### Resource Drift
```bash
# Detect drift
terraform plan -refresh-only

# Import resource
terraform import [address] [id]

# Remove from state
terraform state rm [address]
```

### Debug Mode
```bash
# Enable debug logging
export TF_LOG=DEBUG
export TF_LOG_PATH=./terraform.log
terraform apply

# Disable
unset TF_LOG
unset TF_LOG_PATH
```

### Module Issues
```bash
# Update modules
terraform get -update

# Re-initialize
rm -rf .terraform/modules
terraform init
```

## Useful Snippets

### Backend Configuration

```hcl
# S3 Backend (AWS)
terraform {
  backend "s3" {
    bucket = "terraform-state"
    key    = "path/to/state"
    region = "us-east-1"
  }
}

# Azure Backend
terraform {
  backend "azurerm" {
    storage_account_name = "tfstate"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
  }
}

# GCS Backend (GCP)
terraform {
  backend "gcs" {
    bucket = "terraform-state"
    prefix = "terraform/state"
  }
}
```

### Variable Definitions

```hcl
# String variable
variable "environment" {
  description = "Environment name"
  type        = string
  default     = "dev"
}

# Number variable
variable "instance_count" {
  description = "Number of instances"
  type        = number
  default     = 2
}

# List variable
variable "availability_zones" {
  description = "AZs to use"
  type        = list(string)
  default     = ["us-east-1a", "us-east-1b"]
}

# Map variable
variable "tags" {
  description = "Resource tags"
  type        = map(string)
  default     = {}
}

# Object variable
variable "database_config" {
  description = "Database configuration"
  type = object({
    instance_class = string
    storage_gb     = number
    multi_az       = bool
  })
}
```

### Output Definitions

```hcl
# Simple output
output "instance_id" {
  description = "EC2 instance ID"
  value       = aws_instance.main.id
}

# List output
output "subnet_ids" {
  description = "Subnet IDs"
  value       = aws_subnet.private[*].id
}

# Sensitive output
output "db_password" {
  description = "Database password"
  value       = random_password.db.result
  sensitive   = true
}
```

## Environment Variables

### Terraform
```bash
export TF_LOG=[TRACE|DEBUG|INFO|WARN|ERROR]  # Logging level
export TF_LOG_PATH=./terraform.log           # Log file
export TF_INPUT=false                        # Disable prompts
export TF_VAR_[name]=[value]                 # Set variable
export TF_CLI_ARGS_[command]="[args]"        # Command args
```

### [Cloud Provider]
```bash
export [AUTH_VAR]=[value]       # Authentication
export [REGION_VAR]=[value]     # Default region
export [CONFIG_VAR]=[value]     # Configuration
```

## Links

- [Architecture Docs](ARCHITECTURE.md)
- [Operations Runbook](RUNBOOK.md)
- [Module README](README.md)
- [Terraform Docs](https://terraform.io/docs)
- [Provider Docs]([provider-url])

## Quick Start

```bash
# 1. Initialize
terraform init

# 2. Configure variables
cp terraform.tfvars.example terraform.tfvars
vim terraform.tfvars

# 3. Plan
terraform plan -out=tfplan

# 4. Apply
terraform apply tfplan

# 5. View outputs
terraform output
```

## Emergency Contacts

| Issue Type | Contact |
|------------|---------|
| Critical Outage | [Contact] |
| Security Incident | [Contact] |
| General Support | [Contact] |
