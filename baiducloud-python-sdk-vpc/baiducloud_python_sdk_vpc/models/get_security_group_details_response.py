"""
Request entity for GetSecurityGroupDetailsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.security_group_rule_model import SecurityGroupRuleModel
from baiducloud_python_sdk_vpc.models.tag_model import TagModel


class GetSecurityGroupDetailsResponse(BceResponse):
    """
    GetSecurityGroupDetailsResponse
    """

    def __init__(
        self,
        id=None,
        name=None,
        vpc_id=None,
        desc=None,
        created_time=None,
        sg_version=None,
        bind_instance_num=None,
        rules=None,
        tags=None,
    ):
        """
        Initialize GetSecurityGroupDetailsResponse response.

        :param id: 安全组ID
        :type id: str (optional)

        :param name: 安全组名称
        :type name: str (optional)

        :param vpc_id: 安全组所属VPC的ID
        :type vpc_id: str (optional)

        :param desc: 安全组描述
        :type desc: str (optional)

        :param created_time: 创建时间
        :type created_time: str (optional)

        :param sg_version: 安全组版本
        :type sg_version: int (optional)

        :param bind_instance_num: 安全组所关联的实例数目
        :type bind_instance_num: int (optional)

        :param rules: 安全组规则信息，由SecurityGroupModel组成的集合
        :type rules: List[SecurityGroupRuleModel] (optional)

        :param tags: 标签信息，由Tag组成的集合
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.vpc_id = vpc_id
        self.desc = desc
        self.created_time = created_time
        self.sg_version = sg_version
        self.bind_instance_num = bind_instance_num
        self.rules = rules
        self.tags = tags

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
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.desc is not None:
            result['desc'] = self.desc
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.sg_version is not None:
            result['sgVersion'] = self.sg_version
        if self.bind_instance_num is not None:
            result['bindInstanceNum'] = self.bind_instance_num
        if self.rules is not None:
            result['rules'] = [i.to_dict() for i in self.rules]
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetSecurityGroupDetailsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('sgVersion') is not None:
            self.sg_version = m.get('sgVersion')
        if m.get('bindInstanceNum') is not None:
            self.bind_instance_num = m.get('bindInstanceNum')
        if m.get('rules') is not None:
            self.rules = [SecurityGroupRuleModel().from_dict(i) for i in m.get('rules')]
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
