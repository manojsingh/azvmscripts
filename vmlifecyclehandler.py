from logconfig import logger
from configuration import config
from vminstance import VMInstance
import requests, json, os

vmInstance = VMInstance().populate()
logger.warning(vmInstance)

"""
Check if the vm needs to be deleted
"""
def isInstanceinPendingDelete():
    deleteTag = config.get('imds', 'pending_delete_tag')

    if deleteTag in vmInstance.tags.text:
        return True
    else:
        return False

"""
    Here is where we need to put all the custom tasks that need to be performed
"""
def  performCustomOperation():
    logger.warning("Performing custom operation")

    ## This is where the custom logic will go


"""
This will call the health Probe URL and fail it
"""
def failLoadBalancerProbes():
    logger.warning("Failing Health Probes")
    requests.get("http://localhost:900/fail")

"""
This will kill the cron job which collects and submits custom metric to Azure Monitor
"""
def stopCustomMetricFlow():
    logger.warning("Stopping the Custom Metrics")
    removeCrontab = config.get('shell-commands', 'remove_all_crontab')

    #removeCrontab = "crontab -r"
    
    logger.warning("Deleting all cron jobs")
   
    # Delete all cron jobs
    areCronsRemoved = os.system(removeCrontab)

"""
Call the VMSS Rest API to Delete the VM
"""
def deleteVMFromVMSS():
    logger.warning("Deleting the VM from VMSS")

    vm_delete_url =  config.get('vmss', 'vm_delete_url')
    formatted_url = vm_delete_url.format(subscriptionId = vmInstance.subscriptionId, \
         resourceGroupName = vmInstance.resourceGroupName,\
              vmScaleSetName = vmInstance.vmScaleSetName, instanceId = vmInstance.vmId)

    logger.warning("The Delete URL is - " +  formatted_url)

    requests.delete(formatted_url, data={})

if(isInstanceinPendingDelete()):
    logger.warning("Pending Delete is true ...starting custom clean up logic")
    failLoadBalancerProbes()
    stopCustomMetricFlow()
    performCustomOperation()
    deleteVMFromVMSS()
else: 
    logger.warning("Instance not in Pending Delete, nothing to do")


