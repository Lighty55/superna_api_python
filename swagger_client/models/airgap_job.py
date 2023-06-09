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


class AirgapJob(object):
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
        'cron': 'str',
        'name': 'str'
    }

    attribute_map = {
        'cron': 'cron',
        'name': 'name'
    }

    def __init__(self, cron=None, name=None, _configuration=None):  # noqa: E501
        """AirgapJob - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cron = None
        self._name = None
        self.discriminator = None

        if cron is not None:
            self.cron = cron
        if name is not None:
            self.name = name

    @property
    def cron(self):
        """Gets the cron of this AirgapJob.  # noqa: E501

        cron schedule for the job  # noqa: E501

        :return: The cron of this AirgapJob.  # noqa: E501
        :rtype: str
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        """Sets the cron of this AirgapJob.

        cron schedule for the job  # noqa: E501

        :param cron: The cron of this AirgapJob.  # noqa: E501
        :type: str
        """

        self._cron = cron

    @property
    def name(self):
        """Gets the name of this AirgapJob.  # noqa: E501

        Job name  # noqa: E501

        :return: The name of this AirgapJob.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AirgapJob.

        Job name  # noqa: E501

        :param name: The name of this AirgapJob.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(AirgapJob, dict):
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
        if not isinstance(other, AirgapJob):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AirgapJob):
            return True

        return self.to_dict() != other.to_dict()
