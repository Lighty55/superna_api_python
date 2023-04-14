# swagger_client.NodeV2Api

All URIs are relative to *https://localhost/sera*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_nodes_id_configrep_get**](NodeV2Api.md#v2_nodes_id_configrep_get) | **GET** /v2/nodes/{id}/configrep | Gets all configuration replication jobs for this node
[**v2_nodes_id_configrep_name_get**](NodeV2Api.md#v2_nodes_id_configrep_name_get) | **GET** /v2/nodes/{id}/configrep/{name} | Gets a specific config replication job.
[**v2_nodes_id_configrep_name_put**](NodeV2Api.md#v2_nodes_id_configrep_name_put) | **PUT** /v2/nodes/{id}/configrep/{name} | Updates the status and/or type of a specific configuration job


# **v2_nodes_id_configrep_get**
> list[ConfigRepJob] v2_nodes_id_configrep_get(id)

Gets all configuration replication jobs for this node

Gets all configuration replication jobs for this node.

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
api_instance = swagger_client.NodeV2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the node to retrieve

try:
    # Gets all configuration replication jobs for this node
    api_response = api_instance.v2_nodes_id_configrep_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeV2Api->v2_nodes_id_configrep_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the node to retrieve | 

### Return type

[**list[ConfigRepJob]**](ConfigRepJob.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_nodes_id_configrep_name_get**
> ConfigRepJob v2_nodes_id_configrep_name_get(id, name)

Gets a specific config replication job.

Gets a specific config replication job.

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
api_instance = swagger_client.NodeV2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the node to retrieve
name = 'name_example' # str | The name of the config rep job

try:
    # Gets a specific config replication job.
    api_response = api_instance.v2_nodes_id_configrep_name_get(id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeV2Api->v2_nodes_id_configrep_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the node to retrieve | 
 **name** | **str**| The name of the config rep job | 

### Return type

[**ConfigRepJob**](ConfigRepJob.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_nodes_id_configrep_name_put**
> ConfigRepJob v2_nodes_id_configrep_name_put(id, name, enable=enable, type=type)

Updates the status and/or type of a specific configuration job

Updates the status and/or type of a specific configuration job

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
api_instance = swagger_client.NodeV2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the node to retrieve
name = 'name_example' # str | The name of the config rep job
enable = true # bool | Enable/Disable a job (optional)
type = 'type_example' # str | Set job type to AUTO,AUTODFS or AUTOSKIPCONFIG. (optional)

try:
    # Updates the status and/or type of a specific configuration job
    api_response = api_instance.v2_nodes_id_configrep_name_put(id, name, enable=enable, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeV2Api->v2_nodes_id_configrep_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the node to retrieve | 
 **name** | **str**| The name of the config rep job | 
 **enable** | **bool**| Enable/Disable a job | [optional] 
 **type** | **str**| Set job type to AUTO,AUTODFS or AUTOSKIPCONFIG. | [optional] 

### Return type

[**ConfigRepJob**](ConfigRepJob.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

