# AZVM Scripts
Contains scripts to be used in Azure VMs

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fmanojsingh%2Fazvmscripts%2Fmaster%2Fazuredeploy.json" target="_blank">
<img src="https://raw.githubusercontent.com/Azure/azure-quickstart-templates/master/1-CONTRIBUTION-GUIDE/images/deploytoazure.png"/>
</a>

This template allows deploying a linux VM using new or existing resources for the Virtual Network, Storage and Public IP Address.  It also injects the custom script into the VM, configures cron jobs which will run the scripts as per the configuration.

# Custom Metric Handler
Main custom metric handler is metric_collector.py which contains methods for collecting and posting metrics. Any custom related logic will go into this file.

# Polling IMDS and initiating the deletion process


# logs
All the activity is logged in a file called - azvmscripts.log

This Readme file is still a work in progress (though deploy button should work)....
