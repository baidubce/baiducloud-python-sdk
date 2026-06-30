"""
AttachedEntities information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AttachedEntities(AbstractModel):
    """
    AttachedEntities
    """

    def __init__(self, id=None, name=None, type=None, attach_time=None):
        """
        Initialize AttachedEntities instance.

        :param id: 主体 id
        :type id: str (optional)

        :param name: 主体名称
        :type name: str (optional)

        :param type: UserPolicy或 GroupPolicy
        :type type: str (optional)

        :param attach_time: 策略被授予时间
        :type attach_time: date (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.type = type
        self.attach_time = attach_time

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
        if self.type is not None:
            result['type'] = self.type
        if self.attach_time is not None:
            result['attachTime'] = self.attach_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AttachedEntities

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('attachTime') is not None:
            self.attach_time = m.get('attachTime')
        return self
