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


class GetFwSystems200Ok(object):
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
        'contested': 'str',
        'occupier_faction_id': 'int',
        'owner_faction_id': 'int',
        'solar_system_id': 'int',
        'victory_points': 'int',
        'victory_points_threshold': 'int'
    }

    attribute_map = {
        'contested': 'contested',
        'occupier_faction_id': 'occupier_faction_id',
        'owner_faction_id': 'owner_faction_id',
        'solar_system_id': 'solar_system_id',
        'victory_points': 'victory_points',
        'victory_points_threshold': 'victory_points_threshold'
    }

    def __init__(self, contested=None, occupier_faction_id=None, owner_faction_id=None, solar_system_id=None, victory_points=None, victory_points_threshold=None, _configuration=None):  # noqa: E501
        """GetFwSystems200Ok - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._contested = None
        self._occupier_faction_id = None
        self._owner_faction_id = None
        self._solar_system_id = None
        self._victory_points = None
        self._victory_points_threshold = None
        self.discriminator = None

        self.contested = contested
        self.occupier_faction_id = occupier_faction_id
        self.owner_faction_id = owner_faction_id
        self.solar_system_id = solar_system_id
        self.victory_points = victory_points
        self.victory_points_threshold = victory_points_threshold

    @property
    def contested(self):
        """Gets the contested of this GetFwSystems200Ok.  # noqa: E501

        contested string  # noqa: E501

        :return: The contested of this GetFwSystems200Ok.  # noqa: E501
        :rtype: str
        """
        return self._contested

    @contested.setter
    def contested(self, contested):
        """Sets the contested of this GetFwSystems200Ok.

        contested string  # noqa: E501

        :param contested: The contested of this GetFwSystems200Ok.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and contested is None:
            raise ValueError("Invalid value for `contested`, must not be `None`")  # noqa: E501
        allowed_values = ["captured", "contested", "uncontested", "vulnerable"]  # noqa: E501
        if (self._configuration.client_side_validation and
                contested not in allowed_values):
            raise ValueError(
                "Invalid value for `contested` ({0}), must be one of {1}"  # noqa: E501
                .format(contested, allowed_values)
            )

        self._contested = contested

    @property
    def occupier_faction_id(self):
        """Gets the occupier_faction_id of this GetFwSystems200Ok.  # noqa: E501

        occupier_faction_id integer  # noqa: E501

        :return: The occupier_faction_id of this GetFwSystems200Ok.  # noqa: E501
        :rtype: int
        """
        return self._occupier_faction_id

    @occupier_faction_id.setter
    def occupier_faction_id(self, occupier_faction_id):
        """Sets the occupier_faction_id of this GetFwSystems200Ok.

        occupier_faction_id integer  # noqa: E501

        :param occupier_faction_id: The occupier_faction_id of this GetFwSystems200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and occupier_faction_id is None:
            raise ValueError("Invalid value for `occupier_faction_id`, must not be `None`")  # noqa: E501

        self._occupier_faction_id = occupier_faction_id

    @property
    def owner_faction_id(self):
        """Gets the owner_faction_id of this GetFwSystems200Ok.  # noqa: E501

        owner_faction_id integer  # noqa: E501

        :return: The owner_faction_id of this GetFwSystems200Ok.  # noqa: E501
        :rtype: int
        """
        return self._owner_faction_id

    @owner_faction_id.setter
    def owner_faction_id(self, owner_faction_id):
        """Sets the owner_faction_id of this GetFwSystems200Ok.

        owner_faction_id integer  # noqa: E501

        :param owner_faction_id: The owner_faction_id of this GetFwSystems200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and owner_faction_id is None:
            raise ValueError("Invalid value for `owner_faction_id`, must not be `None`")  # noqa: E501

        self._owner_faction_id = owner_faction_id

    @property
    def solar_system_id(self):
        """Gets the solar_system_id of this GetFwSystems200Ok.  # noqa: E501

        solar_system_id integer  # noqa: E501

        :return: The solar_system_id of this GetFwSystems200Ok.  # noqa: E501
        :rtype: int
        """
        return self._solar_system_id

    @solar_system_id.setter
    def solar_system_id(self, solar_system_id):
        """Sets the solar_system_id of this GetFwSystems200Ok.

        solar_system_id integer  # noqa: E501

        :param solar_system_id: The solar_system_id of this GetFwSystems200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and solar_system_id is None:
            raise ValueError("Invalid value for `solar_system_id`, must not be `None`")  # noqa: E501

        self._solar_system_id = solar_system_id

    @property
    def victory_points(self):
        """Gets the victory_points of this GetFwSystems200Ok.  # noqa: E501

        victory_points integer  # noqa: E501

        :return: The victory_points of this GetFwSystems200Ok.  # noqa: E501
        :rtype: int
        """
        return self._victory_points

    @victory_points.setter
    def victory_points(self, victory_points):
        """Sets the victory_points of this GetFwSystems200Ok.

        victory_points integer  # noqa: E501

        :param victory_points: The victory_points of this GetFwSystems200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and victory_points is None:
            raise ValueError("Invalid value for `victory_points`, must not be `None`")  # noqa: E501

        self._victory_points = victory_points

    @property
    def victory_points_threshold(self):
        """Gets the victory_points_threshold of this GetFwSystems200Ok.  # noqa: E501

        victory_points_threshold integer  # noqa: E501

        :return: The victory_points_threshold of this GetFwSystems200Ok.  # noqa: E501
        :rtype: int
        """
        return self._victory_points_threshold

    @victory_points_threshold.setter
    def victory_points_threshold(self, victory_points_threshold):
        """Sets the victory_points_threshold of this GetFwSystems200Ok.

        victory_points_threshold integer  # noqa: E501

        :param victory_points_threshold: The victory_points_threshold of this GetFwSystems200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and victory_points_threshold is None:
            raise ValueError("Invalid value for `victory_points_threshold`, must not be `None`")  # noqa: E501

        self._victory_points_threshold = victory_points_threshold

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
        if issubclass(GetFwSystems200Ok, dict):
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
        if not isinstance(other, GetFwSystems200Ok):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetFwSystems200Ok):
            return True

        return self.to_dict() != other.to_dict()
