"""
Request entity for UpdateIsManagedV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateIsManagedV2Request(AbstractModel):
    """
    Request entity for UpdateIsManagedV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, group_id, update_is_managed, add_managed_node_ids, del_managed_node_ids):
        """
        Initialize UpdateIsManagedV2Request request entity.

        :param group_id: group_id parameter
        :type group_id: str (required)

        :param update_is_managed: update_is_managed parameter
        :type update_is_managed: str (required)

        :param add_managed_node_ids: 新增托管的节点列表
        :type add_managed_node_ids: List[str] (required)

        :param del_managed_node_ids: 取消托管的节点列表
        :type del_managed_node_ids: List[str] (required)
        """
        super().__init__()
        self.group_id = group_id
        self.update_is_managed = update_is_managed
        self.add_managed_node_ids = add_managed_node_ids
        self.del_managed_node_ids = del_managed_node_ids

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
        if self.add_managed_node_ids is not None:
            result['addManagedNodeIds'] = self.add_managed_node_ids
        if self.del_managed_node_ids is not None:
            result['delManagedNodeIds'] = self.del_managed_node_ids
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateIsManagedV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('updateIsManaged') is not None:
            self.update_is_managed = m.get('updateIsManaged')
        if m.get('addManagedNodeIds') is not None:
            self.add_managed_node_ids = m.get('addManagedNodeIds')
        if m.get('delManagedNodeIds') is not None:
            self.del_managed_node_ids = m.get('delManagedNodeIds')
        return self
