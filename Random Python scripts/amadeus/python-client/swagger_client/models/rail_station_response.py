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


class RailStationResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        RailStationResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'name': 'str',
            'short_name': 'str',
            'country': 'str',
            'location': 'Geolocation',
            'traffic': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'name': 'name',
            'short_name': 'short_name',
            'country': 'country',
            'location': 'location',
            'traffic': 'traffic'
        }

        self._id = None
        self._type = None
        self._name = None
        self._short_name = None
        self._country = None
        self._location = None
        self._traffic = None

    @property
    def id(self):
        """
        Gets the id of this RailStationResponse.
        The ID of this station, as provided in the request

        :return: The id of this RailStationResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RailStationResponse.
        The ID of this station, as provided in the request

        :param id: The id of this RailStationResponse.
        :type: str
        """
        self._id = id

    @property
    def type(self):
        """
        Gets the type of this RailStationResponse.
        The type of code to which this station refers. Some codes represent agglomeration of multiple stations, whereas others represent an individual station. Possible values are AGGLOMERATION and STATION.

        :return: The type of this RailStationResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this RailStationResponse.
        The type of code to which this station refers. Some codes represent agglomeration of multiple stations, whereas others represent an individual station. Possible values are AGGLOMERATION and STATION.

        :param type: The type of this RailStationResponse.
        :type: str
        """
        self._type = type

    @property
    def name(self):
        """
        Gets the name of this RailStationResponse.
        The name of this station.

        :return: The name of this RailStationResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RailStationResponse.
        The name of this station.

        :param name: The name of this RailStationResponse.
        :type: str
        """
        self._name = name

    @property
    def short_name(self):
        """
        Gets the short_name of this RailStationResponse.
        The shortened name of this station (20 characters max) which may be used in certain cases.

        :return: The short_name of this RailStationResponse.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """
        Sets the short_name of this RailStationResponse.
        The shortened name of this station (20 characters max) which may be used in certain cases.

        :param short_name: The short_name of this RailStationResponse.
        :type: str
        """
        self._short_name = short_name

    @property
    def country(self):
        """
        Gets the country of this RailStationResponse.
        The <a href=\"http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2\">ISO 3166-1 alpha-2 country code</a> in which this station can be found.

        :return: The country of this RailStationResponse.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this RailStationResponse.
        The <a href=\"http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2\">ISO 3166-1 alpha-2 country code</a> in which this station can be found.

        :param country: The country of this RailStationResponse.
        :type: str
        """
        self._country = country

    @property
    def location(self):
        """
        Gets the location of this RailStationResponse.
        This stations's approximate geolocation.

        :return: The location of this RailStationResponse.
        :rtype: Geolocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """
        Sets the location of this RailStationResponse.
        This stations's approximate geolocation.

        :param location: The location of this RailStationResponse.
        :type: Geolocation
        """
        self._location = location

    @property
    def traffic(self):
        """
        Gets the traffic of this RailStationResponse.
        An indication of the level of Intercity traffic passing through this station.

        :return: The traffic of this RailStationResponse.
        :rtype: str
        """
        return self._traffic

    @traffic.setter
    def traffic(self, traffic):
        """
        Sets the traffic of this RailStationResponse.
        An indication of the level of Intercity traffic passing through this station.

        :param traffic: The traffic of this RailStationResponse.
        :type: str
        """
        self._traffic = traffic

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

