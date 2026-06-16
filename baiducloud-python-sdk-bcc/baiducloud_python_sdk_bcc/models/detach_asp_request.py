"""
Request entity for DetachAspRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DetachAspRequest(AbstractModel):
    """
    Request entity for DetachAspRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, asp_id, volume_ids, delete_auto_snapshot=None):
        """
        Initialize DetachAspRequest request entity.

        :param asp_id: asp_id parameter
        :type asp_id: str (required)

        :param volume_ids: 需要解绑的磁盘ID列表
        :type volume_ids: List[str] (required)

        :param delete_auto_snapshot: 自动快照随磁盘删除，初始值为false，显式赋值后所有相关磁盘对应属性会被新值替换
        :type delete_auto_snapshot: bool (optional)
        """
        super().__init__()
        self.asp_id = asp_id
        self.volume_ids = volume_ids
        self.delete_auto_snapshot = delete_auto_snapshot

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
        if self.volume_ids is not None:
            result['volumeIds'] = self.volume_ids
        if self.delete_auto_snapshot is not None:
            result['deleteAutoSnapshot'] = self.delete_auto_snapshot
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DetachAspRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('aspId') is not None:
            self.asp_id = m.get('aspId')
        if m.get('volumeIds') is not None:
            self.volume_ids = m.get('volumeIds')
        if m.get('deleteAutoSnapshot') is not None:
            self.delete_auto_snapshot = m.get('deleteAutoSnapshot')
        return self
