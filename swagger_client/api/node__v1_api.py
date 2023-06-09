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


class NodeV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_nodes_get(self, **kwargs):  # noqa: E501
        """Get all nodes  # noqa: E501

        Returns all Superna Eyeglass Managed Devices.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_nodes_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Node]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_nodes_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_nodes_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_nodes_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all nodes  # noqa: E501

        Returns all Superna Eyeglass Managed Devices.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_nodes_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Node]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_nodes_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/v1/nodes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Node]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_nodes_id_get(self, id, **kwargs):  # noqa: E501
        """Find nodes by ID  # noqa: E501

        Returns the Superna Eyeglass Managed Devices based on ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_nodes_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the node to retrieve (required)
        :return: Node
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_nodes_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_nodes_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def v1_nodes_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Find nodes by ID  # noqa: E501

        Returns the Superna Eyeglass Managed Devices based on ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_nodes_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the node to retrieve (required)
        :return: Node
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_nodes_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `v1_nodes_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

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
            '/v1/nodes/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Node',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_nodes_id_policies_get(self, id, fo_readiness, **kwargs):  # noqa: E501
        """Find policies for a node  # noqa: E501

        Returns the syncIQ policies for this node  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_nodes_id_policies_get(id, fo_readiness, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the node to retrieve (required)
        :param bool fo_readiness: Retrieve also failover readiness status details (required)
        :return: list[Policy]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_nodes_id_policies_get_with_http_info(id, fo_readiness, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_nodes_id_policies_get_with_http_info(id, fo_readiness, **kwargs)  # noqa: E501
            return data

    def v1_nodes_id_policies_get_with_http_info(self, id, fo_readiness, **kwargs):  # noqa: E501
        """Find policies for a node  # noqa: E501

        Returns the syncIQ policies for this node  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_nodes_id_policies_get_with_http_info(id, fo_readiness, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the node to retrieve (required)
        :param bool fo_readiness: Retrieve also failover readiness status details (required)
        :return: list[Policy]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'fo_readiness']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_nodes_id_policies_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `v1_nodes_id_policies_get`")  # noqa: E501
        # verify the required parameter 'fo_readiness' is set
        if self.api_client.client_side_validation and ('fo_readiness' not in params or
                                                       params['fo_readiness'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `fo_readiness` when calling `v1_nodes_id_policies_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'fo_readiness' in params:
            query_params.append(('foReadiness', params['fo_readiness']))  # noqa: E501

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
            '/v1/nodes/{id}/policies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Policy]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_nodes_id_policies_name_get(self, id, name, **kwargs):  # noqa: E501
        """Find policy by name  # noqa: E501

        Returns the syncIQ policy for this node and this policy name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_nodes_id_policies_name_get(id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the node to retrieve (required)
        :param str name: name of the policy (required)
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_nodes_id_policies_name_get_with_http_info(id, name, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_nodes_id_policies_name_get_with_http_info(id, name, **kwargs)  # noqa: E501
            return data

    def v1_nodes_id_policies_name_get_with_http_info(self, id, name, **kwargs):  # noqa: E501
        """Find policy by name  # noqa: E501

        Returns the syncIQ policy for this node and this policy name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_nodes_id_policies_name_get_with_http_info(id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the node to retrieve (required)
        :param str name: name of the policy (required)
        :return: Policy
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_nodes_id_policies_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `v1_nodes_id_policies_name_get`")  # noqa: E501
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in params or
                                                       params['name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `name` when calling `v1_nodes_id_policies_name_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

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
            '/v1/nodes/{id}/policies/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Policy',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_nodes_id_pools_get(self, id, fo_readiness, **kwargs):  # noqa: E501
        """Find pools for a node  # noqa: E501

        Returns the pools for this node  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_nodes_id_pools_get(id, fo_readiness, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the node to retrieve (required)
        :param bool fo_readiness: Retrieve also failover readiness status details (required)
        :return: list[Pool]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_nodes_id_pools_get_with_http_info(id, fo_readiness, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_nodes_id_pools_get_with_http_info(id, fo_readiness, **kwargs)  # noqa: E501
            return data

    def v1_nodes_id_pools_get_with_http_info(self, id, fo_readiness, **kwargs):  # noqa: E501
        """Find pools for a node  # noqa: E501

        Returns the pools for this node  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_nodes_id_pools_get_with_http_info(id, fo_readiness, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the node to retrieve (required)
        :param bool fo_readiness: Retrieve also failover readiness status details (required)
        :return: list[Pool]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'fo_readiness']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_nodes_id_pools_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `v1_nodes_id_pools_get`")  # noqa: E501
        # verify the required parameter 'fo_readiness' is set
        if self.api_client.client_side_validation and ('fo_readiness' not in params or
                                                       params['fo_readiness'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `fo_readiness` when calling `v1_nodes_id_pools_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'fo_readiness' in params:
            query_params.append(('foReadiness', params['fo_readiness']))  # noqa: E501

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
            '/v1/nodes/{id}/pools', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Pool]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_nodes_id_pools_name_get(self, id, name, **kwargs):  # noqa: E501
        """Find pool by name   # noqa: E501

        Returns the pool by its name on a given node  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_nodes_id_pools_name_get(id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the node to retrieve (required)
        :param str name: name of the pool (groupName:subnetName:poolName) (required)
        :return: Pool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_nodes_id_pools_name_get_with_http_info(id, name, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_nodes_id_pools_name_get_with_http_info(id, name, **kwargs)  # noqa: E501
            return data

    def v1_nodes_id_pools_name_get_with_http_info(self, id, name, **kwargs):  # noqa: E501
        """Find pool by name   # noqa: E501

        Returns the pool by its name on a given node  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_nodes_id_pools_name_get_with_http_info(id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the node to retrieve (required)
        :param str name: name of the pool (groupName:subnetName:poolName) (required)
        :return: Pool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_nodes_id_pools_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `v1_nodes_id_pools_name_get`")  # noqa: E501
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in params or
                                                       params['name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `name` when calling `v1_nodes_id_pools_name_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

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
            '/v1/nodes/{id}/pools/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Pool',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_nodes_id_zones_get(self, id, fo_readiness, **kwargs):  # noqa: E501
        """Find zones for a node  # noqa: E501

        Returns the access zones for this node  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_nodes_id_zones_get(id, fo_readiness, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the node to retrieve (required)
        :param bool fo_readiness: Retrieve also failover readiness status details (required)
        :return: list[Zone]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_nodes_id_zones_get_with_http_info(id, fo_readiness, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_nodes_id_zones_get_with_http_info(id, fo_readiness, **kwargs)  # noqa: E501
            return data

    def v1_nodes_id_zones_get_with_http_info(self, id, fo_readiness, **kwargs):  # noqa: E501
        """Find zones for a node  # noqa: E501

        Returns the access zones for this node  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_nodes_id_zones_get_with_http_info(id, fo_readiness, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the node to retrieve (required)
        :param bool fo_readiness: Retrieve also failover readiness status details (required)
        :return: list[Zone]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'fo_readiness']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_nodes_id_zones_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `v1_nodes_id_zones_get`")  # noqa: E501
        # verify the required parameter 'fo_readiness' is set
        if self.api_client.client_side_validation and ('fo_readiness' not in params or
                                                       params['fo_readiness'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `fo_readiness` when calling `v1_nodes_id_zones_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []
        if 'fo_readiness' in params:
            query_params.append(('foReadiness', params['fo_readiness']))  # noqa: E501

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
            '/v1/nodes/{id}/zones', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Zone]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_nodes_id_zones_name_get(self, id, name, **kwargs):  # noqa: E501
        """Find zone name for a node  # noqa: E501

        Find job by zone name for a node id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_nodes_id_zones_name_get(id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the node to retrieve (required)
        :param str name: name of the zone (required)
        :return: Zone
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_nodes_id_zones_name_get_with_http_info(id, name, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_nodes_id_zones_name_get_with_http_info(id, name, **kwargs)  # noqa: E501
            return data

    def v1_nodes_id_zones_name_get_with_http_info(self, id, name, **kwargs):  # noqa: E501
        """Find zone name for a node  # noqa: E501

        Find job by zone name for a node id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_nodes_id_zones_name_get_with_http_info(id, name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the node to retrieve (required)
        :param str name: name of the zone (required)
        :return: Zone
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_nodes_id_zones_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `v1_nodes_id_zones_name_get`")  # noqa: E501
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in params or
                                                       params['name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `name` when calling `v1_nodes_id_zones_name_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501
        if 'name' in params:
            path_params['name'] = params['name']  # noqa: E501

        query_params = []

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
            '/v1/nodes/{id}/zones/{name}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Zone',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
