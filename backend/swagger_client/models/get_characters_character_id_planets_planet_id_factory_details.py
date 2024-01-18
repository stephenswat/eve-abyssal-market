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


class GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails(object):
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
        'schematic_id': 'int'
    }

    attribute_map = {
        'schematic_id': 'schematic_id'
    }

    def __init__(self, schematic_id=None, _configuration=None):  # noqa: E501
        """GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._schematic_id = None
        self.discriminator = None

        self.schematic_id = schematic_id

    @property
    def schematic_id(self):
        """Gets the schematic_id of this GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails.  # noqa: E501

        schematic_id integer  # noqa: E501

        :return: The schematic_id of this GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails.  # noqa: E501
        :rtype: int
        """
        return self._schematic_id

    @schematic_id.setter
    def schematic_id(self, schematic_id):
        """Sets the schematic_id of this GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails.

        schematic_id integer  # noqa: E501

        :param schematic_id: The schematic_id of this GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and schematic_id is None:
            raise ValueError("Invalid value for `schematic_id`, must not be `None`")  # noqa: E501

        self._schematic_id = schematic_id

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
        if issubclass(GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails, dict):
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
        if not isinstance(other, GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCharactersCharacterIdPlanetsPlanetIdFactoryDetails):
            return True

        return self.to_dict() != other.to_dict()
