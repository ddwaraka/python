# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Contact(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Contact - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'purpose': 'str',
            'detail': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'purpose': 'purpose',
            'detail': 'detail'
        }

        self._type = None
        self._purpose = None
        self._detail = None

    @property
    def type(self):
        """
        Gets the type of this Contact.
        The method of contact, such as phone or fax.

        :return: The type of this Contact.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Contact.
        The method of contact, such as phone or fax.

        :param type: The type of this Contact.
        :type: str
        """
        self._type = type

    @property
    def purpose(self):
        """
        Gets the purpose of this Contact.
        The reason or channel of that contact method. For example&colon; HOME, EMERGENCY, MOBILE.

        :return: The purpose of this Contact.
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """
        Sets the purpose of this Contact.
        The reason or channel of that contact method. For example&colon; HOME, EMERGENCY, MOBILE.

        :param purpose: The purpose of this Contact.
        :type: str
        """
        self._purpose = purpose

    @property
    def detail(self):
        """
        Gets the detail of this Contact.
        How that contact should be used, eg. a phone number

        :return: The detail of this Contact.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """
        Sets the detail of this Contact.
        How that contact should be used, eg. a phone number

        :param detail: The detail of this Contact.
        :type: str
        """
        self._detail = detail

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """ 
        Returns true if both objects are not equal
        """
        return not self == other
