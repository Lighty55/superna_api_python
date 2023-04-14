# swagger_client.AlarmsV1Api

All URIs are relative to *https://localhost/sera*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_alarms_active_get**](AlarmsV1Api.md#v1_alarms_active_get) | **GET** /v1/alarms/active | Get all active alarms
[**v1_alarms_historical_get**](AlarmsV1Api.md#v1_alarms_historical_get) | **GET** /v1/alarms/historical | Get all historical alarms


# **v1_alarms_active_get**
> list[Alarm] v1_alarms_active_get(since=since, until=until, limit=limit)

Get all active alarms

Returns all active alarms from eyeglass

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
api_instance = swagger_client.AlarmsV1Api(swagger_client.ApiClient(configuration))
since = 789 # int | timestamp for filtering the active alarms newer than (optional)
until = 789 # int | timestamp for filtering the active alarms older than (optional)
limit = 789 # int | limits the number of returned alarms (optional)

try:
    # Get all active alarms
    api_response = api_instance.v1_alarms_active_get(since=since, until=until, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlarmsV1Api->v1_alarms_active_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **int**| timestamp for filtering the active alarms newer than | [optional] 
 **until** | **int**| timestamp for filtering the active alarms older than | [optional] 
 **limit** | **int**| limits the number of returned alarms | [optional] 

### Return type

[**list[Alarm]**](Alarm.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_alarms_historical_get**
> list[Alarm] v1_alarms_historical_get(since=since, until=until, limit=limit)

Get all historical alarms

Returns all historical alarms from eyeglass

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
api_instance = swagger_client.AlarmsV1Api(swagger_client.ApiClient(configuration))
since = 789 # int | timestamp for filtering the active alarms newer than (optional)
until = 789 # int | timestamp for filtering the active alarms older than (optional)
limit = 789 # int | limits the number of returned alarms (optional)

try:
    # Get all historical alarms
    api_response = api_instance.v1_alarms_historical_get(since=since, until=until, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlarmsV1Api->v1_alarms_historical_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **int**| timestamp for filtering the active alarms newer than | [optional] 
 **until** | **int**| timestamp for filtering the active alarms older than | [optional] 
 **limit** | **int**| limits the number of returned alarms | [optional] 

### Return type

[**list[Alarm]**](Alarm.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

