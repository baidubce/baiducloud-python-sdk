"""
APIPGSlowLogTemplateItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class APIPGSlowLogTemplateItem(AbstractModel):
    """
    APIPGSlowLogTemplateItem
    """

    def __init__(
        self,
        fingerprint_md5=None,
        fingerprint=None,
        db_name=None,
        execute_times=None,
        duration_sum=None,
        duration_max=None,
        duration_min=None,
        duration_avg=None,
    ):
        """
        Initialize APIPGSlowLogTemplateItem instance.

        :param fingerprint_md5: SQL指纹的MD5值
        :type fingerprint_md5: str (optional)

        :param fingerprint: SQL指纹
        :type fingerprint: str (optional)

        :param db_name: 数据库名称
        :type db_name: str (optional)

        :param execute_times: 执行次数
        :type execute_times: int (optional)

        :param duration_sum: 总执行时间（毫秒）
        :type duration_sum: int (optional)

        :param duration_max: 最大执行时间（毫秒）
        :type duration_max: int (optional)

        :param duration_min: 最小执行时间（毫秒）
        :type duration_min: int (optional)

        :param duration_avg: 平均执行时间（毫秒）
        :type duration_avg: int (optional)
        """
        super().__init__()
        self.fingerprint_md5 = fingerprint_md5
        self.fingerprint = fingerprint
        self.db_name = db_name
        self.execute_times = execute_times
        self.duration_sum = duration_sum
        self.duration_max = duration_max
        self.duration_min = duration_min
        self.duration_avg = duration_avg

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
            result['fingerprintMD5'] = self.fingerprint_md5
        if self.fingerprint is not None:
            result['fingerprint'] = self.fingerprint
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
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: APIPGSlowLogTemplateItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('fingerprintMD5') is not None:
            self.fingerprint_md5 = m.get('fingerprintMD5')
        if m.get('fingerprint') is not None:
            self.fingerprint = m.get('fingerprint')
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
        return self
