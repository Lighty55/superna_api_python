# swagger_client.RansomwareV1Api

All URIs are relative to *https://localhost/sera*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_ransomware_heartbeat_post**](RansomwareV1Api.md#v1_ransomware_heartbeat_post) | **POST** /v1/ransomware/heartbeat | 
[**v1_ransomware_notification_post**](RansomwareV1Api.md#v1_ransomware_notification_post) | **POST** /v1/ransomware/notification | Send an RDA event to Eyeglass to be handled
[**v1_ransomware_rswevents_get**](RansomwareV1Api.md#v1_ransomware_rswevents_get) | **GET** /v1/ransomware/rswevents | 


# **v1_ransomware_heartbeat_post**
> HeartbeatResponse v1_ransomware_heartbeat_post(ip, token, esaid, name=name, ostime=ostime, status=status)



Eyeglass Service appliance Endpoints register and update at this url.

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
api_instance = swagger_client.RansomwareV1Api(swagger_client.ApiClient(configuration))
ip = 'ip_example' # str | ip address of this node
token = 'token_example' # str | Api token from Eyeglass Rest API
esaid = 'esaid_example' # str | id of the node sending the heartbeat
name = 'name_example' # str | name of this node (optional)
ostime = 'ostime_example' # str | OS time (optional)
status = swagger_client.HeartbeatRequestBody() # HeartbeatRequestBody | List of component statuses (optional)

try:
    api_response = api_instance.v1_ransomware_heartbeat_post(ip, token, esaid, name=name, ostime=ostime, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RansomwareV1Api->v1_ransomware_heartbeat_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| ip address of this node | 
 **token** | **str**| Api token from Eyeglass Rest API | 
 **esaid** | **str**| id of the node sending the heartbeat | 
 **name** | **str**| name of this node | [optional] 
 **ostime** | **str**| OS time | [optional] 
 **status** | [**HeartbeatRequestBody**](HeartbeatRequestBody.md)| List of component statuses | [optional] 

### Return type

[**HeartbeatResponse**](HeartbeatResponse.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ransomware_notification_post**
> NotificationResponse v1_ransomware_notification_post(sid)

Send an RDA event to Eyeglass to be handled

Send a RDA event to Eyeglass.

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
api_instance = swagger_client.RansomwareV1Api(swagger_client.ApiClient(configuration))
sid = 'sid_example' # str | SID of user potentially harmful

try:
    # Send an RDA event to Eyeglass to be handled
    api_response = api_instance.v1_ransomware_notification_post(sid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RansomwareV1Api->v1_ransomware_notification_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sid** | **str**| SID of user potentially harmful | 

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ransomware_rswevents_get**
> list[RSWEventResponse] v1_ransomware_rswevents_get()



Get a list active RSW events

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
api_instance = swagger_client.RansomwareV1Api(swagger_client.ApiClient(configuration))

try:
    api_response = api_instance.v1_ransomware_rswevents_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RansomwareV1Api->v1_ransomware_rswevents_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RSWEventResponse]**](RSWEventResponse.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

