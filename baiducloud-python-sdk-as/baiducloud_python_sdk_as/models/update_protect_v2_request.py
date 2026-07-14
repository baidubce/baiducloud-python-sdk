"""
Request entity for UpdateProtectV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateProtectV2Request(AbstractModel):
    """
    Request entity for UpdateProtectV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, group_id, update_protect, nodes, is_protected):
        """
        Initialize UpdateProtectV2Request request entity.

        :param group_id: group_id parameter
        :type group_id: str (required)

        :param update_protect: update_protect parameter
        :type update_protect: str (required)

        :param nodes: 待移入实例短id列表
        :type nodes: List[str] (required)

        :param is_protected: 是否将nodes中节点设置为保护节点
        :type is_protected: bool (required)
        """
        super().__init__()
        self.group_id = group_id
        self.update_protect = update_protect
        self.nodes = nodes
        self.is_protected = is_protected

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
        if self.is_protected is not None:
            result['isProtected'] = self.is_protected
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateProtectV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('updateProtect') is not None:
            self.update_protect = m.get('updateProtect')
        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')
        if m.get('isProtected') is not None:
            self.is_protected = m.get('isProtected')
        return self
