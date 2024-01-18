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


class GetDogmaDynamicItemsTypeIdItemIdOk(object):
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
        'created_by': 'int',
        'dogma_attributes': 'list[GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute]',
        'dogma_effects': 'list[GetDogmaDynamicItemsTypeIdItemIdDogmaEffect]',
        'mutator_type_id': 'int',
        'source_type_id': 'int'
    }

    attribute_map = {
        'created_by': 'created_by',
        'dogma_attributes': 'dogma_attributes',
        'dogma_effects': 'dogma_effects',
        'mutator_type_id': 'mutator_type_id',
        'source_type_id': 'source_type_id'
    }

    def __init__(self, created_by=None, dogma_attributes=None, dogma_effects=None, mutator_type_id=None, source_type_id=None, _configuration=None):  # noqa: E501
        """GetDogmaDynamicItemsTypeIdItemIdOk - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created_by = None
        self._dogma_attributes = None
        self._dogma_effects = None
        self._mutator_type_id = None
        self._source_type_id = None
        self.discriminator = None

        self.created_by = created_by
        self.dogma_attributes = dogma_attributes
        self.dogma_effects = dogma_effects
        self.mutator_type_id = mutator_type_id
        self.source_type_id = source_type_id

    @property
    def created_by(self):
        """Gets the created_by of this GetDogmaDynamicItemsTypeIdItemIdOk.  # noqa: E501

        The ID of the character who created the item  # noqa: E501

        :return: The created_by of this GetDogmaDynamicItemsTypeIdItemIdOk.  # noqa: E501
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this GetDogmaDynamicItemsTypeIdItemIdOk.

        The ID of the character who created the item  # noqa: E501

        :param created_by: The created_by of this GetDogmaDynamicItemsTypeIdItemIdOk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and created_by is None:
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def dogma_attributes(self):
        """Gets the dogma_attributes of this GetDogmaDynamicItemsTypeIdItemIdOk.  # noqa: E501

        dogma_attributes array  # noqa: E501

        :return: The dogma_attributes of this GetDogmaDynamicItemsTypeIdItemIdOk.  # noqa: E501
        :rtype: list[GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute]
        """
        return self._dogma_attributes

    @dogma_attributes.setter
    def dogma_attributes(self, dogma_attributes):
        """Sets the dogma_attributes of this GetDogmaDynamicItemsTypeIdItemIdOk.

        dogma_attributes array  # noqa: E501

        :param dogma_attributes: The dogma_attributes of this GetDogmaDynamicItemsTypeIdItemIdOk.  # noqa: E501
        :type: list[GetDogmaDynamicItemsTypeIdItemIdDogmaAttribute]
        """
        if self._configuration.client_side_validation and dogma_attributes is None:
            raise ValueError("Invalid value for `dogma_attributes`, must not be `None`")  # noqa: E501

        self._dogma_attributes = dogma_attributes

    @property
    def dogma_effects(self):
        """Gets the dogma_effects of this GetDogmaDynamicItemsTypeIdItemIdOk.  # noqa: E501

        dogma_effects array  # noqa: E501

        :return: The dogma_effects of this GetDogmaDynamicItemsTypeIdItemIdOk.  # noqa: E501
        :rtype: list[GetDogmaDynamicItemsTypeIdItemIdDogmaEffect]
        """
        return self._dogma_effects

    @dogma_effects.setter
    def dogma_effects(self, dogma_effects):
        """Sets the dogma_effects of this GetDogmaDynamicItemsTypeIdItemIdOk.

        dogma_effects array  # noqa: E501

        :param dogma_effects: The dogma_effects of this GetDogmaDynamicItemsTypeIdItemIdOk.  # noqa: E501
        :type: list[GetDogmaDynamicItemsTypeIdItemIdDogmaEffect]
        """
        if self._configuration.client_side_validation and dogma_effects is None:
            raise ValueError("Invalid value for `dogma_effects`, must not be `None`")  # noqa: E501

        self._dogma_effects = dogma_effects

    @property
    def mutator_type_id(self):
        """Gets the mutator_type_id of this GetDogmaDynamicItemsTypeIdItemIdOk.  # noqa: E501

        The type ID of the mutator used to generate the dynamic item.  # noqa: E501

        :return: The mutator_type_id of this GetDogmaDynamicItemsTypeIdItemIdOk.  # noqa: E501
        :rtype: int
        """
        return self._mutator_type_id

    @mutator_type_id.setter
    def mutator_type_id(self, mutator_type_id):
        """Sets the mutator_type_id of this GetDogmaDynamicItemsTypeIdItemIdOk.

        The type ID of the mutator used to generate the dynamic item.  # noqa: E501

        :param mutator_type_id: The mutator_type_id of this GetDogmaDynamicItemsTypeIdItemIdOk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and mutator_type_id is None:
            raise ValueError("Invalid value for `mutator_type_id`, must not be `None`")  # noqa: E501

        self._mutator_type_id = mutator_type_id

    @property
    def source_type_id(self):
        """Gets the source_type_id of this GetDogmaDynamicItemsTypeIdItemIdOk.  # noqa: E501

        The type ID of the source item the mutator was applied to create the dynamic item.  # noqa: E501

        :return: The source_type_id of this GetDogmaDynamicItemsTypeIdItemIdOk.  # noqa: E501
        :rtype: int
        """
        return self._source_type_id

    @source_type_id.setter
    def source_type_id(self, source_type_id):
        """Sets the source_type_id of this GetDogmaDynamicItemsTypeIdItemIdOk.

        The type ID of the source item the mutator was applied to create the dynamic item.  # noqa: E501

        :param source_type_id: The source_type_id of this GetDogmaDynamicItemsTypeIdItemIdOk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and source_type_id is None:
            raise ValueError("Invalid value for `source_type_id`, must not be `None`")  # noqa: E501

        self._source_type_id = source_type_id

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
        if issubclass(GetDogmaDynamicItemsTypeIdItemIdOk, dict):
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
        if not isinstance(other, GetDogmaDynamicItemsTypeIdItemIdOk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetDogmaDynamicItemsTypeIdItemIdOk):
            return True

        return self.to_dict() != other.to_dict()
