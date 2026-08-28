"""
SmartStructKVRelation information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SmartStructKVRelation(AbstractModel):
    """
    SmartStructKVRelation
    """

    def __init__(self, root_node=None, leaf_nodes=None):
        """
        Initialize SmartStructKVRelation instance.

        :param root_node: 根节点的 object_id，即 k-v 区的 key
        :type root_node: int (optional)

        :param leaf_nodes: 由根节点指向叶子节点的 object_id，及 k-v 区的 values
        :type leaf_nodes: List[int] (optional)
        """
        super().__init__()
        self.root_node = root_node
        self.leaf_nodes = leaf_nodes

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
        if self.root_node is not None:
            result['root_node'] = self.root_node
        if self.leaf_nodes is not None:
            result['leaf_nodes'] = self.leaf_nodes
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SmartStructKVRelation

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('root_node') is not None:
            self.root_node = m.get('root_node')
        if m.get('leaf_nodes') is not None:
            self.leaf_nodes = m.get('leaf_nodes')
        return self
