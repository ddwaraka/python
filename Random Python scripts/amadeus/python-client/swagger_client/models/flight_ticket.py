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


class FlightTicket(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        FlightTicket - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'price': 'Amount',
            'traveler_ids': 'list[str]',
            'flight_bounds': 'list[FlightReservationBound]'
        }

        self.attribute_map = {
            'id': 'id',
            'price': 'price',
            'traveler_ids': 'traveler_ids',
            'flight_bounds': 'flight_bounds'
        }

        self._id = None
        self._price = None
        self._traveler_ids = None
        self._flight_bounds = None

    @property
    def id(self):
        """
        Gets the id of this FlightTicket.
        Uniquely identifies this ticket in this travel record. This ID is persistent, and remains the same for the lifetime of the travel record.

        :return: The id of this FlightTicket.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FlightTicket.
        Uniquely identifies this ticket in this travel record. This ID is persistent, and remains the same for the lifetime of the travel record.

        :param id: The id of this FlightTicket.
        :type: str
        """
        self._id = id

    @property
    def price(self):
        """
        Gets the price of this FlightTicket.
        The cost of this ticket.

        :return: The price of this FlightTicket.
        :rtype: Amount
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this FlightTicket.
        The cost of this ticket.

        :param price: The price of this FlightTicket.
        :type: Amount
        """
        self._price = price

    @property
    def traveler_ids(self):
        """
        Gets the traveler_ids of this FlightTicket.
        Traveler identifiers to indicate the travelers to whom this ticket applies.

        :return: The traveler_ids of this FlightTicket.
        :rtype: list[str]
        """
        return self._traveler_ids

    @traveler_ids.setter
    def traveler_ids(self, traveler_ids):
        """
        Sets the traveler_ids of this FlightTicket.
        Traveler identifiers to indicate the travelers to whom this ticket applies.

        :param traveler_ids: The traveler_ids of this FlightTicket.
        :type: list[str]
        """
        self._traveler_ids = traveler_ids

    @property
    def flight_bounds(self):
        """
        Gets the flight_bounds of this FlightTicket.
        The flight itinerary for this ticket.

        :return: The flight_bounds of this FlightTicket.
        :rtype: list[FlightReservationBound]
        """
        return self._flight_bounds

    @flight_bounds.setter
    def flight_bounds(self, flight_bounds):
        """
        Sets the flight_bounds of this FlightTicket.
        The flight itinerary for this ticket.

        :param flight_bounds: The flight_bounds of this FlightTicket.
        :type: list[FlightReservationBound]
        """
        self._flight_bounds = flight_bounds

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

