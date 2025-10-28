# [Module Name]

## Overview

[Brief description of what this module creates and its purpose]

## Architecture

[Simple description or ASCII diagram of resources created and their relationships]

## Usage

### Basic Example

```hcl
module "example" {
  source = "./modules/[module-name]"

  # Required variables
  [var1] = "[value1]"
  [var2] = "[value2]"
}
```

### Complete Example

```hcl
module "example" {
  source = "./modules/[module-name]"

  # Required
  [var1] = "[value1]"
  [var2] = "[value2]"

  # Optional
  [var3] = "[value3]"
  [var4] = "[value4]"

  tags = {
    Environment = "production"
    ManagedBy   = "terraform"
  }
}
```

## Requirements

| Name | Version |
|------|---------|
| terraform | >= 1.0 |
| [provider] | >= [version] |

## Providers

| Name | Version |
|------|---------|
| [provider] | >= [version] |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| [var1] | [description] | `string` | n/a | yes |
| [var2] | [description] | `number` | `10` | no |
| [var3] | [description] | `list(string)` | `[]` | no |
| [var4] | [description] | `bool` | `true` | no |

## Outputs

| Name | Description |
|------|-------------|
| [output1] | [description and example usage] |
| [output2] | [description and example usage] |

## Resources Created

- **[resource_type]** ([resource_name]): [description of what it does and why]
- **[resource_type]** ([resource_name]): [description of what it does and why]

## Security Considerations

- [Security aspect 1 - e.g., encryption, access control]
- [Security aspect 2 - e.g., network isolation]
- [Security aspect 3 - e.g., IAM policies]

## Cost Considerations

[Description of what will incur costs and approximate monthly costs]

Example:
- [Resource type]: ~$XX/month per instance
- [Resource type]: ~$XX/month
- **Estimated total**: ~$XX/month for default configuration

## Examples

See the [examples](examples/) directory for:
- [Example 1 name and description]
- [Example 2 name and description]

## Limitations

- [Known limitation 1]
- [Known limitation 2]

## Related Modules

- [Related module 1]: [Brief description]
- [Related module 2]: [Brief description]

## License

[License information]

## Authors

[Author/team information]

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history.
