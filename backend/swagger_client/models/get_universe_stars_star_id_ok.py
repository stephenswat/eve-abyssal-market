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


class GetUniverseStarsStarIdOk(object):
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
        'age': 'int',
        'luminosity': 'float',
        'name': 'str',
        'radius': 'int',
        'solar_system_id': 'int',
        'spectral_class': 'str',
        'temperature': 'int',
        'type_id': 'int'
    }

    attribute_map = {
        'age': 'age',
        'luminosity': 'luminosity',
        'name': 'name',
        'radius': 'radius',
        'solar_system_id': 'solar_system_id',
        'spectral_class': 'spectral_class',
        'temperature': 'temperature',
        'type_id': 'type_id'
    }

    def __init__(self, age=None, luminosity=None, name=None, radius=None, solar_system_id=None, spectral_class=None, temperature=None, type_id=None, _configuration=None):  # noqa: E501
        """GetUniverseStarsStarIdOk - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._age = None
        self._luminosity = None
        self._name = None
        self._radius = None
        self._solar_system_id = None
        self._spectral_class = None
        self._temperature = None
        self._type_id = None
        self.discriminator = None

        self.age = age
        self.luminosity = luminosity
        self.name = name
        self.radius = radius
        self.solar_system_id = solar_system_id
        self.spectral_class = spectral_class
        self.temperature = temperature
        self.type_id = type_id

    @property
    def age(self):
        """Gets the age of this GetUniverseStarsStarIdOk.  # noqa: E501

        Age of star in years  # noqa: E501

        :return: The age of this GetUniverseStarsStarIdOk.  # noqa: E501
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age):
        """Sets the age of this GetUniverseStarsStarIdOk.

        Age of star in years  # noqa: E501

        :param age: The age of this GetUniverseStarsStarIdOk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and age is None:
            raise ValueError("Invalid value for `age`, must not be `None`")  # noqa: E501

        self._age = age

    @property
    def luminosity(self):
        """Gets the luminosity of this GetUniverseStarsStarIdOk.  # noqa: E501

        luminosity number  # noqa: E501

        :return: The luminosity of this GetUniverseStarsStarIdOk.  # noqa: E501
        :rtype: float
        """
        return self._luminosity

    @luminosity.setter
    def luminosity(self, luminosity):
        """Sets the luminosity of this GetUniverseStarsStarIdOk.

        luminosity number  # noqa: E501

        :param luminosity: The luminosity of this GetUniverseStarsStarIdOk.  # noqa: E501
        :type: float
        """
        if self._configuration.client_side_validation and luminosity is None:
            raise ValueError("Invalid value for `luminosity`, must not be `None`")  # noqa: E501

        self._luminosity = luminosity

    @property
    def name(self):
        """Gets the name of this GetUniverseStarsStarIdOk.  # noqa: E501

        name string  # noqa: E501

        :return: The name of this GetUniverseStarsStarIdOk.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetUniverseStarsStarIdOk.

        name string  # noqa: E501

        :param name: The name of this GetUniverseStarsStarIdOk.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def radius(self):
        """Gets the radius of this GetUniverseStarsStarIdOk.  # noqa: E501

        radius integer  # noqa: E501

        :return: The radius of this GetUniverseStarsStarIdOk.  # noqa: E501
        :rtype: int
        """
        return self._radius

    @radius.setter
    def radius(self, radius):
        """Sets the radius of this GetUniverseStarsStarIdOk.

        radius integer  # noqa: E501

        :param radius: The radius of this GetUniverseStarsStarIdOk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and radius is None:
            raise ValueError("Invalid value for `radius`, must not be `None`")  # noqa: E501

        self._radius = radius

    @property
    def solar_system_id(self):
        """Gets the solar_system_id of this GetUniverseStarsStarIdOk.  # noqa: E501

        solar_system_id integer  # noqa: E501

        :return: The solar_system_id of this GetUniverseStarsStarIdOk.  # noqa: E501
        :rtype: int
        """
        return self._solar_system_id

    @solar_system_id.setter
    def solar_system_id(self, solar_system_id):
        """Sets the solar_system_id of this GetUniverseStarsStarIdOk.

        solar_system_id integer  # noqa: E501

        :param solar_system_id: The solar_system_id of this GetUniverseStarsStarIdOk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and solar_system_id is None:
            raise ValueError("Invalid value for `solar_system_id`, must not be `None`")  # noqa: E501

        self._solar_system_id = solar_system_id

    @property
    def spectral_class(self):
        """Gets the spectral_class of this GetUniverseStarsStarIdOk.  # noqa: E501

        spectral_class string  # noqa: E501

        :return: The spectral_class of this GetUniverseStarsStarIdOk.  # noqa: E501
        :rtype: str
        """
        return self._spectral_class

    @spectral_class.setter
    def spectral_class(self, spectral_class):
        """Sets the spectral_class of this GetUniverseStarsStarIdOk.

        spectral_class string  # noqa: E501

        :param spectral_class: The spectral_class of this GetUniverseStarsStarIdOk.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and spectral_class is None:
            raise ValueError("Invalid value for `spectral_class`, must not be `None`")  # noqa: E501
        allowed_values = ["K2 V", "K4 V", "G2 V", "G8 V", "M7 V", "K7 V", "M2 V", "K5 V", "M3 V", "G0 V", "G7 V", "G3 V", "F9 V", "G5 V", "F6 V", "K8 V", "K9 V", "K6 V", "G9 V", "G6 V", "G4 VI", "G4 V", "F8 V", "F2 V", "F1 V", "K3 V", "F0 VI", "G1 VI", "G0 VI", "K1 V", "M4 V", "M1 V", "M6 V", "M0 V", "K2 IV", "G2 VI", "K0 V", "K5 IV", "F5 VI", "G6 VI", "F6 VI", "F2 IV", "G3 VI", "M8 V", "F1 VI", "K1 IV", "F7 V", "G5 VI", "M5 V", "G7 VI", "F5 V", "F4 VI", "F8 VI", "K3 IV", "F4 IV", "F0 V", "G7 IV", "G8 VI", "F2 VI", "F4 V", "F7 VI", "F3 V", "G1 V", "G9 VI", "F3 IV", "F9 VI", "M9 V", "K0 IV", "F1 IV", "G4 IV", "F3 VI", "K4 IV", "G5 IV", "G3 IV", "G1 IV", "K7 IV", "G0 IV", "K6 IV", "K9 IV", "G2 IV", "F9 IV", "F0 IV", "K8 IV", "G8 IV", "F6 IV", "F5 IV", "A0", "A0IV", "A0IV2"]  # noqa: E501
        if (self._configuration.client_side_validation and
                spectral_class not in allowed_values):
            raise ValueError(
                "Invalid value for `spectral_class` ({0}), must be one of {1}"  # noqa: E501
                .format(spectral_class, allowed_values)
            )

        self._spectral_class = spectral_class

    @property
    def temperature(self):
        """Gets the temperature of this GetUniverseStarsStarIdOk.  # noqa: E501

        temperature integer  # noqa: E501

        :return: The temperature of this GetUniverseStarsStarIdOk.  # noqa: E501
        :rtype: int
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this GetUniverseStarsStarIdOk.

        temperature integer  # noqa: E501

        :param temperature: The temperature of this GetUniverseStarsStarIdOk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and temperature is None:
            raise ValueError("Invalid value for `temperature`, must not be `None`")  # noqa: E501

        self._temperature = temperature

    @property
    def type_id(self):
        """Gets the type_id of this GetUniverseStarsStarIdOk.  # noqa: E501

        type_id integer  # noqa: E501

        :return: The type_id of this GetUniverseStarsStarIdOk.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this GetUniverseStarsStarIdOk.

        type_id integer  # noqa: E501

        :param type_id: The type_id of this GetUniverseStarsStarIdOk.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and type_id is None:
            raise ValueError("Invalid value for `type_id`, must not be `None`")  # noqa: E501

        self._type_id = type_id

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
        if issubclass(GetUniverseStarsStarIdOk, dict):
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
        if not isinstance(other, GetUniverseStarsStarIdOk):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetUniverseStarsStarIdOk):
            return True

        return self.to_dict() != other.to_dict()
