"""
SyncGroupInstanceConnectionResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SyncGroupInstanceConnectionResult(AbstractModel):
    """
    SyncGroupInstanceConnectionResult
    """

    def __init__(self, source_id=None, source_role=None, target_id=None, target_role=None, connectable=None):
        """
        Initialize SyncGroupInstanceConnectionResult instance.

        :param source_id: 源实例ID
        :type source_id: str (optional)

        :param source_role: 源实例角色（可能不返回）
        :type source_role: str (optional)

        :param target_id: 目标实例ID
        :type target_id: str (optional)

        :param target_role: 目标实例角色（可能不返回）
        :type target_role: str (optional)

        :param connectable: 源实例与目标实例是否可连通
        :type connectable: bool (optional)
        """
        super().__init__()
        self.source_id = source_id
        self.source_role = source_role
        self.target_id = target_id
        self.target_role = target_role
        self.connectable = connectable

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
        if self.source_id is not None:
            result['sourceId'] = self.source_id
        if self.source_role is not None:
            result['sourceRole'] = self.source_role
        if self.target_id is not None:
            result['targetId'] = self.target_id
        if self.target_role is not None:
            result['targetRole'] = self.target_role
        if self.connectable is not None:
            result['connectable'] = self.connectable
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SyncGroupInstanceConnectionResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sourceId') is not None:
            self.source_id = m.get('sourceId')
        if m.get('sourceRole') is not None:
            self.source_role = m.get('sourceRole')
        if m.get('targetId') is not None:
            self.target_id = m.get('targetId')
        if m.get('targetRole') is not None:
            self.target_role = m.get('targetRole')
        if m.get('connectable') is not None:
            self.connectable = m.get('connectable')
        return self
