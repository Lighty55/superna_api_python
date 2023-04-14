# swagger_client.AirgapV2Api

All URIs are relative to *https://localhost/sera*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2_airgap_ecs_get**](AirgapV2Api.md#v2_airgap_ecs_get) | **GET** /v2/airgap/ecs | Get all ECS airgap jobs
[**v2_airgap_ecs_post**](AirgapV2Api.md#v2_airgap_ecs_post) | **POST** /v2/airgap/ecs | Update an ECS airgap job status
[**v2_airgap_ecssyncjobs_post**](AirgapV2Api.md#v2_airgap_ecssyncjobs_post) | **POST** /v2/airgap/ecssyncjobs | Vault agent ecs-sync jobs upload to eyeglass
[**v2_airgap_ecssyncschedules_get**](AirgapV2Api.md#v2_airgap_ecssyncschedules_get) | **GET** /v2/airgap/ecssyncschedules | Get all ECS-sync airgap jobs schedules
[**v2_airgap_vaultevents_post**](AirgapV2Api.md#v2_airgap_vaultevents_post) | **POST** /v2/airgap/vaultevents | Vault isilon events
[**v2_airgap_vaultheartbeat_post**](AirgapV2Api.md#v2_airgap_vaultheartbeat_post) | **POST** /v2/airgap/vaultheartbeat | Vault agent heartbeat


# **v2_airgap_ecs_get**
> ECSAirgapJobs v2_airgap_ecs_get(order=order, order_by=order_by, current_page=current_page, page_size=page_size)

Get all ECS airgap jobs

View all ECS airgap jobs that can run through vault engine

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
api_instance = swagger_client.AirgapV2Api(swagger_client.ApiClient(configuration))
order = 'order_example' # str | Optional ordering of results. (optional)
order_by = 'order_by_example' # str | Optional field on which to order results. (optional)
current_page = 56 # int | Current page in an optional paging scheme. (optional)
page_size = 56 # int | Number of results per page in an optional paging scheme. (optional)

try:
    # Get all ECS airgap jobs
    api_response = api_instance.v2_airgap_ecs_get(order=order, order_by=order_by, current_page=current_page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AirgapV2Api->v2_airgap_ecs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | **str**| Optional ordering of results. | [optional] 
 **order_by** | **str**| Optional field on which to order results. | [optional] 
 **current_page** | **int**| Current page in an optional paging scheme. | [optional] 
 **page_size** | **int**| Number of results per page in an optional paging scheme. | [optional] 

### Return type

[**ECSAirgapJobs**](ECSAirgapJobs.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_airgap_ecs_post**
> v2_airgap_ecs_post(name, update_ecs_air_gap)

Update an ECS airgap job status

Update status of an ECS airgap job.

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
api_instance = swagger_client.AirgapV2Api(swagger_client.ApiClient(configuration))
name = 'name_example' # str | Name of the ECS airgap job (as retrieved with /v2/jobs/airgap/ecs GET)
update_ecs_air_gap = swagger_client.UpdateECSAirGap() # UpdateECSAirGap | Update data for the specified ECS airgap job.

try:
    # Update an ECS airgap job status
    api_instance.v2_airgap_ecs_post(name, update_ecs_air_gap)
except ApiException as e:
    print("Exception when calling AirgapV2Api->v2_airgap_ecs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the ECS airgap job (as retrieved with /v2/jobs/airgap/ecs GET) | 
 **update_ecs_air_gap** | [**UpdateECSAirGap**](UpdateECSAirGap.md)| Update data for the specified ECS airgap job. | 

### Return type

void (empty response body)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_airgap_ecssyncjobs_post**
> str v2_airgap_ecssyncjobs_post(ecssyncjobs)

Vault agent ecs-sync jobs upload to eyeglass

Vault agent sends the list of ecs-sync jobs

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
api_instance = swagger_client.AirgapV2Api(swagger_client.ApiClient(configuration))
ecssyncjobs = swagger_client.ECSSyncJobsData() # ECSSyncJobsData | list of ecs-sync jobs.

try:
    # Vault agent ecs-sync jobs upload to eyeglass
    api_response = api_instance.v2_airgap_ecssyncjobs_post(ecssyncjobs)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AirgapV2Api->v2_airgap_ecssyncjobs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ecssyncjobs** | [**ECSSyncJobsData**](ECSSyncJobsData.md)| list of ecs-sync jobs. | 

### Return type

**str**

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_airgap_ecssyncschedules_get**
> list[ECSSyncJob] v2_airgap_ecssyncschedules_get(eva_id)

Get all ECS-sync airgap jobs schedules

Retrieve all ECS-sync jobs schedules

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
api_instance = swagger_client.AirgapV2Api(swagger_client.ApiClient(configuration))
eva_id = 'eva_id_example' # str | Vault agent ID

try:
    # Get all ECS-sync airgap jobs schedules
    api_response = api_instance.v2_airgap_ecssyncschedules_get(eva_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AirgapV2Api->v2_airgap_ecssyncschedules_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eva_id** | **str**| Vault agent ID | 

### Return type

[**list[ECSSyncJob]**](ECSSyncJob.md)

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_airgap_vaultevents_post**
> str v2_airgap_vaultevents_post(vault_events_data)

Vault isilon events

Vault agent sends vault isilon events

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
api_instance = swagger_client.AirgapV2Api(swagger_client.ApiClient(configuration))
vault_events_data = swagger_client.VaultEventsData() # VaultEventsData | Details about events and vault configuration.

try:
    # Vault isilon events
    api_response = api_instance.v2_airgap_vaultevents_post(vault_events_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AirgapV2Api->v2_airgap_vaultevents_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vault_events_data** | [**VaultEventsData**](VaultEventsData.md)| Details about events and vault configuration. | 

### Return type

**str**

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_airgap_vaultheartbeat_post**
> str v2_airgap_vaultheartbeat_post(heartbeat_details)

Vault agent heartbeat

Vault agent sends a heartbeat every minute as long as the vault is open

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
api_instance = swagger_client.AirgapV2Api(swagger_client.ApiClient(configuration))
heartbeat_details = swagger_client.HeartbeatDetails() # HeartbeatDetails | Details about related to vault agent configuration.

try:
    # Vault agent heartbeat
    api_response = api_instance.v2_airgap_vaultheartbeat_post(heartbeat_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AirgapV2Api->v2_airgap_vaultheartbeat_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **heartbeat_details** | [**HeartbeatDetails**](HeartbeatDetails.md)| Details about related to vault agent configuration. | 

### Return type

**str**

### Authorization

[internalApiKey](../README.md#internalApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

