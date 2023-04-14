# swagger_client.RansomwareV2Api

All URIs are relative to *https://localhost/sera*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_ransomware_criticalpaths_get**](RansomwareV2Api.md#v2_ransomware_criticalpaths_get) | **GET** /v2/ransomware/criticalpaths | Get all recent critical path snapshot jobs
[**v2_ransomware_criticalpaths_id_get**](RansomwareV2Api.md#v2_ransomware_criticalpaths_id_get) | **GET** /v2/ransomware/criticalpaths/{id} | Retrieves a recently run snapshot job
[**v2_ransomware_criticalpaths_post**](RansomwareV2Api.md#v2_ransomware_criticalpaths_post) | **POST** /v2/ransomware/criticalpaths | Take a snapshot of all critical paths
[**v2_ransomware_hasactiveevents_get**](RansomwareV2Api.md#v2_ransomware_hasactiveevents_get) | **GET** /v2/ransomware/hasactiveevents | returns true/false wheather there are active events ot not in eyeglass 
[**v2_ransomware_lockout_user_post**](RansomwareV2Api.md#v2_ransomware_lockout_user_post) | **POST** /v2/ransomware/lockout/{user} | Creates a ransomware event and locks out user


# **v2_ransomware_criticalpaths_get**
> list[JobStatusDetail] v2_ransomware_criticalpaths_get(state=state)

Get all recent critical path snapshot jobs

View all recent critical path snapshot jobs

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
api_instance = swagger_client.RansomwareV2Api(swagger_client.ApiClient(configuration))
state = 'state_example' # str | filter running or complete jobs [all, running, finished] (optional)

try:
    # Get all recent critical path snapshot jobs
    api_response = api_instance.v2_ransomware_criticalpaths_get(state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RansomwareV2Api->v2_ransomware_criticalpaths_get: %s\n" % e)
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

# **v2_ransomware_criticalpaths_id_get**
> JobStatusDetail v2_ransomware_criticalpaths_id_get(id)

Retrieves a recently run snapshot job

Retrieves a recently run snapshot job

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
api_instance = swagger_client.RansomwareV2Api(swagger_client.ApiClient(configuration))
id = 'id_example' # str | ID of the job to retrieve

try:
    # Retrieves a recently run snapshot job
    api_response = api_instance.v2_ransomware_criticalpaths_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RansomwareV2Api->v2_ransomware_criticalpaths_id_get: %s\n" % e)
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

# **v2_ransomware_criticalpaths_post**
> PostResponse v2_ransomware_criticalpaths_post()

Take a snapshot of all critical paths

Take a snapshot of all critical paths

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
api_instance = swagger_client.RansomwareV2Api(swagger_client.ApiClient(configuration))

try:
    # Take a snapshot of all critical paths
    api_response = api_instance.v2_ransomware_criticalpaths_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RansomwareV2Api->v2_ransomware_criticalpaths_post: %s\n" % e)
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

# **v2_ransomware_hasactiveevents_get**
> str v2_ransomware_hasactiveevents_get()

returns true/false wheather there are active events ot not in eyeglass 

Checks if there are active rsw events in eyeglass

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
api_instance = swagger_client.RansomwareV2Api(swagger_client.ApiClient(configuration))

try:
    # returns true/false wheather there are active events ot not in eyeglass 
    api_response = api_instance.v2_ransomware_hasactiveevents_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RansomwareV2Api->v2_ransomware_hasactiveevents_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_ransomware_lockout_user_post**
> PostResponse v2_ransomware_lockout_user_post(user)

Creates a ransomware event and locks out user

Creates a ransomware event and locks out user

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
api_instance = swagger_client.RansomwareV2Api(swagger_client.ApiClient(configuration))
user = 'user_example' # str | SID or username of user

try:
    # Creates a ransomware event and locks out user
    api_response = api_instance.v2_ransomware_lockout_user_post(user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RansomwareV2Api->v2_ransomware_lockout_user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | **str**| SID or username of user | 

### Return type

[**PostResponse**](PostResponse.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

