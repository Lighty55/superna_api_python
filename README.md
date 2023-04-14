# swagger-client
A collection of utilities for programmatic interaction with Superna Eyeglass

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 2.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [http://support.superna.net](http://support.superna.net)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: internalApiKey
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AirgapV2Api(swagger_client.ApiClient(configuration))
order = 'order_example' # str | Optional ordering of results. (optional)
order_by = 'order_by_example' # str | Optional field on which to order results. (optional)
current_page = 56 # int | Current page in an optional paging scheme. (optional)
page_size = 56 # int | Number of results per page in an optional paging scheme. (optional)

try:
    # Get all ECS airgap jobs
    api_response = api_instance.v2_airgap_ecs_get(order=order, order_by=order_by, current_page=current_page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AirgapV2Api->v2_airgap_ecs_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost/sera*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AirgapV2Api* | [**v2_airgap_ecs_get**](docs/AirgapV2Api.md#v2_airgap_ecs_get) | **GET** /v2/airgap/ecs | Get all ECS airgap jobs
*AirgapV2Api* | [**v2_airgap_ecs_post**](docs/AirgapV2Api.md#v2_airgap_ecs_post) | **POST** /v2/airgap/ecs | Update an ECS airgap job status
*AirgapV2Api* | [**v2_airgap_ecssyncjobs_post**](docs/AirgapV2Api.md#v2_airgap_ecssyncjobs_post) | **POST** /v2/airgap/ecssyncjobs | Vault agent ecs-sync jobs upload to eyeglass
*AirgapV2Api* | [**v2_airgap_ecssyncschedules_get**](docs/AirgapV2Api.md#v2_airgap_ecssyncschedules_get) | **GET** /v2/airgap/ecssyncschedules | Get all ECS-sync airgap jobs schedules
*AirgapV2Api* | [**v2_airgap_vaultevents_post**](docs/AirgapV2Api.md#v2_airgap_vaultevents_post) | **POST** /v2/airgap/vaultevents | Vault isilon events
*AirgapV2Api* | [**v2_airgap_vaultheartbeat_post**](docs/AirgapV2Api.md#v2_airgap_vaultheartbeat_post) | **POST** /v2/airgap/vaultheartbeat | Vault agent heartbeat
*AlarmsV1Api* | [**v1_alarms_active_get**](docs/AlarmsV1Api.md#v1_alarms_active_get) | **GET** /v1/alarms/active | Get all active alarms
*AlarmsV1Api* | [**v1_alarms_historical_get**](docs/AlarmsV1Api.md#v1_alarms_historical_get) | **GET** /v1/alarms/historical | Get all historical alarms
*AlarmsV2Api* | [**v2_alarms_post**](docs/AlarmsV2Api.md#v2_alarms_post) | **POST** /v2/alarms/ | Post an alarm to be raised in eyeglass.
*HealthcheckV1Api* | [**v1_healthcheck_get**](docs/HealthcheckV1Api.md#v1_healthcheck_get) | **GET** /v1/healthcheck | Get latest health-check timestamp
*JobV1Api* | [**v1_jobs_drtest_post**](docs/JobV1Api.md#v1_jobs_drtest_post) | **POST** /v1/jobs/drtest | Enter/Exit DR test mode
*JobV1Api* | [**v1_jobs_get**](docs/JobV1Api.md#v1_jobs_get) | **GET** /v1/jobs | Get failover jobs
*JobV1Api* | [**v1_jobs_id_delete**](docs/JobV1Api.md#v1_jobs_id_delete) | **DELETE** /v1/jobs/{id} | cancels a running failover job
*JobV1Api* | [**v1_jobs_id_get**](docs/JobV1Api.md#v1_jobs_id_get) | **GET** /v1/jobs/{id} | Retreive a failover job by ID
*JobV1Api* | [**v1_jobs_id_log_get**](docs/JobV1Api.md#v1_jobs_id_log_get) | **GET** /v1/jobs/{id}/log | Retrieve the logfile for a running or finished failover job
*JobV1Api* | [**v1_jobs_post**](docs/JobV1Api.md#v1_jobs_post) | **POST** /v1/jobs | Create a new failover job
*JobV1Api* | [**v1_jobs_rehearsal_post**](docs/JobV1Api.md#v1_jobs_rehearsal_post) | **POST** /v1/jobs/rehearsal | Create a new rehearsal job
*JobV2Api* | [**v2_jobs_airgap_accessrequest_get**](docs/JobV2Api.md#v2_jobs_airgap_accessrequest_get) | **GET** /v2/jobs/airgap/accessrequest | Eyeglass access requests to vault
*JobV2Api* | [**v2_jobs_airgap_get**](docs/JobV2Api.md#v2_jobs_airgap_get) | **GET** /v2/jobs/airgap | Get all airgap jobs
*JobV2Api* | [**v2_jobs_airgap_id_get**](docs/JobV2Api.md#v2_jobs_airgap_id_get) | **GET** /v2/jobs/airgap/{id} | Retrieves a specific recently run airgap job, if it exists
*JobV2Api* | [**v2_jobs_airgap_post**](docs/JobV2Api.md#v2_jobs_airgap_post) | **POST** /v2/jobs/airgap | Start an airgap job
*JobV2Api* | [**v2_jobs_airgap_status_post**](docs/JobV2Api.md#v2_jobs_airgap_status_post) | **POST** /v2/jobs/airgap/status | post airgap job status
*JobV2Api* | [**v2_jobs_airgap_uploadlogs_post**](docs/JobV2Api.md#v2_jobs_airgap_uploadlogs_post) | **POST** /v2/jobs/airgap/uploadlogs | Uploads the logs under eyeglass logs directory.
*JobV2Api* | [**v2_jobs_failover_drtest_post**](docs/JobV2Api.md#v2_jobs_failover_drtest_post) | **POST** /v2/jobs/failover/drtest | Enter/Exit DR test mode
*JobV2Api* | [**v2_jobs_failover_get**](docs/JobV2Api.md#v2_jobs_failover_get) | **GET** /v2/jobs/failover | Get failover jobs
*JobV2Api* | [**v2_jobs_failover_id_delete**](docs/JobV2Api.md#v2_jobs_failover_id_delete) | **DELETE** /v2/jobs/failover/{id} | 
*JobV2Api* | [**v2_jobs_failover_id_get**](docs/JobV2Api.md#v2_jobs_failover_id_get) | **GET** /v2/jobs/failover/{id} | Retreive a failover job by ID
*JobV2Api* | [**v2_jobs_failover_id_log_get**](docs/JobV2Api.md#v2_jobs_failover_id_log_get) | **GET** /v2/jobs/failover/{id}/log | Retrieve the logfile for a running or finished failover job
*JobV2Api* | [**v2_jobs_failover_post**](docs/JobV2Api.md#v2_jobs_failover_post) | **POST** /v2/jobs/failover | Create a new failover job
*JobV2Api* | [**v2_jobs_failover_rehearsal_post**](docs/JobV2Api.md#v2_jobs_failover_rehearsal_post) | **POST** /v2/jobs/failover/rehearsal | Create a new rehearsal job
*JobV2Api* | [**v2_jobs_readiness_get**](docs/JobV2Api.md#v2_jobs_readiness_get) | **GET** /v2/jobs/readiness | View all recent readiness jobs
*JobV2Api* | [**v2_jobs_readiness_id_get**](docs/JobV2Api.md#v2_jobs_readiness_id_get) | **GET** /v2/jobs/readiness/{id} | Retrieves a specific recently run readiness job, if it exists
*JobV2Api* | [**v2_jobs_readiness_post**](docs/JobV2Api.md#v2_jobs_readiness_post) | **POST** /v2/jobs/readiness | Run zone readiness job
*JobV2Api* | [**v2_jobs_replication_get**](docs/JobV2Api.md#v2_jobs_replication_get) | **GET** /v2/jobs/replication | Get all recent replication jobs
*JobV2Api* | [**v2_jobs_replication_id_get**](docs/JobV2Api.md#v2_jobs_replication_id_get) | **GET** /v2/jobs/replication/{id} | Retrieves a specific replication job, if it was run recently
*JobV2Api* | [**v2_jobs_replication_post**](docs/JobV2Api.md#v2_jobs_replication_post) | **POST** /v2/jobs/replication | Run a configuration replication job
*NodeV1Api* | [**v1_nodes_get**](docs/NodeV1Api.md#v1_nodes_get) | **GET** /v1/nodes | Get all nodes
*NodeV1Api* | [**v1_nodes_id_get**](docs/NodeV1Api.md#v1_nodes_id_get) | **GET** /v1/nodes/{id} | Find nodes by ID
*NodeV1Api* | [**v1_nodes_id_policies_get**](docs/NodeV1Api.md#v1_nodes_id_policies_get) | **GET** /v1/nodes/{id}/policies | Find policies for a node
*NodeV1Api* | [**v1_nodes_id_policies_name_get**](docs/NodeV1Api.md#v1_nodes_id_policies_name_get) | **GET** /v1/nodes/{id}/policies/{name} | Find policy by name
*NodeV1Api* | [**v1_nodes_id_pools_get**](docs/NodeV1Api.md#v1_nodes_id_pools_get) | **GET** /v1/nodes/{id}/pools | Find pools for a node
*NodeV1Api* | [**v1_nodes_id_pools_name_get**](docs/NodeV1Api.md#v1_nodes_id_pools_name_get) | **GET** /v1/nodes/{id}/pools/{name} | Find pool by name 
*NodeV1Api* | [**v1_nodes_id_zones_get**](docs/NodeV1Api.md#v1_nodes_id_zones_get) | **GET** /v1/nodes/{id}/zones | Find zones for a node
*NodeV1Api* | [**v1_nodes_id_zones_name_get**](docs/NodeV1Api.md#v1_nodes_id_zones_name_get) | **GET** /v1/nodes/{id}/zones/{name} | Find zone name for a node
*NodeV2Api* | [**v2_nodes_id_configrep_get**](docs/NodeV2Api.md#v2_nodes_id_configrep_get) | **GET** /v2/nodes/{id}/configrep | Gets all configuration replication jobs for this node
*NodeV2Api* | [**v2_nodes_id_configrep_name_get**](docs/NodeV2Api.md#v2_nodes_id_configrep_name_get) | **GET** /v2/nodes/{id}/configrep/{name} | Gets a specific config replication job.
*NodeV2Api* | [**v2_nodes_id_configrep_name_put**](docs/NodeV2Api.md#v2_nodes_id_configrep_name_put) | **PUT** /v2/nodes/{id}/configrep/{name} | Updates the status and/or type of a specific configuration job
*RansomwareV1Api* | [**v1_ransomware_heartbeat_post**](docs/RansomwareV1Api.md#v1_ransomware_heartbeat_post) | **POST** /v1/ransomware/heartbeat | 
*RansomwareV1Api* | [**v1_ransomware_notification_post**](docs/RansomwareV1Api.md#v1_ransomware_notification_post) | **POST** /v1/ransomware/notification | Send an RDA event to Eyeglass to be handled
*RansomwareV1Api* | [**v1_ransomware_rswevents_get**](docs/RansomwareV1Api.md#v1_ransomware_rswevents_get) | **GET** /v1/ransomware/rswevents | 
*RansomwareV2Api* | [**v2_ransomware_criticalpaths_get**](docs/RansomwareV2Api.md#v2_ransomware_criticalpaths_get) | **GET** /v2/ransomware/criticalpaths | Get all recent critical path snapshot jobs
*RansomwareV2Api* | [**v2_ransomware_criticalpaths_id_get**](docs/RansomwareV2Api.md#v2_ransomware_criticalpaths_id_get) | **GET** /v2/ransomware/criticalpaths/{id} | Retrieves a recently run snapshot job
*RansomwareV2Api* | [**v2_ransomware_criticalpaths_post**](docs/RansomwareV2Api.md#v2_ransomware_criticalpaths_post) | **POST** /v2/ransomware/criticalpaths | Take a snapshot of all critical paths
*RansomwareV2Api* | [**v2_ransomware_hasactiveevents_get**](docs/RansomwareV2Api.md#v2_ransomware_hasactiveevents_get) | **GET** /v2/ransomware/hasactiveevents | returns true/false wheather there are active events ot not in eyeglass 
*RansomwareV2Api* | [**v2_ransomware_lockout_user_post**](docs/RansomwareV2Api.md#v2_ransomware_lockout_user_post) | **POST** /v2/ransomware/lockout/{user} | Creates a ransomware event and locks out user
*SecurityEventsV1Api* | [**v1_securityevents_get**](docs/SecurityEventsV1Api.md#v1_securityevents_get) | **GET** /v1/securityevents | 
*WhitelistV1Api* | [**v1_ransomware_whitelist_get**](docs/WhitelistV1Api.md#v1_ransomware_whitelist_get) | **GET** /v1/ransomware/whitelist | Get all Whitelist settings
*WhitelistV1Api* | [**v1_ransomware_whitelist_newer_than_get**](docs/WhitelistV1Api.md#v1_ransomware_whitelist_newer_than_get) | **GET** /v1/ransomware/whitelist/{newer_than} | Get Whitelist settings that have changed
*WritableSnapshotsV2Api* | [**v2_writable_snapshots_delete**](docs/WritableSnapshotsV2Api.md#v2_writable_snapshots_delete) | **DELETE** /v2/writable-snapshots | delete a writable snapshot
*WritableSnapshotsV2Api* | [**v2_writable_snapshots_get**](docs/WritableSnapshotsV2Api.md#v2_writable_snapshots_get) | **GET** /v2/writable-snapshots | Get all recent writable-snapshots snapshost jobs
*WritableSnapshotsV2Api* | [**v2_writable_snapshots_job_status_get**](docs/WritableSnapshotsV2Api.md#v2_writable_snapshots_job_status_get) | **GET** /v2/writable-snapshots/jobStatus | Get status of writable snapshots job by id
*WritableSnapshotsV2Api* | [**v2_writable_snapshots_post**](docs/WritableSnapshotsV2Api.md#v2_writable_snapshots_post) | **POST** /v2/writable-snapshots | Create a writable snapshot


## Documentation For Models

 - [AirgapJob](docs/AirgapJob.md)
 - [Alarm](docs/Alarm.md)
 - [ComponentStatus](docs/ComponentStatus.md)
 - [ConfigRepJob](docs/ConfigRepJob.md)
 - [DRFailoverStatus](docs/DRFailoverStatus.md)
 - [ECSAirgapJobs](docs/ECSAirgapJobs.md)
 - [ECSAirgapJobsData](docs/ECSAirgapJobsData.md)
 - [ECSSyncJob](docs/ECSSyncJob.md)
 - [ECSSyncJobsData](docs/ECSSyncJobsData.md)
 - [Empty](docs/Empty.md)
 - [Empty1](docs/Empty1.md)
 - [ErrorModel](docs/ErrorModel.md)
 - [HeartbeatDetails](docs/HeartbeatDetails.md)
 - [HeartbeatRequestBody](docs/HeartbeatRequestBody.md)
 - [HeartbeatResponse](docs/HeartbeatResponse.md)
 - [Job](docs/Job.md)
 - [JobFailoverTarget](docs/JobFailoverTarget.md)
 - [JobStatusDetail](docs/JobStatusDetail.md)
 - [Node](docs/Node.md)
 - [NotificationResponse](docs/NotificationResponse.md)
 - [Policy](docs/Policy.md)
 - [Pool](docs/Pool.md)
 - [PostResponse](docs/PostResponse.md)
 - [RSWEventResponse](docs/RSWEventResponse.md)
 - [StatusDetail](docs/StatusDetail.md)
 - [StatusResponse](docs/StatusResponse.md)
 - [UpdateECSAirGap](docs/UpdateECSAirGap.md)
 - [VaultEvent](docs/VaultEvent.md)
 - [VaultEventsData](docs/VaultEventsData.md)
 - [VaultEventsDataConfig](docs/VaultEventsDataConfig.md)
 - [Whitelist](docs/Whitelist.md)
 - [WritableSnapshotModel](docs/WritableSnapshotModel.md)
 - [WritableSnapshotsResponse](docs/WritableSnapshotsResponse.md)
 - [Zone](docs/Zone.md)


## Documentation For Authorization


## internalApiKey

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: HTTP header


## Author

support@superna.net

