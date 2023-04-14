# swagger_client.NodeV1Api

All URIs are relative to *https://localhost/sera*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_nodes_get**](NodeV1Api.md#v1_nodes_get) | **GET** /v1/nodes | Get all nodes
[**v1_nodes_id_get**](NodeV1Api.md#v1_nodes_id_get) | **GET** /v1/nodes/{id} | Find nodes by ID
[**v1_nodes_id_policies_get**](NodeV1Api.md#v1_nodes_id_policies_get) | **GET** /v1/nodes/{id}/policies | Find policies for a node
[**v1_nodes_id_policies_name_get**](NodeV1Api.md#v1_nodes_id_policies_name_get) | **GET** /v1/nodes/{id}/policies/{name} | Find policy by name
[**v1_nodes_id_pools_get**](NodeV1Api.md#v1_nodes_id_pools_get) | **GET** /v1/nodes/{id}/pools | Find pools for a node
[**v1_nodes_id_pools_name_get**](NodeV1Api.md#v1_nodes_id_pools_name_get) | **GET** /v1/nodes/{id}/pools/{name} | Find pool by name 
[**v1_nodes_id_zones_get**](NodeV1Api.md#v1_nodes_id_zones_get) | **GET** /v1/nodes/{id}/zones | Find zones for a node
[**v1_nodes_id_zones_name_get**](NodeV1Api.md#v1_nodes_id_zones_name_get) | **GET** /v1/nodes/{id}/zones/{name} | Find zone name for a node


# **v1_nodes_get**
> list[Node] v1_nodes_get()

Get all nodes

Returns all Superna Eyeglass Managed Devices.

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
api_instance = swagger_client.NodeV1Api(swagger_client.ApiClient(configuration))

try:
    # Get all nodes
    api_response = api_instance.v1_nodes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeV1Api->v1_nodes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Node]**](Node.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_nodes_id_get**
> Node v1_nodes_id_get(id)

Find nodes by ID

Returns the Superna Eyeglass Managed Devices based on ID

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
api_instance = swagger_client.NodeV1Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the node to retrieve

try:
    # Find nodes by ID
    api_response = api_instance.v1_nodes_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeV1Api->v1_nodes_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the node to retrieve | 

### Return type

[**Node**](Node.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_nodes_id_policies_get**
> list[Policy] v1_nodes_id_policies_get(id, fo_readiness)

Find policies for a node

Returns the syncIQ policies for this node

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
api_instance = swagger_client.NodeV1Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the node to retrieve
fo_readiness = false # bool | Retrieve also failover readiness status details (default to false)

try:
    # Find policies for a node
    api_response = api_instance.v1_nodes_id_policies_get(id, fo_readiness)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeV1Api->v1_nodes_id_policies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the node to retrieve | 
 **fo_readiness** | **bool**| Retrieve also failover readiness status details | [default to false]

### Return type

[**list[Policy]**](Policy.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_nodes_id_policies_name_get**
> Policy v1_nodes_id_policies_name_get(id, name)

Find policy by name

Returns the syncIQ policy for this node and this policy name

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
api_instance = swagger_client.NodeV1Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the node to retrieve
name = 'name_example' # str | name of the policy

try:
    # Find policy by name
    api_response = api_instance.v1_nodes_id_policies_name_get(id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeV1Api->v1_nodes_id_policies_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the node to retrieve | 
 **name** | **str**| name of the policy | 

### Return type

[**Policy**](Policy.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_nodes_id_pools_get**
> list[Pool] v1_nodes_id_pools_get(id, fo_readiness)

Find pools for a node

Returns the pools for this node

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
api_instance = swagger_client.NodeV1Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the node to retrieve
fo_readiness = false # bool | Retrieve also failover readiness status details (default to false)

try:
    # Find pools for a node
    api_response = api_instance.v1_nodes_id_pools_get(id, fo_readiness)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeV1Api->v1_nodes_id_pools_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the node to retrieve | 
 **fo_readiness** | **bool**| Retrieve also failover readiness status details | [default to false]

### Return type

[**list[Pool]**](Pool.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_nodes_id_pools_name_get**
> Pool v1_nodes_id_pools_name_get(id, name)

Find pool by name 

Returns the pool by its name on a given node

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
api_instance = swagger_client.NodeV1Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the node to retrieve
name = 'name_example' # str | name of the pool (groupName:subnetName:poolName)

try:
    # Find pool by name 
    api_response = api_instance.v1_nodes_id_pools_name_get(id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeV1Api->v1_nodes_id_pools_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the node to retrieve | 
 **name** | **str**| name of the pool (groupName:subnetName:poolName) | 

### Return type

[**Pool**](Pool.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_nodes_id_zones_get**
> list[Zone] v1_nodes_id_zones_get(id, fo_readiness)

Find zones for a node

Returns the access zones for this node

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
api_instance = swagger_client.NodeV1Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the node to retrieve
fo_readiness = false # bool | Retrieve also failover readiness status details (default to false)

try:
    # Find zones for a node
    api_response = api_instance.v1_nodes_id_zones_get(id, fo_readiness)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeV1Api->v1_nodes_id_zones_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the node to retrieve | 
 **fo_readiness** | **bool**| Retrieve also failover readiness status details | [default to false]

### Return type

[**list[Zone]**](Zone.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_nodes_id_zones_name_get**
> Zone v1_nodes_id_zones_name_get(id, name)

Find zone name for a node

Find job by zone name for a node id

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
api_instance = swagger_client.NodeV1Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the node to retrieve
name = 'name_example' # str | name of the zone

try:
    # Find zone name for a node
    api_response = api_instance.v1_nodes_id_zones_name_get(id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodeV1Api->v1_nodes_id_zones_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the node to retrieve | 
 **name** | **str**| name of the zone | 

### Return type

[**Zone**](Zone.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

