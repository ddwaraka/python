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


class TopSearchesSearchResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        TopSearchesSearchResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'market': 'str',
            'period': 'str',
            'origin': 'str',
            'destination': 'str',
            'results': 'list[TopSearchesSearchResult]'
        }

        self.attribute_map = {
            'market': 'market',
            'period': 'period',
            'origin': 'origin',
            'destination': 'destination',
            'results': 'results'
        }

        self._market = None
        self._period = None
        self._origin = None
        self._destination = None
        self._results = None

    @property
    def market(self):
        """
        Gets the market of this TopSearchesSearchResponse.
        Country code

        :return: The market of this TopSearchesSearchResponse.
        :rtype: str
        """
        return self._market

    @market.setter
    def market(self, market):
        """
        Sets the market of this TopSearchesSearchResponse.
        Country code

        :param market: The market of this TopSearchesSearchResponse.
        :type: str
        """
        self._market = market

    @property
    def period(self):
        """
        Gets the period of this TopSearchesSearchResponse.
        The date period, in <a href=\"https://en.wikipedia.org/wiki/ISO_8601\">ISO 8601</a> date format YYYY-MM or YYYY

        :return: The period of this TopSearchesSearchResponse.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Sets the period of this TopSearchesSearchResponse.
        The date period, in <a href=\"https://en.wikipedia.org/wiki/ISO_8601\">ISO 8601</a> date format YYYY-MM or YYYY

        :param period: The period of this TopSearchesSearchResponse.
        :type: str
        """
        self._period = period

    @property
    def origin(self):
        """
        Gets the origin of this TopSearchesSearchResponse.
        IATA code

        :return: The origin of this TopSearchesSearchResponse.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """
        Sets the origin of this TopSearchesSearchResponse.
        IATA code

        :param origin: The origin of this TopSearchesSearchResponse.
        :type: str
        """
        self._origin = origin

    @property
    def destination(self):
        """
        Gets the destination of this TopSearchesSearchResponse.
        IATA code

        :return: The destination of this TopSearchesSearchResponse.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """
        Sets the destination of this TopSearchesSearchResponse.
        IATA code

        :param destination: The destination of this TopSearchesSearchResponse.
        :type: str
        """
        self._destination = destination

    @property
    def results(self):
        """
        Gets the results of this TopSearchesSearchResponse.


        :return: The results of this TopSearchesSearchResponse.
        :rtype: list[TopSearchesSearchResult]
        """
        return self._results

    @results.setter
    def results(self, results):
        """
        Sets the results of this TopSearchesSearchResponse.


        :param results: The results of this TopSearchesSearchResponse.
        :type: list[TopSearchesSearchResult]
        """
        self._results = results

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

