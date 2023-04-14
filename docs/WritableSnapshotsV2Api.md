# swagger_client.WritableSnapshotsV2Api

All URIs are relative to *https://localhost/sera*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_writable_snapshots_delete**](WritableSnapshotsV2Api.md#v2_writable_snapshots_delete) | **DELETE** /v2/writable-snapshots | delete a writable snapshot
[**v2_writable_snapshots_get**](WritableSnapshotsV2Api.md#v2_writable_snapshots_get) | **GET** /v2/writable-snapshots | Get all recent writable-snapshots snapshost jobs
[**v2_writable_snapshots_job_status_get**](WritableSnapshotsV2Api.md#v2_writable_snapshots_job_status_get) | **GET** /v2/writable-snapshots/jobStatus | Get status of writable snapshots job by id
[**v2_writable_snapshots_post**](WritableSnapshotsV2Api.md#v2_writable_snapshots_post) | **POST** /v2/writable-snapshots | Create a writable snapshot


# **v2_writable_snapshots_delete**
> WritableSnapshotsResponse v2_writable_snapshots_delete(source_snap, target_path, ne, delete_config)

delete a writable snapshot

Delete a writable snapshot

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
api_instance = swagger_client.WritableSnapshotsV2Api(swagger_client.ApiClient(configuration))
source_snap = 'source_snap_example' # str | Source Snapshot parameter
target_path = 'target_path_example' # str | Target path for writable snapshot
ne = 'ne_example' # str | Cluster name parameter
delete_config = 'delete_config_example' # str | Flag for delete configuration for deleting writable snapshot

try:
    # delete a writable snapshot
    api_response = api_instance.v2_writable_snapshots_delete(source_snap, target_path, ne, delete_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WritableSnapshotsV2Api->v2_writable_snapshots_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_snap** | **str**| Source Snapshot parameter | 
 **target_path** | **str**| Target path for writable snapshot | 
 **ne** | **str**| Cluster name parameter | 
 **delete_config** | **str**| Flag for delete configuration for deleting writable snapshot | 

### Return type

[**WritableSnapshotsResponse**](WritableSnapshotsResponse.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_writable_snapshots_get**
> WritableSnapshotsResponse v2_writable_snapshots_get()

Get all recent writable-snapshots snapshost jobs

View all recent writable snapshots jobs

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
api_instance = swagger_client.WritableSnapshotsV2Api(swagger_client.ApiClient(configuration))

try:
    # Get all recent writable-snapshots snapshost jobs
    api_response = api_instance.v2_writable_snapshots_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WritableSnapshotsV2Api->v2_writable_snapshots_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WritableSnapshotsResponse**](WritableSnapshotsResponse.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_writable_snapshots_job_status_get**
> JobStatusDetail v2_writable_snapshots_job_status_get(job_id)

Get status of writable snapshots job by id

Get status of writable snapshots job by id

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
api_instance = swagger_client.WritableSnapshotsV2Api(swagger_client.ApiClient(configuration))
job_id = 'job_id_example' # str | Job ID

try:
    # Get status of writable snapshots job by id
    api_response = api_instance.v2_writable_snapshots_job_status_get(job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WritableSnapshotsV2Api->v2_writable_snapshots_job_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID | 

### Return type

[**JobStatusDetail**](JobStatusDetail.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_writable_snapshots_post**
> WritableSnapshotsResponse v2_writable_snapshots_post(ne, target_path, source_path, copy_config_flag)

Create a writable snapshot

Start a job to create a writable snapshot

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
api_instance = swagger_client.WritableSnapshotsV2Api(swagger_client.ApiClient(configuration))
ne = 'ne_example' # str | Cluster Name
target_path = 'target_path_example' # str | Target path for writable snapshot
source_path = 'source_path_example' # str | Source path for writable snapshot
copy_config_flag = 'copy_config_flag_example' # str | Flag for copy config while creating writable snapshot (true/false)

try:
    # Create a writable snapshot
    api_response = api_instance.v2_writable_snapshots_post(ne, target_path, source_path, copy_config_flag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WritableSnapshotsV2Api->v2_writable_snapshots_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ne** | **str**| Cluster Name | 
 **target_path** | **str**| Target path for writable snapshot | 
 **source_path** | **str**| Source path for writable snapshot | 
 **copy_config_flag** | **str**| Flag for copy config while creating writable snapshot (true/false) | 

### Return type

[**WritableSnapshotsResponse**](WritableSnapshotsResponse.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

