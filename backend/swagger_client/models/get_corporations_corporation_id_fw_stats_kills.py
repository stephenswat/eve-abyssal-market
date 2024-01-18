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


class GetCorporationsCorporationIdFwStatsKills(object):
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
        'last_week': 'int',
        'total': 'int',
        'yesterday': 'int'
    }

    attribute_map = {
        'last_week': 'last_week',
        'total': 'total',
        'yesterday': 'yesterday'
    }

    def __init__(self, last_week=None, total=None, yesterday=None, _configuration=None):  # noqa: E501
        """GetCorporationsCorporationIdFwStatsKills - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._last_week = None
        self._total = None
        self._yesterday = None
        self.discriminator = None

        self.last_week = last_week
        self.total = total
        self.yesterday = yesterday

    @property
    def last_week(self):
        """Gets the last_week of this GetCorporationsCorporationIdFwStatsKills.  # noqa: E501

        Last week's total number of kills by members of the given corporation against enemy factions  # noqa: E501

        :return: The last_week of this GetCorporationsCorporationIdFwStatsKills.  # noqa: E501
        :rtype: int
        """
        return self._last_week

    @last_week.setter
    def last_week(self, last_week):
        """Sets the last_week of this GetCorporationsCorporationIdFwStatsKills.

        Last week's total number of kills by members of the given corporation against enemy factions  # noqa: E501

        :param last_week: The last_week of this GetCorporationsCorporationIdFwStatsKills.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and last_week is None:
            raise ValueError("Invalid value for `last_week`, must not be `None`")  # noqa: E501

        self._last_week = last_week

    @property
    def total(self):
        """Gets the total of this GetCorporationsCorporationIdFwStatsKills.  # noqa: E501

        Total number of kills by members of the given corporation against enemy factions since the corporation enlisted  # noqa: E501

        :return: The total of this GetCorporationsCorporationIdFwStatsKills.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this GetCorporationsCorporationIdFwStatsKills.

        Total number of kills by members of the given corporation against enemy factions since the corporation enlisted  # noqa: E501

        :param total: The total of this GetCorporationsCorporationIdFwStatsKills.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def yesterday(self):
        """Gets the yesterday of this GetCorporationsCorporationIdFwStatsKills.  # noqa: E501

        Yesterday's total number of kills by members of the given corporation against enemy factions  # noqa: E501

        :return: The yesterday of this GetCorporationsCorporationIdFwStatsKills.  # noqa: E501
        :rtype: int
        """
        return self._yesterday

    @yesterday.setter
    def yesterday(self, yesterday):
        """Sets the yesterday of this GetCorporationsCorporationIdFwStatsKills.

        Yesterday's total number of kills by members of the given corporation against enemy factions  # noqa: E501

        :param yesterday: The yesterday of this GetCorporationsCorporationIdFwStatsKills.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and yesterday is None:
            raise ValueError("Invalid value for `yesterday`, must not be `None`")  # noqa: E501

        self._yesterday = yesterday

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
        if issubclass(GetCorporationsCorporationIdFwStatsKills, dict):
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
        if not isinstance(other, GetCorporationsCorporationIdFwStatsKills):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCorporationsCorporationIdFwStatsKills):
            return True

        return self.to_dict() != other.to_dict()
