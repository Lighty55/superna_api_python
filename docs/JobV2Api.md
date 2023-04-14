# swagger_client.JobV2Api

All URIs are relative to *https://localhost/sera*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_jobs_airgap_accessrequest_get**](JobV2Api.md#v2_jobs_airgap_accessrequest_get) | **GET** /v2/jobs/airgap/accessrequest | Eyeglass access requests to vault
[**v2_jobs_airgap_get**](JobV2Api.md#v2_jobs_airgap_get) | **GET** /v2/jobs/airgap | Get all airgap jobs
[**v2_jobs_airgap_id_get**](JobV2Api.md#v2_jobs_airgap_id_get) | **GET** /v2/jobs/airgap/{id} | Retrieves a specific recently run airgap job, if it exists
[**v2_jobs_airgap_post**](JobV2Api.md#v2_jobs_airgap_post) | **POST** /v2/jobs/airgap | Start an airgap job
[**v2_jobs_airgap_status_post**](JobV2Api.md#v2_jobs_airgap_status_post) | **POST** /v2/jobs/airgap/status | post airgap job status
[**v2_jobs_airgap_uploadlogs_post**](JobV2Api.md#v2_jobs_airgap_uploadlogs_post) | **POST** /v2/jobs/airgap/uploadlogs | Uploads the logs under eyeglass logs directory.
[**v2_jobs_failover_drtest_post**](JobV2Api.md#v2_jobs_failover_drtest_post) | **POST** /v2/jobs/failover/drtest | Enter/Exit DR test mode
[**v2_jobs_failover_get**](JobV2Api.md#v2_jobs_failover_get) | **GET** /v2/jobs/failover | Get failover jobs
[**v2_jobs_failover_id_delete**](JobV2Api.md#v2_jobs_failover_id_delete) | **DELETE** /v2/jobs/failover/{id} | 
[**v2_jobs_failover_id_get**](JobV2Api.md#v2_jobs_failover_id_get) | **GET** /v2/jobs/failover/{id} | Retreive a failover job by ID
[**v2_jobs_failover_id_log_get**](JobV2Api.md#v2_jobs_failover_id_log_get) | **GET** /v2/jobs/failover/{id}/log | Retrieve the logfile for a running or finished failover job
[**v2_jobs_failover_post**](JobV2Api.md#v2_jobs_failover_post) | **POST** /v2/jobs/failover | Create a new failover job
[**v2_jobs_failover_rehearsal_post**](JobV2Api.md#v2_jobs_failover_rehearsal_post) | **POST** /v2/jobs/failover/rehearsal | Create a new rehearsal job
[**v2_jobs_readiness_get**](JobV2Api.md#v2_jobs_readiness_get) | **GET** /v2/jobs/readiness | View all recent readiness jobs
[**v2_jobs_readiness_id_get**](JobV2Api.md#v2_jobs_readiness_id_get) | **GET** /v2/jobs/readiness/{id} | Retrieves a specific recently run readiness job, if it exists
[**v2_jobs_readiness_post**](JobV2Api.md#v2_jobs_readiness_post) | **POST** /v2/jobs/readiness | Run zone readiness job
[**v2_jobs_replication_get**](JobV2Api.md#v2_jobs_replication_get) | **GET** /v2/jobs/replication | Get all recent replication jobs
[**v2_jobs_replication_id_get**](JobV2Api.md#v2_jobs_replication_id_get) | **GET** /v2/jobs/replication/{id} | Retrieves a specific replication job, if it was run recently
[**v2_jobs_replication_post**](JobV2Api.md#v2_jobs_replication_post) | **POST** /v2/jobs/replication | Run a configuration replication job


# **v2_jobs_airgap_accessrequest_get**
> AirgapJob v2_jobs_airgap_accessrequest_get(eva_id)

Eyeglass access requests to vault

retrieves and resets the eyeglass access request to vault

### Example
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
api_instance = swagger_client.JobV2Api(swagger_client.ApiClient(configuration))
eva_id = 'eva_id_example' # str | Vault agent ID

try:
    # Eyeglass access requests to vault
    api_response = api_instance.v2_jobs_airgap_accessrequest_get(eva_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV2Api->v2_jobs_airgap_accessrequest_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eva_id** | **str**| Vault agent ID | 

### Return type

[**AirgapJob**](AirgapJob.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_jobs_airgap_get**
> list[AirgapJob] v2_jobs_airgap_get(eva_id)

Get all airgap jobs

View all airgap jobs that can run through vault engine

### Example
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
api_instance = swagger_client.JobV2Api(swagger_client.ApiClient(configuration))
eva_id = 'eva_id_example' # str | Vault agent ID

try:
    # Get all airgap jobs
    api_response = api_instance.v2_jobs_airgap_get(eva_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV2Api->v2_jobs_airgap_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eva_id** | **str**| Vault agent ID | 

### Return type

[**list[AirgapJob]**](AirgapJob.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_jobs_airgap_id_get**
> JobStatusDetail v2_jobs_airgap_id_get(id, jobname)

Retrieves a specific recently run airgap job, if it exists

Retrieves a specific recently run airgap job, if it exists

### Example
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
api_instance = swagger_client.JobV2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the job to retrieve
jobname = 'jobname_example' # str | Name of the airgap job (as retrieved with /v2/jobs/airgap GET)

try:
    # Retrieves a specific recently run airgap job, if it exists
    api_response = api_instance.v2_jobs_airgap_id_get(id, jobname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV2Api->v2_jobs_airgap_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the job to retrieve | 
 **jobname** | **str**| Name of the airgap job (as retrieved with /v2/jobs/airgap GET) | 

### Return type

[**JobStatusDetail**](JobStatusDetail.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_jobs_airgap_post**
> PostResponse v2_jobs_airgap_post(jobname)

Start an airgap job

Start an airgap job

### Example
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
api_instance = swagger_client.JobV2Api(swagger_client.ApiClient(configuration))
jobname = 'jobname_example' # str | Name of the airgap job (as retrieved with /v2/jobs/airgap GET)

try:
    # Start an airgap job
    api_response = api_instance.v2_jobs_airgap_post(jobname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV2Api->v2_jobs_airgap_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobname** | **str**| Name of the airgap job (as retrieved with /v2/jobs/airgap GET) | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_jobs_airgap_status_post**
> StatusResponse v2_jobs_airgap_status_post(jobname, job_status_detail)

post airgap job status

Send status of vault initiated airgap job back to eyeglass

### Example
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
api_instance = swagger_client.JobV2Api(swagger_client.ApiClient(configuration))
jobname = 'jobname_example' # str | Name of the airgap job
job_status_detail = swagger_client.JobStatusDetail() # JobStatusDetail | Update data for the specified ECS airgap job.

try:
    # post airgap job status
    api_response = api_instance.v2_jobs_airgap_status_post(jobname, job_status_detail)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV2Api->v2_jobs_airgap_status_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobname** | **str**| Name of the airgap job | 
 **job_status_detail** | [**JobStatusDetail**](JobStatusDetail.md)| Update data for the specified ECS airgap job. | 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_jobs_airgap_uploadlogs_post**
> StatusResponse v2_jobs_airgap_uploadlogs_post(filename, nodename, destfilename=destfilename)

Uploads the logs under eyeglass logs directory.

Uploads the vault airgap logs

### Example
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
api_instance = swagger_client.JobV2Api(swagger_client.ApiClient(configuration))
filename = 'filename_example' # str | The name and path of the file to upload from node to eyeglass
nodename = 'nodename_example' # str | The name of the node where file resides
destfilename = 'destfilename_example' # str | The name of the file on destination (optional)

try:
    # Uploads the logs under eyeglass logs directory.
    api_response = api_instance.v2_jobs_airgap_uploadlogs_post(filename, nodename, destfilename=destfilename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV2Api->v2_jobs_airgap_uploadlogs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| The name and path of the file to upload from node to eyeglass | 
 **nodename** | **str**| The name of the node where file resides | 
 **destfilename** | **str**| The name of the file on destination | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_jobs_failover_drtest_post**
> PostResponse v2_jobs_failover_drtest_post(enable, policy, configsync=configsync, datasync=datasync)

Enter/Exit DR test mode

Enter/Exit DR test mode for a given policy

### Example
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
api_instance = swagger_client.JobV2Api(swagger_client.ApiClient(configuration))
enable = true # bool | True = Make target writable (Enter DR test mode). False = Make target read-only (Exit DR test mode)  (default to true)
policy = 'policy_example' # str | DR testing policy id (as retrieved with /nodes/{id}/policies GET)
configsync = false # bool | Run a configuration while DR test job (optional) (default to false)
datasync = true # bool | Run policy while DR test job (optional) (default to true)

try:
    # Enter/Exit DR test mode
    api_response = api_instance.v2_jobs_failover_drtest_post(enable, policy, configsync=configsync, datasync=datasync)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV2Api->v2_jobs_failover_drtest_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable** | **bool**| True &#x3D; Make target writable (Enter DR test mode). False &#x3D; Make target read-only (Exit DR test mode)  | [default to true]
 **policy** | **str**| DR testing policy id (as retrieved with /nodes/{id}/policies GET) | 
 **configsync** | **bool**| Run a configuration while DR test job | [optional] [default to false]
 **datasync** | **bool**| Run policy while DR test job | [optional] [default to true]

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_jobs_failover_get**
> list[Job] v2_jobs_failover_get(state=state, success=success)

Get failover jobs

Returns failover jobs from Superna Eyeglass.

### Example
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
api_instance = swagger_client.JobV2Api(swagger_client.ApiClient(configuration))
state = 'state_example' # str | filter running or complete jobs [all, running, finished] (optional)
success = true # bool | filter jobs by result success [true, false] (optional)

try:
    # Get failover jobs
    api_response = api_instance.v2_jobs_failover_get(state=state, success=success)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV2Api->v2_jobs_failover_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| filter running or complete jobs [all, running, finished] | [optional] 
 **success** | **bool**| filter jobs by result success [true, false] | [optional] 

### Return type

[**list[Job]**](Job.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_jobs_failover_id_delete**
> Job v2_jobs_failover_id_delete(id, empty=empty)



Cancels a running failover job

### Example
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
api_instance = swagger_client.JobV2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the job to retrieve
empty = swagger_client.Empty1() # Empty1 | Empty body for delete request {} (optional)

try:
    api_response = api_instance.v2_jobs_failover_id_delete(id, empty=empty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV2Api->v2_jobs_failover_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the job to retrieve | 
 **empty** | [**Empty1**](Empty1.md)| Empty body for delete request {} | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_jobs_failover_id_get**
> Job v2_jobs_failover_id_get(id)

Retreive a failover job by ID

Retrieve a failover job by id

### Example
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
api_instance = swagger_client.JobV2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the job to retrieve

try:
    # Retreive a failover job by ID
    api_response = api_instance.v2_jobs_failover_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV2Api->v2_jobs_failover_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the job to retrieve | 

### Return type

[**Job**](Job.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_jobs_failover_id_log_get**
> str v2_jobs_failover_id_log_get(id)

Retrieve the logfile for a running or finished failover job

Get the failover jobs log

### Example
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
api_instance = swagger_client.JobV2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the job to retrieve

try:
    # Retrieve the logfile for a running or finished failover job
    api_response = api_instance.v2_jobs_failover_id_log_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV2Api->v2_jobs_failover_id_log_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the job to retrieve | 

### Return type

**str**

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_jobs_failover_post**
> PostResponse v2_jobs_failover_post(sourceid, targetid, failovertarget, blockonwarnings, pool=pool, controlled=controlled, datasync=datasync, configsync=configsync, resyncprep=resyncprep, disablemirror=disablemirror, quotasync=quotasync, rollbackrenameshares=rollbackrenameshares, smbdataintegrity=smbdataintegrity)

Create a new failover job

Launch a new failover job in Eyeglass.

### Example
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
api_instance = swagger_client.JobV2Api(swagger_client.ApiClient(configuration))
sourceid = 'sourceid_example' # str | ID of the source node for this job
targetid = 'targetid_example' # str | ID of the target node for this job
failovertarget = 'failovertarget_example' # str | ID of the access zone to failover OR IDs of syncIQ policies (comma separated) to failover.
blockonwarnings = true # bool | Block failover on warnings (default to true)
pool = '' # str | Pool name in case of pool failover. The name format is groupName:subnetName:poolName (optional) (default to )
controlled = true # bool | Execute a controlled failover by running operations against the source cluster  as well as the target (optional) (default to true)
datasync = true # bool | Run the final incremental data sync before failover (optional) (default to true)
configsync = false # bool | Run a configuration sync before failover (optional) (default to false)
resyncprep = true # bool | Run resync prep on the source cluster to create the mirror policies (optional) (default to true)
disablemirror = false # bool | Disable mirror policies created on the failover target (optional) (default to false)
quotasync = true # bool | Run quota jobs to failover quotas to target (optional) (default to true)
rollbackrenameshares = true # bool | Rollback renamed shares on failure (optional) (default to true)
smbdataintegrity = false # bool | SMB data integrity failover (optional) (default to false)

try:
    # Create a new failover job
    api_response = api_instance.v2_jobs_failover_post(sourceid, targetid, failovertarget, blockonwarnings, pool=pool, controlled=controlled, datasync=datasync, configsync=configsync, resyncprep=resyncprep, disablemirror=disablemirror, quotasync=quotasync, rollbackrenameshares=rollbackrenameshares, smbdataintegrity=smbdataintegrity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV2Api->v2_jobs_failover_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sourceid** | **str**| ID of the source node for this job | 
 **targetid** | **str**| ID of the target node for this job | 
 **failovertarget** | **str**| ID of the access zone to failover OR IDs of syncIQ policies (comma separated) to failover. | 
 **blockonwarnings** | **bool**| Block failover on warnings | [default to true]
 **pool** | **str**| Pool name in case of pool failover. The name format is groupName:subnetName:poolName | [optional] [default to ]
 **controlled** | **bool**| Execute a controlled failover by running operations against the source cluster  as well as the target | [optional] [default to true]
 **datasync** | **bool**| Run the final incremental data sync before failover | [optional] [default to true]
 **configsync** | **bool**| Run a configuration sync before failover | [optional] [default to false]
 **resyncprep** | **bool**| Run resync prep on the source cluster to create the mirror policies | [optional] [default to true]
 **disablemirror** | **bool**| Disable mirror policies created on the failover target | [optional] [default to false]
 **quotasync** | **bool**| Run quota jobs to failover quotas to target | [optional] [default to true]
 **rollbackrenameshares** | **bool**| Rollback renamed shares on failure | [optional] [default to true]
 **smbdataintegrity** | **bool**| SMB data integrity failover | [optional] [default to false]

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_jobs_failover_rehearsal_post**
> PostResponse v2_jobs_failover_rehearsal_post(enable, sourceid, targetid, failovertarget, pool=pool)

Create a new rehearsal job

Launch a new rehearsal job in Eyeglass.

### Example
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
api_instance = swagger_client.JobV2Api(swagger_client.ApiClient(configuration))
enable = true # bool | Enable or disable (=false) the rehearsal mode (default to true)
sourceid = 'sourceid_example' # str | ID of the source node for this job
targetid = 'targetid_example' # str | ID of the target node for this job
failovertarget = 'failovertarget_example' # str | ID of the access zone to failover OR IDs of syncIQ policies (comma separated) to failover.
pool = '' # str | Pool name in case of pool failover. The name format is groupName:subnetName:poolName (optional) (default to )

try:
    # Create a new rehearsal job
    api_response = api_instance.v2_jobs_failover_rehearsal_post(enable, sourceid, targetid, failovertarget, pool=pool)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV2Api->v2_jobs_failover_rehearsal_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enable** | **bool**| Enable or disable (&#x3D;false) the rehearsal mode | [default to true]
 **sourceid** | **str**| ID of the source node for this job | 
 **targetid** | **str**| ID of the target node for this job | 
 **failovertarget** | **str**| ID of the access zone to failover OR IDs of syncIQ policies (comma separated) to failover. | 
 **pool** | **str**| Pool name in case of pool failover. The name format is groupName:subnetName:poolName | [optional] [default to ]

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_jobs_readiness_get**
> list[JobStatusDetail] v2_jobs_readiness_get(state=state)

View all recent readiness jobs

View all recent readiness jobs

### Example
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
api_instance = swagger_client.JobV2Api(swagger_client.ApiClient(configuration))
state = 'state_example' # str | filter running or complete jobs [all, running, finished] (optional)

try:
    # View all recent readiness jobs
    api_response = api_instance.v2_jobs_readiness_get(state=state)
    print(api_response)
except ApiException as e:
    print("Exception when calling JobV2Api->v2_jobs_readiness_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| filter running or complete jobs [all, running, finished] | [optional] 

### Return type

[**list[JobStatusDetail]**](JobStatusDetail.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_jobs_readiness_id_get**
> JobStatusDetail v2_jobs_readiness_id_get(id)

Retrieves a specific recently run readiness job, if it exists

Retrieves a specific recently run readiness job, if it exists

### Example
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
api_instance = swagger_client.JobV2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the job to retrieve

try:
    # Retrieves a specific recently run readiness job, if it exists
    api_response = api_instance.v2_jobs_readiness_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV2Api->v2_jobs_readiness_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the job to retrieve | 

### Return type

[**JobStatusDetail**](JobStatusDetail.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_jobs_readiness_post**
> PostResponse v2_jobs_readiness_post()

Run zone readiness job

Run zone readiness job

### Example
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
api_instance = swagger_client.JobV2Api(swagger_client.ApiClient(configuration))

try:
    # Run zone readiness job
    api_response = api_instance.v2_jobs_readiness_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV2Api->v2_jobs_readiness_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_jobs_replication_get**
> list[JobStatusDetail] v2_jobs_replication_get(state=state)

Get all recent replication jobs

View all recent replication jobs

### Example
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
api_instance = swagger_client.JobV2Api(swagger_client.ApiClient(configuration))
state = 'state_example' # str | filter running or complete jobs [all, running, finished] (optional)

try:
    # Get all recent replication jobs
    api_response = api_instance.v2_jobs_replication_get(state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV2Api->v2_jobs_replication_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| filter running or complete jobs [all, running, finished] | [optional] 

### Return type

[**list[JobStatusDetail]**](JobStatusDetail.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_jobs_replication_id_get**
> JobStatusDetail v2_jobs_replication_id_get(id)

Retrieves a specific replication job, if it was run recently

Retrieves a specific replication job, if it was run recently

### Example
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
api_instance = swagger_client.JobV2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the job to retrieve

try:
    # Retrieves a specific replication job, if it was run recently
    api_response = api_instance.v2_jobs_replication_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV2Api->v2_jobs_replication_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the job to retrieve | 

### Return type

[**JobStatusDetail**](JobStatusDetail.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_jobs_replication_post**
> PostResponse v2_jobs_replication_post()

Run a configuration replication job

Run a configuration replication job

### Example
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
api_instance = swagger_client.JobV2Api(swagger_client.ApiClient(configuration))

try:
    # Run a configuration replication job
    api_response = api_instance.v2_jobs_replication_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV2Api->v2_jobs_replication_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

