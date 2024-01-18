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


class GetCharactersCharacterIdSkillsSkill(object):
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
        'active_skill_level': 'int',
        'skill_id': 'int',
        'skillpoints_in_skill': 'int',
        'trained_skill_level': 'int'
    }

    attribute_map = {
        'active_skill_level': 'active_skill_level',
        'skill_id': 'skill_id',
        'skillpoints_in_skill': 'skillpoints_in_skill',
        'trained_skill_level': 'trained_skill_level'
    }

    def __init__(self, active_skill_level=None, skill_id=None, skillpoints_in_skill=None, trained_skill_level=None, _configuration=None):  # noqa: E501
        """GetCharactersCharacterIdSkillsSkill - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._active_skill_level = None
        self._skill_id = None
        self._skillpoints_in_skill = None
        self._trained_skill_level = None
        self.discriminator = None

        self.active_skill_level = active_skill_level
        self.skill_id = skill_id
        self.skillpoints_in_skill = skillpoints_in_skill
        self.trained_skill_level = trained_skill_level

    @property
    def active_skill_level(self):
        """Gets the active_skill_level of this GetCharactersCharacterIdSkillsSkill.  # noqa: E501

        active_skill_level integer  # noqa: E501

        :return: The active_skill_level of this GetCharactersCharacterIdSkillsSkill.  # noqa: E501
        :rtype: int
        """
        return self._active_skill_level

    @active_skill_level.setter
    def active_skill_level(self, active_skill_level):
        """Sets the active_skill_level of this GetCharactersCharacterIdSkillsSkill.

        active_skill_level integer  # noqa: E501

        :param active_skill_level: The active_skill_level of this GetCharactersCharacterIdSkillsSkill.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and active_skill_level is None:
            raise ValueError("Invalid value for `active_skill_level`, must not be `None`")  # noqa: E501

        self._active_skill_level = active_skill_level

    @property
    def skill_id(self):
        """Gets the skill_id of this GetCharactersCharacterIdSkillsSkill.  # noqa: E501

        skill_id integer  # noqa: E501

        :return: The skill_id of this GetCharactersCharacterIdSkillsSkill.  # noqa: E501
        :rtype: int
        """
        return self._skill_id

    @skill_id.setter
    def skill_id(self, skill_id):
        """Sets the skill_id of this GetCharactersCharacterIdSkillsSkill.

        skill_id integer  # noqa: E501

        :param skill_id: The skill_id of this GetCharactersCharacterIdSkillsSkill.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and skill_id is None:
            raise ValueError("Invalid value for `skill_id`, must not be `None`")  # noqa: E501

        self._skill_id = skill_id

    @property
    def skillpoints_in_skill(self):
        """Gets the skillpoints_in_skill of this GetCharactersCharacterIdSkillsSkill.  # noqa: E501

        skillpoints_in_skill integer  # noqa: E501

        :return: The skillpoints_in_skill of this GetCharactersCharacterIdSkillsSkill.  # noqa: E501
        :rtype: int
        """
        return self._skillpoints_in_skill

    @skillpoints_in_skill.setter
    def skillpoints_in_skill(self, skillpoints_in_skill):
        """Sets the skillpoints_in_skill of this GetCharactersCharacterIdSkillsSkill.

        skillpoints_in_skill integer  # noqa: E501

        :param skillpoints_in_skill: The skillpoints_in_skill of this GetCharactersCharacterIdSkillsSkill.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and skillpoints_in_skill is None:
            raise ValueError("Invalid value for `skillpoints_in_skill`, must not be `None`")  # noqa: E501

        self._skillpoints_in_skill = skillpoints_in_skill

    @property
    def trained_skill_level(self):
        """Gets the trained_skill_level of this GetCharactersCharacterIdSkillsSkill.  # noqa: E501

        trained_skill_level integer  # noqa: E501

        :return: The trained_skill_level of this GetCharactersCharacterIdSkillsSkill.  # noqa: E501
        :rtype: int
        """
        return self._trained_skill_level

    @trained_skill_level.setter
    def trained_skill_level(self, trained_skill_level):
        """Sets the trained_skill_level of this GetCharactersCharacterIdSkillsSkill.

        trained_skill_level integer  # noqa: E501

        :param trained_skill_level: The trained_skill_level of this GetCharactersCharacterIdSkillsSkill.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and trained_skill_level is None:
            raise ValueError("Invalid value for `trained_skill_level`, must not be `None`")  # noqa: E501

        self._trained_skill_level = trained_skill_level

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
        if issubclass(GetCharactersCharacterIdSkillsSkill, dict):
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
        if not isinstance(other, GetCharactersCharacterIdSkillsSkill):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetCharactersCharacterIdSkillsSkill):
            return True

        return self.to_dict() != other.to_dict()
