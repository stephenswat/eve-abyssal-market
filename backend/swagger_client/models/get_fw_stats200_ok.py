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


class GetFwStats200Ok(object):
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
        'faction_id': 'int',
        'kills': 'GetFwStatsKills',
        'pilots': 'int',
        'systems_controlled': 'int',
        'victory_points': 'GetFwStatsVictoryPoints'
    }

    attribute_map = {
        'faction_id': 'faction_id',
        'kills': 'kills',
        'pilots': 'pilots',
        'systems_controlled': 'systems_controlled',
        'victory_points': 'victory_points'
    }

    def __init__(self, faction_id=None, kills=None, pilots=None, systems_controlled=None, victory_points=None, _configuration=None):  # noqa: E501
        """GetFwStats200Ok - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._faction_id = None
        self._kills = None
        self._pilots = None
        self._systems_controlled = None
        self._victory_points = None
        self.discriminator = None

        self.faction_id = faction_id
        self.kills = kills
        self.pilots = pilots
        self.systems_controlled = systems_controlled
        self.victory_points = victory_points

    @property
    def faction_id(self):
        """Gets the faction_id of this GetFwStats200Ok.  # noqa: E501

        faction_id integer  # noqa: E501

        :return: The faction_id of this GetFwStats200Ok.  # noqa: E501
        :rtype: int
        """
        return self._faction_id

    @faction_id.setter
    def faction_id(self, faction_id):
        """Sets the faction_id of this GetFwStats200Ok.

        faction_id integer  # noqa: E501

        :param faction_id: The faction_id of this GetFwStats200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and faction_id is None:
            raise ValueError("Invalid value for `faction_id`, must not be `None`")  # noqa: E501

        self._faction_id = faction_id

    @property
    def kills(self):
        """Gets the kills of this GetFwStats200Ok.  # noqa: E501


        :return: The kills of this GetFwStats200Ok.  # noqa: E501
        :rtype: GetFwStatsKills
        """
        return self._kills

    @kills.setter
    def kills(self, kills):
        """Sets the kills of this GetFwStats200Ok.


        :param kills: The kills of this GetFwStats200Ok.  # noqa: E501
        :type: GetFwStatsKills
        """
        if self._configuration.client_side_validation and kills is None:
            raise ValueError("Invalid value for `kills`, must not be `None`")  # noqa: E501

        self._kills = kills

    @property
    def pilots(self):
        """Gets the pilots of this GetFwStats200Ok.  # noqa: E501

        How many pilots fight for the given faction  # noqa: E501

        :return: The pilots of this GetFwStats200Ok.  # noqa: E501
        :rtype: int
        """
        return self._pilots

    @pilots.setter
    def pilots(self, pilots):
        """Sets the pilots of this GetFwStats200Ok.

        How many pilots fight for the given faction  # noqa: E501

        :param pilots: The pilots of this GetFwStats200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and pilots is None:
            raise ValueError("Invalid value for `pilots`, must not be `None`")  # noqa: E501

        self._pilots = pilots

    @property
    def systems_controlled(self):
        """Gets the systems_controlled of this GetFwStats200Ok.  # noqa: E501

        The number of solar systems controlled by the given faction  # noqa: E501

        :return: The systems_controlled of this GetFwStats200Ok.  # noqa: E501
        :rtype: int
        """
        return self._systems_controlled

    @systems_controlled.setter
    def systems_controlled(self, systems_controlled):
        """Sets the systems_controlled of this GetFwStats200Ok.

        The number of solar systems controlled by the given faction  # noqa: E501

        :param systems_controlled: The systems_controlled of this GetFwStats200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and systems_controlled is None:
            raise ValueError("Invalid value for `systems_controlled`, must not be `None`")  # noqa: E501

        self._systems_controlled = systems_controlled

    @property
    def victory_points(self):
        """Gets the victory_points of this GetFwStats200Ok.  # noqa: E501


        :return: The victory_points of this GetFwStats200Ok.  # noqa: E501
        :rtype: GetFwStatsVictoryPoints
        """
        return self._victory_points

    @victory_points.setter
    def victory_points(self, victory_points):
        """Sets the victory_points of this GetFwStats200Ok.


        :param victory_points: The victory_points of this GetFwStats200Ok.  # noqa: E501
        :type: GetFwStatsVictoryPoints
        """
        if self._configuration.client_side_validation and victory_points is None:
            raise ValueError("Invalid value for `victory_points`, must not be `None`")  # noqa: E501

        self._victory_points = victory_points

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
        if issubclass(GetFwStats200Ok, dict):
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
        if not isinstance(other, GetFwStats200Ok):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetFwStats200Ok):
            return True

        return self.to_dict() != other.to_dict()
