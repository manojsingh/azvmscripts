import psutil, requests, datetime, json
from logconfig import logger
from configuration import config
from vminstance import VMInstance

def collect_metrics():
    logger.warning("Collecting Metrics .....")

    global cpu_percent = psutil.cpu_percent()
    global memory_percent = psutil.virtual_memory()[2]
    logger.warning("Current CPU utilization is %s percent.  " % cpu_percent)
    logger.warning("Current memory utilization is %s percent. " % memory_percent)


def post_metrics():
    logger.warning("Posting Custom metrics")

    metric_post_url = config.get('monitor', 'metric_post_url')

    formatted_url = metric_post_url.format(subscriptionId = vmInstance.subscriptionId, \
         resourceGroupName = vmInstance.resourceGroupName,\
             resourceName = vmInstance.name)


    data = getMetricPostData()
    formatted_data = data.format(timestamp = datetime.datetime.now().isoformat(),\
                                cpu_percent = cpu_percent, memory_percent = memory_percent)

    headers = config.get('monitor', 'metric_headers');
    formatted_headers = headers.format(clength = len(formatted_data), token = vmInstance.access_token)

    requests.post(formatted_url, data=json.dumps(formatted_data), headers=formatted_headers)

def getMetricPostData():
    data = """
           {
               "time": "{timestamp}",
                "data": {
                    "baseData": {
                        "metric": "VM Info",
                        "namespace": "Custom Metric",
                        "dimNames": [
                             "CPU Utilization Percentage",
                             "Memory Utilized Percentage
                        ],
                        "series": [
                            {
                                "dimValues": [
                                    "{cpu_percent}",
                                    "{memory_percent}",
                                ]
                            }
                        ]
                    }
                }
            }
        """
    return data


vmInstance = VMInstance().populate()
collect_metrics()
post_metrics()