from logconfig import logger
from configuration import config
import requests, json, os

class VMInstance:

    '''This is the current VM Instance'''
        
    def __init__(self, access_token, subscriptionId, vmScaleSetName, resourceGroupName, vmId, tags):
        self.access_token = access_token
        self.subscriptionId = subscriptionId
        self.vmScaleSetName = vmScaleSetName
        self.resourceGroupName = resourceGroupName
        self.vmId = vmId
        self.tags = tags

    def __str__(self):
        return """
                VMInstance:
                     Id - {vmId}
                     SubscriptionId - {subscriptionId}
                     ResourceGroupName - {resourceGroupName}
                     VMScaleSetName - {vmScaleSetName}
                     Tags - {tags}
                     Access-Token - {access_token}
                """.format(
                    vmId = self.vmId,
                    subscriptionId = self.subscriptionId,
                    resourceGroupName = self.resourceGroupName,
                    vmScaleSetName = self.vmScaleSetName,
                    tags = self.tags,
                    access_token = self.access_token
                )



"""
This loads the instance info which can be used at other places for 
calling diffrent Rest Endpoints
"""
def populateInstanceInfo():
    imds_url = config.get('imds', 'imds_url')
    response = requests.get(imds_url, headers={"Metadata":"true"})
    response_txt = json.loads(response.text)
    logger.warning("Response:" + str(response.text))

    #populate required instance variables
    vmId = response_txt['vmId']
    subscriptionId = response_txt['subscriptionId']
    vmScaleSetName = response_txt['vmScaleSetName']
    resourceGroupName = response_txt['resourceGroupName']
    tags = response_txt['tags']

    #populate access_token
    accesstoken_url = config.get('imds', 'accesstoken_url')

    access_token_response = requests.get(accesstoken_url, headers={"Metadata":"true"})
    access_token_text = json.loads(access_token_response.text)
    access_token = access_token_text['access_token']

    #instantiate vmInstance
    vmInstance = VMInstance(access_token,subscriptionId, vmScaleSetName, resourceGroupName, vmId, tags)
    logger.warning(vmInstance)

    logger.warning("VM Instance information populated")


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
     requests.get("http://localhost:900/fail", headers={"Metadata":"true"})

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
    vm_delete_url.format("subscriptionId", "resourceGroupName", "vmScaleSetName")

    logger.warning("The Delete URL is %s", vm_delete_url)


    # # data to be sent to api 
    # data = {'instanceIds ': [API_KEY]}

    # r = requests.post(url = API_ENDPOINT, data = data) 
   


# if(isInstanceinPendingDelete()):
#     logger.warning("Pending Delete is true ...starting custom clean up logic")
#     failLoadBalancerProbes()
#     stopCustomMetricFlow()
#     performCustomOperation()
#     deleteVMFromVMSS()
# else: 
#     logger.warning("Instance not in Pending Delete, nothing to do")
populateInstanceInfo()
#logger.warning(vmInstance)
deleteVMFromVMSS()