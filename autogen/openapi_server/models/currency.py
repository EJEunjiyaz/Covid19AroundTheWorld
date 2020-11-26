# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Currency(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, rates=None, base=None, date=None):  # noqa: E501
        """Currency - a model defined in OpenAPI

        :param rates: The rates of this Currency.  # noqa: E501
        :type rates: float
        :param base: The base of this Currency.  # noqa: E501
        :type base: str
        :param date: The date of this Currency.  # noqa: E501
        :type date: str
        """
        self.openapi_types = {
            'rates': float,
            'base': str,
            'date': str
        }

        self.attribute_map = {
            'rates': 'rates',
            'base': 'base',
            'date': 'date'
        }

        self._rates = rates
        self._base = base
        self._date = date

    @classmethod
    def from_dict(cls, dikt) -> 'Currency':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Currency of this Currency.  # noqa: E501
        :rtype: Currency
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rates(self):
        """Gets the rates of this Currency.


        :return: The rates of this Currency.
        :rtype: float
        """
        return self._rates

    @rates.setter
    def rates(self, rates):
        """Sets the rates of this Currency.


        :param rates: The rates of this Currency.
        :type rates: float
        """

        self._rates = rates

    @property
    def base(self):
        """Gets the base of this Currency.


        :return: The base of this Currency.
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this Currency.


        :param base: The base of this Currency.
        :type base: str
        """

        self._base = base

    @property
    def date(self):
        """Gets the date of this Currency.


        :return: The date of this Currency.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Currency.


        :param date: The date of this Currency.
        :type date: str
        """

        self._date = date