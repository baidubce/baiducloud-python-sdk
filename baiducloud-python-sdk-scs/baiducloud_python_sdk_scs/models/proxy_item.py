"""
ProxyItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ProxyItem(AbstractModel):
    """
    ProxyItem
    """

    def __init__(self, uuid=None, node_show_id=None, availability_zone=None, node_id=None):
        """
        Initialize ProxyItem instance.

        :param uuid: 代理节点UUID
        :type uuid: str (optional)

        :param node_show_id: 代理节点展示ID
        :type node_show_id: str (optional)

        :param availability_zone: 可用区
        :type availability_zone: str (optional)

        :param node_id: api返回参数，同 nodeShowId
        :type node_id: str (optional)
        """
        super().__init__()
        self.uuid = uuid
        self.node_show_id = node_show_id
        self.availability_zone = availability_zone
        self.node_id = node_id

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
        if self.uuid is not None:
            result['uuid'] = self.uuid
        if self.node_show_id is not None:
            result['nodeShowId'] = self.node_show_id
        if self.availability_zone is not None:
            result['availabilityZone'] = self.availability_zone
        if self.node_id is not None:
            result['nodeId'] = self.node_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ProxyItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        if m.get('nodeShowId') is not None:
            self.node_show_id = m.get('nodeShowId')
        if m.get('availabilityZone') is not None:
            self.availability_zone = m.get('availabilityZone')
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')
        return self
