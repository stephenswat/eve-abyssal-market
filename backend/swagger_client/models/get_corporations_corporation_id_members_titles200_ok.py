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


class GetCorporationsCorporationIdMembersTitles200Ok(object):
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
        'character_id': 'int',
        'titles': 'list[int]'
    }

    attribute_map = {
        'character_id': 'character_id',
        'titles': 'titles'
    }

    def __init__(self, character_id=None, titles=None, _configuration=None):  # noqa: E501
        """GetCorporationsCorporationIdMembersTitles200Ok - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._character_id = None
        self._titles = None
        self.discriminator = None

        self.character_id = character_id
        self.titles = titles

    @property
    def character_id(self):
        """Gets the character_id of this GetCorporationsCorporationIdMembersTitles200Ok.  # noqa: E501

        character_id integer  # noqa: E501

        :return: The character_id of this GetCorporationsCorporationIdMembersTitles200Ok.  # noqa: E501
        :rtype: int
        """
        return self._character_id

    @character_id.setter
    def character_id(self, character_id):
        """Sets the character_id of this GetCorporationsCorporationIdMembersTitles200Ok.

        character_id integer  # noqa: E501

        :param character_id: The character_id of this GetCorporationsCorporationIdMembersTitles200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and character_id is None:
            raise ValueError("Invalid value for `character_id`, must not be `None`")  # noqa: E501

        self._character_id = character_id

    @property
    def titles(self):
        """Gets the titles of this GetCorporationsCorporationIdMembersTitles200Ok.  # noqa: E501

        A list of title_id  # noqa: E501

        :return: The titles of this GetCorporationsCorporationIdMembersTitles200Ok.  # noqa: E501
        :rtype: list[int]
        """
        return self._titles

    @titles.setter
    def titles(self, titles):
        """Sets the titles of this GetCorporationsCorporationIdMembersTitles200Ok.

        A list of title_id  # noqa: E501

        :param titles: The titles of this GetCorporationsCorporationIdMembersTitles200Ok.  # noqa: E501
        :type: list[int]
        """
        if self._configuration.client_side_validation and titles is None:
            raise ValueError("Invalid value for `titles`, must not be `None`")  # noqa: E501

        self._titles = titles

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
        if issubclass(GetCorporationsCorporationIdMembersTitles200Ok, dict):
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
        if not isinstance(other, GetCorporationsCorporationIdMembersTitles200Ok):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCorporationsCorporationIdMembersTitles200Ok):
            return True

        return self.to_dict() != other.to_dict()
