"""
Request entity for CreateSecurityGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.tag import Tag
from baiducloud_python_sdk_bcc.models.security_group_rule_model import SecurityGroupRuleModel


class CreateSecurityGroupRequest(AbstractModel):
    """
    Request entity for CreateSecurityGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, rules, desc=None, vpc_id=None, tags=None):
        """
        Initialize CreateSecurityGroupRequest request entity.

        :param name: 安全组名称，支持大小写字母、数字、中文以及-_ /.特殊字符，必须以字母开头，长度1-65
        :type name: str (required)

        :param desc: 安全组描述信息
        :type desc: str (optional)

        :param vpc_id: 安全组所属的vpcId
        :type vpc_id: str (optional)

        :param tags: 标签列表
        :type tags: List[Tag] (optional)

        :param rules: 安全组规则列表
        :type rules: List[SecurityGroupRuleModel] (required)
        """
        super().__init__()
        self.name = name
        self.desc = desc
        self.vpc_id = vpc_id
        self.tags = tags
        self.rules = rules

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
        if self.name is not None:
            result['name'] = self.name
        if self.desc is not None:
            result['desc'] = self.desc
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.rules is not None:
            result['rules'] = [i.to_dict() for i in self.rules]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateSecurityGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('rules') is not None:
            self.rules = [SecurityGroupRuleModel().from_dict(i) for i in m.get('rules')]
        return self
