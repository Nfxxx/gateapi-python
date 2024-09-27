# coding: utf-8

"""
    Gate API v4

    Welcome to Gate.io API  APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gate_api.configuration import Configuration


class OptionsSettlement(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'time': 'float',
        'contract': 'str',
        'profit': 'str',
        'fee': 'str',
        'strike_price': 'str',
        'settle_price': 'str',
    }

    attribute_map = {
        'time': 'time',
        'contract': 'contract',
        'profit': 'profit',
        'fee': 'fee',
        'strike_price': 'strike_price',
        'settle_price': 'settle_price',
    }

    def __init__(
        self,
        time=None,
        contract=None,
        profit=None,
        fee=None,
        strike_price=None,
        settle_price=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (float, str, str, str, str, str, Configuration) -> None
        """OptionsSettlement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._time = None
        self._contract = None
        self._profit = None
        self._fee = None
        self._strike_price = None
        self._settle_price = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if contract is not None:
            self.contract = contract
        if profit is not None:
            self.profit = profit
        if fee is not None:
            self.fee = fee
        if strike_price is not None:
            self.strike_price = strike_price
        if settle_price is not None:
            self.settle_price = settle_price

    @property
    def time(self):
        """Gets the time of this OptionsSettlement.  # noqa: E501

        Last changed time of configuration  # noqa: E501

        :return: The time of this OptionsSettlement.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this OptionsSettlement.

        Last changed time of configuration  # noqa: E501

        :param time: The time of this OptionsSettlement.  # noqa: E501
        :type: float
        """

        self._time = time

    @property
    def contract(self):
        """Gets the contract of this OptionsSettlement.  # noqa: E501

        Options contract name  # noqa: E501

        :return: The contract of this OptionsSettlement.  # noqa: E501
        :rtype: str
        """
        return self._contract

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this OptionsSettlement.

        Options contract name  # noqa: E501

        :param contract: The contract of this OptionsSettlement.  # noqa: E501
        :type: str
        """

        self._contract = contract

    @property
    def profit(self):
        """Gets the profit of this OptionsSettlement.  # noqa: E501

        Settlement profit per size (quote currency)  # noqa: E501

        :return: The profit of this OptionsSettlement.  # noqa: E501
        :rtype: str
        """
        return self._profit

    @profit.setter
    def profit(self, profit):
        """Sets the profit of this OptionsSettlement.

        Settlement profit per size (quote currency)  # noqa: E501

        :param profit: The profit of this OptionsSettlement.  # noqa: E501
        :type: str
        """

        self._profit = profit

    @property
    def fee(self):
        """Gets the fee of this OptionsSettlement.  # noqa: E501

        Settlement fee per size (quote currency)  # noqa: E501

        :return: The fee of this OptionsSettlement.  # noqa: E501
        :rtype: str
        """
        return self._fee

    @fee.setter
    def fee(self, fee):
        """Sets the fee of this OptionsSettlement.

        Settlement fee per size (quote currency)  # noqa: E501

        :param fee: The fee of this OptionsSettlement.  # noqa: E501
        :type: str
        """

        self._fee = fee

    @property
    def strike_price(self):
        """Gets the strike_price of this OptionsSettlement.  # noqa: E501

        Strike price (quote currency)  # noqa: E501

        :return: The strike_price of this OptionsSettlement.  # noqa: E501
        :rtype: str
        """
        return self._strike_price

    @strike_price.setter
    def strike_price(self, strike_price):
        """Sets the strike_price of this OptionsSettlement.

        Strike price (quote currency)  # noqa: E501

        :param strike_price: The strike_price of this OptionsSettlement.  # noqa: E501
        :type: str
        """

        self._strike_price = strike_price

    @property
    def settle_price(self):
        """Gets the settle_price of this OptionsSettlement.  # noqa: E501

        Settlement price (quote currency)  # noqa: E501

        :return: The settle_price of this OptionsSettlement.  # noqa: E501
        :rtype: str
        """
        return self._settle_price

    @settle_price.setter
    def settle_price(self, settle_price):
        """Sets the settle_price of this OptionsSettlement.

        Settlement price (quote currency)  # noqa: E501

        :param settle_price: The settle_price of this OptionsSettlement.  # noqa: E501
        :type: str
        """

        self._settle_price = settle_price

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OptionsSettlement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OptionsSettlement):
            return True

        return self.to_dict() != other.to_dict()
