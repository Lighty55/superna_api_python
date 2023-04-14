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


class VaultEvent(object):
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
        'devid': 'int',
        'message': 'str',
        'severity': 'str',
        'time': 'int'
    }

    attribute_map = {
        'devid': 'devid',
        'message': 'message',
        'severity': 'severity',
        'time': 'time'
    }

    def __init__(self, devid=None, message=None, severity=None, time=None, _configuration=None):  # noqa: E501
        """VaultEvent - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._devid = None
        self._message = None
        self._severity = None
        self._time = None
        self.discriminator = None

        if devid is not None:
            self.devid = devid
        if message is not None:
            self.message = message
        if severity is not None:
            self.severity = severity
        if time is not None:
            self.time = time

    @property
    def devid(self):
        """Gets the devid of this VaultEvent.  # noqa: E501

        devid  # noqa: E501

        :return: The devid of this VaultEvent.  # noqa: E501
        :rtype: int
        """
        return self._devid

    @devid.setter
    def devid(self, devid):
        """Sets the devid of this VaultEvent.

        devid  # noqa: E501

        :param devid: The devid of this VaultEvent.  # noqa: E501
        :type: int
        """

        self._devid = devid

    @property
    def message(self):
        """Gets the message of this VaultEvent.  # noqa: E501

        Event message.  # noqa: E501

        :return: The message of this VaultEvent.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this VaultEvent.

        Event message.  # noqa: E501

        :param message: The message of this VaultEvent.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def severity(self):
        """Gets the severity of this VaultEvent.  # noqa: E501

        Severity of the event  # noqa: E501

        :return: The severity of this VaultEvent.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this VaultEvent.

        Severity of the event  # noqa: E501

        :param severity: The severity of this VaultEvent.  # noqa: E501
        :type: str
        """

        self._severity = severity

    @property
    def time(self):
        """Gets the time of this VaultEvent.  # noqa: E501

        Event creation timestamp.  # noqa: E501

        :return: The time of this VaultEvent.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this VaultEvent.

        Event creation timestamp.  # noqa: E501

        :param time: The time of this VaultEvent.  # noqa: E501
        :type: int
        """

        self._time = time

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
        if issubclass(VaultEvent, dict):
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
        if not isinstance(other, VaultEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VaultEvent):
            return True

        return self.to_dict() != other.to_dict()