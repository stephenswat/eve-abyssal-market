# coding: utf-8

"""
    EVE Swagger Interface

    An OpenAPI for EVE Online  # noqa: E501

    OpenAPI spec version: 1.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class GatewayTimeout(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'error': 'str',
        'timeout': 'int'
    }

    attribute_map = {
        'error': 'error',
        'timeout': 'timeout'
    }

    def __init__(self, error=None, timeout=None, _configuration=None):  # noqa: E501
        """GatewayTimeout - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._error = None
        self._timeout = None
        self.discriminator = None

        self.error = error
        if timeout is not None:
            self.timeout = timeout

    @property
    def error(self):
        """Gets the error of this GatewayTimeout.  # noqa: E501

        Gateway timeout message  # noqa: E501

        :return: The error of this GatewayTimeout.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this GatewayTimeout.

        Gateway timeout message  # noqa: E501

        :param error: The error of this GatewayTimeout.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and error is None:
            raise ValueError("Invalid value for `error`, must not be `None`")  # noqa: E501

        self._error = error

    @property
    def timeout(self):
        """Gets the timeout of this GatewayTimeout.  # noqa: E501

        number of seconds the request was given  # noqa: E501

        :return: The timeout of this GatewayTimeout.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this GatewayTimeout.

        number of seconds the request was given  # noqa: E501

        :param timeout: The timeout of this GatewayTimeout.  # noqa: E501
        :type: int
        """

        self._timeout = timeout

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(GatewayTimeout, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GatewayTimeout):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GatewayTimeout):
            return True

        return self.to_dict() != other.to_dict()
