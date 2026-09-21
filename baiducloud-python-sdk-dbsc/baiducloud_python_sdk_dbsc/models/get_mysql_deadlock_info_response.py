"""
Request entity for GetMysqlDeadlockInfoResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_dbsc.models.mysql_dead_lock_transaction import MysqlDeadLockTransaction


class GetMysqlDeadlockInfoResponse(BceResponse):
    """
    GetMysqlDeadlockInfoResponse
    """

    def __init__(self, meta_info=None, dead_lock_id=None, timestamp=None, raw_content=None, transaction_locks=None):
        """
        Initialize GetMysqlDeadlockInfoResponse response.

        :param meta_info: 死锁元信息
        :type meta_info: object (optional)

        :param dead_lock_id: 死锁ID
        :type dead_lock_id: str (optional)

        :param timestamp: 生成时间
        :type timestamp: datetime (optional)

        :param raw_content: 原始死锁信息
        :type raw_content: str (optional)

        :param transaction_locks: 死锁事务信息
        :type transaction_locks: List[MysqlDeadLockTransaction] (optional)
        """
        super().__init__()
        self.meta_info = meta_info
        self.dead_lock_id = dead_lock_id
        self.timestamp = timestamp
        self.raw_content = raw_content
        self.transaction_locks = transaction_locks

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.meta_info is not None:
            result['metaInfo'] = self.meta_info
        if self.dead_lock_id is not None:
            result['deadLockId'] = self.dead_lock_id
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.raw_content is not None:
            result['rawContent'] = self.raw_content
        if self.transaction_locks is not None:
            result['transactionLocks'] = [i.to_dict() for i in self.transaction_locks]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetMysqlDeadlockInfoResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('metaInfo') is not None:
            self.meta_info = m.get('metaInfo')
        if m.get('deadLockId') is not None:
            self.dead_lock_id = m.get('deadLockId')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('rawContent') is not None:
            self.raw_content = m.get('rawContent')
        if m.get('transactionLocks') is not None:
            self.transaction_locks = [MysqlDeadLockTransaction().from_dict(i) for i in m.get('transactionLocks')]
        return self
