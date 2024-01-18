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


class GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute(object):
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
        'attribute_id': 'int',
        'value': 'float'
    }

    attribute_map = {
        'attribute_id': 'attribute_id',
        'value': 'value'
    }

    def __init__(self, attribute_id=None, value=None, _configuration=None):  # noqa: E501
        """GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._attribute_id = None
        self._value = None
        self.discriminator = None

        self.attribute_id = attribute_id
        self.value = value

    @property
    def attribute_id(self):
        """Gets the attribute_id of this GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute.  # noqa: E501

        attribute_id integer  # noqa: E501

        :return: The attribute_id of this GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute.  # noqa: E501
        :rtype: int
        """
        return self._attribute_id

    @attribute_id.setter
    def attribute_id(self, attribute_id):
        """Sets the attribute_id of this GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute.

        attribute_id integer  # noqa: E501

        :param attribute_id: The attribute_id of this GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and attribute_id is None:
            raise ValueError("Invalid value for `attribute_id`, must not be `None`")  # noqa: E501

        self._attribute_id = attribute_id

    @property
    def value(self):
        """Gets the value of this GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute.  # noqa: E501

        value number  # noqa: E501

        :return: The value of this GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute.

        value number  # noqa: E501

        :param value: The value of this GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute, dict):
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
        if not isinstance(other, GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute):
            return True

        return self.to_dict() != other.to_dict()
