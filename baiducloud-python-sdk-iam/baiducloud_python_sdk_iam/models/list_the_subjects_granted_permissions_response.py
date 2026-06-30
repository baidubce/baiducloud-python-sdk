"""
Request entity for ListTheSubjectsGrantedPermissionsResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_iam.models.attached_entities import AttachedEntities


class ListTheSubjectsGrantedPermissionsResponse(BceResponse):
    """
    ListTheSubjectsGrantedPermissionsResponse
    """

    def __init__(self, entities=None, id=None, name=None, type=None, attach_time=None):
        """
        Initialize ListTheSubjectsGrantedPermissionsResponse response.

        :param entities: 策略被授予主体对象的列表
        :type entities: List[AttachedEntities] (optional)

        :param id: 主体 id
        :type id: str (optional)

        :param name: 主体名称
        :type name: str (optional)

        :param type: UserPolicy或 GroupPolicy
        :type type: str (optional)

        :param attach_time: 策略被授予时间
        :type attach_time: datetime (optional)
        """
        super().__init__()
        self.entities = entities
        self.id = id
        self.name = name
        self.type = type
        self.attach_time = attach_time

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
        if self.entities is not None:
            result['entities'] = [i.to_dict() for i in self.entities]
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.attach_time is not None:
            result['attach_time'] = self.attach_time
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListTheSubjectsGrantedPermissionsResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('entities') is not None:
            self.entities = [AttachedEntities().from_dict(i) for i in m.get('entities')]
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('attach_time') is not None:
            self.attach_time = m.get('attach_time')
        return self
