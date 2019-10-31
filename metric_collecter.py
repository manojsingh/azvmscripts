import psutil
import requests
from logconfig import logger
from configuration import config

def collect_metrics():
    logger.warning("Collecting Metrics .....")

    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory()[2]
    logger.warning("Current CPU utilization is %s percent.  " % cpu_percent)
    logger.warning("Current memory utilization is %s percent. " % memory_percent)


def post_metrics():
    logger.warning("Posting Custom metrics")

    mmetric_post_url = config.get('monitor', 'metric_post_url')
    formatted_url = mmetric_post_url.format(subscriptionId = "testSSID", resourceGroupName = "rgname", resourceProvider = "vmssName", resourceTypeName = "instanceId", resourceName = "resourceName")


    

    # url = "http://localhost:8080"
    # data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
    # headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    # r = requests.post(url, data=json.dumps(data), headers=headers)


collect_metrics()
post_metrics()
