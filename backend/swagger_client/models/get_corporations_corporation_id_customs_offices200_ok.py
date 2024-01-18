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


class GetCorporationsCorporationIdCustomsOffices200Ok(object):
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
        'alliance_tax_rate': 'float',
        'allow_access_with_standings': 'bool',
        'allow_alliance_access': 'bool',
        'bad_standing_tax_rate': 'float',
        'corporation_tax_rate': 'float',
        'excellent_standing_tax_rate': 'float',
        'good_standing_tax_rate': 'float',
        'neutral_standing_tax_rate': 'float',
        'office_id': 'int',
        'reinforce_exit_end': 'int',
        'reinforce_exit_start': 'int',
        'standing_level': 'str',
        'system_id': 'int',
        'terrible_standing_tax_rate': 'float'
    }

    attribute_map = {
        'alliance_tax_rate': 'alliance_tax_rate',
        'allow_access_with_standings': 'allow_access_with_standings',
        'allow_alliance_access': 'allow_alliance_access',
        'bad_standing_tax_rate': 'bad_standing_tax_rate',
        'corporation_tax_rate': 'corporation_tax_rate',
        'excellent_standing_tax_rate': 'excellent_standing_tax_rate',
        'good_standing_tax_rate': 'good_standing_tax_rate',
        'neutral_standing_tax_rate': 'neutral_standing_tax_rate',
        'office_id': 'office_id',
        'reinforce_exit_end': 'reinforce_exit_end',
        'reinforce_exit_start': 'reinforce_exit_start',
        'standing_level': 'standing_level',
        'system_id': 'system_id',
        'terrible_standing_tax_rate': 'terrible_standing_tax_rate'
    }

    def __init__(self, alliance_tax_rate=None, allow_access_with_standings=None, allow_alliance_access=None, bad_standing_tax_rate=None, corporation_tax_rate=None, excellent_standing_tax_rate=None, good_standing_tax_rate=None, neutral_standing_tax_rate=None, office_id=None, reinforce_exit_end=None, reinforce_exit_start=None, standing_level=None, system_id=None, terrible_standing_tax_rate=None, _configuration=None):  # noqa: E501
        """GetCorporationsCorporationIdCustomsOffices200Ok - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alliance_tax_rate = None
        self._allow_access_with_standings = None
        self._allow_alliance_access = None
        self._bad_standing_tax_rate = None
        self._corporation_tax_rate = None
        self._excellent_standing_tax_rate = None
        self._good_standing_tax_rate = None
        self._neutral_standing_tax_rate = None
        self._office_id = None
        self._reinforce_exit_end = None
        self._reinforce_exit_start = None
        self._standing_level = None
        self._system_id = None
        self._terrible_standing_tax_rate = None
        self.discriminator = None

        if alliance_tax_rate is not None:
            self.alliance_tax_rate = alliance_tax_rate
        self.allow_access_with_standings = allow_access_with_standings
        self.allow_alliance_access = allow_alliance_access
        if bad_standing_tax_rate is not None:
            self.bad_standing_tax_rate = bad_standing_tax_rate
        if corporation_tax_rate is not None:
            self.corporation_tax_rate = corporation_tax_rate
        if excellent_standing_tax_rate is not None:
            self.excellent_standing_tax_rate = excellent_standing_tax_rate
        if good_standing_tax_rate is not None:
            self.good_standing_tax_rate = good_standing_tax_rate
        if neutral_standing_tax_rate is not None:
            self.neutral_standing_tax_rate = neutral_standing_tax_rate
        self.office_id = office_id
        self.reinforce_exit_end = reinforce_exit_end
        self.reinforce_exit_start = reinforce_exit_start
        if standing_level is not None:
            self.standing_level = standing_level
        self.system_id = system_id
        if terrible_standing_tax_rate is not None:
            self.terrible_standing_tax_rate = terrible_standing_tax_rate

    @property
    def alliance_tax_rate(self):
        """Gets the alliance_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501

        Only present if alliance access is allowed  # noqa: E501

        :return: The alliance_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :rtype: float
        """
        return self._alliance_tax_rate

    @alliance_tax_rate.setter
    def alliance_tax_rate(self, alliance_tax_rate):
        """Sets the alliance_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.

        Only present if alliance access is allowed  # noqa: E501

        :param alliance_tax_rate: The alliance_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :type: float
        """

        self._alliance_tax_rate = alliance_tax_rate

    @property
    def allow_access_with_standings(self):
        """Gets the allow_access_with_standings of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501

        standing_level and any standing related tax rate only present when this is true  # noqa: E501

        :return: The allow_access_with_standings of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :rtype: bool
        """
        return self._allow_access_with_standings

    @allow_access_with_standings.setter
    def allow_access_with_standings(self, allow_access_with_standings):
        """Sets the allow_access_with_standings of this GetCorporationsCorporationIdCustomsOffices200Ok.

        standing_level and any standing related tax rate only present when this is true  # noqa: E501

        :param allow_access_with_standings: The allow_access_with_standings of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and allow_access_with_standings is None:
            raise ValueError("Invalid value for `allow_access_with_standings`, must not be `None`")  # noqa: E501

        self._allow_access_with_standings = allow_access_with_standings

    @property
    def allow_alliance_access(self):
        """Gets the allow_alliance_access of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501

        allow_alliance_access boolean  # noqa: E501

        :return: The allow_alliance_access of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :rtype: bool
        """
        return self._allow_alliance_access

    @allow_alliance_access.setter
    def allow_alliance_access(self, allow_alliance_access):
        """Sets the allow_alliance_access of this GetCorporationsCorporationIdCustomsOffices200Ok.

        allow_alliance_access boolean  # noqa: E501

        :param allow_alliance_access: The allow_alliance_access of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and allow_alliance_access is None:
            raise ValueError("Invalid value for `allow_alliance_access`, must not be `None`")  # noqa: E501

        self._allow_alliance_access = allow_alliance_access

    @property
    def bad_standing_tax_rate(self):
        """Gets the bad_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501

        bad_standing_tax_rate number  # noqa: E501

        :return: The bad_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :rtype: float
        """
        return self._bad_standing_tax_rate

    @bad_standing_tax_rate.setter
    def bad_standing_tax_rate(self, bad_standing_tax_rate):
        """Sets the bad_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.

        bad_standing_tax_rate number  # noqa: E501

        :param bad_standing_tax_rate: The bad_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :type: float
        """

        self._bad_standing_tax_rate = bad_standing_tax_rate

    @property
    def corporation_tax_rate(self):
        """Gets the corporation_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501

        corporation_tax_rate number  # noqa: E501

        :return: The corporation_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :rtype: float
        """
        return self._corporation_tax_rate

    @corporation_tax_rate.setter
    def corporation_tax_rate(self, corporation_tax_rate):
        """Sets the corporation_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.

        corporation_tax_rate number  # noqa: E501

        :param corporation_tax_rate: The corporation_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :type: float
        """

        self._corporation_tax_rate = corporation_tax_rate

    @property
    def excellent_standing_tax_rate(self):
        """Gets the excellent_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501

        Tax rate for entities with excellent level of standing, only present if this level is allowed, same for all other standing related tax rates  # noqa: E501

        :return: The excellent_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :rtype: float
        """
        return self._excellent_standing_tax_rate

    @excellent_standing_tax_rate.setter
    def excellent_standing_tax_rate(self, excellent_standing_tax_rate):
        """Sets the excellent_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.

        Tax rate for entities with excellent level of standing, only present if this level is allowed, same for all other standing related tax rates  # noqa: E501

        :param excellent_standing_tax_rate: The excellent_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :type: float
        """

        self._excellent_standing_tax_rate = excellent_standing_tax_rate

    @property
    def good_standing_tax_rate(self):
        """Gets the good_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501

        good_standing_tax_rate number  # noqa: E501

        :return: The good_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :rtype: float
        """
        return self._good_standing_tax_rate

    @good_standing_tax_rate.setter
    def good_standing_tax_rate(self, good_standing_tax_rate):
        """Sets the good_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.

        good_standing_tax_rate number  # noqa: E501

        :param good_standing_tax_rate: The good_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :type: float
        """

        self._good_standing_tax_rate = good_standing_tax_rate

    @property
    def neutral_standing_tax_rate(self):
        """Gets the neutral_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501

        neutral_standing_tax_rate number  # noqa: E501

        :return: The neutral_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :rtype: float
        """
        return self._neutral_standing_tax_rate

    @neutral_standing_tax_rate.setter
    def neutral_standing_tax_rate(self, neutral_standing_tax_rate):
        """Sets the neutral_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.

        neutral_standing_tax_rate number  # noqa: E501

        :param neutral_standing_tax_rate: The neutral_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :type: float
        """

        self._neutral_standing_tax_rate = neutral_standing_tax_rate

    @property
    def office_id(self):
        """Gets the office_id of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501

        unique ID of this customs office  # noqa: E501

        :return: The office_id of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :rtype: int
        """
        return self._office_id

    @office_id.setter
    def office_id(self, office_id):
        """Sets the office_id of this GetCorporationsCorporationIdCustomsOffices200Ok.

        unique ID of this customs office  # noqa: E501

        :param office_id: The office_id of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and office_id is None:
            raise ValueError("Invalid value for `office_id`, must not be `None`")  # noqa: E501

        self._office_id = office_id

    @property
    def reinforce_exit_end(self):
        """Gets the reinforce_exit_end of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501

        reinforce_exit_end integer  # noqa: E501

        :return: The reinforce_exit_end of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :rtype: int
        """
        return self._reinforce_exit_end

    @reinforce_exit_end.setter
    def reinforce_exit_end(self, reinforce_exit_end):
        """Sets the reinforce_exit_end of this GetCorporationsCorporationIdCustomsOffices200Ok.

        reinforce_exit_end integer  # noqa: E501

        :param reinforce_exit_end: The reinforce_exit_end of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and reinforce_exit_end is None:
            raise ValueError("Invalid value for `reinforce_exit_end`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                reinforce_exit_end is not None and reinforce_exit_end > 23):  # noqa: E501
            raise ValueError("Invalid value for `reinforce_exit_end`, must be a value less than or equal to `23`")  # noqa: E501
        if (self._configuration.client_side_validation and
                reinforce_exit_end is not None and reinforce_exit_end < 0):  # noqa: E501
            raise ValueError("Invalid value for `reinforce_exit_end`, must be a value greater than or equal to `0`")  # noqa: E501

        self._reinforce_exit_end = reinforce_exit_end

    @property
    def reinforce_exit_start(self):
        """Gets the reinforce_exit_start of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501

        Together with reinforce_exit_end, marks a 2-hour period where this customs office could exit reinforcement mode during the day after initial attack  # noqa: E501

        :return: The reinforce_exit_start of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :rtype: int
        """
        return self._reinforce_exit_start

    @reinforce_exit_start.setter
    def reinforce_exit_start(self, reinforce_exit_start):
        """Sets the reinforce_exit_start of this GetCorporationsCorporationIdCustomsOffices200Ok.

        Together with reinforce_exit_end, marks a 2-hour period where this customs office could exit reinforcement mode during the day after initial attack  # noqa: E501

        :param reinforce_exit_start: The reinforce_exit_start of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and reinforce_exit_start is None:
            raise ValueError("Invalid value for `reinforce_exit_start`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                reinforce_exit_start is not None and reinforce_exit_start > 23):  # noqa: E501
            raise ValueError("Invalid value for `reinforce_exit_start`, must be a value less than or equal to `23`")  # noqa: E501
        if (self._configuration.client_side_validation and
                reinforce_exit_start is not None and reinforce_exit_start < 0):  # noqa: E501
            raise ValueError("Invalid value for `reinforce_exit_start`, must be a value greater than or equal to `0`")  # noqa: E501

        self._reinforce_exit_start = reinforce_exit_start

    @property
    def standing_level(self):
        """Gets the standing_level of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501

        Access is allowed only for entities with this level of standing or better  # noqa: E501

        :return: The standing_level of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :rtype: str
        """
        return self._standing_level

    @standing_level.setter
    def standing_level(self, standing_level):
        """Sets the standing_level of this GetCorporationsCorporationIdCustomsOffices200Ok.

        Access is allowed only for entities with this level of standing or better  # noqa: E501

        :param standing_level: The standing_level of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :type: str
        """
        allowed_values = ["bad", "excellent", "good", "neutral", "terrible"]  # noqa: E501
        if (self._configuration.client_side_validation and
                standing_level not in allowed_values):
            raise ValueError(
                "Invalid value for `standing_level` ({0}), must be one of {1}"  # noqa: E501
                .format(standing_level, allowed_values)
            )

        self._standing_level = standing_level

    @property
    def system_id(self):
        """Gets the system_id of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501

        ID of the solar system this customs office is located in  # noqa: E501

        :return: The system_id of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this GetCorporationsCorporationIdCustomsOffices200Ok.

        ID of the solar system this customs office is located in  # noqa: E501

        :param system_id: The system_id of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and system_id is None:
            raise ValueError("Invalid value for `system_id`, must not be `None`")  # noqa: E501

        self._system_id = system_id

    @property
    def terrible_standing_tax_rate(self):
        """Gets the terrible_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501

        terrible_standing_tax_rate number  # noqa: E501

        :return: The terrible_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :rtype: float
        """
        return self._terrible_standing_tax_rate

    @terrible_standing_tax_rate.setter
    def terrible_standing_tax_rate(self, terrible_standing_tax_rate):
        """Sets the terrible_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.

        terrible_standing_tax_rate number  # noqa: E501

        :param terrible_standing_tax_rate: The terrible_standing_tax_rate of this GetCorporationsCorporationIdCustomsOffices200Ok.  # noqa: E501
        :type: float
        """

        self._terrible_standing_tax_rate = terrible_standing_tax_rate

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
        if issubclass(GetCorporationsCorporationIdCustomsOffices200Ok, dict):
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
        if not isinstance(other, GetCorporationsCorporationIdCustomsOffices200Ok):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCorporationsCorporationIdCustomsOffices200Ok):
            return True

        return self.to_dict() != other.to_dict()
