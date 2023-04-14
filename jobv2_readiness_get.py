from __future__ import print_function
import swagger_client
from requests.auth import HTTPBasicAuth
import requests, time, json, logging
from prometheus_client import Gauge, CollectorRegistry, Enum, Info, generate_latest, REGISTRY, Histogram


requests.packages.urllib3.disable_warnings()
API_KEY = "igls-id3004q7fdh54ium70bm5psns2n70fm5mke7l9tpe5gs76lvkv6" 
registry = CollectorRegistry()


def auth_data():
    # Configure API key authorization: internalApiKey
    try: 
        configuration = swagger_client.Configuration()
        host = configuration.host
        username = configuration.username
        password = configuration.password
        headers = {'api_key': F"{API_KEY}"}
        auth = HTTPBasicAuth(F"{username}", F"{password}")
        return host, username, password, headers, auth
    except:
        logging.error("Connection fail to F'{host}'") 

def get_jobv2_readiness():
    host, username, password, headers, auth = auth_data() # define data from auth_data()
    api_url = '%s/v2/jobs/readiness?state=all' % host 
    response = requests.get(F"{api_url}", auth=auth, headers=headers, verify=False)
    data = json.loads(response.text)
    return data

def get_nodev1():
    host, username, password, headers, auth = auth_data() # define data from auth_data()
    api_url = '%s/v1/nodes' % host 
    response = requests.get(F"{api_url}", auth=auth, headers=headers, verify=False)
    data = json.loads(response.text)
    return data
        
def fetch_data():
    try:
        data = {} # list api data from superna
        data['get_jobv2_readiness'] = get_jobv2_readiness()
        data['get_nodev1'] = get_nodev1()
        return data
    except:
        logging.error("Fetching Data Error")
     
def refresh_registry():
    # registry metrics 
    collectors = list(REGISTRY._collector_to_names.keys())
    for collector in collectors:
        registry = REGISTRY.unregister(collector)

def parse_jobv2_readiness():
    data = fetch_data()
    registry = refresh_registry()
    # labels = ["name", "started", "finished", "state", 'status', 'id']
    readiness_zone_state = Enum('readiness_zone_state', 'Zone readiness state', states=['all', 'running', 'finished'])
    readiness_zone_info = Info('readiness_zone_info', 'Zone readiness state')
    readiness_zone_status = Gauge('readiness_zone_status', 'Zone Readiness status')
    readiness_zone_histogram = Histogram('readiness_zone_request_latency_seconds', 'Description of histogram')
    readiness_zone_histogram.observe(4.7) 
    readiness_zone_state.state('all')
    nodev1_info = Info('nodev1_info', 'Node Info')
    if data is not None:
        for job_data in data['get_jobv2_readiness']:
            if job_data['started'] or job_data['finished']:
                started = time.strftime('%Y-%m-%d %H:%M:%S %z', time.localtime(job_data['started']/1000))
                finished = time.strftime('%Y-%m-%d %H:%M:%S %z', time.localtime(job_data['finished']/1000))
                readiness_zone_info.info({'started': F'{started}', 'finished': F'{finished}'})
            if job_data['status'] == 'OK':
                readiness_zone_status.set(1)
            else:
                readiness_zone_status.set(0)
        for job_data in data['get_nodev1']:
            if job_data['name'] or job_data['ip']:
                name = job_data['name']
                ip =  job_data['ip']
                node_id =  job_data['id']
                nodev1_info.info({'name': F'{name}', 'ip': F'{ip}', 'id': F'{node_id}'})
        
def parse_metrics():
    parse_jobv2_readiness()

def get_metrics():
    metrics = generate_latest()
    return metrics
