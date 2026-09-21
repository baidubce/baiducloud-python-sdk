"""
PGSlowLogInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PGSlowLogInfo(AbstractModel):
    """
    PGSlowLogInfo
    """

    def __init__(
        self,
        product=None,
        app_id=None,
        app_name=None,
        app_short_id=None,
        cluster_id=None,
        node_id=None,
        uuid=None,
        pid=None,
        client_ip=None,
        current_db=None,
        current_user=None,
        duration=None,
        start=None,
        end=None,
        statement=None,
        fingerprint=None,
        fingerprint_md5=None,
    ):
        """
        Initialize PGSlowLogInfo instance.

        :param product: 产品类型
        :type product: str (optional)

        :param app_id: 实例ID
        :type app_id: str (optional)

        :param app_name: 实例名称
        :type app_name: str (optional)

        :param app_short_id: 实例短ID
        :type app_short_id: str (optional)

        :param cluster_id: 集群ID
        :type cluster_id: str (optional)

        :param node_id: 节点ID
        :type node_id: str (optional)

        :param uuid: 慢日志记录唯一标识
        :type uuid: str (optional)

        :param pid: 进程ID
        :type pid: int (optional)

        :param client_ip: 客户端IP
        :type client_ip: str (optional)

        :param current_db: 数据库名称
        :type current_db: str (optional)

        :param current_user: 用户名
        :type current_user: str (optional)

        :param duration: 执行时间（毫秒）
        :type duration: int (optional)

        :param start: 开始时间
        :type start: str (optional)

        :param end: 结束时间
        :type end: str (optional)

        :param statement: SQL语句
        :type statement: str (optional)

        :param fingerprint: SQL指纹
        :type fingerprint: str (optional)

        :param fingerprint_md5: SQL指纹的MD5值
        :type fingerprint_md5: str (optional)
        """
        super().__init__()
        self.product = product
        self.app_id = app_id
        self.app_name = app_name
        self.app_short_id = app_short_id
        self.cluster_id = cluster_id
        self.node_id = node_id
        self.uuid = uuid
        self.pid = pid
        self.client_ip = client_ip
        self.current_db = current_db
        self.current_user = current_user
        self.duration = duration
        self.start = start
        self.end = end
        self.statement = statement
        self.fingerprint = fingerprint
        self.fingerprint_md5 = fingerprint_md5

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
        if self.product is not None:
            result['product'] = self.product
        if self.app_id is not None:
            result['appID'] = self.app_id
        if self.app_name is not None:
            result['appName'] = self.app_name
        if self.app_short_id is not None:
            result['appShortID'] = self.app_short_id
        if self.cluster_id is not None:
            result['clusterID'] = self.cluster_id
        if self.node_id is not None:
            result['nodeID'] = self.node_id
        if self.uuid is not None:
            result['uuid'] = self.uuid
        if self.pid is not None:
            result['pid'] = self.pid
        if self.client_ip is not None:
            result['clientIP'] = self.client_ip
        if self.current_db is not None:
            result['currentDB'] = self.current_db
        if self.current_user is not None:
            result['currentUser'] = self.current_user
        if self.duration is not None:
            result['duration'] = self.duration
        if self.start is not None:
            result['start'] = self.start
        if self.end is not None:
            result['end'] = self.end
        if self.statement is not None:
            result['statement'] = self.statement
        if self.fingerprint is not None:
            result['fingerprint'] = self.fingerprint
        if self.fingerprint_md5 is not None:
            result['fingerprintMD5'] = self.fingerprint_md5
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PGSlowLogInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('appID') is not None:
            self.app_id = m.get('appID')
        if m.get('appName') is not None:
            self.app_name = m.get('appName')
        if m.get('appShortID') is not None:
            self.app_short_id = m.get('appShortID')
        if m.get('clusterID') is not None:
            self.cluster_id = m.get('clusterID')
        if m.get('nodeID') is not None:
            self.node_id = m.get('nodeID')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        if m.get('pid') is not None:
            self.pid = m.get('pid')
        if m.get('clientIP') is not None:
            self.client_ip = m.get('clientIP')
        if m.get('currentDB') is not None:
            self.current_db = m.get('currentDB')
        if m.get('currentUser') is not None:
            self.current_user = m.get('currentUser')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('start') is not None:
            self.start = m.get('start')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('statement') is not None:
            self.statement = m.get('statement')
        if m.get('fingerprint') is not None:
            self.fingerprint = m.get('fingerprint')
        if m.get('fingerprintMD5') is not None:
            self.fingerprint_md5 = m.get('fingerprintMD5')
        return self
