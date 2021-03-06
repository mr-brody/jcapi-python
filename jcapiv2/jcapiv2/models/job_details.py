# coding: utf-8

"""
    JumpCloud APIs

    V1 & V2 versions of JumpCloud's API. The next version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings. The most recent version of JumpCloud's API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings.

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class JobDetails(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'status': 'str',
        'total_work_count': 'int',
        'work_completed_count': 'int',
        'meta': 'object'
    }

    attribute_map = {
        'status': 'status',
        'total_work_count': 'totalWorkCount',
        'work_completed_count': 'workCompletedCount',
        'meta': 'meta'
    }

    def __init__(self, status=None, total_work_count=None, work_completed_count=None, meta=None):
        """
        JobDetails - a model defined in Swagger
        """

        self._status = None
        self._total_work_count = None
        self._work_completed_count = None
        self._meta = None

        if status is not None:
          self.status = status
        if total_work_count is not None:
          self.total_work_count = total_work_count
        if work_completed_count is not None:
          self.work_completed_count = work_completed_count
        if meta is not None:
          self.meta = meta

    @property
    def status(self):
        """
        Gets the status of this JobDetails.

        :return: The status of this JobDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this JobDetails.

        :param status: The status of this JobDetails.
        :type: str
        """

        self._status = status

    @property
    def total_work_count(self):
        """
        Gets the total_work_count of this JobDetails.

        :return: The total_work_count of this JobDetails.
        :rtype: int
        """
        return self._total_work_count

    @total_work_count.setter
    def total_work_count(self, total_work_count):
        """
        Sets the total_work_count of this JobDetails.

        :param total_work_count: The total_work_count of this JobDetails.
        :type: int
        """

        self._total_work_count = total_work_count

    @property
    def work_completed_count(self):
        """
        Gets the work_completed_count of this JobDetails.

        :return: The work_completed_count of this JobDetails.
        :rtype: int
        """
        return self._work_completed_count

    @work_completed_count.setter
    def work_completed_count(self, work_completed_count):
        """
        Sets the work_completed_count of this JobDetails.

        :param work_completed_count: The work_completed_count of this JobDetails.
        :type: int
        """

        self._work_completed_count = work_completed_count

    @property
    def meta(self):
        """
        Gets the meta of this JobDetails.

        :return: The meta of this JobDetails.
        :rtype: object
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """
        Sets the meta of this JobDetails.

        :param meta: The meta of this JobDetails.
        :type: object
        """

        self._meta = meta

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
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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
        if not isinstance(other, JobDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
