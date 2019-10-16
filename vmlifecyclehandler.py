from logconfig import logger
from configuration import config

def isInstanceinPendingDelete():

    
    imds_url = config.get('imds', 'imds_url')
    logger.warning(imds_url)    
    # import requests

    # resp = requests.get('http://localhost:8080/hello')
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

