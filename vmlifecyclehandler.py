from logconfig import logger
from configuration import config

def isInstanceinPendingDelete():

    imds_tags_url = config.get('imds', 'imds_tags_url')

    # Call the IMD Service to pull VM tags
    tags = requests.get('imds_tags_url')

    logger.warning(tags)    
    # import requests

    
    # if resp.status_code != 200:
    #     # This means something went wrong.
    #     raise ApiError('GET /helthCheck/ {}'.format(resp.status_code))
    # logger.warning(resp.text)




#if(isInstanceinPendingDelete)
   # failLBProbes()
    #performCustomOperation()
    #stopCustomMetricFlow()
    #deleteVMFromVMSS()

 
def stopCustomMetricFlow():
    import os
    
    # Delete all cron jobs
    myCmd = 'crontab -r'
    os.system(myCmd)


isInstanceinPendingDelete()

