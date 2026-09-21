"""
Request entity for KillMysqlSessionRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class KillMysqlSessionRequest(AbstractModel):
    """
    Request entity for KillMysqlSessionRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, app_id, id_items, node_id=None):
        """
        Initialize KillMysqlSessionRequest request entity.

        :param app_id: 集群ID
        :type app_id: str (required)

        :param node_id: 节点ID
        :type node_id: str (optional)

        :param id_items: idItems 指定了需要查杀的会话ID列表
        :type id_items: List[int] (required)
        """
        super().__init__()
        self.app_id = app_id
        self.node_id = node_id
        self.id_items = id_items

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
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.node_id is not None:
            result['nodeId'] = self.node_id
        if self.id_items is not None:
            result['idItems'] = self.id_items
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: KillMysqlSessionRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')
        if m.get('idItems') is not None:
            self.id_items = m.get('idItems')
        return self
