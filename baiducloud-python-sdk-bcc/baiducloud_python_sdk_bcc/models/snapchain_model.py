"""
SnapchainModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SnapchainModel(AbstractModel):
    """
    SnapchainModel
    """

    def __init__(
        self,
        status=None,
        instance_id=None,
        user_id=None,
        chain_size=None,
        chain_id=None,
        volume_id=None,
        manual_snap_count=None,
        auto_snap_count=None,
        volume_size=None,
        create_time=None,
    ):
        """
        Initialize SnapchainModel instance.

        :param status: 快照链状态
        :type status: str (optional)

        :param instance_id: 实例ID
        :type instance_id: str (optional)

        :param user_id: 用户ID
        :type user_id: str (optional)

        :param chain_size: 快照链大小
        :type chain_size: str (optional)

        :param chain_id: 快照链ID
        :type chain_id: str (optional)

        :param volume_id: 磁盘ID
        :type volume_id: str (optional)

        :param manual_snap_count: 手动快照数量
        :type manual_snap_count: int (optional)

        :param auto_snap_count: 自动快照数量
        :type auto_snap_count: int (optional)

        :param volume_size: 磁盘大小
        :type volume_size: int (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)
        """
        super().__init__()
        self.status = status
        self.instance_id = instance_id
        self.user_id = user_id
        self.chain_size = chain_size
        self.chain_id = chain_id
        self.volume_id = volume_id
        self.manual_snap_count = manual_snap_count
        self.auto_snap_count = auto_snap_count
        self.volume_size = volume_size
        self.create_time = create_time

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
        if self.status is not None:
            result['status'] = self.status
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.chain_size is not None:
            result['chainSize'] = self.chain_size
        if self.chain_id is not None:
            result['chainId'] = self.chain_id
        if self.volume_id is not None:
            result['volumeId'] = self.volume_id
        if self.manual_snap_count is not None:
            result['manualSnapCount'] = self.manual_snap_count
        if self.auto_snap_count is not None:
            result['autoSnapCount'] = self.auto_snap_count
        if self.volume_size is not None:
            result['volumeSize'] = self.volume_size
        if self.create_time is not None:
            result['createTime'] = self.create_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SnapchainModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('chainSize') is not None:
            self.chain_size = m.get('chainSize')
        if m.get('chainId') is not None:
            self.chain_id = m.get('chainId')
        if m.get('volumeId') is not None:
            self.volume_id = m.get('volumeId')
        if m.get('manualSnapCount') is not None:
            self.manual_snap_count = m.get('manualSnapCount')
        if m.get('autoSnapCount') is not None:
            self.auto_snap_count = m.get('autoSnapCount')
        if m.get('volumeSize') is not None:
            self.volume_size = m.get('volumeSize')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        return self
