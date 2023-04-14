# coding: utf-8

"""
    Superna Eyeglass REST API

    A collection of utilities for programmatic interaction with Superna Eyeglass  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@superna.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AirgapV2Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v2_airgap_ecs_get(self, **kwargs):  # noqa: E501
        """Get all ECS airgap jobs  # noqa: E501

        View all ECS airgap jobs that can run through vault engine  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_airgap_ecs_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order: Optional ordering of results.
        :param str order_by: Optional field on which to order results.
        :param int current_page: Current page in an optional paging scheme.
        :param int page_size: Number of results per page in an optional paging scheme.
        :return: ECSAirgapJobs
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_airgap_ecs_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v2_airgap_ecs_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v2_airgap_ecs_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all ECS airgap jobs  # noqa: E501

        View all ECS airgap jobs that can run through vault engine  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_airgap_ecs_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order: Optional ordering of results.
        :param str order_by: Optional field on which to order results.
        :param int current_page: Current page in an optional paging scheme.
        :param int page_size: Number of results per page in an optional paging scheme.
        :return: ECSAirgapJobs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order', 'order_by', 'current_page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_airgap_ecs_get" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('page_size' in params and params['page_size'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `page_size` when calling `v2_airgap_ecs_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'order_by' in params:
            query_params.append(('orderBy', params['order_by']))  # noqa: E501
        if 'current_page' in params:
            query_params.append(('currentPage', params['current_page']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('pageSize', params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['internalApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/airgap/ecs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ECSAirgapJobs',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_airgap_ecs_post(self, name, update_ecs_air_gap, **kwargs):  # noqa: E501
        """Update an ECS airgap job status  # noqa: E501

        Update status of an ECS airgap job.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_airgap_ecs_post(name, update_ecs_air_gap, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name of the ECS airgap job (as retrieved with /v2/jobs/airgap/ecs GET) (required)
        :param UpdateECSAirGap update_ecs_air_gap: Update data for the specified ECS airgap job. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_airgap_ecs_post_with_http_info(name, update_ecs_air_gap, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_airgap_ecs_post_with_http_info(name, update_ecs_air_gap, **kwargs)  # noqa: E501
            return data

    def v2_airgap_ecs_post_with_http_info(self, name, update_ecs_air_gap, **kwargs):  # noqa: E501
        """Update an ECS airgap job status  # noqa: E501

        Update status of an ECS airgap job.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_airgap_ecs_post_with_http_info(name, update_ecs_air_gap, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: Name of the ECS airgap job (as retrieved with /v2/jobs/airgap/ecs GET) (required)
        :param UpdateECSAirGap update_ecs_air_gap: Update data for the specified ECS airgap job. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'update_ecs_air_gap']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_airgap_ecs_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in params or
                                                       params['name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `name` when calling `v2_airgap_ecs_post`")  # noqa: E501
        # verify the required parameter 'update_ecs_air_gap' is set
        if self.api_client.client_side_validation and ('update_ecs_air_gap' not in params or
                                                       params['update_ecs_air_gap'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `update_ecs_air_gap` when calling `v2_airgap_ecs_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_ecs_air_gap' in params:
            body_params = params['update_ecs_air_gap']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['internalApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/airgap/ecs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_airgap_ecssyncjobs_post(self, ecssyncjobs, **kwargs):  # noqa: E501
        """Vault agent ecs-sync jobs upload to eyeglass  # noqa: E501

        Vault agent sends the list of ecs-sync jobs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_airgap_ecssyncjobs_post(ecssyncjobs, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ECSSyncJobsData ecssyncjobs: list of ecs-sync jobs. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_airgap_ecssyncjobs_post_with_http_info(ecssyncjobs, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_airgap_ecssyncjobs_post_with_http_info(ecssyncjobs, **kwargs)  # noqa: E501
            return data

    def v2_airgap_ecssyncjobs_post_with_http_info(self, ecssyncjobs, **kwargs):  # noqa: E501
        """Vault agent ecs-sync jobs upload to eyeglass  # noqa: E501

        Vault agent sends the list of ecs-sync jobs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_airgap_ecssyncjobs_post_with_http_info(ecssyncjobs, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ECSSyncJobsData ecssyncjobs: list of ecs-sync jobs. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ecssyncjobs']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_airgap_ecssyncjobs_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ecssyncjobs' is set
        if self.api_client.client_side_validation and ('ecssyncjobs' not in params or
                                                       params['ecssyncjobs'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `ecssyncjobs` when calling `v2_airgap_ecssyncjobs_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ecssyncjobs' in params:
            body_params = params['ecssyncjobs']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['internalApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/airgap/ecssyncjobs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_airgap_ecssyncschedules_get(self, eva_id, **kwargs):  # noqa: E501
        """Get all ECS-sync airgap jobs schedules  # noqa: E501

        Retrieve all ECS-sync jobs schedules  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_airgap_ecssyncschedules_get(eva_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str eva_id: Vault agent ID (required)
        :return: list[ECSSyncJob]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_airgap_ecssyncschedules_get_with_http_info(eva_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_airgap_ecssyncschedules_get_with_http_info(eva_id, **kwargs)  # noqa: E501
            return data

    def v2_airgap_ecssyncschedules_get_with_http_info(self, eva_id, **kwargs):  # noqa: E501
        """Get all ECS-sync airgap jobs schedules  # noqa: E501

        Retrieve all ECS-sync jobs schedules  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_airgap_ecssyncschedules_get_with_http_info(eva_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str eva_id: Vault agent ID (required)
        :return: list[ECSSyncJob]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['eva_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_airgap_ecssyncschedules_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'eva_id' is set
        if self.api_client.client_side_validation and ('eva_id' not in params or
                                                       params['eva_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `eva_id` when calling `v2_airgap_ecssyncschedules_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'eva_id' in params:
            query_params.append(('evaID', params['eva_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['internalApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/airgap/ecssyncschedules', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ECSSyncJob]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_airgap_vaultevents_post(self, vault_events_data, **kwargs):  # noqa: E501
        """Vault isilon events  # noqa: E501

        Vault agent sends vault isilon events  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_airgap_vaultevents_post(vault_events_data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VaultEventsData vault_events_data: Details about events and vault configuration. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_airgap_vaultevents_post_with_http_info(vault_events_data, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_airgap_vaultevents_post_with_http_info(vault_events_data, **kwargs)  # noqa: E501
            return data

    def v2_airgap_vaultevents_post_with_http_info(self, vault_events_data, **kwargs):  # noqa: E501
        """Vault isilon events  # noqa: E501

        Vault agent sends vault isilon events  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_airgap_vaultevents_post_with_http_info(vault_events_data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VaultEventsData vault_events_data: Details about events and vault configuration. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vault_events_data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_airgap_vaultevents_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vault_events_data' is set
        if self.api_client.client_side_validation and ('vault_events_data' not in params or
                                                       params['vault_events_data'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `vault_events_data` when calling `v2_airgap_vaultevents_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'vault_events_data' in params:
            body_params = params['vault_events_data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['internalApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/airgap/vaultevents', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_airgap_vaultheartbeat_post(self, heartbeat_details, **kwargs):  # noqa: E501
        """Vault agent heartbeat  # noqa: E501

        Vault agent sends a heartbeat every minute as long as the vault is open  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_airgap_vaultheartbeat_post(heartbeat_details, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HeartbeatDetails heartbeat_details: Details about related to vault agent configuration. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_airgap_vaultheartbeat_post_with_http_info(heartbeat_details, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_airgap_vaultheartbeat_post_with_http_info(heartbeat_details, **kwargs)  # noqa: E501
            return data

    def v2_airgap_vaultheartbeat_post_with_http_info(self, heartbeat_details, **kwargs):  # noqa: E501
        """Vault agent heartbeat  # noqa: E501

        Vault agent sends a heartbeat every minute as long as the vault is open  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_airgap_vaultheartbeat_post_with_http_info(heartbeat_details, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param HeartbeatDetails heartbeat_details: Details about related to vault agent configuration. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['heartbeat_details']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_airgap_vaultheartbeat_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'heartbeat_details' is set
        if self.api_client.client_side_validation and ('heartbeat_details' not in params or
                                                       params['heartbeat_details'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `heartbeat_details` when calling `v2_airgap_vaultheartbeat_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'heartbeat_details' in params:
            body_params = params['heartbeat_details']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['internalApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/v2/airgap/vaultheartbeat', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)