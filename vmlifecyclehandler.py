from logconfig import logger
from configuration import config
import requests

def isInstanceinPendingDelete():

    imds_tags_url = config.get('imds', 'imds_tags_url')

    # Call the IMD Service to pull VM tags
    tags = requests.get(imds_tags_url, headers={"Metadata":"true"})
    # tags = 'PendingDelete:true;anothertag:scloud;testtag:123'

    deleteTag = config.get('imds', 'pending_delete_tag')

    if deleteTag in tags:
        logger.warning("Pending Delete is true ...starting custom clean up logic")
    else:
        logger.warning("Pending Delete is false, nothing to do")


    # logger.warning(tags.text)    
    

    
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

