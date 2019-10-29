import psutil
import requests
from logconfig import logger



def collect_metrics():
    logger.warning("Collecting Metrics .....")

    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory()[2]
    logger.warning("Current CPU utilization is %s percent.  " % cpu_percent)
    logger.warning("Current memory utilization is %s percent. " % memory_percent)


def post_metrics():
    logger.warning("Posting metrics")


collect_metrics()
post_metrics()
