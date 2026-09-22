"""
SwitchMasterSlaveShard information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SwitchMasterSlaveShard(AbstractModel):
    """
    SwitchMasterSlaveShard
    """

    def __init__(self, hash_name=None, node_show_id=None):
        """
        Initialize SwitchMasterSlaveShard instance.

        :param hash_name: 指定要切换的分片。可从实例详情接口RedisList字段中获取分片信息。
        :type hash_name: str (optional)

        :param node_show_id: 指定该分片中要切换为主的节点ID。可从实例详情接口RedisList字段中获取分片中节点ID的信息。
        :type node_show_id: str (optional)
        """
        super().__init__()
        self.hash_name = hash_name
        self.node_show_id = node_show_id

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
        if self.hash_name is not None:
            result['hashName'] = self.hash_name
        if self.node_show_id is not None:
            result['nodeShowId'] = self.node_show_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SwitchMasterSlaveShard

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('hashName') is not None:
            self.hash_name = m.get('hashName')
        if m.get('nodeShowId') is not None:
            self.node_show_id = m.get('nodeShowId')
        return self
