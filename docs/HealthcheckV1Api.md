# swagger_client.HealthcheckV1Api

All URIs are relative to *https://localhost/sera*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_healthcheck_get**](HealthcheckV1Api.md#v1_healthcheck_get) | **GET** /v1/healthcheck | Get latest health-check timestamp


# **v1_healthcheck_get**
> str v1_healthcheck_get()

Get latest health-check timestamp

Returns latest health-check timestamp from Superna Eyeglass.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HealthcheckV1Api()

try:
    # Get latest health-check timestamp
    api_response = api_instance.v1_healthcheck_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthcheckV1Api->v1_healthcheck_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

