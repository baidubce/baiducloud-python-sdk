"""
Request entity for DescribeAlarmPolicyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeAlarmPolicyRequest(AbstractModel):
    """
    Request entity for DescribeAlarmPolicyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id, require_sub_resource_type=None):
        """
        Initialize DescribeAlarmPolicyRequest request entity.

        :param id: 策略ID
        :type id: str (required)

        :param require_sub_resource_type: 是否返回SubResourceType，默认值：false
        :type require_sub_resource_type: bool (optional)
        """
        super().__init__()
        self.id = id
        self.require_sub_resource_type = require_sub_resource_type

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.require_sub_resource_type is not None:
            result['requireSubResourceType'] = self.require_sub_resource_type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeAlarmPolicyRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('requireSubResourceType') is not None:
            self.require_sub_resource_type = m.get('requireSubResourceType')
        return self
