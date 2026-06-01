"""
RequestConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RequestConfig(AbstractModel):
    """
    RequestConfig
    """

    def __init__(
        self,
        var_global=None,
        server_slow_request_threshold_seconds=None,
        db_slow_request_threshold_seconds=None,
        ok_http_status=None,
    ):
        """
        Initialize RequestConfig instance.

        :param var_global: 该配置是否来自全局默认配置，仅在应用配置中返回
        :type var_global: bool (optional)

        :param server_slow_request_threshold_seconds: 接口慢调用阈值，单位：秒
        :type server_slow_request_threshold_seconds: float (optional)

        :param db_slow_request_threshold_seconds: 数据库慢调用阈值，单位：秒
        :type db_slow_request_threshold_seconds: float (optional)

        :param ok_http_status: 用户自定义不被视为错误的HTTP状态码列表
        :type ok_http_status: List[int] (optional)
        """
        super().__init__()
        self.var_global = var_global
        self.server_slow_request_threshold_seconds = server_slow_request_threshold_seconds
        self.db_slow_request_threshold_seconds = db_slow_request_threshold_seconds
        self.ok_http_status = ok_http_status

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
        if self.var_global is not None:
            result['global'] = self.var_global
        if self.server_slow_request_threshold_seconds is not None:
            result['serverSlowRequestThresholdSeconds'] = self.server_slow_request_threshold_seconds
        if self.db_slow_request_threshold_seconds is not None:
            result['dbSlowRequestThresholdSeconds'] = self.db_slow_request_threshold_seconds
        if self.ok_http_status is not None:
            result['okHttpStatus'] = self.ok_http_status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RequestConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('global') is not None:
            self.var_global = m.get('global')
        if m.get('serverSlowRequestThresholdSeconds') is not None:
            self.server_slow_request_threshold_seconds = m.get('serverSlowRequestThresholdSeconds')
        if m.get('dbSlowRequestThresholdSeconds') is not None:
            self.db_slow_request_threshold_seconds = m.get('dbSlowRequestThresholdSeconds')
        if m.get('okHttpStatus') is not None:
            self.ok_http_status = m.get('okHttpStatus')
        return self
