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


class WritableSnapshotsV2Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v2_writable_snapshots_delete(self, source_snap, target_path, ne, delete_config, **kwargs):  # noqa: E501
        """delete a writable snapshot  # noqa: E501

        Delete a writable snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_writable_snapshots_delete(source_snap, target_path, ne, delete_config, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_snap: Source Snapshot parameter (required)
        :param str target_path: Target path for writable snapshot (required)
        :param str ne: Cluster name parameter (required)
        :param str delete_config: Flag for delete configuration for deleting writable snapshot (required)
        :return: WritableSnapshotsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_writable_snapshots_delete_with_http_info(source_snap, target_path, ne, delete_config, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_writable_snapshots_delete_with_http_info(source_snap, target_path, ne, delete_config, **kwargs)  # noqa: E501
            return data

    def v2_writable_snapshots_delete_with_http_info(self, source_snap, target_path, ne, delete_config, **kwargs):  # noqa: E501
        """delete a writable snapshot  # noqa: E501

        Delete a writable snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_writable_snapshots_delete_with_http_info(source_snap, target_path, ne, delete_config, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_snap: Source Snapshot parameter (required)
        :param str target_path: Target path for writable snapshot (required)
        :param str ne: Cluster name parameter (required)
        :param str delete_config: Flag for delete configuration for deleting writable snapshot (required)
        :return: WritableSnapshotsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['source_snap', 'target_path', 'ne', 'delete_config']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_writable_snapshots_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'source_snap' is set
        if self.api_client.client_side_validation and ('source_snap' not in params or
                                                       params['source_snap'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `source_snap` when calling `v2_writable_snapshots_delete`")  # noqa: E501
        # verify the required parameter 'target_path' is set
        if self.api_client.client_side_validation and ('target_path' not in params or
                                                       params['target_path'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `target_path` when calling `v2_writable_snapshots_delete`")  # noqa: E501
        # verify the required parameter 'ne' is set
        if self.api_client.client_side_validation and ('ne' not in params or
                                                       params['ne'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `ne` when calling `v2_writable_snapshots_delete`")  # noqa: E501
        # verify the required parameter 'delete_config' is set
        if self.api_client.client_side_validation and ('delete_config' not in params or
                                                       params['delete_config'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `delete_config` when calling `v2_writable_snapshots_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'source_snap' in params:
            query_params.append(('sourceSnap', params['source_snap']))  # noqa: E501
        if 'target_path' in params:
            query_params.append(('targetPath', params['target_path']))  # noqa: E501
        if 'ne' in params:
            query_params.append(('ne', params['ne']))  # noqa: E501
        if 'delete_config' in params:
            query_params.append(('deleteConfig', params['delete_config']))  # noqa: E501

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
            '/v2/writable-snapshots', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WritableSnapshotsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_writable_snapshots_get(self, **kwargs):  # noqa: E501
        """Get all recent writable-snapshots snapshost jobs  # noqa: E501

        View all recent writable snapshots jobs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_writable_snapshots_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: WritableSnapshotsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_writable_snapshots_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v2_writable_snapshots_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v2_writable_snapshots_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all recent writable-snapshots snapshost jobs  # noqa: E501

        View all recent writable snapshots jobs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_writable_snapshots_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: WritableSnapshotsResponse
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
                    " to method v2_writable_snapshots_get" % key
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
            '/v2/writable-snapshots', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WritableSnapshotsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_writable_snapshots_job_status_get(self, job_id, **kwargs):  # noqa: E501
        """Get status of writable snapshots job by id  # noqa: E501

        Get status of writable snapshots job by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_writable_snapshots_job_status_get(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: Job ID (required)
        :return: JobStatusDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_writable_snapshots_job_status_get_with_http_info(job_id, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_writable_snapshots_job_status_get_with_http_info(job_id, **kwargs)  # noqa: E501
            return data

    def v2_writable_snapshots_job_status_get_with_http_info(self, job_id, **kwargs):  # noqa: E501
        """Get status of writable snapshots job by id  # noqa: E501

        Get status of writable snapshots job by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_writable_snapshots_job_status_get_with_http_info(job_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str job_id: Job ID (required)
        :return: JobStatusDetail
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_writable_snapshots_job_status_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if self.api_client.client_side_validation and ('job_id' not in params or
                                                       params['job_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `job_id` when calling `v2_writable_snapshots_job_status_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in params:
            query_params.append(('jobId', params['job_id']))  # noqa: E501

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
            '/v2/writable-snapshots/jobStatus', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JobStatusDetail',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v2_writable_snapshots_post(self, ne, target_path, source_path, copy_config_flag, **kwargs):  # noqa: E501
        """Create a writable snapshot  # noqa: E501

        Start a job to create a writable snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_writable_snapshots_post(ne, target_path, source_path, copy_config_flag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ne: Cluster Name (required)
        :param str target_path: Target path for writable snapshot (required)
        :param str source_path: Source path for writable snapshot (required)
        :param str copy_config_flag: Flag for copy config while creating writable snapshot (true/false) (required)
        :return: WritableSnapshotsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v2_writable_snapshots_post_with_http_info(ne, target_path, source_path, copy_config_flag, **kwargs)  # noqa: E501
        else:
            (data) = self.v2_writable_snapshots_post_with_http_info(ne, target_path, source_path, copy_config_flag, **kwargs)  # noqa: E501
            return data

    def v2_writable_snapshots_post_with_http_info(self, ne, target_path, source_path, copy_config_flag, **kwargs):  # noqa: E501
        """Create a writable snapshot  # noqa: E501

        Start a job to create a writable snapshot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v2_writable_snapshots_post_with_http_info(ne, target_path, source_path, copy_config_flag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ne: Cluster Name (required)
        :param str target_path: Target path for writable snapshot (required)
        :param str source_path: Source path for writable snapshot (required)
        :param str copy_config_flag: Flag for copy config while creating writable snapshot (true/false) (required)
        :return: WritableSnapshotsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ne', 'target_path', 'source_path', 'copy_config_flag']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v2_writable_snapshots_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ne' is set
        if self.api_client.client_side_validation and ('ne' not in params or
                                                       params['ne'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `ne` when calling `v2_writable_snapshots_post`")  # noqa: E501
        # verify the required parameter 'target_path' is set
        if self.api_client.client_side_validation and ('target_path' not in params or
                                                       params['target_path'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `target_path` when calling `v2_writable_snapshots_post`")  # noqa: E501
        # verify the required parameter 'source_path' is set
        if self.api_client.client_side_validation and ('source_path' not in params or
                                                       params['source_path'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `source_path` when calling `v2_writable_snapshots_post`")  # noqa: E501
        # verify the required parameter 'copy_config_flag' is set
        if self.api_client.client_side_validation and ('copy_config_flag' not in params or
                                                       params['copy_config_flag'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `copy_config_flag` when calling `v2_writable_snapshots_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ne' in params:
            query_params.append(('ne', params['ne']))  # noqa: E501
        if 'target_path' in params:
            query_params.append(('targetPath', params['target_path']))  # noqa: E501
        if 'source_path' in params:
            query_params.append(('sourcePath', params['source_path']))  # noqa: E501
        if 'copy_config_flag' in params:
            query_params.append(('copyConfigFlag', params['copy_config_flag']))  # noqa: E501

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
            '/v2/writable-snapshots', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WritableSnapshotsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
