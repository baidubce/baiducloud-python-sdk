"""
Request entity for CreateEnterpriseSecurityGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vpc.models.enterprise_security_group_rule_model import EnterpriseSecurityGroupRuleModel
from baiducloud_python_sdk_vpc.models.tag_model import TagModel


class CreateEnterpriseSecurityGroupRequest(AbstractModel):
    """
    Request entity for CreateEnterpriseSecurityGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, client_token=None, desc=None, rules=None, tags=None):
        """
        Initialize CreateEnterpriseSecurityGroupRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 创建的企业安全组的名字,支持大小写字母、数字、中文以及-\\_/.特殊字符，必须以字母开头，长度1-65。
        :type name: str (required)

        :param desc: 对所创建的企业安全组的描述信息
        :type desc: str (optional)

        :param rules: 创建企业安全组时绑定的安全组规则列表
        :type rules: List[EnterpriseSecurityGroupRuleModel] (optional)

        :param tags: 创建企业安全组时绑定的标签列表
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.desc = desc
        self.rules = rules
        self.tags = tags

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
        if self.rules is not None:
            result['rules'] = [i.to_dict() for i in self.rules]
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateEnterpriseSecurityGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('rules') is not None:
            self.rules = [EnterpriseSecurityGroupRuleModel().from_dict(i) for i in m.get('rules')]
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
