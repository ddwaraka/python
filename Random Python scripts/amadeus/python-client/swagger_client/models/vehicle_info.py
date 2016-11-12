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


class VehicleInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        VehicleInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'acriss_code': 'str',
            'category': 'str',
            'type': 'str',
            'transmission': 'str',
            'air_conditioning': 'bool',
            'fuel': 'str'
        }

        self.attribute_map = {
            'acriss_code': 'acriss_code',
            'category': 'category',
            'type': 'type',
            'transmission': 'transmission',
            'air_conditioning': 'air_conditioning',
            'fuel': 'fuel'
        }

        self._acriss_code = None
        self._category = None
        self._type = None
        self._transmission = None
        self._air_conditioning = None
        self._fuel = None

    @property
    def acriss_code(self):
        """
        Gets the acriss_code of this VehicleInfo.
        The 4 letter <a href=\"http://en.wikipedia.org/wiki/ACRISS_Car_Classification_Code\">ACRISS code</a> that defines the properties of vehicle being rented.

        :return: The acriss_code of this VehicleInfo.
        :rtype: str
        """
        return self._acriss_code

    @acriss_code.setter
    def acriss_code(self, acriss_code):
        """
        Sets the acriss_code of this VehicleInfo.
        The 4 letter <a href=\"http://en.wikipedia.org/wiki/ACRISS_Car_Classification_Code\">ACRISS code</a> that defines the properties of vehicle being rented.

        :param acriss_code: The acriss_code of this VehicleInfo.
        :type: str
        """
        self._acriss_code = acriss_code

    @property
    def category(self):
        """
        Gets the category of this VehicleInfo.
        The decoded ACRISS vehicle category (For example&colon; Economy, Luxury, Standard).

        :return: The category of this VehicleInfo.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this VehicleInfo.
        The decoded ACRISS vehicle category (For example&colon; Economy, Luxury, Standard).

        :param category: The category of this VehicleInfo.
        :type: str
        """
        self._category = category

    @property
    def type(self):
        """
        Gets the type of this VehicleInfo.
        The decoded ACRISS vehicle type, to let you know what kind of vehicle this is (For example&colon; Van, SUV, Pickup).

        :return: The type of this VehicleInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this VehicleInfo.
        The decoded ACRISS vehicle type, to let you know what kind of vehicle this is (For example&colon; Van, SUV, Pickup).

        :param type: The type of this VehicleInfo.
        :type: str
        """
        self._type = type

    @property
    def transmission(self):
        """
        Gets the transmission of this VehicleInfo.
        The decoded ACRISS transmission type, to let you know if this vehicle is Automatic or Manual Transmission (stick-shift).

        :return: The transmission of this VehicleInfo.
        :rtype: str
        """
        return self._transmission

    @transmission.setter
    def transmission(self, transmission):
        """
        Sets the transmission of this VehicleInfo.
        The decoded ACRISS transmission type, to let you know if this vehicle is Automatic or Manual Transmission (stick-shift).

        :param transmission: The transmission of this VehicleInfo.
        :type: str
        """
        self._transmission = transmission

    @property
    def air_conditioning(self):
        """
        Gets the air_conditioning of this VehicleInfo.
        The decoded ACRISS air_conditioning information, to let you know if this vehicle has air conditioning

        :return: The air_conditioning of this VehicleInfo.
        :rtype: bool
        """
        return self._air_conditioning

    @air_conditioning.setter
    def air_conditioning(self, air_conditioning):
        """
        Sets the air_conditioning of this VehicleInfo.
        The decoded ACRISS air_conditioning information, to let you know if this vehicle has air conditioning

        :param air_conditioning: The air_conditioning of this VehicleInfo.
        :type: bool
        """
        self._air_conditioning = air_conditioning

    @property
    def fuel(self):
        """
        Gets the fuel of this VehicleInfo.
        The decoded ACRISS fuel type, to let you know if this vehicle is hybrid, electric, etc.

        :return: The fuel of this VehicleInfo.
        :rtype: str
        """
        return self._fuel

    @fuel.setter
    def fuel(self, fuel):
        """
        Sets the fuel of this VehicleInfo.
        The decoded ACRISS fuel type, to let you know if this vehicle is hybrid, electric, etc.

        :param fuel: The fuel of this VehicleInfo.
        :type: str
        """
        self._fuel = fuel

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

