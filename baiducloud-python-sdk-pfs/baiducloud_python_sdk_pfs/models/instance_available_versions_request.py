"""
Request entity for InstanceAvailableVersionsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class InstanceAvailableVersionsRequest(AbstractModel):
    """
    Request entity for InstanceAvailableVersionsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, vpc_id, instance_type=None):
        """
        Initialize InstanceAvailableVersionsRequest request entity.

        :param instance_type: 实例类型
        :type instance_type: str (optional)

        :param vpc_id: 实例所在 VPC 的 ID，支持短 ID 或长 ID
        :type vpc_id: str (required)
        """
        super().__init__()
        self.instance_type = instance_type
        self.vpc_id = vpc_id

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
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceAvailableVersionsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        return self
