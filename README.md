# Azure Native Python Pulumi Template

A minimal Pulumi template for provisioning an Azure Resource Group and a Storage Account using the Azure Native provider with Python.

## Updated Overview

This template demonstrates:

- Provider: `pulumi-azure-native`
- Resources:
  - `azure-native:resources:ResourceGroup` — a new resource group
  - `azure-native:storage:StorageAccount` — a storage account in the resource group
- Output:
  - `primary_storage_key` — the primary key of the storage account

### Key Features

- **Security**: Uses managed identity for authentication, avoiding hardcoded credentials.
- **Scalability**: Designed to be extended with additional Azure services.
- **Best Practices**: Follows Azure's recommended guidelines for resource management and deployment.

## Updated Prerequisites

- An Azure subscription with sufficient permissions
- Azure CLI installed and authenticated (`az login`)
- Python 3.7 or later
- Pulumi CLI installed (`https://www.pulumi.com/docs/get-started/install/`)

## Updated Usage

1. Create a new project from this template:

    ```bash
    pulumi new azure-python
    ```

2. When prompted, enter your project name, description, and Azure location. The default `azure-native:location` is `WestUS2`.

3. Preview the stack to validate changes:

    ```bash
    pulumi preview
    ```

4. Deploy the stack:

    ```bash
    pulumi up
    ```

5. After deployment, retrieve the primary storage key:

    ```bash
    pulumi stack output primary_storage_key
    ```

## Project Layout

```plaintext
.
├── __main__.py        # Pulumi program defining your infrastructure
├── Pulumi.yaml        # Project settings and template metadata
└── requirements.txt   # Python dependencies (Pulumi SDK and provider)
```

## Updated Configuration

This template exposes the following configuration variable:

- `azure-native:location` — Azure region to deploy resources. Defaults to `WestUS2`.

Set or override it with:

```bash
pulumi config set azure-native:location eastus
```

## Outputs

After deployment, the following output is available:

- `primary_storage_key` — the primary access key for the storage account

Retrieve it with:

```bash
pulumi stack output primary_storage_key
```

## When to Use This Template

- You want a quick Azure infrastructure starter with Pulumi and Python
- You're learning infrastructure-as-code patterns on Azure
- You need a simple storage account setup to build applications

## Updated Next Steps

- Customize resource names and add more Azure services (e.g., Virtual Networks, Key Vault).
- Explore the `pulumi-azure-native` documentation for available services.
- Migrate this template into a larger multi-stack setup.
- Implement monitoring and logging for deployed resources using Azure Monitor.

## Getting Help

- Pulumi Documentation: https://www.pulumi.com/docs/
- Azure Native Provider Reference: https://www.pulumi.com/registry/packages/azure-native/
- Community Support: https://pulumi.com/community/