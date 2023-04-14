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


class WhitelistV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_ransomware_whitelist_get(self, **kwargs):  # noqa: E501
        """Get all Whitelist settings  # noqa: E501

        Returns all Whitelist settings for ransomware  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_ransomware_whitelist_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Whitelist]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_ransomware_whitelist_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_ransomware_whitelist_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_ransomware_whitelist_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all Whitelist settings  # noqa: E501

        Returns all Whitelist settings for ransomware  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_ransomware_whitelist_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Whitelist]
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
                    " to method v1_ransomware_whitelist_get" % key
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
            '/v1/ransomware/whitelist', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Whitelist]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_ransomware_whitelist_newer_than_get(self, newer_than, **kwargs):  # noqa: E501
        """Get Whitelist settings that have changed  # noqa: E501

        Returns Whitelist settings that were changed since given timestamp  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_ransomware_whitelist_newer_than_get(newer_than, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int newer_than: timestamp for filtering the whitelist settings (required)
        :return: list[Whitelist]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_ransomware_whitelist_newer_than_get_with_http_info(newer_than, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_ransomware_whitelist_newer_than_get_with_http_info(newer_than, **kwargs)  # noqa: E501
            return data

    def v1_ransomware_whitelist_newer_than_get_with_http_info(self, newer_than, **kwargs):  # noqa: E501
        """Get Whitelist settings that have changed  # noqa: E501

        Returns Whitelist settings that were changed since given timestamp  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_ransomware_whitelist_newer_than_get_with_http_info(newer_than, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int newer_than: timestamp for filtering the whitelist settings (required)
        :return: list[Whitelist]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['newer_than']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_ransomware_whitelist_newer_than_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'newer_than' is set
        if self.api_client.client_side_validation and ('newer_than' not in params or
                                                       params['newer_than'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `newer_than` when calling `v1_ransomware_whitelist_newer_than_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'newer_than' in params:
            path_params['newer_than'] = params['newer_than']  # noqa: E501

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
            '/v1/ransomware/whitelist/{newer_than}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Whitelist]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)