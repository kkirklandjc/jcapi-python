# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CommandsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def graph_command_associations_list(self, command_id, targets, content_type, accept, **kwargs):
        """
        List the associations of a Command
        This endpoint will return the _direct_ associations of this Command.  A direct association can be a non-homogenous relationship between 2 different objects. for example Commands and User Groups.   #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/commands/{Command_ID}/associations?targets=system_group \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.graph_command_associations_list(command_id, targets, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str command_id: ObjectID of the Command. (required)
        :param list[str] targets:  (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: 
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.graph_command_associations_list_with_http_info(command_id, targets, content_type, accept, **kwargs)
        else:
            (data) = self.graph_command_associations_list_with_http_info(command_id, targets, content_type, accept, **kwargs)
            return data

    def graph_command_associations_list_with_http_info(self, command_id, targets, content_type, accept, **kwargs):
        """
        List the associations of a Command
        This endpoint will return the _direct_ associations of this Command.  A direct association can be a non-homogenous relationship between 2 different objects. for example Commands and User Groups.   #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/commands/{Command_ID}/associations?targets=system_group \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.graph_command_associations_list_with_http_info(command_id, targets, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str command_id: ObjectID of the Command. (required)
        :param list[str] targets:  (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: 
        :return: list[GraphConnection]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['command_id', 'targets', 'content_type', 'accept', 'limit', 'skip', 'x_org_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_command_associations_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'command_id' is set
        if ('command_id' not in params) or (params['command_id'] is None):
            raise ValueError("Missing the required parameter `command_id` when calling `graph_command_associations_list`")
        # verify the required parameter 'targets' is set
        if ('targets' not in params) or (params['targets'] is None):
            raise ValueError("Missing the required parameter `targets` when calling `graph_command_associations_list`")
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params) or (params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `graph_command_associations_list`")
        # verify the required parameter 'accept' is set
        if ('accept' not in params) or (params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `graph_command_associations_list`")


        collection_formats = {}

        path_params = {}
        if 'command_id' in params:
            path_params['command_id'] = params['command_id']

        query_params = []
        if 'targets' in params:
            query_params.append(('targets', params['targets']))
            collection_formats['targets'] = 'csv'
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'skip' in params:
            query_params.append(('skip', params['skip']))

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']
        if 'accept' in params:
            header_params['Accept'] = params['accept']
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['x-api-key']

        return self.api_client.call_api('/commands/{command_id}/associations', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GraphConnection]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def graph_command_associations_post(self, command_id, content_type, accept, **kwargs):
        """
        Manage the associations of a Command
        This endpoint will allow you to manage the _direct_ associations of this Command.  A direct association can be a non-homogenous relationship between 2 different objects. for example Commands and User Groups.   #### Sample Request ```  curl -X POST https://console.jumpcloud.com/api/v2/commands/{Command_ID}/associations \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"system_group\",     \"id\": \"Group_ID\" }' ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.graph_command_associations_post(command_id, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str command_id: ObjectID of the Command. (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param GraphManagementReq body:
        :param str x_org_id: 
        :return: InlineResponse204
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.graph_command_associations_post_with_http_info(command_id, content_type, accept, **kwargs)
        else:
            (data) = self.graph_command_associations_post_with_http_info(command_id, content_type, accept, **kwargs)
            return data

    def graph_command_associations_post_with_http_info(self, command_id, content_type, accept, **kwargs):
        """
        Manage the associations of a Command
        This endpoint will allow you to manage the _direct_ associations of this Command.  A direct association can be a non-homogenous relationship between 2 different objects. for example Commands and User Groups.   #### Sample Request ```  curl -X POST https://console.jumpcloud.com/api/v2/commands/{Command_ID}/associations \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' \\   -d '{     \"op\": \"add\",     \"type\": \"system_group\",     \"id\": \"Group_ID\" }' ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.graph_command_associations_post_with_http_info(command_id, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str command_id: ObjectID of the Command. (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param GraphManagementReq body:
        :param str x_org_id: 
        :return: InlineResponse204
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['command_id', 'content_type', 'accept', 'body', 'x_org_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_command_associations_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'command_id' is set
        if ('command_id' not in params) or (params['command_id'] is None):
            raise ValueError("Missing the required parameter `command_id` when calling `graph_command_associations_post`")
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params) or (params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `graph_command_associations_post`")
        # verify the required parameter 'accept' is set
        if ('accept' not in params) or (params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `graph_command_associations_post`")


        collection_formats = {}

        path_params = {}
        if 'command_id' in params:
            path_params['command_id'] = params['command_id']

        query_params = []

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']
        if 'accept' in params:
            header_params['Accept'] = params['accept']
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['x-api-key']

        return self.api_client.call_api('/commands/{command_id}/associations', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InlineResponse204',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def graph_command_traverse_system(self, command_id, content_type, accept, **kwargs):
        """
        List the Systems bound to a Command
        This endpoint will return all Systems bound to a Command, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Command to the corresponding System; this array represents all grouping and/or associations that would have to be removed to deprovision the System from this Command.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/commands/{Command_ID}/systems \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.graph_command_traverse_system(command_id, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str command_id: ObjectID of the Command. (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: 
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.graph_command_traverse_system_with_http_info(command_id, content_type, accept, **kwargs)
        else:
            (data) = self.graph_command_traverse_system_with_http_info(command_id, content_type, accept, **kwargs)
            return data

    def graph_command_traverse_system_with_http_info(self, command_id, content_type, accept, **kwargs):
        """
        List the Systems bound to a Command
        This endpoint will return all Systems bound to a Command, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Command to the corresponding System; this array represents all grouping and/or associations that would have to be removed to deprovision the System from this Command.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/commands/{Command_ID}/systems \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.graph_command_traverse_system_with_http_info(command_id, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str command_id: ObjectID of the Command. (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: 
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['command_id', 'content_type', 'accept', 'limit', 'skip', 'x_org_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_command_traverse_system" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'command_id' is set
        if ('command_id' not in params) or (params['command_id'] is None):
            raise ValueError("Missing the required parameter `command_id` when calling `graph_command_traverse_system`")
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params) or (params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `graph_command_traverse_system`")
        # verify the required parameter 'accept' is set
        if ('accept' not in params) or (params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `graph_command_traverse_system`")


        collection_formats = {}

        path_params = {}
        if 'command_id' in params:
            path_params['command_id'] = params['command_id']

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'skip' in params:
            query_params.append(('skip', params['skip']))

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']
        if 'accept' in params:
            header_params['Accept'] = params['accept']
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['x-api-key']

        return self.api_client.call_api('/commands/{command_id}/systems', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GraphObjectWithPaths]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def graph_command_traverse_system_group(self, command_id, content_type, accept, **kwargs):
        """
        List the System Groups bound to a Command
        This endpoint will return all System Groups bound to a Command, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Command to the corresponding System Group; this array represents all grouping and/or associations that would have to be removed to deprovision the System Group from this Command.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/commands/{Command_ID}/systemgroups \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.graph_command_traverse_system_group(command_id, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str command_id: ObjectID of the Command. (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: 
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.graph_command_traverse_system_group_with_http_info(command_id, content_type, accept, **kwargs)
        else:
            (data) = self.graph_command_traverse_system_group_with_http_info(command_id, content_type, accept, **kwargs)
            return data

    def graph_command_traverse_system_group_with_http_info(self, command_id, content_type, accept, **kwargs):
        """
        List the System Groups bound to a Command
        This endpoint will return all System Groups bound to a Command, either directly or indirectly, essentially traversing the JumpCloud Graph for your Organization.  Each element will contain the group's type, id, attributes and paths.  The `attributes` object is a key/value hash of compiled graph attributes for all paths followed.  The `paths` array enumerates each path from this Command to the corresponding System Group; this array represents all grouping and/or associations that would have to be removed to deprovision the System Group from this Command.  See `/members` and `/associations` endpoints to manage those collections.  #### Sample Request ``` curl -X GET https://console.jumpcloud.com/api/v2/commands/{Command_ID}/systemgroups \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.graph_command_traverse_system_group_with_http_info(command_id, content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str command_id: ObjectID of the Command. (required)
        :param str content_type: (required)
        :param str accept: (required)
        :param int limit: The number of records to return at once. Limited to 100.
        :param int skip: The offset into the records to return.
        :param str x_org_id: 
        :return: list[GraphObjectWithPaths]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['command_id', 'content_type', 'accept', 'limit', 'skip', 'x_org_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method graph_command_traverse_system_group" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'command_id' is set
        if ('command_id' not in params) or (params['command_id'] is None):
            raise ValueError("Missing the required parameter `command_id` when calling `graph_command_traverse_system_group`")
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params) or (params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `graph_command_traverse_system_group`")
        # verify the required parameter 'accept' is set
        if ('accept' not in params) or (params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `graph_command_traverse_system_group`")


        collection_formats = {}

        path_params = {}
        if 'command_id' in params:
            path_params['command_id'] = params['command_id']

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'skip' in params:
            query_params.append(('skip', params['skip']))

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']
        if 'accept' in params:
            header_params['Accept'] = params['accept']
        if 'x_org_id' in params:
            header_params['x-org-id'] = params['x_org_id']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['x-api-key']

        return self.api_client.call_api('/commands/{command_id}/systemgroups', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[GraphObjectWithPaths]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
