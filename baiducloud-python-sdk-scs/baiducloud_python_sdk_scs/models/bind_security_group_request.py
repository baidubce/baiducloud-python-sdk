"""
Request entity for BindSecurityGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BindSecurityGroupRequest(AbstractModel):
    """
    Request entity for BindSecurityGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, security_group_ids):
        """
        Initialize BindSecurityGroupRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param security_group_ids: 绑定的安全组ID列表。
        :type security_group_ids: List[str] (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.security_group_ids = security_group_ids

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
        if self.security_group_ids is not None:
            result['securityGroupIds'] = self.security_group_ids
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BindSecurityGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')
        return self
