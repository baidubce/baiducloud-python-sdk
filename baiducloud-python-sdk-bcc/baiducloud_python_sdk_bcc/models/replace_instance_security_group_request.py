"""
Request entity for ReplaceInstanceSecurityGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ReplaceInstanceSecurityGroupRequest(AbstractModel):
    """
    Request entity for ReplaceInstanceSecurityGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_ids, security_group_ids, security_group_type):
        """
        Initialize ReplaceInstanceSecurityGroupRequest request entity.

        :param instance_ids: 待替换的虚机的短id列表
        :type instance_ids: List[str] (required)

        :param security_group_ids: 目标安全组的短id列表
        :type security_group_ids: List[str] (required)

        :param security_group_type: 目标安全组类型（企业安全组：enterprise，普通安全组：normal）
        :type security_group_type: str (required)
        """
        super().__init__()
        self.instance_ids = instance_ids
        self.security_group_ids = security_group_ids
        self.security_group_type = security_group_type

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
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.security_group_ids is not None:
            result['securityGroupIds'] = self.security_group_ids
        if self.security_group_type is not None:
            result['securityGroupType'] = self.security_group_type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ReplaceInstanceSecurityGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')
        if m.get('securityGroupType') is not None:
            self.security_group_type = m.get('securityGroupType')
        return self
