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


class GetCorporationsCorporationIdStarbasesStarbaseIdOk(object):
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
        'allow_alliance_members': 'bool',
        'allow_corporation_members': 'bool',
        'anchor': 'str',
        'attack_if_at_war': 'bool',
        'attack_if_other_security_status_dropping': 'bool',
        'attack_security_status_threshold': 'float',
        'attack_standing_threshold': 'float',
        'fuel_bay_take': 'str',
        'fuel_bay_view': 'str',
        'fuels': 'list[GetCorporationsCorporationIdStarbasesStarbaseIdFuel]',
        'offline': 'str',
        'online': 'str',
        'unanchor': 'str',
        'use_alliance_standings': 'bool'
    }

    attribute_map = {
        'allow_alliance_members': 'allow_alliance_members',
        'allow_corporation_members': 'allow_corporation_members',
        'anchor': 'anchor',
        'attack_if_at_war': 'attack_if_at_war',
        'attack_if_other_security_status_dropping': 'attack_if_other_security_status_dropping',
        'attack_security_status_threshold': 'attack_security_status_threshold',
        'attack_standing_threshold': 'attack_standing_threshold',
        'fuel_bay_take': 'fuel_bay_take',
        'fuel_bay_view': 'fuel_bay_view',
        'fuels': 'fuels',
        'offline': 'offline',
        'online': 'online',
        'unanchor': 'unanchor',
        'use_alliance_standings': 'use_alliance_standings'
    }

    def __init__(self, allow_alliance_members=None, allow_corporation_members=None, anchor=None, attack_if_at_war=None, attack_if_other_security_status_dropping=None, attack_security_status_threshold=None, attack_standing_threshold=None, fuel_bay_take=None, fuel_bay_view=None, fuels=None, offline=None, online=None, unanchor=None, use_alliance_standings=None, _configuration=None):  # noqa: E501
        """GetCorporationsCorporationIdStarbasesStarbaseIdOk - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._allow_alliance_members = None
        self._allow_corporation_members = None
        self._anchor = None
        self._attack_if_at_war = None
        self._attack_if_other_security_status_dropping = None
        self._attack_security_status_threshold = None
        self._attack_standing_threshold = None
        self._fuel_bay_take = None
        self._fuel_bay_view = None
        self._fuels = None
        self._offline = None
        self._online = None
        self._unanchor = None
        self._use_alliance_standings = None
        self.discriminator = None

        self.allow_alliance_members = allow_alliance_members
        self.allow_corporation_members = allow_corporation_members
        self.anchor = anchor
        self.attack_if_at_war = attack_if_at_war
        self.attack_if_other_security_status_dropping = attack_if_other_security_status_dropping
        if attack_security_status_threshold is not None:
            self.attack_security_status_threshold = attack_security_status_threshold
        if attack_standing_threshold is not None:
            self.attack_standing_threshold = attack_standing_threshold
        self.fuel_bay_take = fuel_bay_take
        self.fuel_bay_view = fuel_bay_view
        if fuels is not None:
            self.fuels = fuels
        self.offline = offline
        self.online = online
        self.unanchor = unanchor
        self.use_alliance_standings = use_alliance_standings

    @property
    def allow_alliance_members(self):
        """Gets the allow_alliance_members of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501

        allow_alliance_members boolean  # noqa: E501

        :return: The allow_alliance_members of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :rtype: bool
        """
        return self._allow_alliance_members

    @allow_alliance_members.setter
    def allow_alliance_members(self, allow_alliance_members):
        """Sets the allow_alliance_members of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.

        allow_alliance_members boolean  # noqa: E501

        :param allow_alliance_members: The allow_alliance_members of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and allow_alliance_members is None:
            raise ValueError("Invalid value for `allow_alliance_members`, must not be `None`")  # noqa: E501

        self._allow_alliance_members = allow_alliance_members

    @property
    def allow_corporation_members(self):
        """Gets the allow_corporation_members of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501

        allow_corporation_members boolean  # noqa: E501

        :return: The allow_corporation_members of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :rtype: bool
        """
        return self._allow_corporation_members

    @allow_corporation_members.setter
    def allow_corporation_members(self, allow_corporation_members):
        """Sets the allow_corporation_members of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.

        allow_corporation_members boolean  # noqa: E501

        :param allow_corporation_members: The allow_corporation_members of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and allow_corporation_members is None:
            raise ValueError("Invalid value for `allow_corporation_members`, must not be `None`")  # noqa: E501

        self._allow_corporation_members = allow_corporation_members

    @property
    def anchor(self):
        """Gets the anchor of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501

        Who can anchor starbase (POS) and its structures  # noqa: E501

        :return: The anchor of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :rtype: str
        """
        return self._anchor

    @anchor.setter
    def anchor(self, anchor):
        """Sets the anchor of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.

        Who can anchor starbase (POS) and its structures  # noqa: E501

        :param anchor: The anchor of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and anchor is None:
            raise ValueError("Invalid value for `anchor`, must not be `None`")  # noqa: E501
        allowed_values = ["alliance_member", "config_starbase_equipment_role", "corporation_member", "starbase_fuel_technician_role"]  # noqa: E501
        if (self._configuration.client_side_validation and
                anchor not in allowed_values):
            raise ValueError(
                "Invalid value for `anchor` ({0}), must be one of {1}"  # noqa: E501
                .format(anchor, allowed_values)
            )

        self._anchor = anchor

    @property
    def attack_if_at_war(self):
        """Gets the attack_if_at_war of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501

        attack_if_at_war boolean  # noqa: E501

        :return: The attack_if_at_war of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :rtype: bool
        """
        return self._attack_if_at_war

    @attack_if_at_war.setter
    def attack_if_at_war(self, attack_if_at_war):
        """Sets the attack_if_at_war of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.

        attack_if_at_war boolean  # noqa: E501

        :param attack_if_at_war: The attack_if_at_war of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and attack_if_at_war is None:
            raise ValueError("Invalid value for `attack_if_at_war`, must not be `None`")  # noqa: E501

        self._attack_if_at_war = attack_if_at_war

    @property
    def attack_if_other_security_status_dropping(self):
        """Gets the attack_if_other_security_status_dropping of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501

        attack_if_other_security_status_dropping boolean  # noqa: E501

        :return: The attack_if_other_security_status_dropping of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :rtype: bool
        """
        return self._attack_if_other_security_status_dropping

    @attack_if_other_security_status_dropping.setter
    def attack_if_other_security_status_dropping(self, attack_if_other_security_status_dropping):
        """Sets the attack_if_other_security_status_dropping of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.

        attack_if_other_security_status_dropping boolean  # noqa: E501

        :param attack_if_other_security_status_dropping: The attack_if_other_security_status_dropping of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and attack_if_other_security_status_dropping is None:
            raise ValueError("Invalid value for `attack_if_other_security_status_dropping`, must not be `None`")  # noqa: E501

        self._attack_if_other_security_status_dropping = attack_if_other_security_status_dropping

    @property
    def attack_security_status_threshold(self):
        """Gets the attack_security_status_threshold of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501

        Starbase (POS) will attack if target's security standing is lower than this value  # noqa: E501

        :return: The attack_security_status_threshold of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :rtype: float
        """
        return self._attack_security_status_threshold

    @attack_security_status_threshold.setter
    def attack_security_status_threshold(self, attack_security_status_threshold):
        """Sets the attack_security_status_threshold of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.

        Starbase (POS) will attack if target's security standing is lower than this value  # noqa: E501

        :param attack_security_status_threshold: The attack_security_status_threshold of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :type: float
        """

        self._attack_security_status_threshold = attack_security_status_threshold

    @property
    def attack_standing_threshold(self):
        """Gets the attack_standing_threshold of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501

        Starbase (POS) will attack if target's standing is lower than this value  # noqa: E501

        :return: The attack_standing_threshold of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :rtype: float
        """
        return self._attack_standing_threshold

    @attack_standing_threshold.setter
    def attack_standing_threshold(self, attack_standing_threshold):
        """Sets the attack_standing_threshold of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.

        Starbase (POS) will attack if target's standing is lower than this value  # noqa: E501

        :param attack_standing_threshold: The attack_standing_threshold of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :type: float
        """

        self._attack_standing_threshold = attack_standing_threshold

    @property
    def fuel_bay_take(self):
        """Gets the fuel_bay_take of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501

        Who can take fuel blocks out of the starbase (POS)'s fuel bay  # noqa: E501

        :return: The fuel_bay_take of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :rtype: str
        """
        return self._fuel_bay_take

    @fuel_bay_take.setter
    def fuel_bay_take(self, fuel_bay_take):
        """Sets the fuel_bay_take of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.

        Who can take fuel blocks out of the starbase (POS)'s fuel bay  # noqa: E501

        :param fuel_bay_take: The fuel_bay_take of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and fuel_bay_take is None:
            raise ValueError("Invalid value for `fuel_bay_take`, must not be `None`")  # noqa: E501
        allowed_values = ["alliance_member", "config_starbase_equipment_role", "corporation_member", "starbase_fuel_technician_role"]  # noqa: E501
        if (self._configuration.client_side_validation and
                fuel_bay_take not in allowed_values):
            raise ValueError(
                "Invalid value for `fuel_bay_take` ({0}), must be one of {1}"  # noqa: E501
                .format(fuel_bay_take, allowed_values)
            )

        self._fuel_bay_take = fuel_bay_take

    @property
    def fuel_bay_view(self):
        """Gets the fuel_bay_view of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501

        Who can view the starbase (POS)'s fule bay. Characters either need to have required role or belong to the starbase (POS) owner's corporation or alliance, as described by the enum, all other access settings follows the same scheme  # noqa: E501

        :return: The fuel_bay_view of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :rtype: str
        """
        return self._fuel_bay_view

    @fuel_bay_view.setter
    def fuel_bay_view(self, fuel_bay_view):
        """Sets the fuel_bay_view of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.

        Who can view the starbase (POS)'s fule bay. Characters either need to have required role or belong to the starbase (POS) owner's corporation or alliance, as described by the enum, all other access settings follows the same scheme  # noqa: E501

        :param fuel_bay_view: The fuel_bay_view of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and fuel_bay_view is None:
            raise ValueError("Invalid value for `fuel_bay_view`, must not be `None`")  # noqa: E501
        allowed_values = ["alliance_member", "config_starbase_equipment_role", "corporation_member", "starbase_fuel_technician_role"]  # noqa: E501
        if (self._configuration.client_side_validation and
                fuel_bay_view not in allowed_values):
            raise ValueError(
                "Invalid value for `fuel_bay_view` ({0}), must be one of {1}"  # noqa: E501
                .format(fuel_bay_view, allowed_values)
            )

        self._fuel_bay_view = fuel_bay_view

    @property
    def fuels(self):
        """Gets the fuels of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501

        Fuel blocks and other things that will be consumed when operating a starbase (POS)  # noqa: E501

        :return: The fuels of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :rtype: list[GetCorporationsCorporationIdStarbasesStarbaseIdFuel]
        """
        return self._fuels

    @fuels.setter
    def fuels(self, fuels):
        """Sets the fuels of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.

        Fuel blocks and other things that will be consumed when operating a starbase (POS)  # noqa: E501

        :param fuels: The fuels of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :type: list[GetCorporationsCorporationIdStarbasesStarbaseIdFuel]
        """

        self._fuels = fuels

    @property
    def offline(self):
        """Gets the offline of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501

        Who can offline starbase (POS) and its structures  # noqa: E501

        :return: The offline of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :rtype: str
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        """Sets the offline of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.

        Who can offline starbase (POS) and its structures  # noqa: E501

        :param offline: The offline of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and offline is None:
            raise ValueError("Invalid value for `offline`, must not be `None`")  # noqa: E501
        allowed_values = ["alliance_member", "config_starbase_equipment_role", "corporation_member", "starbase_fuel_technician_role"]  # noqa: E501
        if (self._configuration.client_side_validation and
                offline not in allowed_values):
            raise ValueError(
                "Invalid value for `offline` ({0}), must be one of {1}"  # noqa: E501
                .format(offline, allowed_values)
            )

        self._offline = offline

    @property
    def online(self):
        """Gets the online of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501

        Who can online starbase (POS) and its structures  # noqa: E501

        :return: The online of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :rtype: str
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.

        Who can online starbase (POS) and its structures  # noqa: E501

        :param online: The online of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and online is None:
            raise ValueError("Invalid value for `online`, must not be `None`")  # noqa: E501
        allowed_values = ["alliance_member", "config_starbase_equipment_role", "corporation_member", "starbase_fuel_technician_role"]  # noqa: E501
        if (self._configuration.client_side_validation and
                online not in allowed_values):
            raise ValueError(
                "Invalid value for `online` ({0}), must be one of {1}"  # noqa: E501
                .format(online, allowed_values)
            )

        self._online = online

    @property
    def unanchor(self):
        """Gets the unanchor of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501

        Who can unanchor starbase (POS) and its structures  # noqa: E501

        :return: The unanchor of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :rtype: str
        """
        return self._unanchor

    @unanchor.setter
    def unanchor(self, unanchor):
        """Sets the unanchor of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.

        Who can unanchor starbase (POS) and its structures  # noqa: E501

        :param unanchor: The unanchor of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and unanchor is None:
            raise ValueError("Invalid value for `unanchor`, must not be `None`")  # noqa: E501
        allowed_values = ["alliance_member", "config_starbase_equipment_role", "corporation_member", "starbase_fuel_technician_role"]  # noqa: E501
        if (self._configuration.client_side_validation and
                unanchor not in allowed_values):
            raise ValueError(
                "Invalid value for `unanchor` ({0}), must be one of {1}"  # noqa: E501
                .format(unanchor, allowed_values)
            )

        self._unanchor = unanchor

    @property
    def use_alliance_standings(self):
        """Gets the use_alliance_standings of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501

        True if the starbase (POS) is using alliance standings, otherwise using corporation's  # noqa: E501

        :return: The use_alliance_standings of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :rtype: bool
        """
        return self._use_alliance_standings

    @use_alliance_standings.setter
    def use_alliance_standings(self, use_alliance_standings):
        """Sets the use_alliance_standings of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.

        True if the starbase (POS) is using alliance standings, otherwise using corporation's  # noqa: E501

        :param use_alliance_standings: The use_alliance_standings of this GetCorporationsCorporationIdStarbasesStarbaseIdOk.  # noqa: E501
        :type: bool
        """
        if self._configuration.client_side_validation and use_alliance_standings is None:
            raise ValueError("Invalid value for `use_alliance_standings`, must not be `None`")  # noqa: E501

        self._use_alliance_standings = use_alliance_standings

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
        if issubclass(GetCorporationsCorporationIdStarbasesStarbaseIdOk, dict):
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
        if not isinstance(other, GetCorporationsCorporationIdStarbasesStarbaseIdOk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCorporationsCorporationIdStarbasesStarbaseIdOk):
            return True

        return self.to_dict() != other.to_dict()
