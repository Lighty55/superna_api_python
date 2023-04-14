# coding: utf-8

"""
    Superna Eyeglass REST API

    A collection of utilities for programmatic interaction with Superna Eyeglass  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@superna.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class Empty(object):
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
        '_none': 'str'
    }

    attribute_map = {
        '_none': 'none'
    }

    def __init__(self, _none=None, _configuration=None):  # noqa: E501
        """Empty - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self.__none = None
        self.discriminator = None

        if _none is not None:
            self._none = _none

    @property
    def _none(self):
        """Gets the _none of this Empty.  # noqa: E501


        :return: The _none of this Empty.  # noqa: E501
        :rtype: str
        """
        return self.__none

    @_none.setter
    def _none(self, _none):
        """Sets the _none of this Empty.


        :param _none: The _none of this Empty.  # noqa: E501
        :type: str
        """

        self.__none = _none

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
        if issubclass(Empty, dict):
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
        if not isinstance(other, Empty):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Empty):
            return True

        return self.to_dict() != other.to_dict()
