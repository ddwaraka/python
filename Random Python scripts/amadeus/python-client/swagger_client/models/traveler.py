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


class Traveler(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Traveler - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'last_name': 'str',
            'first_name': 'str',
            'traveler_type': 'str',
            'infant': 'Infant',
            'date_of_birth': 'date',
            'contacts': 'list[Contact]',
            'frequent_traveler_cards': 'list[FrequentTravelerCard]'
        }

        self.attribute_map = {
            'id': 'id',
            'last_name': 'last_name',
            'first_name': 'first_name',
            'traveler_type': 'traveler_type',
            'infant': 'infant',
            'date_of_birth': 'date_of_birth',
            'contacts': 'contacts',
            'frequent_traveler_cards': 'frequent_traveler_cards'
        }

        self._id = None
        self._last_name = None
        self._first_name = None
        self._traveler_type = None
        self._infant = None
        self._date_of_birth = None
        self._contacts = None
        self._frequent_traveler_cards = None

    @property
    def id(self):
        """
        Gets the id of this Traveler.
        Uniquely identifies this traveler in this travel record. This ID is persistent, and remains the same for the lifetime of the travel record.

        :return: The id of this Traveler.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Traveler.
        Uniquely identifies this traveler in this travel record. This ID is persistent, and remains the same for the lifetime of the travel record.

        :param id: The id of this Traveler.
        :type: str
        """
        self._id = id

    @property
    def last_name(self):
        """
        Gets the last_name of this Traveler.
        The last name of the passenger, as entered by the agent, in upper-case. May include suffixes. For example&colon; THACKSTON, KING III, LU.

        :return: The last_name of this Traveler.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this Traveler.
        The last name of the passenger, as entered by the agent, in upper-case. May include suffixes. For example&colon; THACKSTON, KING III, LU.

        :param last_name: The last_name of this Traveler.
        :type: str
        """
        self._last_name = last_name

    @property
    def first_name(self):
        """
        Gets the first_name of this Traveler.
        The first name of the passenger, as entered by the agent, in upper-case. May include middle names, initials or prefixes. The total combined length of the first name and last name must be between 2 and 57 characters. For example&colon; ALEXANDRA, JOSE-ANTONIO MR, ELAINE T DR.

        :return: The first_name of this Traveler.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this Traveler.
        The first name of the passenger, as entered by the agent, in upper-case. May include middle names, initials or prefixes. The total combined length of the first name and last name must be between 2 and 57 characters. For example&colon; ALEXANDRA, JOSE-ANTONIO MR, ELAINE T DR.

        :param first_name: The first_name of this Traveler.
        :type: str
        """
        self._first_name = first_name

    @property
    def traveler_type(self):
        """
        Gets the traveler_type of this Traveler.
        Enumeration of the type of traveler. May be ADULT or CHILD.

        :return: The traveler_type of this Traveler.
        :rtype: str
        """
        return self._traveler_type

    @traveler_type.setter
    def traveler_type(self, traveler_type):
        """
        Sets the traveler_type of this Traveler.
        Enumeration of the type of traveler. May be ADULT or CHILD.

        :param traveler_type: The traveler_type of this Traveler.
        :type: str
        """
        self._traveler_type = traveler_type

    @property
    def infant(self):
        """
        Gets the infant of this Traveler.
        Details on any infant that may be sharing this seat with this traveler. Absence of this key indicates that no infant is traveling with this passenger. An empty object at this key indicated an anonymous infant is traveling with the passenger.

        :return: The infant of this Traveler.
        :rtype: Infant
        """
        return self._infant

    @infant.setter
    def infant(self, infant):
        """
        Sets the infant of this Traveler.
        Details on any infant that may be sharing this seat with this traveler. Absence of this key indicates that no infant is traveling with this passenger. An empty object at this key indicated an anonymous infant is traveling with the passenger.

        :param infant: The infant of this Traveler.
        :type: Infant
        """
        self._infant = infant

    @property
    def date_of_birth(self):
        """
        Gets the date_of_birth of this Traveler.
        An <a href=\"https://en.wikipedia.org/wiki/ISO_8601\">ISO 8601</a> date indicating the birth date of the traveler, as provided by the agent. For example&colon; 1972-02-19.

        :return: The date_of_birth of this Traveler.
        :rtype: date
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """
        Sets the date_of_birth of this Traveler.
        An <a href=\"https://en.wikipedia.org/wiki/ISO_8601\">ISO 8601</a> date indicating the birth date of the traveler, as provided by the agent. For example&colon; 1972-02-19.

        :param date_of_birth: The date_of_birth of this Traveler.
        :type: date
        """
        self._date_of_birth = date_of_birth

    @property
    def contacts(self):
        """
        Gets the contacts of this Traveler.
        Details on how to contact this traveler. At least one traveler in a travel-record will have a contact element.

        :return: The contacts of this Traveler.
        :rtype: list[Contact]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """
        Sets the contacts of this Traveler.
        Details on how to contact this traveler. At least one traveler in a travel-record will have a contact element.

        :param contacts: The contacts of this Traveler.
        :type: list[Contact]
        """
        self._contacts = contacts

    @property
    def frequent_traveler_cards(self):
        """
        Gets the frequent_traveler_cards of this Traveler.
        Information regarding loyalty cards that the traveler would like to use to accrue benefits as part of this travel record. Where possible, the system will attempt to validate that the frequent traveler card is eligible for use in the context of this travel record.

        :return: The frequent_traveler_cards of this Traveler.
        :rtype: list[FrequentTravelerCard]
        """
        return self._frequent_traveler_cards

    @frequent_traveler_cards.setter
    def frequent_traveler_cards(self, frequent_traveler_cards):
        """
        Sets the frequent_traveler_cards of this Traveler.
        Information regarding loyalty cards that the traveler would like to use to accrue benefits as part of this travel record. Where possible, the system will attempt to validate that the frequent traveler card is eligible for use in the context of this travel record.

        :param frequent_traveler_cards: The frequent_traveler_cards of this Traveler.
        :type: list[FrequentTravelerCard]
        """
        self._frequent_traveler_cards = frequent_traveler_cards

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

