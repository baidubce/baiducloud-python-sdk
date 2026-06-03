"""
Request entity for DescribeInstanceResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_rapidfs.models.instance_info import InstanceInfo


class DescribeInstanceResponse(BceResponse):
    """
    DescribeInstanceResponse
    """

    def __init__(self, instance_info=None):
        """
        Initialize DescribeInstanceResponse response.

        :param instance_info: instance_info field
        :type instance_info: InstanceInfo (optional)
        """
        super().__init__()
        self.instance_info = instance_info

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.instance_info is not None:
            result['instanceInfo'] = self.instance_info.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeInstanceResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceInfo') is not None:
            self.instance_info = InstanceInfo().from_dict(m.get('instanceInfo'))
        return self
