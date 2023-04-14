# import requests, time
# from prometheus_client import Gauge, CollectorRegistry, Enum, Info
# import jobv2_readiness_get
# import datetime


# class supernaMetrics:
#     def __init__(self):
#         self.define_jobv2_readiness()
    
#     def define_jobv2_readiness(self):
#         labels = ["name", "started", "finished", "state", 'status']
#         self.get_readiness_zone = Gauge('get_readiness_zone', 'Zone readiness status', labels)

#     def parse_jobv2_readiness(self, data):
#         self.get_readiness_zone._metrics.clear()
#         if data is not None:
#             for status in data:
#                 if status['status'] == 'OK':
#                     value = 1
#                 else:
#                     value = 0
#                 if status['started']:
#                     value = time.strftime('%Y-%m-%d %H:%M:%S %z', time.localtime(status['started']/1000))
#                 if status['finished']:   
#                     value = time.strftime('%Y-%m-%d %H:%M:%S %z', time.localtime(status['finished']/1000))
#                 self.get_readiness_zone.labels(name=status['name'], status=status['status'], state=status['state'], 
#                                                started=status['started'], finished=status['finished'])
        
    # def parse_metrics(self):
    #     data = jobv2_readiness_get.run()
    #     self.parse_jobv2_readiness(data['get_jobv2_readiness'])

# def parse_jobv2_readiness():
#     data = jobv2_readiness_get.run()
#     registry = CollectorRegistry()
#     labels = ["name", "started", "finished", "state", 'status']
#     get_readiness_zone = Gauge('get_readiness_zone', 'Zone readiness status', labels, registry=registry)
#     get_readiness_zone._metrics.clear()
#     for job_data in data['get_jobv2_readiness']:
#         if job_data['status'] == 'OK':
#             value = 1
#         else:
#             value = 0
#         if job_data['started']:
#             value = time.strftime('%Y-%m-%d %H:%M:%S %z', time.localtime(job_data['started']/1000))
#         if job_data['finished']:   
#             value = time.strftime('%Y-%m-%d %H:%M:%S %z', time.localtime(job_data['finished']/1000))
#         get_readiness_zone.labels(name=job_data['name'], status=job_data['status'], state=job_data['state'], 
#                                 started=job_data['started'], finished=job_data['finished'])

# def parse_metrics():
#     parse_jobv2_readiness()
