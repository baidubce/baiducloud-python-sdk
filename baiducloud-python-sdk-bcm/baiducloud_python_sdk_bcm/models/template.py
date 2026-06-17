"""
Template information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcm.models.alarm_rule import AlarmRule


class Template(AbstractModel):
    """
    Template
    """

    def __init__(self, scope=None, resource_type=None, sub_resource_type=None, name=None, comment=None, rules=None):
        """
        Initialize Template instance.

        :param scope: 云产品类型
        :type scope: str (optional)

        :param resource_type: 资源类型
        :type resource_type: str (optional)

        :param sub_resource_type: 子资源类型
        :type sub_resource_type: str (optional)

        :param name: 模板名称
        :type name: str (optional)

        :param comment: 备注信息
        :type comment: str (optional)

        :param rules: 报警规则列表
        :type rules: List[AlarmRule] (optional)
        """
        super().__init__()
        self.scope = scope
        self.resource_type = resource_type
        self.sub_resource_type = sub_resource_type
        self.name = name
        self.comment = comment
        self.rules = rules

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
        if self.scope is not None:
            result['scope'] = self.scope
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.sub_resource_type is not None:
            result['subResourceType'] = self.sub_resource_type
        if self.name is not None:
            result['name'] = self.name
        if self.comment is not None:
            result['comment'] = self.comment
        if self.rules is not None:
            result['rules'] = [i.to_dict() for i in self.rules]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Template

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('subResourceType') is not None:
            self.sub_resource_type = m.get('subResourceType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('rules') is not None:
            self.rules = [AlarmRule().from_dict(i) for i in m.get('rules')]
        return self
