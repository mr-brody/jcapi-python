# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The next version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings. The most recent version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings.

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PolicyValue(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'config_field_id': 'str'
    }

    attribute_map = {
        'config_field_id': 'configFieldID'
    }

    def __init__(self, config_field_id=None):
        """
        PolicyValue - a model defined in Swagger
        """

        self._config_field_id = None

        if config_field_id is not None:
          self.config_field_id = config_field_id

    @property
    def config_field_id(self):
        """
        Gets the config_field_id of this PolicyValue.
        The ObjectId of the corresponding Policy Template configuration field.

        :return: The config_field_id of this PolicyValue.
        :rtype: str
        """
        return self._config_field_id

    @config_field_id.setter
    def config_field_id(self, config_field_id):
        """
        Sets the config_field_id of this PolicyValue.
        The ObjectId of the corresponding Policy Template configuration field.

        :param config_field_id: The config_field_id of this PolicyValue.
        :type: str
        """

        self._config_field_id = config_field_id

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, PolicyValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
