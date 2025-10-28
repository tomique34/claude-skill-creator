# [Infrastructure Name] - Operations Runbook

## Quick Reference

| Item | Value |
|------|-------|
| Cloud Provider | [AWS/Azure/GCP] |
| Account/Subscription | [ID] |
| Region | [primary region] |
| Environment | [prod/staging/dev] |
| Terraform Backend | [S3/Azure Storage/GCS location] |
| State Lock | [DynamoDB/other] |

## Prerequisites

### Required Tools
- Terraform >= [version]
- [Cloud CLI] configured and authenticated
- [Additional tools]

### Required Access
- [Cloud account] with [specific permissions]
- Access to Terraform state backend
- [VPN/bastion access if needed]

### Required Credentials
- [Credential type 1]
- [Credential type 2]

## Initial Deployment

### Step 1: Environment Setup

```bash
# Install required tools
[installation commands]

# Configure cloud provider credentials
[configuration commands]

# Verify access
[verification commands]
```

### Step 2: Configure Backend

```bash
# Initialize Terraform with backend configuration
terraform init \
  -backend-config="[config-key]=[value]" \
  -backend-config="[config-key]=[value]"
```

### Step 3: Configure Variables

```bash
# Copy example variables file
cp terraform.tfvars.example terraform.tfvars

# Edit with your values
# Required variables:
# - [var1]: [description]
# - [var2]: [description]
# - [var3]: [description]
```

### Step 4: Review Plan

```bash
# Validate configuration
terraform validate

# Create execution plan
terraform plan -out=tfplan

# Review the plan carefully before proceeding
# Check:
# - Resource counts
# - Naming conventions
# - Cost implications
# - Security configurations
```

### Step 5: Deploy Infrastructure

```bash
# Apply the plan
terraform apply tfplan

# Note: This may take [X] minutes

# Verify outputs
terraform output

# Test connectivity/accessibility
[verification commands]
```

### Step 6: Post-Deployment Verification

```bash
# Verify critical resources
[verification commands]

# Check monitoring/logging
[verification commands]

# Run smoke tests
[test commands]
```

## Daily Operations

### Viewing Current State

```bash
# Show current infrastructure state
terraform show

# List all resources
terraform state list

# Show specific resource details
terraform state show [resource_address]

# View outputs
terraform output
terraform output [specific_output]
```

### Making Changes

#### Standard Change Process

```bash
# 1. Create/update .tf files or variables

# 2. Format code
terraform fmt

# 3. Validate syntax
terraform validate

# 4. Create plan
terraform plan -out=tfplan

# 5. Review plan
# - What's being added/changed/destroyed?
# - Are there unintended changes?
# - Impact on running systems?

# 6. Apply changes
terraform apply tfplan

# 7. Verify changes
[verification commands]

# 8. Document changes
git commit -m "Description of changes"
```

#### Emergency Changes

```bash
# For urgent fixes only
terraform apply -auto-approve

# Always followed by:
# - Immediate verification
# - Team notification
# - Post-incident documentation
```

### Checking Resource Status

```bash
# Cloud provider specific commands
[provider CLI commands to check resources]

# Example for AWS:
# aws ec2 describe-instances
# aws rds describe-db-instances
# aws ecs list-services

# Example for Azure:
# az vm list
# az sql db list
# az aks list
```

## Common Tasks

### Task 1: [Common Task Name]

**When to do this**: [scenario]

**Procedure**:
```bash
# Step 1
[command]

# Step 2
[command]

# Step 3
[command]

# Verification
[verification command]
```

**Expected outcome**: [what should happen]

### Task 2: Scaling Resources

**Scale Up**:
```bash
# Update capacity variable
terraform apply -var="[capacity_var]=[new_value]"

# Or edit terraform.tfvars and apply
terraform apply
```

**Scale Down**:
```bash
# WARNING: Ensure no active traffic/workload before scaling down

# Update capacity
terraform apply -var="[capacity_var]=[lower_value]"
```

### Task 3: Updating Security Groups/Firewall Rules

```bash
# 1. Update security group rules in main.tf or security.tf

# 2. Plan to see exact changes
terraform plan

# 3. Apply
terraform apply

# 4. Test connectivity
[test commands]
```

### Task 4: Database Operations

**Backup**:
```bash
# Trigger manual backup
[backup command]
```

**Restore**:
```bash
# WARNING: This will affect production data

# 1. Identify restore point
[list backups command]

# 2. Restore
[restore command]

# 3. Verify
[verification command]
```

### Task 5: Rotating Secrets/Credentials

```bash
# 1. Generate new credentials
[generation command]

# 2. Update in secrets manager
[update command]

# 3. Trigger resource update
terraform apply -replace="[resource_address]"

# 4. Verify new credentials work
[test command]

# 5. Revoke old credentials
[revocation command]
```

### Task 6: Adding New Environment

```bash
# 1. Create new workspace (optional)
terraform workspace new [env-name]

# 2. Create environment-specific tfvars
cp production.tfvars [env-name].tfvars

# 3. Edit variables
vim [env-name].tfvars

# 4. Deploy
terraform apply -var-file=[env-name].tfvars
```

## Troubleshooting

### Issue 1: State Lock Error

**Symptoms**:
```
Error: Error acquiring the state lock
```

**Diagnosis**:
```bash
# Check lock table
[provider-specific command to view locks]

# Get lock info
terraform force-unlock -help
```

**Solution**:
```bash
# Verify no one else is running terraform
# Contact team to confirm

# Force unlock (use with extreme caution)
terraform force-unlock [lock-id]
```

**Prevention**: Communicate with team before running terraform

### Issue 2: Resource Creation Fails

**Symptoms**: Apply fails with error creating specific resource

**Diagnosis**:
```bash
# Enable debug logging
export TF_LOG=DEBUG
terraform apply 2>&1 | tee terraform-debug.log

# Check service limits
[command to check quotas]

# Verify IAM permissions
[command to check permissions]

# Check resource dependencies
terraform graph | dot -Tpng > graph.png
```

**Solutions**:

1. **Service Limit**: Request limit increase
2. **Permission Issue**: Add required IAM permissions
3. **Dependency Issue**: Fix resource dependencies
4. **Transient Error**: Retry after a few minutes

### Issue 3: Drift Detected

**Symptoms**: `terraform plan` shows changes when none were made

**Diagnosis**:
```bash
# Identify what changed
terraform plan -refresh-only

# Check recent changes in cloud console
[provider audit log commands]
```

**Solutions**:

**Option 1 - Update Terraform to Match Reality**:
```bash
# Import changes to state
terraform apply -refresh-only
```

**Option 2 - Revert Manual Changes**:
```bash
# Re-apply Terraform config
terraform apply
```

### Issue 4: Failed Destroy

**Symptoms**: `terraform destroy` fails

**Common Causes**:
- Dependencies preventing deletion
- Protection settings
- Resources created outside Terraform

**Solution**:
```bash
# 1. Identify blocking resources
terraform destroy

# 2. Remove dependencies manually
[provider-specific deletion commands]

# 3. Remove from state
terraform state rm [resource_address]

# 4. Retry destroy
terraform destroy
```

### Issue 5: Performance Degradation

**Symptoms**: Infrastructure performing poorly

**Diagnosis**:
```bash
# Check monitoring dashboards
[monitoring commands]

# Check resource utilization
[utilization commands]

# Review recent changes
git log --oneline -10
```

**Solutions**: [Environment-specific troubleshooting]

## Disaster Recovery

### Scenario 1: Complete Infrastructure Loss

**Recovery Steps**:

1. **Retrieve State File**:
   ```bash
   # State should be in backend
   terraform init
   terraform state pull > verify-state.json
   ```

2. **Verify State Integrity**:
   ```bash
   terraform state list
   ```

3. **Rebuild Infrastructure**:
   ```bash
   terraform apply
   ```

4. **Restore Data**:
   ```bash
   [data restoration commands]
   ```

### Scenario 2: State File Corruption

**Recovery**:
```bash
# List available state versions
[backend-specific list versions command]

# Download previous version
[download command]

# Restore state
terraform state push [backup-file]
```

### Scenario 3: Accidental Resource Deletion

**Recovery**:

1. **Don't Panic**
2. **Check if backed up**
3. **Restore from backup if available**
4. **Otherwise recreate**:
   ```bash
   terraform apply
   ```

## Maintenance Windows

### Scheduled Maintenance

**Before Maintenance**:
```bash
# 1. Notify stakeholders
# 2. Create state backup
terraform state pull > backup-$(date +%Y%m%d-%H%M%S).tfstate

# 3. Create plan
terraform plan -out=tfplan

# 4. Review and approve plan
```

**During Maintenance**:
```bash
# 1. Apply changes
terraform apply tfplan

# 2. Monitor
[monitoring commands]

# 3. Verify
[verification commands]
```

**After Maintenance**:
```bash
# 1. Verify everything works
[smoke tests]

# 2. Update documentation
# 3. Notify stakeholders
```

### Rollback Procedure

```bash
# Option 1: Revert code and re-apply
git revert [commit-hash]
terraform apply

# Option 2: Restore state
terraform state push [backup-file]

# Option 3: Targeted rollback
terraform apply -replace="[resource_address]"
```

## Monitoring

### Key Metrics

| Metric | Threshold | Action |
|--------|-----------|--------|
| [Metric 1] | [Warning/Critical] | [What to do] |
| [Metric 2] | [Warning/Critical] | [What to do] |

### Accessing Logs

```bash
# Application logs
[log access command]

# Infrastructure logs
[log access command]

# Audit logs
[log access command]
```

### Health Checks

```bash
# Automated health check script
[health check command]

# Manual verification
[manual check commands]
```

## Decommissioning

### Pre-Destruction Checklist

- [ ] All stakeholders notified
- [ ] Data backed up and verified
- [ ] Dependencies identified and handled
- [ ] Final state backup created
- [ ] Approval obtained

### Destruction Procedure

```bash
# 1. Create final backup
terraform state pull > final-state-$(date +%Y%m%d).tfstate

# 2. Backup critical data
[backup commands]

# 3. Plan destroy
terraform plan -destroy

# 4. Review what will be destroyed
# Verify each resource

# 5. Destroy infrastructure
terraform destroy

# 6. Verify deletion
[verification commands]

# 7. Clean up backend
[cleanup commands]

# 8. Archive documentation
```

## Emergency Contacts

| Role | Name | Contact | Availability |
|------|------|---------|--------------|
| Primary On-Call | [Name] | [Phone/Email] | 24/7 |
| Secondary On-Call | [Name] | [Phone/Email] | 24/7 |
| Manager | [Name] | [Email] | Business hours |
| Cloud Support | [Provider] | [Support link] | 24/7 |

## Escalation Procedure

1. **Severity 1** (Critical): Contact primary on-call immediately
2. **Severity 2** (High): Contact primary on-call, escalate if no response in 30min
3. **Severity 3** (Medium): Create ticket, contact during business hours
4. **Severity 4** (Low): Create ticket for next sprint

## References

- [Architecture Documentation](ARCHITECTURE.md)
- [Module README](README.md)
- [Quick Reference](QUICK_REFERENCE.md)
- [Terraform Documentation](https://terraform.io/docs)
- [Provider Documentation]([provider-docs-url])

## Appendix

### Environment Variables

```bash
# Terraform
export TF_LOG=[DEBUG|INFO|WARN|ERROR]
export TF_LOG_PATH=./terraform.log

# Cloud Provider
export [PROVIDER_CONFIG_VAR]=[value]
```

### Useful Commands Reference

```bash
# [Category]
[command] # [description]
[command] # [description]

# [Category]
[command] # [description]
[command] # [description]
```

## Revision History

| Date | Version | Author | Changes |
|------|---------|--------|---------|
| YYYY-MM-DD | 1.0 | [Name] | Initial runbook |
