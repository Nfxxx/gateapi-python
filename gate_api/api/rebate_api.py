# coding: utf-8

"""
    Gate API v4

    Welcome to Gate.io API  APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from gate_api.api_client import ApiClient
from gate_api.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class RebateApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def agency_transaction_history(self, **kwargs):  # noqa: E501
        """The broker obtains the transaction history of the recommended user  # noqa: E501

        Record time range cannot exceed 30 days  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agency_transaction_history(async_req=True)
        >>> result = thread.get()

        :param bool async_req: execute request asynchronously
        :param str currency_pair: Specify the currency pair, if not specified, return all currency pairs
        :param str user_id: User ID. If not specified, all user records will be returned
        :param int _from: Time range beginning, default to 7 days before current time
        :param int to: Time range ending, default to current time
        :param int limit: Maximum number of records to be returned in a single list
        :param int offset: List offset, starting from 0
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :rtype: list[gate_api.AgencyTransactionHistory]
        :return: If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.agency_transaction_history_with_http_info(**kwargs)  # noqa: E501

    def agency_transaction_history_with_http_info(self, **kwargs):  # noqa: E501
        """The broker obtains the transaction history of the recommended user  # noqa: E501

        Record time range cannot exceed 30 days  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agency_transaction_history_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool async_req: execute request asynchronously
        :param str currency_pair: Specify the currency pair, if not specified, return all currency pairs
        :param str user_id: User ID. If not specified, all user records will be returned
        :param int _from: Time range beginning, default to 7 days before current time
        :param int to: Time range ending, default to current time
        :param int limit: Maximum number of records to be returned in a single list
        :param int offset: List offset, starting from 0
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :rtype: tuple(list[gate_api.AgencyTransactionHistory], status_code(int), headers(HTTPHeaderDict))
        :return: If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['currency_pair', 'user_id', '_from', 'to', 'limit', 'offset']
        all_params.extend(['async_req', '_return_http_data_only', '_preload_content', '_request_timeout'])

        for k, v in six.iteritems(local_var_params['kwargs']):
            if k not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'" " to method agency_transaction_history" % k
                )
            local_var_params[k] = v
        del local_var_params['kwargs']

        if (
            self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 1000
        ):  # noqa: E501
            raise ApiValueError(
                "Invalid value for parameter `limit` when calling `agency_transaction_history`, must be a value less than or equal to `1000`"
            )  # noqa: E501
        if (
            self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1
        ):  # noqa: E501
            raise ApiValueError(
                "Invalid value for parameter `limit` when calling `agency_transaction_history`, must be a value greater than or equal to `1`"
            )  # noqa: E501
        if (
            self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0
        ):  # noqa: E501
            raise ApiValueError(
                "Invalid value for parameter `offset` when calling `agency_transaction_history`, must be a value greater than or equal to `0`"
            )  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'currency_pair' in local_var_params and local_var_params['currency_pair'] is not None:  # noqa: E501
            query_params.append(('currency_pair', local_var_params['currency_pair']))  # noqa: E501
        if 'user_id' in local_var_params and local_var_params['user_id'] is not None:  # noqa: E501
            query_params.append(('user_id', local_var_params['user_id']))  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'to' in local_var_params and local_var_params['to'] is not None:  # noqa: E501
            query_params.append(('to', local_var_params['to']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiv4']  # noqa: E501

        return self.api_client.call_api(
            '/rebate/agency/transaction_history',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AgencyTransactionHistory]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
        )

    def agency_commissions_history(self, **kwargs):  # noqa: E501
        """The broker obtains the commission history of the recommended user  # noqa: E501

        Record time range cannot exceed 30 days  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agency_commissions_history(async_req=True)
        >>> result = thread.get()

        :param bool async_req: execute request asynchronously
        :param str currency: Filter by currency. Return all currency records if not specified
        :param str user_id: User ID. If not specified, all user records will be returned
        :param int _from: Time range beginning, default to 7 days before current time
        :param int to: Time range ending, default to current time
        :param int limit: Maximum number of records to be returned in a single list
        :param int offset: List offset, starting from 0
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :rtype: list[gate_api.AgencyCommissionHistory]
        :return: If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.agency_commissions_history_with_http_info(**kwargs)  # noqa: E501

    def agency_commissions_history_with_http_info(self, **kwargs):  # noqa: E501
        """The broker obtains the commission history of the recommended user  # noqa: E501

        Record time range cannot exceed 30 days  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.agency_commissions_history_with_http_info(async_req=True)
        >>> result = thread.get()

        :param bool async_req: execute request asynchronously
        :param str currency: Filter by currency. Return all currency records if not specified
        :param str user_id: User ID. If not specified, all user records will be returned
        :param int _from: Time range beginning, default to 7 days before current time
        :param int to: Time range ending, default to current time
        :param int limit: Maximum number of records to be returned in a single list
        :param int offset: List offset, starting from 0
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :rtype: tuple(list[gate_api.AgencyCommissionHistory], status_code(int), headers(HTTPHeaderDict))
        :return: If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['currency', 'user_id', '_from', 'to', 'limit', 'offset']
        all_params.extend(['async_req', '_return_http_data_only', '_preload_content', '_request_timeout'])

        for k, v in six.iteritems(local_var_params['kwargs']):
            if k not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'" " to method agency_commissions_history" % k
                )
            local_var_params[k] = v
        del local_var_params['kwargs']

        if (
            self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] > 1000
        ):  # noqa: E501
            raise ApiValueError(
                "Invalid value for parameter `limit` when calling `agency_commissions_history`, must be a value less than or equal to `1000`"
            )  # noqa: E501
        if (
            self.api_client.client_side_validation and 'limit' in local_var_params and local_var_params['limit'] < 1
        ):  # noqa: E501
            raise ApiValueError(
                "Invalid value for parameter `limit` when calling `agency_commissions_history`, must be a value greater than or equal to `1`"
            )  # noqa: E501
        if (
            self.api_client.client_side_validation and 'offset' in local_var_params and local_var_params['offset'] < 0
        ):  # noqa: E501
            raise ApiValueError(
                "Invalid value for parameter `offset` when calling `agency_commissions_history`, must be a value greater than or equal to `0`"
            )  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'currency' in local_var_params and local_var_params['currency'] is not None:  # noqa: E501
            query_params.append(('currency', local_var_params['currency']))  # noqa: E501
        if 'user_id' in local_var_params and local_var_params['user_id'] is not None:  # noqa: E501
            query_params.append(('user_id', local_var_params['user_id']))  # noqa: E501
        if '_from' in local_var_params and local_var_params['_from'] is not None:  # noqa: E501
            query_params.append(('from', local_var_params['_from']))  # noqa: E501
        if 'to' in local_var_params and local_var_params['to'] is not None:  # noqa: E501
            query_params.append(('to', local_var_params['to']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiv4']  # noqa: E501

        return self.api_client.call_api(
            '/rebate/agency/commission_history',
            'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AgencyCommissionHistory]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats,
        )
