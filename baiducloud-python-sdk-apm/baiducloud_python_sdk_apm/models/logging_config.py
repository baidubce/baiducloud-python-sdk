"""
LoggingConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LoggingConfig(AbstractModel):
    """
    LoggingConfig
    """

    def __init__(
        self,
        enabled=None,
        region=None,
        project=None,
        log_store_name=None,
        trace_id_index=None,
        trace_id_key=None,
        span_id_index=None,
        span_id_key=None,
    ):
        """
        Initialize LoggingConfig instance.

        :param enabled: 是否开启日志关联
        :type enabled: bool (optional)

        :param region: 地域
        :type region: str (optional)

        :param project: 日志集所属project
        :type project: str (optional)

        :param log_store_name: 日志集名称
        :type log_store_name: str (optional)

        :param trace_id_index: 在日志中搜索traceId的方式，可选项：`FIELD` - 指定字段搜索（默认），`FULLTEXT` - 全文检索
        :type trace_id_index: str (optional)

        :param trace_id_key: 当traceIdIndex=FIELD时搜索的key，默认值：trace_id
        :type trace_id_key: str (optional)

        :param span_id_index: 在日志中搜索spanId的方式，可选项：`FIELD` - 指定字段搜索（默认），`FULLTEXT` - 全文检索
        :type span_id_index: str (optional)

        :param span_id_key: 当spanIdIndex=FIELD时搜索的key，默认值：span_id
        :type span_id_key: str (optional)
        """
        super().__init__()
        self.enabled = enabled
        self.region = region
        self.project = project
        self.log_store_name = log_store_name
        self.trace_id_index = trace_id_index
        self.trace_id_key = trace_id_key
        self.span_id_index = span_id_index
        self.span_id_key = span_id_key

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
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.region is not None:
            result['region'] = self.region
        if self.project is not None:
            result['project'] = self.project
        if self.log_store_name is not None:
            result['logStoreName'] = self.log_store_name
        if self.trace_id_index is not None:
            result['traceIdIndex'] = self.trace_id_index
        if self.trace_id_key is not None:
            result['traceIdKey'] = self.trace_id_key
        if self.span_id_index is not None:
            result['spanIdIndex'] = self.span_id_index
        if self.span_id_key is not None:
            result['spanIdKey'] = self.span_id_key
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LoggingConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        if m.get('traceIdIndex') is not None:
            self.trace_id_index = m.get('traceIdIndex')
        if m.get('traceIdKey') is not None:
            self.trace_id_key = m.get('traceIdKey')
        if m.get('spanIdIndex') is not None:
            self.span_id_index = m.get('spanIdIndex')
        if m.get('spanIdKey') is not None:
            self.span_id_key = m.get('spanIdKey')
        return self
