"""
EnterpriseSecurityGroupModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_vpc.models.enterprise_security_group_rule_model import EnterpriseSecurityGroupRuleModel

from baiducloud_python_sdk_vpc.models.tag_model import TagModel


class EnterpriseSecurityGroupModel(AbstractModel):
    """
    EnterpriseSecurityGroupModel
    """

    def __init__(self, id=None, name=None, desc=None, created_time=None, updated_time=None, rules=None, tags=None):
        """
        Initialize EnterpriseSecurityGroupModel instance.

        :param id: 企业安全组ID
        :type id: str (optional)

        :param name: 名称,支持大小写字母、数字、中文以及-\\_ /.特殊字符，必须以字母开头，长度1-65。
        :type name: str (optional)

        :param desc: 描述
        :type desc: str (optional)

        :param created_time: 企业安全组创建时间
        :type created_time: str (optional)

        :param updated_time: 企业安全组更新时间
        :type updated_time: str (optional)

        :param rules: 企业安全组规则
        :type rules: List[EnterpriseSecurityGroupRuleModel] (optional)

        :param tags: 企业安全组绑定的标签列表
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.desc = desc
        self.created_time = created_time
        self.updated_time = updated_time
        self.rules = rules
        self.tags = tags

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
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.desc is not None:
            result['desc'] = self.desc
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.updated_time is not None:
            result['updatedTime'] = self.updated_time
        if self.rules is not None:
            result['rules'] = [i.to_dict() for i in self.rules]
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EnterpriseSecurityGroupModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')
        if m.get('rules') is not None:
            self.rules = [EnterpriseSecurityGroupRuleModel().from_dict(i) for i in m.get('rules')]
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
