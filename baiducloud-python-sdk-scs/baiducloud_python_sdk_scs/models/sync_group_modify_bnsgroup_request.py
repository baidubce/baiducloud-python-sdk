"""
Request entity for SyncGroupModifyBnsgroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SyncGroupModifyBnsgroupRequest(AbstractModel):
    """
    Request entity for SyncGroupModifyBnsgroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, group_id, bns_group=None):
        """
        Initialize SyncGroupModifyBnsgroupRequest request entity.

        :param group_id: group_id parameter
        :type group_id: str (required)

        :param bns_group: BNS Group
        :type bns_group: str (optional)
        """
        super().__init__()
        self.group_id = group_id
        self.bns_group = bns_group

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
        if self.bns_group is not None:
            result['bnsGroup'] = self.bns_group
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SyncGroupModifyBnsgroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('bnsGroup') is not None:
            self.bns_group = m.get('bnsGroup')
        return self
