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

    def showInstanceInfo():
        logger.warning(access_token)
        logger.warning(subscriptionId)
        logger.warning(vmScaleSetName)
        logger.warning(resourceGroupName)
        logger.warning(vmId)
        logger.warning(tags)



def populateInstanceInfo():
    imds_url = config.get('imds', 'imds_url')
    response = requests.get(imds_url, headers={"Metadata":"true"})
    response_txt = json.loads(response.text)

    logger.warning(response_txt)

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

    global vmInstance = VMInstance(access_token,subscriptionId, vmScaleSetName, resourceGroupName, vmId, tags)


def isInstanceinPendingDelete():
    #imds_url = config.get('imds', 'imds_url')

    # Call the IMD Service to pull VM tags
    #tags = requests.get(imds_url, headers={"Metadata":"true"})
    #tags = 'PendingDelete:true;anothertag:scloud;testtag:123'

    deleteTag = config.get('imds', 'pending_delete_tag')

    if deleteTag in vmInstance.tags.text:
        return True
    else:
        return False

def  performCustomOperation():
    logger.warning("Performing custom operation")

    ## This is where the custom logic will go

def failLoadBalancerProbes():
    logger.warning("Failing Health Probes")

    requests.get("http://localhost:900/fail", headers={"Metadata":"true"})

def stopCustomMetricFlow():
    logger.warning("Stopping the Custom Metrics")
    removeCrontab = config.get('shell-commands', 'remove_all_crontab')

    #removeCrontab = "crontab -r"
    
    logger.warning("Deleting all cron jobs")
    # Delete all cron jobs
    areCronsRemoved = os.system(removeCrontab)

def deleteVMFromVMSS():
    logger.warning("Deleting the VM from VMSS")

    populateInstanceInfo()

    vm_delete_url =  config.get('vmss', 'vm_delete_url')
    vm_delete_url.format(subscriptionId, resourceGroupName, vmScaleSetName)

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
#     logger.warning("Intance not in Pending Delete, nothing to do")
populateInstanceInfo()
vmInstance.showInstanceInfo()