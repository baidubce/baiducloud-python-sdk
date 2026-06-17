"""
SrcConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bls.models.process_config import ProcessConfig


class SrcConfig(AbstractModel):
    """
    SrcConfig
    """

    def __init__(
        self,
        src_type=None,
        log_type=None,
        src_dir=None,
        matched_pattern=None,
        ignore_pattern=None,
        time_format=None,
        ttl=None,
        use_multiline=None,
        multiline_regex=None,
        recursive_dir=None,
        process_type=None,
        process_config=None,
        log_time=None,
        timestamp_key=None,
        date_format=None,
        filter_expr=None,
        addition_config=None,
        meta_env=None,
        meta_label=None,
        meta_container=None,
        meta_to_fields=None,
        harvester_limit=None,
    ):
        """
        Initialize SrcConfig instance.

        :param src_type: 普通主机类型填host，容器类型填container
        :type src_type: str (optional)

        :param log_type: 容器场景日志类型，可选值为stdout、internal
        :type log_type: str (optional)

        :param src_dir: src_dir attribute
        :type src_dir: str (optional)

        :param matched_pattern: matched_pattern attribute
        :type matched_pattern: str (optional)

        :param ignore_pattern: 忽略的源日志文件
        :type ignore_pattern: str (optional)

        :param time_format: 用于投BOS时，原文件路径日期解析。BLS场景通常不需要填写
        :type time_format: str (optional)

        :param ttl: 有效日志文件时间范围
        :type ttl: int (optional)

        :param use_multiline: 是否启用多行模式
        :type use_multiline: bool (optional)

        :param multiline_regex: 多行模式首行正则表达式，useMultiline=true 时必填
        :type multiline_regex: str (optional)

        :param recursive_dir: 是否启动目录递归匹配，容器采集目前没有目录递归
        :type recursive_dir: bool (optional)

        :param process_type: process_type attribute
        :type process_type: str (optional)

        :param process_config: process_config attribute
        :type process_config: ProcessConfig (optional)

        :param log_time: 日志时间，可选system、logTime，分别表示使用系统时间和使用日志时间
        :type log_time: str (optional)

        :param timestamp_key: 指定解析后的字段作为日志时间
        :type timestamp_key: str (optional)

        :param date_format: date_format attribute
        :type date_format: str (optional)

        :param filter_expr: 日志匹配表达式，符合规则的日志将被采集
        :type filter_expr: str (optional)

        :param addition_config: 追加采集器参数
        :type addition_config: Dict[str, object] (optional)

        :param meta_env: 采集环境变量的列表
        :type meta_env: List[str] (optional)

        :param meta_label: 采集自定义Label列表
        :type meta_label: List[str] (optional)

        :param meta_container: 采集容器固定元数据
        :type meta_container: List[str] (optional)

        :param meta_to_fields: 是否将采集到的元数据写入日志字段
        :type meta_to_fields: bool (optional)

        :param harvester_limit: harvester_limit attribute
        :type harvester_limit: int (optional)
        """
        super().__init__()
        self.src_type = src_type
        self.log_type = log_type
        self.src_dir = src_dir
        self.matched_pattern = matched_pattern
        self.ignore_pattern = ignore_pattern
        self.time_format = time_format
        self.ttl = ttl
        self.use_multiline = use_multiline
        self.multiline_regex = multiline_regex
        self.recursive_dir = recursive_dir
        self.process_type = process_type
        self.process_config = process_config
        self.log_time = log_time
        self.timestamp_key = timestamp_key
        self.date_format = date_format
        self.filter_expr = filter_expr
        self.addition_config = addition_config
        self.meta_env = meta_env
        self.meta_label = meta_label
        self.meta_container = meta_container
        self.meta_to_fields = meta_to_fields
        self.harvester_limit = harvester_limit

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
        if self.src_type is not None:
            result['srcType'] = self.src_type
        if self.log_type is not None:
            result['logType'] = self.log_type
        if self.src_dir is not None:
            result['srcDir'] = self.src_dir
        if self.matched_pattern is not None:
            result['matchedPattern'] = self.matched_pattern
        if self.ignore_pattern is not None:
            result['ignorePattern'] = self.ignore_pattern
        if self.time_format is not None:
            result['timeFormat'] = self.time_format
        if self.ttl is not None:
            result['ttl'] = self.ttl
        if self.use_multiline is not None:
            result['useMultiline'] = self.use_multiline
        if self.multiline_regex is not None:
            result['multilineRegex'] = self.multiline_regex
        if self.recursive_dir is not None:
            result['recursiveDir'] = self.recursive_dir
        if self.process_type is not None:
            result['processType'] = self.process_type
        if self.process_config is not None:
            result['processConfig'] = self.process_config.to_dict()
        if self.log_time is not None:
            result['logTime'] = self.log_time
        if self.timestamp_key is not None:
            result['timestampKey'] = self.timestamp_key
        if self.date_format is not None:
            result['dateFormat'] = self.date_format
        if self.filter_expr is not None:
            result['filterExpr'] = self.filter_expr
        if self.addition_config is not None:
            result['additionConfig'] = self.addition_config
        if self.meta_env is not None:
            result['metaEnv'] = self.meta_env
        if self.meta_label is not None:
            result['metaLabel'] = self.meta_label
        if self.meta_container is not None:
            result['metaContainer'] = self.meta_container
        if self.meta_to_fields is not None:
            result['metaToFields'] = self.meta_to_fields
        if self.harvester_limit is not None:
            result['HarvesterLimit'] = self.harvester_limit
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SrcConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('srcType') is not None:
            self.src_type = m.get('srcType')
        if m.get('logType') is not None:
            self.log_type = m.get('logType')
        if m.get('srcDir') is not None:
            self.src_dir = m.get('srcDir')
        if m.get('matchedPattern') is not None:
            self.matched_pattern = m.get('matchedPattern')
        if m.get('ignorePattern') is not None:
            self.ignore_pattern = m.get('ignorePattern')
        if m.get('timeFormat') is not None:
            self.time_format = m.get('timeFormat')
        if m.get('ttl') is not None:
            self.ttl = m.get('ttl')
        if m.get('useMultiline') is not None:
            self.use_multiline = m.get('useMultiline')
        if m.get('multilineRegex') is not None:
            self.multiline_regex = m.get('multilineRegex')
        if m.get('recursiveDir') is not None:
            self.recursive_dir = m.get('recursiveDir')
        if m.get('processType') is not None:
            self.process_type = m.get('processType')
        if m.get('processConfig') is not None:
            self.process_config = ProcessConfig().from_dict(m.get('processConfig'))
        if m.get('logTime') is not None:
            self.log_time = m.get('logTime')
        if m.get('timestampKey') is not None:
            self.timestamp_key = m.get('timestampKey')
        if m.get('dateFormat') is not None:
            self.date_format = m.get('dateFormat')
        if m.get('filterExpr') is not None:
            self.filter_expr = m.get('filterExpr')
        if m.get('additionConfig') is not None:
            self.addition_config = m.get('additionConfig')
        if m.get('metaEnv') is not None:
            self.meta_env = m.get('metaEnv')
        if m.get('metaLabel') is not None:
            self.meta_label = m.get('metaLabel')
        if m.get('metaContainer') is not None:
            self.meta_container = m.get('metaContainer')
        if m.get('metaToFields') is not None:
            self.meta_to_fields = m.get('metaToFields')
        if m.get('HarvesterLimit') is not None:
            self.harvester_limit = m.get('HarvesterLimit')
        return self
