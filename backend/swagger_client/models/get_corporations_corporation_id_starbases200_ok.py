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


class GetCorporationsCorporationIdStarbases200Ok(object):
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
        'moon_id': 'int',
        'onlined_since': 'datetime',
        'reinforced_until': 'datetime',
        'starbase_id': 'int',
        'state': 'str',
        'system_id': 'int',
        'type_id': 'int',
        'unanchor_at': 'datetime'
    }

    attribute_map = {
        'moon_id': 'moon_id',
        'onlined_since': 'onlined_since',
        'reinforced_until': 'reinforced_until',
        'starbase_id': 'starbase_id',
        'state': 'state',
        'system_id': 'system_id',
        'type_id': 'type_id',
        'unanchor_at': 'unanchor_at'
    }

    def __init__(self, moon_id=None, onlined_since=None, reinforced_until=None, starbase_id=None, state=None, system_id=None, type_id=None, unanchor_at=None, _configuration=None):  # noqa: E501
        """GetCorporationsCorporationIdStarbases200Ok - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._moon_id = None
        self._onlined_since = None
        self._reinforced_until = None
        self._starbase_id = None
        self._state = None
        self._system_id = None
        self._type_id = None
        self._unanchor_at = None
        self.discriminator = None

        if moon_id is not None:
            self.moon_id = moon_id
        if onlined_since is not None:
            self.onlined_since = onlined_since
        if reinforced_until is not None:
            self.reinforced_until = reinforced_until
        self.starbase_id = starbase_id
        if state is not None:
            self.state = state
        self.system_id = system_id
        self.type_id = type_id
        if unanchor_at is not None:
            self.unanchor_at = unanchor_at

    @property
    def moon_id(self):
        """Gets the moon_id of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501

        The moon this starbase (POS) is anchored on, unanchored POSes do not have this information  # noqa: E501

        :return: The moon_id of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501
        :rtype: int
        """
        return self._moon_id

    @moon_id.setter
    def moon_id(self, moon_id):
        """Sets the moon_id of this GetCorporationsCorporationIdStarbases200Ok.

        The moon this starbase (POS) is anchored on, unanchored POSes do not have this information  # noqa: E501

        :param moon_id: The moon_id of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501
        :type: int
        """

        self._moon_id = moon_id

    @property
    def onlined_since(self):
        """Gets the onlined_since of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501

        When the POS onlined, for starbases (POSes) in online state  # noqa: E501

        :return: The onlined_since of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._onlined_since

    @onlined_since.setter
    def onlined_since(self, onlined_since):
        """Sets the onlined_since of this GetCorporationsCorporationIdStarbases200Ok.

        When the POS onlined, for starbases (POSes) in online state  # noqa: E501

        :param onlined_since: The onlined_since of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501
        :type: datetime
        """

        self._onlined_since = onlined_since

    @property
    def reinforced_until(self):
        """Gets the reinforced_until of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501

        When the POS will be out of reinforcement, for starbases (POSes) in reinforced state  # noqa: E501

        :return: The reinforced_until of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._reinforced_until

    @reinforced_until.setter
    def reinforced_until(self, reinforced_until):
        """Sets the reinforced_until of this GetCorporationsCorporationIdStarbases200Ok.

        When the POS will be out of reinforcement, for starbases (POSes) in reinforced state  # noqa: E501

        :param reinforced_until: The reinforced_until of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501
        :type: datetime
        """

        self._reinforced_until = reinforced_until

    @property
    def starbase_id(self):
        """Gets the starbase_id of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501

        Unique ID for this starbase (POS)  # noqa: E501

        :return: The starbase_id of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501
        :rtype: int
        """
        return self._starbase_id

    @starbase_id.setter
    def starbase_id(self, starbase_id):
        """Sets the starbase_id of this GetCorporationsCorporationIdStarbases200Ok.

        Unique ID for this starbase (POS)  # noqa: E501

        :param starbase_id: The starbase_id of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and starbase_id is None:
            raise ValueError("Invalid value for `starbase_id`, must not be `None`")  # noqa: E501

        self._starbase_id = starbase_id

    @property
    def state(self):
        """Gets the state of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501

        state string  # noqa: E501

        :return: The state of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this GetCorporationsCorporationIdStarbases200Ok.

        state string  # noqa: E501

        :param state: The state of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501
        :type: str
        """
        allowed_values = ["offline", "online", "onlining", "reinforced", "unanchoring"]  # noqa: E501
        if (self._configuration.client_side_validation and
                state not in allowed_values):
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def system_id(self):
        """Gets the system_id of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501

        The solar system this starbase (POS) is in, unanchored POSes have this information  # noqa: E501

        :return: The system_id of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this GetCorporationsCorporationIdStarbases200Ok.

        The solar system this starbase (POS) is in, unanchored POSes have this information  # noqa: E501

        :param system_id: The system_id of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and system_id is None:
            raise ValueError("Invalid value for `system_id`, must not be `None`")  # noqa: E501

        self._system_id = system_id

    @property
    def type_id(self):
        """Gets the type_id of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501

        Starbase (POS) type  # noqa: E501

        :return: The type_id of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetCorporationsCorporationIdStarbases200Ok.

        Starbase (POS) type  # noqa: E501

        :param type_id: The type_id of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")  # noqa: E501

        self._type_id = type_id

    @property
    def unanchor_at(self):
        """Gets the unanchor_at of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501

        When the POS started unanchoring, for starbases (POSes) in unanchoring state  # noqa: E501

        :return: The unanchor_at of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501
        :rtype: datetime
        """
        return self._unanchor_at

    @unanchor_at.setter
    def unanchor_at(self, unanchor_at):
        """Sets the unanchor_at of this GetCorporationsCorporationIdStarbases200Ok.

        When the POS started unanchoring, for starbases (POSes) in unanchoring state  # noqa: E501

        :param unanchor_at: The unanchor_at of this GetCorporationsCorporationIdStarbases200Ok.  # noqa: E501
        :type: datetime
        """

        self._unanchor_at = unanchor_at

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
        if issubclass(GetCorporationsCorporationIdStarbases200Ok, dict):
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
        if not isinstance(other, GetCorporationsCorporationIdStarbases200Ok):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCorporationsCorporationIdStarbases200Ok):
            return True

        return self.to_dict() != other.to_dict()
