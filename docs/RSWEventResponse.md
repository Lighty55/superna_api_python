# RSWEventResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_source** | **str** | Ransomware event source. | [optional] 
**object_buckets** | **list[str]** | S3 buckets involved in this ransomware event. This will be an empty array if this is not an ECS or AWS event. | [optional] 
**severity** | **str** | event severity (WARNING, MAJOR, CRITICAL) | [optional] 
**user** | **str** | user sid | [optional] 
**user_name** | **str** | user name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


