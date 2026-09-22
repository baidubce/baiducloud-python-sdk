"""
SyncStatusItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SyncStatusItem(AbstractModel):
    """
    SyncStatusItem
    """

    def __init__(self, member_id=None, status=None):
        """
        Initialize SyncStatusItem instance.

        :param member_id: 成员集群ID。
        :type member_id: str (optional)

        :param status: 同步状态。normal为正常，其他为异常。
        :type status: str (optional)
        """
        super().__init__()
        self.member_id = member_id
        self.status = status

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
        if self.member_id is not None:
            result['memberId'] = self.member_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SyncStatusItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('memberId') is not None:
            self.member_id = m.get('memberId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
