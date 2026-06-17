"""
Request entity for ChangeVpcRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ChangeVpcRequest(AbstractModel):
    """
    Request entity for ChangeVpcRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        subnet_id,
        internal_ip=None,
        security_group_ids=None,
        enterprise_security_group_ids=None,
        reboot=None,
    ):
        """
        Initialize ChangeVpcRequest request entity.

        :param instance_id: 虚机ID
        :type instance_id: str (required)

        :param subnet_id: 目标VPC的子网ID
        :type subnet_id: str (required)

        :param internal_ip: 内网IP
        :type internal_ip: str (optional)

        :param security_group_ids: 安全组列表
        :type security_group_ids: List[str] (optional)

        :param enterprise_security_group_ids: 企业安全组列表，不能同时指定普通安全组和企业安全组
        :type enterprise_security_group_ids: List[str] (optional)

        :param reboot: 是否重启实例
        :type reboot: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.subnet_id = subnet_id
        self.internal_ip = internal_ip
        self.security_group_ids = security_group_ids
        self.enterprise_security_group_ids = enterprise_security_group_ids
        self.reboot = reboot

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.internal_ip is not None:
            result['internalIp'] = self.internal_ip
        if self.security_group_ids is not None:
            result['securityGroupIds'] = self.security_group_ids
        if self.enterprise_security_group_ids is not None:
            result['enterpriseSecurityGroupIds'] = self.enterprise_security_group_ids
        if self.reboot is not None:
            result['reboot'] = self.reboot
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ChangeVpcRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('internalIp') is not None:
            self.internal_ip = m.get('internalIp')
        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')
        if m.get('enterpriseSecurityGroupIds') is not None:
            self.enterprise_security_group_ids = m.get('enterpriseSecurityGroupIds')
        if m.get('reboot') is not None:
            self.reboot = m.get('reboot')
        return self
