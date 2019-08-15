# coding: utf-8

"""
    JumpCloud APIs

     JumpCloud's V2 API. This set of endpoints allows JumpCloud customers to manage objects, groupings and mappings and interact with the JumpCloud Graph.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SystemInsightsInterfaceAddresses(object):
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
        'interface': 'str',
        'address': 'str',
        'mask': 'str',
        'broadcast': 'str',
        'point_to_point': 'str',
        'type': 'str',
        'friendly_name': 'str',
        'jc_collection_time': 'str',
        'jc_system_id': 'str'
    }

    attribute_map = {
        'interface': 'interface',
        'address': 'address',
        'mask': 'mask',
        'broadcast': 'broadcast',
        'point_to_point': 'point_to_point',
        'type': 'type',
        'friendly_name': 'friendly_name',
        'jc_collection_time': 'jc_collection_time',
        'jc_system_id': 'jc_system_id'
    }

    def __init__(self, interface=None, address=None, mask=None, broadcast=None, point_to_point=None, type=None, friendly_name=None, jc_collection_time=None, jc_system_id=None):  # noqa: E501
        """SystemInsightsInterfaceAddresses - a model defined in Swagger"""  # noqa: E501

        self._interface = None
        self._address = None
        self._mask = None
        self._broadcast = None
        self._point_to_point = None
        self._type = None
        self._friendly_name = None
        self._jc_collection_time = None
        self._jc_system_id = None
        self.discriminator = None

        if interface is not None:
            self.interface = interface
        if address is not None:
            self.address = address
        if mask is not None:
            self.mask = mask
        if broadcast is not None:
            self.broadcast = broadcast
        if point_to_point is not None:
            self.point_to_point = point_to_point
        if type is not None:
            self.type = type
        if friendly_name is not None:
            self.friendly_name = friendly_name
        if jc_collection_time is not None:
            self.jc_collection_time = jc_collection_time
        if jc_system_id is not None:
            self.jc_system_id = jc_system_id

    @property
    def interface(self):
        """Gets the interface of this SystemInsightsInterfaceAddresses.  # noqa: E501


        :return: The interface of this SystemInsightsInterfaceAddresses.  # noqa: E501
        :rtype: str
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """Sets the interface of this SystemInsightsInterfaceAddresses.


        :param interface: The interface of this SystemInsightsInterfaceAddresses.  # noqa: E501
        :type: str
        """

        self._interface = interface

    @property
    def address(self):
        """Gets the address of this SystemInsightsInterfaceAddresses.  # noqa: E501


        :return: The address of this SystemInsightsInterfaceAddresses.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SystemInsightsInterfaceAddresses.


        :param address: The address of this SystemInsightsInterfaceAddresses.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def mask(self):
        """Gets the mask of this SystemInsightsInterfaceAddresses.  # noqa: E501


        :return: The mask of this SystemInsightsInterfaceAddresses.  # noqa: E501
        :rtype: str
        """
        return self._mask

    @mask.setter
    def mask(self, mask):
        """Sets the mask of this SystemInsightsInterfaceAddresses.


        :param mask: The mask of this SystemInsightsInterfaceAddresses.  # noqa: E501
        :type: str
        """

        self._mask = mask

    @property
    def broadcast(self):
        """Gets the broadcast of this SystemInsightsInterfaceAddresses.  # noqa: E501


        :return: The broadcast of this SystemInsightsInterfaceAddresses.  # noqa: E501
        :rtype: str
        """
        return self._broadcast

    @broadcast.setter
    def broadcast(self, broadcast):
        """Sets the broadcast of this SystemInsightsInterfaceAddresses.


        :param broadcast: The broadcast of this SystemInsightsInterfaceAddresses.  # noqa: E501
        :type: str
        """

        self._broadcast = broadcast

    @property
    def point_to_point(self):
        """Gets the point_to_point of this SystemInsightsInterfaceAddresses.  # noqa: E501


        :return: The point_to_point of this SystemInsightsInterfaceAddresses.  # noqa: E501
        :rtype: str
        """
        return self._point_to_point

    @point_to_point.setter
    def point_to_point(self, point_to_point):
        """Sets the point_to_point of this SystemInsightsInterfaceAddresses.


        :param point_to_point: The point_to_point of this SystemInsightsInterfaceAddresses.  # noqa: E501
        :type: str
        """

        self._point_to_point = point_to_point

    @property
    def type(self):
        """Gets the type of this SystemInsightsInterfaceAddresses.  # noqa: E501


        :return: The type of this SystemInsightsInterfaceAddresses.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SystemInsightsInterfaceAddresses.


        :param type: The type of this SystemInsightsInterfaceAddresses.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def friendly_name(self):
        """Gets the friendly_name of this SystemInsightsInterfaceAddresses.  # noqa: E501


        :return: The friendly_name of this SystemInsightsInterfaceAddresses.  # noqa: E501
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name):
        """Sets the friendly_name of this SystemInsightsInterfaceAddresses.


        :param friendly_name: The friendly_name of this SystemInsightsInterfaceAddresses.  # noqa: E501
        :type: str
        """

        self._friendly_name = friendly_name

    @property
    def jc_collection_time(self):
        """Gets the jc_collection_time of this SystemInsightsInterfaceAddresses.  # noqa: E501


        :return: The jc_collection_time of this SystemInsightsInterfaceAddresses.  # noqa: E501
        :rtype: str
        """
        return self._jc_collection_time

    @jc_collection_time.setter
    def jc_collection_time(self, jc_collection_time):
        """Sets the jc_collection_time of this SystemInsightsInterfaceAddresses.


        :param jc_collection_time: The jc_collection_time of this SystemInsightsInterfaceAddresses.  # noqa: E501
        :type: str
        """

        self._jc_collection_time = jc_collection_time

    @property
    def jc_system_id(self):
        """Gets the jc_system_id of this SystemInsightsInterfaceAddresses.  # noqa: E501


        :return: The jc_system_id of this SystemInsightsInterfaceAddresses.  # noqa: E501
        :rtype: str
        """
        return self._jc_system_id

    @jc_system_id.setter
    def jc_system_id(self, jc_system_id):
        """Sets the jc_system_id of this SystemInsightsInterfaceAddresses.


        :param jc_system_id: The jc_system_id of this SystemInsightsInterfaceAddresses.  # noqa: E501
        :type: str
        """

        self._jc_system_id = jc_system_id

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
        if issubclass(SystemInsightsInterfaceAddresses, dict):
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
        if not isinstance(other, SystemInsightsInterfaceAddresses):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other