"""
MysqlDeadLockTransaction information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MysqlDeadLockTransaction(AbstractModel):
    """
    MysqlDeadLockTransaction
    """

    def __init__(
        self,
        database=None,
        heap_no=None,
        index=None,
        is_prediction=None,
        lock_mode=None,
        lock_type=None,
        page_no=None,
        record_lock_type=None,
        space_id=None,
        table=None,
        wait_hold=None,
        query=None,
        thread_id=None,
        trx_id=None,
        trx_seq=None,
        trx_time=None,
        user=None,
        victim=None,
    ):
        """
        Initialize MysqlDeadLockTransaction instance.

        :param database: 数据库名
        :type database: str (optional)

        :param heap_no: 堆号
        :type heap_no: int (optional)

        :param index: 索引名
        :type index: str (optional)

        :param is_prediction: 是否预测生成
        :type is_prediction: bool (optional)

        :param lock_mode: 锁模式
        :type lock_mode: str (optional)

        :param lock_type: 锁类型
        :type lock_type: str (optional)

        :param page_no: 页号
        :type page_no: int (optional)

        :param record_lock_type: 记录锁类型
        :type record_lock_type: str (optional)

        :param space_id: 空间ID
        :type space_id: int (optional)

        :param table: 表名
        :type table: str (optional)

        :param wait_hold: 等待/持有
        :type wait_hold: str (optional)

        :param query: 查询语句
        :type query: str (optional)

        :param thread_id: 线程ID
        :type thread_id: int (optional)

        :param trx_id: 事务ID
        :type trx_id: str (optional)

        :param trx_seq: 事务序号
        :type trx_seq: int (optional)

        :param trx_time: 事务时间
        :type trx_time: str (optional)

        :param user: 用户名
        :type user: str (optional)

        :param victim: 是否被Kill0-否1-是
        :type victim: int (optional)
        """
        super().__init__()
        self.database = database
        self.heap_no = heap_no
        self.index = index
        self.is_prediction = is_prediction
        self.lock_mode = lock_mode
        self.lock_type = lock_type
        self.page_no = page_no
        self.record_lock_type = record_lock_type
        self.space_id = space_id
        self.table = table
        self.wait_hold = wait_hold
        self.query = query
        self.thread_id = thread_id
        self.trx_id = trx_id
        self.trx_seq = trx_seq
        self.trx_time = trx_time
        self.user = user
        self.victim = victim

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
        if self.database is not None:
            result['database'] = self.database
        if self.heap_no is not None:
            result['heapNo'] = self.heap_no
        if self.index is not None:
            result['index'] = self.index
        if self.is_prediction is not None:
            result['isPrediction'] = self.is_prediction
        if self.lock_mode is not None:
            result['lockMode'] = self.lock_mode
        if self.lock_type is not None:
            result['lockType'] = self.lock_type
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.record_lock_type is not None:
            result['recordLockType'] = self.record_lock_type
        if self.space_id is not None:
            result['spaceId'] = self.space_id
        if self.table is not None:
            result['table'] = self.table
        if self.wait_hold is not None:
            result['waitHold'] = self.wait_hold
        if self.query is not None:
            result['query'] = self.query
        if self.thread_id is not None:
            result['threadID'] = self.thread_id
        if self.trx_id is not None:
            result['trxId'] = self.trx_id
        if self.trx_seq is not None:
            result['trxSeq'] = self.trx_seq
        if self.trx_time is not None:
            result['trxTime'] = self.trx_time
        if self.user is not None:
            result['user'] = self.user
        if self.victim is not None:
            result['victim'] = self.victim
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MysqlDeadLockTransaction

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('database') is not None:
            self.database = m.get('database')
        if m.get('heapNo') is not None:
            self.heap_no = m.get('heapNo')
        if m.get('index') is not None:
            self.index = m.get('index')
        if m.get('isPrediction') is not None:
            self.is_prediction = m.get('isPrediction')
        if m.get('lockMode') is not None:
            self.lock_mode = m.get('lockMode')
        if m.get('lockType') is not None:
            self.lock_type = m.get('lockType')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('recordLockType') is not None:
            self.record_lock_type = m.get('recordLockType')
        if m.get('spaceId') is not None:
            self.space_id = m.get('spaceId')
        if m.get('table') is not None:
            self.table = m.get('table')
        if m.get('waitHold') is not None:
            self.wait_hold = m.get('waitHold')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('threadID') is not None:
            self.thread_id = m.get('threadID')
        if m.get('trxId') is not None:
            self.trx_id = m.get('trxId')
        if m.get('trxSeq') is not None:
            self.trx_seq = m.get('trxSeq')
        if m.get('trxTime') is not None:
            self.trx_time = m.get('trxTime')
        if m.get('user') is not None:
            self.user = m.get('user')
        if m.get('victim') is not None:
            self.victim = m.get('victim')
        return self
