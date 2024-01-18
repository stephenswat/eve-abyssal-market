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


class GetCharactersCharacterIdOnlineOk(object):
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
        'last_login': 'datetime',
        'last_logout': 'datetime',
        'logins': 'int',
        'online': 'bool'
    }

    attribute_map = {
        'last_login': 'last_login',
        'last_logout': 'last_logout',
        'logins': 'logins',
        'online': 'online'
    }

    def __init__(self, last_login=None, last_logout=None, logins=None, online=None, _configuration=None):  # noqa: E501
        """GetCharactersCharacterIdOnlineOk - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._last_login = None
        self._last_logout = None
        self._logins = None
        self._online = None
        self.discriminator = None

        if last_login is not None:
            self.last_login = last_login
        if last_logout is not None:
            self.last_logout = last_logout
        if logins is not None:
            self.logins = logins
        self.online = online

    @property
    def last_login(self):
        """Gets the last_login of this GetCharactersCharacterIdOnlineOk.  # noqa: E501

        Timestamp of the last login  # noqa: E501

        :return: The last_login of this GetCharactersCharacterIdOnlineOk.  # noqa: E501
        :rtype: datetime
        """
        return self._last_login

    @last_login.setter
    def last_login(self, last_login):
        """Sets the last_login of this GetCharactersCharacterIdOnlineOk.

        Timestamp of the last login  # noqa: E501

        :param last_login: The last_login of this GetCharactersCharacterIdOnlineOk.  # noqa: E501
        :type: datetime
        """

        self._last_login = last_login

    @property
    def last_logout(self):
        """Gets the last_logout of this GetCharactersCharacterIdOnlineOk.  # noqa: E501

        Timestamp of the last logout  # noqa: E501

        :return: The last_logout of this GetCharactersCharacterIdOnlineOk.  # noqa: E501
        :rtype: datetime
        """
        return self._last_logout

    @last_logout.setter
    def last_logout(self, last_logout):
        """Sets the last_logout of this GetCharactersCharacterIdOnlineOk.

        Timestamp of the last logout  # noqa: E501

        :param last_logout: The last_logout of this GetCharactersCharacterIdOnlineOk.  # noqa: E501
        :type: datetime
        """

        self._last_logout = last_logout

    @property
    def logins(self):
        """Gets the logins of this GetCharactersCharacterIdOnlineOk.  # noqa: E501

        Total number of times the character has logged in  # noqa: E501

        :return: The logins of this GetCharactersCharacterIdOnlineOk.  # noqa: E501
        :rtype: int
        """
        return self._logins

    @logins.setter
    def logins(self, logins):
        """Sets the logins of this GetCharactersCharacterIdOnlineOk.

        Total number of times the character has logged in  # noqa: E501

        :param logins: The logins of this GetCharactersCharacterIdOnlineOk.  # noqa: E501
        :type: int
        """

        self._logins = logins

    @property
    def online(self):
        """Gets the online of this GetCharactersCharacterIdOnlineOk.  # noqa: E501

        If the character is online  # noqa: E501

        :return: The online of this GetCharactersCharacterIdOnlineOk.  # noqa: E501
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this GetCharactersCharacterIdOnlineOk.

        If the character is online  # noqa: E501

        :param online: The online of this GetCharactersCharacterIdOnlineOk.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and online is None:
            raise ValueError("Invalid value for `online`, must not be `None`")  # noqa: E501

        self._online = online

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
        if issubclass(GetCharactersCharacterIdOnlineOk, dict):
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
        if not isinstance(other, GetCharactersCharacterIdOnlineOk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCharactersCharacterIdOnlineOk):
            return True

        return self.to_dict() != other.to_dict()
