# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class LOG(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, logentry=None):  # noqa: E501
        """LOG - a model defined in Swagger

        :param logentry: The logentry of this LOG.  # noqa: E501
        :type logentry: str
        """
        self.swagger_types = {
            'logentry': str
        }

        self.attribute_map = {
            'logentry': 'logentry'
        }

        self._logentry = logentry

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LOG of this LOG.  # noqa: E501
        :rtype: LOG
        """
        return util.deserialize_model(dikt, cls)

    @property
    def logentry(self):
        """Gets the logentry of this LOG.


        :return: The logentry of this LOG.
        :rtype: str
        """
        return self._logentry

    @logentry.setter
    def logentry(self, logentry):
        """Sets the logentry of this LOG.


        :param logentry: The logentry of this LOG.
        :type logentry: str
        """
        if logentry is None:
            raise ValueError("Invalid value for `logentry`, must not be `None`")  # noqa: E501

        self._logentry = logentry
