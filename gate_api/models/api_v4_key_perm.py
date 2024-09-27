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


class ApiV4KeyPerm(object):
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
    openapi_types = {'name': 'str', 'read_only': 'bool'}

    attribute_map = {'name': 'name', 'read_only': 'read_only'}

    def __init__(self, name=None, read_only=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, bool, Configuration) -> None
        """ApiV4KeyPerm - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._read_only = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if read_only is not None:
            self.read_only = read_only

    @property
    def name(self):
        """Gets the name of this ApiV4KeyPerm.  # noqa: E501

        Permission name (all permissions will be removed if no value is passed)  - wallet: wallet - spot: spot/margin - futures: perpetual contract - delivery: delivery - earn: earn - options: options  # noqa: E501

        :return: The name of this ApiV4KeyPerm.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiV4KeyPerm.

        Permission name (all permissions will be removed if no value is passed)  - wallet: wallet - spot: spot/margin - futures: perpetual contract - delivery: delivery - earn: earn - options: options  # noqa: E501

        :param name: The name of this ApiV4KeyPerm.  # noqa: E501
        :type: str
        """
        allowed_values = ["wallet", "spot", "futures", "delivery", "earn", "options"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and name not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}".format(name, allowed_values)  # noqa: E501
            )

        self._name = name

    @property
    def read_only(self):
        """Gets the read_only of this ApiV4KeyPerm.  # noqa: E501

        read only  # noqa: E501

        :return: The read_only of this ApiV4KeyPerm.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this ApiV4KeyPerm.

        read only  # noqa: E501

        :param read_only: The read_only of this ApiV4KeyPerm.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

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
        if not isinstance(other, ApiV4KeyPerm):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApiV4KeyPerm):
            return True

        return self.to_dict() != other.to_dict()
