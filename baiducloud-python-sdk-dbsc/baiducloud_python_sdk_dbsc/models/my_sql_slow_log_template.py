"""
MySQLSlowLogTemplate information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MySQLSlowLogTemplate(AbstractModel):
    """
    MySQLSlowLogTemplate
    """

    def __init__(
        self,
        fringerprint=None,
        fringerprint_md5=None,
        db_name=None,
        execute_times=None,
        duration_sum=None,
        duration_max=None,
        duration_min=None,
        duration_avg=None,
        lock_time_sum=None,
        lock_time_max=None,
        lock_time_min=None,
        lock_time_avg=None,
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
        Initialize MySQLSlowLogTemplate instance.

        :param fringerprint: 归一化SQL
        :type fringerprint: str (optional)

        :param fringerprint_md5: 归一化SQL的MD5值
        :type fringerprint_md5: str (optional)

        :param db_name: 数据库名称
        :type db_name: str (optional)

        :param execute_times: 执行次数
        :type execute_times: int (optional)

        :param duration_sum: 总执行时间，单位毫秒
        :type duration_sum: int (optional)

        :param duration_max: 最大执行时间，单位毫秒
        :type duration_max: int (optional)

        :param duration_min: 最小执行时间，单位毫秒
        :type duration_min: int (optional)

        :param duration_avg: 平均执行时间，单位毫秒
        :type duration_avg: int (optional)

        :param lock_time_sum: 总锁时间，单位毫秒
        :type lock_time_sum: int (optional)

        :param lock_time_max: 最大锁时间，单位毫秒
        :type lock_time_max: int (optional)

        :param lock_time_min: 最小锁时间，单位毫秒
        :type lock_time_min: int (optional)

        :param lock_time_avg: 平均锁时间，单位毫秒
        :type lock_time_avg: int (optional)

        :param scan_rows_sum: 总扫描行数
        :type scan_rows_sum: int (optional)

        :param scan_rows_max: 最大扫描行数
        :type scan_rows_max: int (optional)

        :param scan_rows_min: 最小扫描行数
        :type scan_rows_min: int (optional)

        :param scan_rows_avg: 平均扫描行数
        :type scan_rows_avg: int (optional)

        :param return_rows_sum: 总返回行数
        :type return_rows_sum: int (optional)

        :param return_rows_max: 最大返回行数
        :type return_rows_max: int (optional)

        :param return_rows_min: 最小返回行数
        :type return_rows_min: int (optional)

        :param return_rows_avg: 平均返回行数
        :type return_rows_avg: int (optional)
        """
        super().__init__()
        self.fringerprint = fringerprint
        self.fringerprint_md5 = fringerprint_md5
        self.db_name = db_name
        self.execute_times = execute_times
        self.duration_sum = duration_sum
        self.duration_max = duration_max
        self.duration_min = duration_min
        self.duration_avg = duration_avg
        self.lock_time_sum = lock_time_sum
        self.lock_time_max = lock_time_max
        self.lock_time_min = lock_time_min
        self.lock_time_avg = lock_time_avg
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
        if self.fringerprint is not None:
            result['fringerprint'] = self.fringerprint
        if self.fringerprint_md5 is not None:
            result['fringerprintMD5'] = self.fringerprint_md5
        if self.db_name is not None:
            result['dbName'] = self.db_name
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
        if self.lock_time_sum is not None:
            result['lockTimeSum'] = self.lock_time_sum
        if self.lock_time_max is not None:
            result['lockTimeMax'] = self.lock_time_max
        if self.lock_time_min is not None:
            result['lockTimeMin'] = self.lock_time_min
        if self.lock_time_avg is not None:
            result['lockTimeAvg'] = self.lock_time_avg
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
        :rtype: MySQLSlowLogTemplate

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('fringerprint') is not None:
            self.fringerprint = m.get('fringerprint')
        if m.get('fringerprintMD5') is not None:
            self.fringerprint_md5 = m.get('fringerprintMD5')
        if m.get('dbName') is not None:
            self.db_name = m.get('dbName')
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
        if m.get('lockTimeSum') is not None:
            self.lock_time_sum = m.get('lockTimeSum')
        if m.get('lockTimeMax') is not None:
            self.lock_time_max = m.get('lockTimeMax')
        if m.get('lockTimeMin') is not None:
            self.lock_time_min = m.get('lockTimeMin')
        if m.get('lockTimeAvg') is not None:
            self.lock_time_avg = m.get('lockTimeAvg')
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
