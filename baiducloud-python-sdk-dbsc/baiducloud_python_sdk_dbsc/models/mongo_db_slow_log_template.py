"""
MongoDBSlowLogTemplate information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MongoDBSlowLogTemplate(AbstractModel):
    """
    MongoDBSlowLogTemplate
    """

    def __init__(
        self,
        fingerprint_md5=None,
        fingerprint=None,
        namespace=None,
        execute_times=None,
        duration_sum=None,
        duration_max=None,
        duration_min=None,
        duration_avg=None,
        key_scan_rows_sum=None,
        key_scan_rows_max=None,
        key_scan_rows_min=None,
        key_scan_rows_avg=None,
        scan_rows_sum=None,
        scan_rows_max=None,
        scan_rows_min=None,
        scan_rows_avg=None,
        return_rows_sum=None,
        return_rows_max=None,
        return_rows_min=None,
        return_rows_avg=None,
    ):
        """
        Initialize MongoDBSlowLogTemplate instance.

        :param fingerprint_md5: 命令唯一标识
        :type fingerprint_md5: str (optional)

        :param fingerprint: 归一化SQL
        :type fingerprint: str (optional)

        :param namespace: 命名空间
        :type namespace: str (optional)

        :param execute_times: 执行次数
        :type execute_times: str (optional)

        :param duration_sum: 命令执行总时间，单位毫秒
        :type duration_sum: int (optional)

        :param duration_max: 命令执行最大时间，单位毫秒
        :type duration_max: int (optional)

        :param duration_min: 命令执行最小时间，单位毫秒
        :type duration_min: int (optional)

        :param duration_avg: 命令执行平均时间，单位毫秒
        :type duration_avg: int (optional)

        :param key_scan_rows_sum: 命令索引扫描总行数
        :type key_scan_rows_sum: int (optional)

        :param key_scan_rows_max: 命令索引扫描总大行数
        :type key_scan_rows_max: int (optional)

        :param key_scan_rows_min: 命令索引扫描总小行数
        :type key_scan_rows_min: int (optional)

        :param key_scan_rows_avg: 命令索引扫描平均行数
        :type key_scan_rows_avg: int (optional)

        :param scan_rows_sum: 命令扫描平均行数
        :type scan_rows_sum: int (optional)

        :param scan_rows_max: 命令扫描最大行数
        :type scan_rows_max: int (optional)

        :param scan_rows_min: 命令扫描最小行数
        :type scan_rows_min: int (optional)

        :param scan_rows_avg: 命令扫描平均行数
        :type scan_rows_avg: int (optional)

        :param return_rows_sum: 命令返回总行数
        :type return_rows_sum: int (optional)

        :param return_rows_max: 命令返回最大行数
        :type return_rows_max: int (optional)

        :param return_rows_min: 命令返回最小行数
        :type return_rows_min: int (optional)

        :param return_rows_avg: 命令返回平均行数
        :type return_rows_avg: int (optional)
        """
        super().__init__()
        self.fingerprint_md5 = fingerprint_md5
        self.fingerprint = fingerprint
        self.namespace = namespace
        self.execute_times = execute_times
        self.duration_sum = duration_sum
        self.duration_max = duration_max
        self.duration_min = duration_min
        self.duration_avg = duration_avg
        self.key_scan_rows_sum = key_scan_rows_sum
        self.key_scan_rows_max = key_scan_rows_max
        self.key_scan_rows_min = key_scan_rows_min
        self.key_scan_rows_avg = key_scan_rows_avg
        self.scan_rows_sum = scan_rows_sum
        self.scan_rows_max = scan_rows_max
        self.scan_rows_min = scan_rows_min
        self.scan_rows_avg = scan_rows_avg
        self.return_rows_sum = return_rows_sum
        self.return_rows_max = return_rows_max
        self.return_rows_min = return_rows_min
        self.return_rows_avg = return_rows_avg

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
        if self.fingerprint_md5 is not None:
            result['fingerprintMd5'] = self.fingerprint_md5
        if self.fingerprint is not None:
            result['fingerprint'] = self.fingerprint
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.execute_times is not None:
            result['executeTimes'] = self.execute_times
        if self.duration_sum is not None:
            result['durationSum'] = self.duration_sum
        if self.duration_max is not None:
            result['durationMax'] = self.duration_max
        if self.duration_min is not None:
            result['durationMin'] = self.duration_min
        if self.duration_avg is not None:
            result['durationAvg'] = self.duration_avg
        if self.key_scan_rows_sum is not None:
            result['keyScanRowsSum'] = self.key_scan_rows_sum
        if self.key_scan_rows_max is not None:
            result['keyScanRowsMax'] = self.key_scan_rows_max
        if self.key_scan_rows_min is not None:
            result['keyScanRowsMin'] = self.key_scan_rows_min
        if self.key_scan_rows_avg is not None:
            result['keyScanRowsAvg'] = self.key_scan_rows_avg
        if self.scan_rows_sum is not None:
            result['scanRowsSum'] = self.scan_rows_sum
        if self.scan_rows_max is not None:
            result['scanRowsMax'] = self.scan_rows_max
        if self.scan_rows_min is not None:
            result['scanRowsMin'] = self.scan_rows_min
        if self.scan_rows_avg is not None:
            result['scanRowsAvg'] = self.scan_rows_avg
        if self.return_rows_sum is not None:
            result['returnRowsSum'] = self.return_rows_sum
        if self.return_rows_max is not None:
            result['returnRowsMax'] = self.return_rows_max
        if self.return_rows_min is not None:
            result['returnRowsMin'] = self.return_rows_min
        if self.return_rows_avg is not None:
            result['returnRowsAvg'] = self.return_rows_avg
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MongoDBSlowLogTemplate

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('fingerprintMd5') is not None:
            self.fingerprint_md5 = m.get('fingerprintMd5')
        if m.get('fingerprint') is not None:
            self.fingerprint = m.get('fingerprint')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('executeTimes') is not None:
            self.execute_times = m.get('executeTimes')
        if m.get('durationSum') is not None:
            self.duration_sum = m.get('durationSum')
        if m.get('durationMax') is not None:
            self.duration_max = m.get('durationMax')
        if m.get('durationMin') is not None:
            self.duration_min = m.get('durationMin')
        if m.get('durationAvg') is not None:
            self.duration_avg = m.get('durationAvg')
        if m.get('keyScanRowsSum') is not None:
            self.key_scan_rows_sum = m.get('keyScanRowsSum')
        if m.get('keyScanRowsMax') is not None:
            self.key_scan_rows_max = m.get('keyScanRowsMax')
        if m.get('keyScanRowsMin') is not None:
            self.key_scan_rows_min = m.get('keyScanRowsMin')
        if m.get('keyScanRowsAvg') is not None:
            self.key_scan_rows_avg = m.get('keyScanRowsAvg')
        if m.get('scanRowsSum') is not None:
            self.scan_rows_sum = m.get('scanRowsSum')
        if m.get('scanRowsMax') is not None:
            self.scan_rows_max = m.get('scanRowsMax')
        if m.get('scanRowsMin') is not None:
            self.scan_rows_min = m.get('scanRowsMin')
        if m.get('scanRowsAvg') is not None:
            self.scan_rows_avg = m.get('scanRowsAvg')
        if m.get('returnRowsSum') is not None:
            self.return_rows_sum = m.get('returnRowsSum')
        if m.get('returnRowsMax') is not None:
            self.return_rows_max = m.get('returnRowsMax')
        if m.get('returnRowsMin') is not None:
            self.return_rows_min = m.get('returnRowsMin')
        if m.get('returnRowsAvg') is not None:
            self.return_rows_avg = m.get('returnRowsAvg')
        return self
