"""An Azure RM Python Pulumi program"""

import pulumi
from pulumi_azure_native import storage
from pulumi_azure_native import resources
from pulumi_azure_native import containerservice

# Create an Azure Resource Group
resource_group = resources.ResourceGroup("resource_group")

# Create an Azure resource (Storage Account)
account = storage.StorageAccount(
    "sa",
    resource_group_name=resource_group.name,
    sku={
        "name": storage.SkuName.STANDARD_LRS,
    },
    kind=storage.Kind.STORAGE_V2,
)

# Export the primary key of the Storage Account
primary_key = (
    pulumi.Output.all(resource_group.name, account.name)
    .apply(
        lambda args: storage.list_storage_account_keys(
            resource_group_name=args[0], account_name=args[1]
        )
    )
    .apply(lambda accountKeys: accountKeys.keys[0].value)
)

pulumi.export("primary_storage_key", primary_key)

# Create an Azure Kubernetes Service (AKS) cluster
aks_cluster = containerservice.ManagedCluster(
    "aksCluster",
    resource_group_name=resource_group.name,
    agent_pool_profiles=[
        containerservice.ManagedClusterAgentPoolProfileArgs(
            name="agentpool",
            count=2,
            vm_size="Standard_DS2_v2",
            os_type="Linux",
            mode="System",
        )
    ],
    dns_prefix=resource_group.name.apply(lambda name: f"{name}-dns"),
    identity=containerservice.ManagedClusterIdentityArgs(
        type="SystemAssigned"
    ),
    enable_rbac=True,
)

# Export the AKS cluster name
pulumi.export("aks_cluster_name", aks_cluster.name)
