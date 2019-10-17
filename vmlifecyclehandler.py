from logconfig import logger
from configuration import config
import requests, json, os

global access_token, subscriptionId , vmScaleSetName, resourceGroupName

def populateInstanceInfo():
    access_token_url = config.get('imds', 'accesstoken_url')
    response = requests.get(access_token_url, headers={"Metadata":"true"})
    response_txt = json.loads(response.text)

    #populate required instance variables
    access_token = response_txt['access_token']
    subscriptionId = response_txt['subscriptionId']
    vmScaleSetName = response_txt['vmScaleSetName']
    resourceGroupName = response_txt['resourceGroupName']

    logger.warning(access_token)
    return token


def isInstanceinPendingDelete():
    imds_tags_url = config.get('imds', 'imds_tags_url')

    # Call the IMD Service to pull VM tags
    tags = requests.get(imds_tags_url, headers={"Metadata":"true"})
    #tags = 'PendingDelete:true;anothertag:scloud;testtag:123'

    deleteTag = config.get('imds', 'pending_delete_tag')

    if deleteTag in tags.text:
        return True
    else:
        return False

def  performCustomOperation():
    logger.warning("Performing custom operation")

    ## This is where the custom logic will go

def failLoadBalancerProbes():
    logger.warning("Failing Health Probes")

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
   


if(isInstanceinPendingDelete()):
    logger.warning("Pending Delete is true ...starting custom clean up logic")
    failLoadBalancerProbes()
    performCustomOperation()
    stopCustomMetricFlow()
    deleteVMFromVMSS()
else: 
    logger.warning("Intance not in Pending Delete, nothing to do")