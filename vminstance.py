from configuration import config
from logconfig import logger
import requests, json

class VMInstance:
    '''This is the current VM Instance'''
        
    def __init__(self):
        self.populate()
        # self.access_token = access_token
        # self.subscriptionId = subscriptionId
        # self.vmScaleSetName = vmScaleSetName
        # self.resourceGroupName = resourceGroupName
        # self.vmId = vmId
        # self.tags = tags

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
    
    def populate(self):
        imds_url = config.get('imds', 'imds_url')
        response = requests.get(imds_url, headers={"Metadata":"true"})
        response_txt = json.loads(response.text)
        logger.warning("Response:" + str(response.text))

        #populate required instance variables
        self.vmId = response_txt['vmId']
        self.subscriptionId = response_txt['subscriptionId']
        self.vmScaleSetName = response_txt['vmScaleSetName']
        self.resourceGroupName = response_txt['resourceGroupName']
        self.tags = response_txt['tags']

        #populate access_token
        accesstoken_url = config.get('imds', 'accesstoken_url')

        access_token_response = requests.get(accesstoken_url, headers={"Metadata":"true"})
        access_token_text = json.loads(access_token_response.text)
        self.access_token = access_token_text['access_token']

        #instantiate vmInstance
        #vmInstance = VMInstance(access_token,subscriptionId, vmScaleSetName, resourceGroupName, vmId, tags)

        return self

