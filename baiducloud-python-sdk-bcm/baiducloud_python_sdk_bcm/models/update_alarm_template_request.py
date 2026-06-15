"""
Request entity for UpdateAlarmTemplateRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcm.models.alarm_rule import AlarmRule


class UpdateAlarmTemplateRequest(AbstractModel):
    """
    Request entity for UpdateAlarmTemplateRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id, scope, resource_type, name, rules, sub_resource_type=None, comment=None):
        """
        Initialize UpdateAlarmTemplateRequest request entity.

        :param id: 报警模板ID
        :type id: str (required)

        :param scope: 云产品类型
        :type scope: str (required)

        :param resource_type: 资源类型
        :type resource_type: str (required)

        :param sub_resource_type: 子资源类型
        :type sub_resource_type: str (optional)

        :param name: 模板名称
        :type name: str (required)

        :param comment: 备注信息
        :type comment: str (optional)

        :param rules: 报警规则列表（OR规则）
        :type rules: List[AlarmRule] (required)
        """
        super().__init__()
        self.id = id
        self.scope = scope
        self.resource_type = resource_type
        self.sub_resource_type = sub_resource_type
        self.name = name
        self.comment = comment
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
        if self.id is not None:
            result['id'] = self.id
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
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateAlarmTemplateRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
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
