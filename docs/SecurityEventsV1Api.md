# swagger_client.SecurityEventsV1Api

All URIs are relative to *https://localhost/sera*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_securityevents_get**](SecurityEventsV1Api.md#v1_securityevents_get) | **GET** /v1/securityevents | 


# **v1_securityevents_get**
> list[RSWEventResponse] v1_securityevents_get(type)



Get a list of active (RSW, EA) events

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
api_instance = swagger_client.SecurityEventsV1Api(swagger_client.ApiClient(configuration))
type = 'type_example' # str | Event types: [all, rsw, ea]

try:
    api_response = api_instance.v1_securityevents_get(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecurityEventsV1Api->v1_securityevents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Event types: [all, rsw, ea] | 

### Return type

[**list[RSWEventResponse]**](RSWEventResponse.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

