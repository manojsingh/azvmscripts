#!/usr/bin/python3

import psutil, requests, datetime, json
from logconfig import logger
from configuration import config
from vminstance import VMInstance
from bearer_token import BearerAuth

def collect_metrics():
    global cpu_percent
    logger.info("Collecting Metrics .....")

    cpu_percent = psutil.cpu_percent()
    logger.info("Current CPU utilization is %s percent.  " % cpu_percent)

def post_metrics():
    global cpu_percent
    logger.info("Posting Custom metrics.....")

    metric_post_url = config.get('monitor', 'metric_post_url')

    formatted_url = metric_post_url.format(subscriptionId = vmInstance.subscriptionId, \
         resourceGroupName = vmInstance.resourceGroupName,\
             resourceName = vmInstance.name)


    data = getMetricPostData()

    headers = config.get('monitor', 'metric_headers');
    formatted_headers = headers.format(clength = len(data))

    requests.post(formatted_url, data=data, headers=formatted_headers, auth=BearerAuth(vmInstance.access_token))

def getMetricPostData():
    # data = {
    #     'time': datetime.datetime.now().isoformat(),
    #     'data':{
    #         'baseData':{
    #             'metric': 'VM Info',
    #             'namespace': 'Samsung',
    #             'dimNames':[
    #                 "CPU Utilization Percentage"
    #             ],
    #             'series':[
    #                 {
    #                     'dimValue':[
    #                         cpu_percent
    #                     ]
    #                 }
    #             ]
    #         }
    #     }
    # }
    data = "{'time':" + timestamp + "', data : {'baseData': { 'metric': 'VM Info','namespace': 'Samsung', \
                    'dimNames': [ 'CPU Utilization Percentage'], 'series': [{'dimValues': [" + cpu_percent + \
                        "]}]}}}"
        
    return data


vmInstance = VMInstance().populate()
collect_metrics()
post_metrics()