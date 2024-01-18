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


class GetCorporationCorporationIdMiningObservers200Ok(object):
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
        'last_updated': 'date',
        'observer_id': 'int',
        'observer_type': 'str'
    }

    attribute_map = {
        'last_updated': 'last_updated',
        'observer_id': 'observer_id',
        'observer_type': 'observer_type'
    }

    def __init__(self, last_updated=None, observer_id=None, observer_type=None, _configuration=None):  # noqa: E501
        """GetCorporationCorporationIdMiningObservers200Ok - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._last_updated = None
        self._observer_id = None
        self._observer_type = None
        self.discriminator = None

        self.last_updated = last_updated
        self.observer_id = observer_id
        self.observer_type = observer_type

    @property
    def last_updated(self):
        """Gets the last_updated of this GetCorporationCorporationIdMiningObservers200Ok.  # noqa: E501

        last_updated string  # noqa: E501

        :return: The last_updated of this GetCorporationCorporationIdMiningObservers200Ok.  # noqa: E501
        :rtype: date
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this GetCorporationCorporationIdMiningObservers200Ok.

        last_updated string  # noqa: E501

        :param last_updated: The last_updated of this GetCorporationCorporationIdMiningObservers200Ok.  # noqa: E501
        :type: date
        """
        if self._configuration.client_side_validation and last_updated is None:
            raise ValueError("Invalid value for `last_updated`, must not be `None`")  # noqa: E501

        self._last_updated = last_updated

    @property
    def observer_id(self):
        """Gets the observer_id of this GetCorporationCorporationIdMiningObservers200Ok.  # noqa: E501

        The entity that was observing the asteroid field when it was mined.   # noqa: E501

        :return: The observer_id of this GetCorporationCorporationIdMiningObservers200Ok.  # noqa: E501
        :rtype: int
        """
        return self._observer_id

    @observer_id.setter
    def observer_id(self, observer_id):
        """Sets the observer_id of this GetCorporationCorporationIdMiningObservers200Ok.

        The entity that was observing the asteroid field when it was mined.   # noqa: E501

        :param observer_id: The observer_id of this GetCorporationCorporationIdMiningObservers200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and observer_id is None:
            raise ValueError("Invalid value for `observer_id`, must not be `None`")  # noqa: E501

        self._observer_id = observer_id

    @property
    def observer_type(self):
        """Gets the observer_type of this GetCorporationCorporationIdMiningObservers200Ok.  # noqa: E501

        The category of the observing entity  # noqa: E501

        :return: The observer_type of this GetCorporationCorporationIdMiningObservers200Ok.  # noqa: E501
        :rtype: str
        """
        return self._observer_type

    @observer_type.setter
    def observer_type(self, observer_type):
        """Sets the observer_type of this GetCorporationCorporationIdMiningObservers200Ok.

        The category of the observing entity  # noqa: E501

        :param observer_type: The observer_type of this GetCorporationCorporationIdMiningObservers200Ok.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and observer_type is None:
            raise ValueError("Invalid value for `observer_type`, must not be `None`")  # noqa: E501
        allowed_values = ["structure"]  # noqa: E501
        if (self._configuration.client_side_validation and
                observer_type not in allowed_values):
            raise ValueError(
                "Invalid value for `observer_type` ({0}), must be one of {1}"  # noqa: E501
                .format(observer_type, allowed_values)
            )

        self._observer_type = observer_type

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
        if issubclass(GetCorporationCorporationIdMiningObservers200Ok, dict):
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
        if not isinstance(other, GetCorporationCorporationIdMiningObservers200Ok):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCorporationCorporationIdMiningObservers200Ok):
            return True

        return self.to_dict() != other.to_dict()
