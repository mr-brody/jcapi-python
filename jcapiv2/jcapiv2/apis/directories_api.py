# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The next version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings. The most recent version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings.

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


class DirectoriesApi(object):
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

    def directories_list(self, content_type, accept, **kwargs):
        """
        List All Directories
        This endpoint returns all active directories (LDAP, O365 Suite, G-Suite).  #### Sample Request ```  curl -X GET https://console.jumpcloud.com/api/v2/directories \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.directories_list(content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str content_type: (required)
        :param str accept: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted the default list of fields will be returned. 
        :param int limit: The number of records to return at once.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: list[Directory]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.directories_list_with_http_info(content_type, accept, **kwargs)
        else:
            (data) = self.directories_list_with_http_info(content_type, accept, **kwargs)
            return data

    def directories_list_with_http_info(self, content_type, accept, **kwargs):
        """
        List All Directories
        This endpoint returns all active directories (LDAP, O365 Suite, G-Suite).  #### Sample Request ```  curl -X GET https://console.jumpcloud.com/api/v2/directories \\   -H 'accept: application/json' \\   -H 'content-type: application/json' \\   -H 'x-api-key: {API_KEY}' ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.directories_list_with_http_info(content_type, accept, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str content_type: (required)
        :param str accept: (required)
        :param list[str] fields: The comma separated fields included in the returned records. If omitted the default list of fields will be returned. 
        :param int limit: The number of records to return at once.
        :param int skip: The offset into the records to return.
        :param list[str] sort: The comma separated fields used to sort the collection. Default sort is ascending, prefix with `-` to sort descending. 
        :return: list[Directory]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_type', 'accept', 'fields', 'limit', 'skip', 'sort']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method directories_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params) or (params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `directories_list`")
        # verify the required parameter 'accept' is set
        if ('accept' not in params) or (params['accept'] is None):
            raise ValueError("Missing the required parameter `accept` when calling `directories_list`")


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'fields' in params:
            query_params.append(('fields', params['fields']))
            collection_formats['fields'] = 'csv'
        if 'limit' in params:
            query_params.append(('limit', params['limit']))
        if 'skip' in params:
            query_params.append(('skip', params['skip']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))
            collection_formats['sort'] = 'csv'

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']
        if 'accept' in params:
            header_params['Accept'] = params['accept']

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

        return self.api_client.call_api('/directories', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[Directory]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
