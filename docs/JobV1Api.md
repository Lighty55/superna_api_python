# swagger_client.JobV1Api

All URIs are relative to *https://localhost/sera*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_jobs_drtest_post**](JobV1Api.md#v1_jobs_drtest_post) | **POST** /v1/jobs/drtest | Enter/Exit DR test mode
[**v1_jobs_get**](JobV1Api.md#v1_jobs_get) | **GET** /v1/jobs | Get failover jobs
[**v1_jobs_id_delete**](JobV1Api.md#v1_jobs_id_delete) | **DELETE** /v1/jobs/{id} | cancels a running failover job
[**v1_jobs_id_get**](JobV1Api.md#v1_jobs_id_get) | **GET** /v1/jobs/{id} | Retreive a failover job by ID
[**v1_jobs_id_log_get**](JobV1Api.md#v1_jobs_id_log_get) | **GET** /v1/jobs/{id}/log | Retrieve the logfile for a running or finished failover job
[**v1_jobs_post**](JobV1Api.md#v1_jobs_post) | **POST** /v1/jobs | Create a new failover job
[**v1_jobs_rehearsal_post**](JobV1Api.md#v1_jobs_rehearsal_post) | **POST** /v1/jobs/rehearsal | Create a new rehearsal job


# **v1_jobs_drtest_post**
> PostResponse v1_jobs_drtest_post(enable, policy, configsync=configsync, datasync=datasync)

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
api_instance = swagger_client.JobV1Api(swagger_client.ApiClient(configuration))
enable = true # bool | True = Make target writable (Enter DR test mode). False = Make target read-only (Exit DR test mode)  (default to true)
policy = 'policy_example' # str | DR testing policy id (as retrieved with /nodes/{id}/policies GET)
configsync = false # bool | Run a configuration while DR test job (optional) (default to false)
datasync = true # bool | Run policy while DR test job (optional) (default to true)

try:
    # Enter/Exit DR test mode
    api_response = api_instance.v1_jobs_drtest_post(enable, policy, configsync=configsync, datasync=datasync)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV1Api->v1_jobs_drtest_post: %s\n" % e)
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

# **v1_jobs_get**
> list[Job] v1_jobs_get(state=state, success=success)

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
api_instance = swagger_client.JobV1Api(swagger_client.ApiClient(configuration))
state = 'state_example' # str | filter running or complete jobs [all, running, finished] (optional)
success = true # bool | filter jobs by result success [true, false] (optional)

try:
    # Get failover jobs
    api_response = api_instance.v1_jobs_get(state=state, success=success)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV1Api->v1_jobs_get: %s\n" % e)
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

# **v1_jobs_id_delete**
> Job v1_jobs_id_delete(id, empty=empty)

cancels a running failover job

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
api_instance = swagger_client.JobV1Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the job to retrieve
empty = swagger_client.Empty() # Empty | Empty body for delete request {} (optional)

try:
    # cancels a running failover job
    api_response = api_instance.v1_jobs_id_delete(id, empty=empty)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV1Api->v1_jobs_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the job to retrieve | 
 **empty** | [**Empty**](Empty.md)| Empty body for delete request {} | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_jobs_id_get**
> Job v1_jobs_id_get(id)

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
api_instance = swagger_client.JobV1Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the job to retrieve

try:
    # Retreive a failover job by ID
    api_response = api_instance.v1_jobs_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV1Api->v1_jobs_id_get: %s\n" % e)
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

# **v1_jobs_id_log_get**
> str v1_jobs_id_log_get(id)

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
api_instance = swagger_client.JobV1Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the job to retrieve

try:
    # Retrieve the logfile for a running or finished failover job
    api_response = api_instance.v1_jobs_id_log_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV1Api->v1_jobs_id_log_get: %s\n" % e)
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

# **v1_jobs_post**
> PostResponse v1_jobs_post(sourceid, targetid, failovertarget, blockonwarnings, pool=pool, controlled=controlled, datasync=datasync, configsync=configsync, resyncprep=resyncprep, disablemirror=disablemirror, quotasync=quotasync, rollbackrenameshares=rollbackrenameshares, smbdataintegrity=smbdataintegrity)

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
api_instance = swagger_client.JobV1Api(swagger_client.ApiClient(configuration))
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
    api_response = api_instance.v1_jobs_post(sourceid, targetid, failovertarget, blockonwarnings, pool=pool, controlled=controlled, datasync=datasync, configsync=configsync, resyncprep=resyncprep, disablemirror=disablemirror, quotasync=quotasync, rollbackrenameshares=rollbackrenameshares, smbdataintegrity=smbdataintegrity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV1Api->v1_jobs_post: %s\n" % e)
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

# **v1_jobs_rehearsal_post**
> PostResponse v1_jobs_rehearsal_post(enable, sourceid, targetid, failovertarget, pool=pool)

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
api_instance = swagger_client.JobV1Api(swagger_client.ApiClient(configuration))
enable = true # bool | Enable or disable (=false) the rehearsal mode (default to true)
sourceid = 'sourceid_example' # str | ID of the source node for this job
targetid = 'targetid_example' # str | ID of the target node for this job
failovertarget = 'failovertarget_example' # str | ID of the access zone to failover OR IDs of syncIQ policies (comma separated) to failover.
pool = '' # str | Pool name in case of pool failover. The name format is groupName:subnetName:poolName (optional) (default to )

try:
    # Create a new rehearsal job
    api_response = api_instance.v1_jobs_rehearsal_post(enable, sourceid, targetid, failovertarget, pool=pool)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobV1Api->v1_jobs_rehearsal_post: %s\n" % e)
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

