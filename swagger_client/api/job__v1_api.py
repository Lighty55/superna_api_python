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


class JobV1Api(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_jobs_drtest_post(self, enable, policy, **kwargs):  # noqa: E501
        """Enter/Exit DR test mode  # noqa: E501

        Enter/Exit DR test mode for a given policy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_jobs_drtest_post(enable, policy, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool enable: True = Make target writable (Enter DR test mode). False = Make target read-only (Exit DR test mode)  (required)
        :param str policy: DR testing policy id (as retrieved with /nodes/{id}/policies GET) (required)
        :param bool configsync: Run a configuration while DR test job
        :param bool datasync: Run policy while DR test job
        :return: PostResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_jobs_drtest_post_with_http_info(enable, policy, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_jobs_drtest_post_with_http_info(enable, policy, **kwargs)  # noqa: E501
            return data

    def v1_jobs_drtest_post_with_http_info(self, enable, policy, **kwargs):  # noqa: E501
        """Enter/Exit DR test mode  # noqa: E501

        Enter/Exit DR test mode for a given policy  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_jobs_drtest_post_with_http_info(enable, policy, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool enable: True = Make target writable (Enter DR test mode). False = Make target read-only (Exit DR test mode)  (required)
        :param str policy: DR testing policy id (as retrieved with /nodes/{id}/policies GET) (required)
        :param bool configsync: Run a configuration while DR test job
        :param bool datasync: Run policy while DR test job
        :return: PostResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enable', 'policy', 'configsync', 'datasync']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_jobs_drtest_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enable' is set
        if self.api_client.client_side_validation and ('enable' not in params or
                                                       params['enable'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `enable` when calling `v1_jobs_drtest_post`")  # noqa: E501
        # verify the required parameter 'policy' is set
        if self.api_client.client_side_validation and ('policy' not in params or
                                                       params['policy'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `policy` when calling `v1_jobs_drtest_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enable' in params:
            query_params.append(('enable', params['enable']))  # noqa: E501
        if 'configsync' in params:
            query_params.append(('configsync', params['configsync']))  # noqa: E501
        if 'datasync' in params:
            query_params.append(('datasync', params['datasync']))  # noqa: E501
        if 'policy' in params:
            query_params.append(('policy', params['policy']))  # noqa: E501

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
            '/v1/jobs/drtest', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_jobs_get(self, **kwargs):  # noqa: E501
        """Get failover jobs  # noqa: E501

        Returns failover jobs from Superna Eyeglass.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_jobs_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str state: filter running or complete jobs [all, running, finished]
        :param bool success: filter jobs by result success [true, false]
        :return: list[Job]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_jobs_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_jobs_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_jobs_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get failover jobs  # noqa: E501

        Returns failover jobs from Superna Eyeglass.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_jobs_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str state: filter running or complete jobs [all, running, finished]
        :param bool success: filter jobs by result success [true, false]
        :return: list[Job]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['state', 'success']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_jobs_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
        if 'success' in params:
            query_params.append(('success', params['success']))  # noqa: E501

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
            '/v1/jobs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Job]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_jobs_id_delete(self, id, **kwargs):  # noqa: E501
        """cancels a running failover job  # noqa: E501

        Cancels a running failover job  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_jobs_id_delete(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the job to retrieve (required)
        :param Empty empty: Empty body for delete request {}
        :return: Job
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_jobs_id_delete_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_jobs_id_delete_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def v1_jobs_id_delete_with_http_info(self, id, **kwargs):  # noqa: E501
        """cancels a running failover job  # noqa: E501

        Cancels a running failover job  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_jobs_id_delete_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the job to retrieve (required)
        :param Empty empty: Empty body for delete request {}
        :return: Job
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'empty']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_jobs_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `v1_jobs_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'empty' in params:
            body_params = params['empty']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['internalApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/v1/jobs/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Job',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_jobs_id_get(self, id, **kwargs):  # noqa: E501
        """Retreive a failover job by ID  # noqa: E501

        Retrieve a failover job by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_jobs_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the job to retrieve (required)
        :return: Job
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_jobs_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_jobs_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def v1_jobs_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retreive a failover job by ID  # noqa: E501

        Retrieve a failover job by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_jobs_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the job to retrieve (required)
        :return: Job
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
                    " to method v1_jobs_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `v1_jobs_id_get`")  # noqa: E501

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
            '/v1/jobs/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Job',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_jobs_id_log_get(self, id, **kwargs):  # noqa: E501
        """Retrieve the logfile for a running or finished failover job  # noqa: E501

        Get the failover jobs log  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_jobs_id_log_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the job to retrieve (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_jobs_id_log_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_jobs_id_log_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def v1_jobs_id_log_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieve the logfile for a running or finished failover job  # noqa: E501

        Get the failover jobs log  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_jobs_id_log_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: ID of the job to retrieve (required)
        :return: str
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
                    " to method v1_jobs_id_log_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `v1_jobs_id_log_get`")  # noqa: E501

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
            ['text/plain'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['internalApiKey']  # noqa: E501

        return self.api_client.call_api(
            '/v1/jobs/{id}/log', 'GET',
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

    def v1_jobs_post(self, sourceid, targetid, failovertarget, blockonwarnings, **kwargs):  # noqa: E501
        """Create a new failover job  # noqa: E501

        Launch a new failover job in Eyeglass.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_jobs_post(sourceid, targetid, failovertarget, blockonwarnings, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sourceid: ID of the source node for this job (required)
        :param str targetid: ID of the target node for this job (required)
        :param str failovertarget: ID of the access zone to failover OR IDs of syncIQ policies (comma separated) to failover. (required)
        :param bool blockonwarnings: Block failover on warnings (required)
        :param str pool: Pool name in case of pool failover. The name format is groupName:subnetName:poolName
        :param bool controlled: Execute a controlled failover by running operations against the source cluster  as well as the target
        :param bool datasync: Run the final incremental data sync before failover
        :param bool configsync: Run a configuration sync before failover
        :param bool resyncprep: Run resync prep on the source cluster to create the mirror policies
        :param bool disablemirror: Disable mirror policies created on the failover target
        :param bool quotasync: Run quota jobs to failover quotas to target
        :param bool rollbackrenameshares: Rollback renamed shares on failure
        :param bool smbdataintegrity: SMB data integrity failover
        :return: PostResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_jobs_post_with_http_info(sourceid, targetid, failovertarget, blockonwarnings, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_jobs_post_with_http_info(sourceid, targetid, failovertarget, blockonwarnings, **kwargs)  # noqa: E501
            return data

    def v1_jobs_post_with_http_info(self, sourceid, targetid, failovertarget, blockonwarnings, **kwargs):  # noqa: E501
        """Create a new failover job  # noqa: E501

        Launch a new failover job in Eyeglass.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_jobs_post_with_http_info(sourceid, targetid, failovertarget, blockonwarnings, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str sourceid: ID of the source node for this job (required)
        :param str targetid: ID of the target node for this job (required)
        :param str failovertarget: ID of the access zone to failover OR IDs of syncIQ policies (comma separated) to failover. (required)
        :param bool blockonwarnings: Block failover on warnings (required)
        :param str pool: Pool name in case of pool failover. The name format is groupName:subnetName:poolName
        :param bool controlled: Execute a controlled failover by running operations against the source cluster  as well as the target
        :param bool datasync: Run the final incremental data sync before failover
        :param bool configsync: Run a configuration sync before failover
        :param bool resyncprep: Run resync prep on the source cluster to create the mirror policies
        :param bool disablemirror: Disable mirror policies created on the failover target
        :param bool quotasync: Run quota jobs to failover quotas to target
        :param bool rollbackrenameshares: Rollback renamed shares on failure
        :param bool smbdataintegrity: SMB data integrity failover
        :return: PostResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sourceid', 'targetid', 'failovertarget', 'blockonwarnings', 'pool', 'controlled', 'datasync', 'configsync', 'resyncprep', 'disablemirror', 'quotasync', 'rollbackrenameshares', 'smbdataintegrity']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_jobs_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sourceid' is set
        if self.api_client.client_side_validation and ('sourceid' not in params or
                                                       params['sourceid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sourceid` when calling `v1_jobs_post`")  # noqa: E501
        # verify the required parameter 'targetid' is set
        if self.api_client.client_side_validation and ('targetid' not in params or
                                                       params['targetid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `targetid` when calling `v1_jobs_post`")  # noqa: E501
        # verify the required parameter 'failovertarget' is set
        if self.api_client.client_side_validation and ('failovertarget' not in params or
                                                       params['failovertarget'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `failovertarget` when calling `v1_jobs_post`")  # noqa: E501
        # verify the required parameter 'blockonwarnings' is set
        if self.api_client.client_side_validation and ('blockonwarnings' not in params or
                                                       params['blockonwarnings'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `blockonwarnings` when calling `v1_jobs_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'sourceid' in params:
            query_params.append(('sourceid', params['sourceid']))  # noqa: E501
        if 'targetid' in params:
            query_params.append(('targetid', params['targetid']))  # noqa: E501
        if 'failovertarget' in params:
            query_params.append(('failovertarget', params['failovertarget']))  # noqa: E501
        if 'pool' in params:
            query_params.append(('pool', params['pool']))  # noqa: E501
        if 'controlled' in params:
            query_params.append(('controlled', params['controlled']))  # noqa: E501
        if 'datasync' in params:
            query_params.append(('datasync', params['datasync']))  # noqa: E501
        if 'configsync' in params:
            query_params.append(('configsync', params['configsync']))  # noqa: E501
        if 'resyncprep' in params:
            query_params.append(('resyncprep', params['resyncprep']))  # noqa: E501
        if 'disablemirror' in params:
            query_params.append(('disablemirror', params['disablemirror']))  # noqa: E501
        if 'quotasync' in params:
            query_params.append(('quotasync', params['quotasync']))  # noqa: E501
        if 'blockonwarnings' in params:
            query_params.append(('blockonwarnings', params['blockonwarnings']))  # noqa: E501
        if 'rollbackrenameshares' in params:
            query_params.append(('rollbackrenameshares', params['rollbackrenameshares']))  # noqa: E501
        if 'smbdataintegrity' in params:
            query_params.append(('smbdataintegrity', params['smbdataintegrity']))  # noqa: E501

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
            '/v1/jobs', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_jobs_rehearsal_post(self, enable, sourceid, targetid, failovertarget, **kwargs):  # noqa: E501
        """Create a new rehearsal job  # noqa: E501

        Launch a new rehearsal job in Eyeglass.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_jobs_rehearsal_post(enable, sourceid, targetid, failovertarget, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool enable: Enable or disable (=false) the rehearsal mode (required)
        :param str sourceid: ID of the source node for this job (required)
        :param str targetid: ID of the target node for this job (required)
        :param str failovertarget: ID of the access zone to failover OR IDs of syncIQ policies (comma separated) to failover. (required)
        :param str pool: Pool name in case of pool failover. The name format is groupName:subnetName:poolName
        :return: PostResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_jobs_rehearsal_post_with_http_info(enable, sourceid, targetid, failovertarget, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_jobs_rehearsal_post_with_http_info(enable, sourceid, targetid, failovertarget, **kwargs)  # noqa: E501
            return data

    def v1_jobs_rehearsal_post_with_http_info(self, enable, sourceid, targetid, failovertarget, **kwargs):  # noqa: E501
        """Create a new rehearsal job  # noqa: E501

        Launch a new rehearsal job in Eyeglass.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_jobs_rehearsal_post_with_http_info(enable, sourceid, targetid, failovertarget, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool enable: Enable or disable (=false) the rehearsal mode (required)
        :param str sourceid: ID of the source node for this job (required)
        :param str targetid: ID of the target node for this job (required)
        :param str failovertarget: ID of the access zone to failover OR IDs of syncIQ policies (comma separated) to failover. (required)
        :param str pool: Pool name in case of pool failover. The name format is groupName:subnetName:poolName
        :return: PostResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['enable', 'sourceid', 'targetid', 'failovertarget', 'pool']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_jobs_rehearsal_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'enable' is set
        if self.api_client.client_side_validation and ('enable' not in params or
                                                       params['enable'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `enable` when calling `v1_jobs_rehearsal_post`")  # noqa: E501
        # verify the required parameter 'sourceid' is set
        if self.api_client.client_side_validation and ('sourceid' not in params or
                                                       params['sourceid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sourceid` when calling `v1_jobs_rehearsal_post`")  # noqa: E501
        # verify the required parameter 'targetid' is set
        if self.api_client.client_side_validation and ('targetid' not in params or
                                                       params['targetid'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `targetid` when calling `v1_jobs_rehearsal_post`")  # noqa: E501
        # verify the required parameter 'failovertarget' is set
        if self.api_client.client_side_validation and ('failovertarget' not in params or
                                                       params['failovertarget'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `failovertarget` when calling `v1_jobs_rehearsal_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'enable' in params:
            query_params.append(('enable', params['enable']))  # noqa: E501
        if 'sourceid' in params:
            query_params.append(('sourceid', params['sourceid']))  # noqa: E501
        if 'targetid' in params:
            query_params.append(('targetid', params['targetid']))  # noqa: E501
        if 'failovertarget' in params:
            query_params.append(('failovertarget', params['failovertarget']))  # noqa: E501
        if 'pool' in params:
            query_params.append(('pool', params['pool']))  # noqa: E501

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
            '/v1/jobs/rehearsal', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PostResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)