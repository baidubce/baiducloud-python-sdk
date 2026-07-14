"""
Request entity for DetachNodeV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DetachNodeV2Request(AbstractModel):
    """
    Request entity for DetachNodeV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, group_id, detach_node, nodes):
        """
        Initialize DetachNodeV2Request request entity.

        :param group_id: group_id parameter
        :type group_id: str (required)

        :param detach_node: detach_node parameter
        :type detach_node: str (required)

        :param nodes: 待移出实例短id列表
        :type nodes: List[str] (required)
        """
        super().__init__()
        self.group_id = group_id
        self.detach_node = detach_node
        self.nodes = nodes

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
        if self.nodes is not None:
            result['nodes'] = self.nodes
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DetachNodeV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('detachNode') is not None:
            self.detach_node = m.get('detachNode')
        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')
        return self
