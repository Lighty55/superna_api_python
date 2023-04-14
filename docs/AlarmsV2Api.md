# swagger_client.AlarmsV2Api

All URIs are relative to *https://localhost/sera*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_alarms_post**](AlarmsV2Api.md#v2_alarms_post) | **POST** /v2/alarms/ | Post an alarm to be raised in eyeglass.


# **v2_alarms_post**
> StatusResponse v2_alarms_post(name, source=source, info=info, clear=clear)

Post an alarm to be raised in eyeglass.

Raise or clear an alarm

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
api_instance = swagger_client.AlarmsV2Api(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Eyeglass alarm name
source = 'source_example' # str | Source of the alarm (optional)
info = 'info_example' # str | Extra info (optional)
clear = false # bool | Clear an existing alarm if set to true, raise alarm if set to false (optional) (default to false)

try:
    # Post an alarm to be raised in eyeglass.
    api_response = api_instance.v2_alarms_post(name, source=source, info=info, clear=clear)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlarmsV2Api->v2_alarms_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Eyeglass alarm name | 
 **source** | **str**| Source of the alarm | [optional] 
 **info** | **str**| Extra info | [optional] 
 **clear** | **bool**| Clear an existing alarm if set to true, raise alarm if set to false | [optional] [default to false]

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

