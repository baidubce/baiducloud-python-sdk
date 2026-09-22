"""
Group information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_scs.models.rule import Rule


class Group(AbstractModel):
    """
    Group
    """

    def __init__(
        self,
        security_group_remark=None,
        security_group_name=None,
        security_group_id=None,
        security_group_uuid=None,
        vpc_id=None,
        vpc_name=None,
        outbound=None,
    ):
        """
        Initialize Group instance.

        :param security_group_remark: 安全组备注。
        :type security_group_remark: str (optional)

        :param security_group_name: 安全组名称。
        :type security_group_name: str (optional)

        :param security_group_id: 安全组ID。
        :type security_group_id: str (optional)

        :param security_group_uuid: 安全组长ID。
        :type security_group_uuid: str (optional)

        :param vpc_id: vpcId。
        :type vpc_id: str (optional)

        :param vpc_name: vpc名称。
        :type vpc_name: str (optional)

        :param outbound: 安全组规则。
        :type outbound: List[Rule] (optional)
        """
        super().__init__()
        self.security_group_remark = security_group_remark
        self.security_group_name = security_group_name
        self.security_group_id = security_group_id
        self.security_group_uuid = security_group_uuid
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name
        self.outbound = outbound

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.security_group_remark is not None:
            result['securityGroupRemark'] = self.security_group_remark
        if self.security_group_name is not None:
            result['securityGroupName'] = self.security_group_name
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.security_group_uuid is not None:
            result['securityGroupUuid'] = self.security_group_uuid
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.vpc_name is not None:
            result['vpcName'] = self.vpc_name
        if self.outbound is not None:
            result['outbound'] = [i.to_dict() for i in self.outbound]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Group

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('securityGroupRemark') is not None:
            self.security_group_remark = m.get('securityGroupRemark')
        if m.get('securityGroupName') is not None:
            self.security_group_name = m.get('securityGroupName')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('securityGroupUuid') is not None:
            self.security_group_uuid = m.get('securityGroupUuid')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('vpcName') is not None:
            self.vpc_name = m.get('vpcName')
        if m.get('outbound') is not None:
            self.outbound = [Rule().from_dict(i) for i in m.get('outbound')]
        return self
