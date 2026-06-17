"""
DestConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DestConfig(AbstractModel):
    """
    DestConfig
    """

    def __init__(
        self,
        bos_path=None,
        partition_format_ts=None,
        partition_format_log_stream=None,
        max_object_size=None,
        compress_type=None,
        deliver_interval=None,
        storage_format=None,
        csv_headline=None,
        csv_delimiter=None,
        csv_quote=None,
        null_identifier=None,
        selected_column_name=None,
        selected_column_type=None,
        fields_name=None,
        fields_type=None,
        shipper_type=None,
        kafka_config=None,
        dest_type=None,
        log_store=None,
        rate_limit=None,
        client_count=None,
    ):
        """
        Initialize DestConfig instance.

        :param bos_path: BOSPath为Bucket加用户自定义路径组成，最长256个字符
        :type bos_path: str (optional)

        :param partition_format_ts: 分区格式，如%Y/%m/%d/%H/%M/，仅支持到分钟级别，可自定义，可为空，默认为%Y/%m/%d/%H/%M/
        :type partition_format_ts: str (optional)

        :param partition_format_log_stream: 是否使用logstream作为partition层级，默认false
        :type partition_format_log_stream: bool (optional)

        :param max_object_size: 最大对象大小，单位MB，范围为1 - 5*1024*1024（5TB），默认64
        :type max_object_size: int (optional)

        :param compress_type: 压缩类型，可选参数：snappy/gzip/bzip2/lzop和不压缩（none），默认不压缩
        :type compress_type: str (optional)

        :param deliver_interval: 投递间隔，单位分钟，限制范围为5-60的整数，默认5
        :type deliver_interval: int (optional)

        :param storage_format: 存储格式，可选参数： parquet, json, csv，默认json
        :type storage_format: str (optional)

        :param csv_headline: csv时是否投递字段名称，默认false，不投递
        :type csv_headline: bool (optional)

        :param csv_delimiter: csv时的分隔符，可选：逗号（，），空格（ ）、竖线（
        :type csv_delimiter: str (optional)

        :param csv_quote: csv时的引用符，可选：单引号(')，双引号(\")，空(none)，可自定义，默认为空
        :type csv_quote: str (optional)

        :param null_identifier: csv时，列为空时，填写的指定内容，默认为空
        :type null_identifier: str (optional)

        :param selected_column_name: csv和parquet时，必填，选择的列名, 逗号分割的列名参数
        :type selected_column_name: str (optional)

        :param selected_column_type: parquet时，必填，选择的列类型，逗号分割的列类型参数
        :type selected_column_type: str (optional)

        :param fields_name: 投递类型为kv时选择的字段名称，大小与fieldsType相同
        :type fields_name: List[str] (optional)

        :param fields_type: 投递类型为kv时选择的字段类型，大小与fieldsName相同
        :type fields_type: List[str] (optional)

        :param shipper_type: shipper_type attribute
        :type shipper_type: str (optional)

        :param kafka_config: kafka配置
        :type kafka_config: str (optional)

        :param dest_type: 目的端类型，当前接口支持BLS，固定填BLS
        :type dest_type: str (optional)

        :param log_store: 日志集名称，必填
        :type log_store: str (optional)

        :param rate_limit: 采集速率限制，单位MB/秒
        :type rate_limit: int (optional)

        :param client_count: 推送服务端的客户端数量，默认值为1，当日志量比较大时，增加客户端数量可以提升数据采集速度
        :type client_count: int (optional)
        """
        super().__init__()
        self.bos_path = bos_path
        self.partition_format_ts = partition_format_ts
        self.partition_format_log_stream = partition_format_log_stream
        self.max_object_size = max_object_size
        self.compress_type = compress_type
        self.deliver_interval = deliver_interval
        self.storage_format = storage_format
        self.csv_headline = csv_headline
        self.csv_delimiter = csv_delimiter
        self.csv_quote = csv_quote
        self.null_identifier = null_identifier
        self.selected_column_name = selected_column_name
        self.selected_column_type = selected_column_type
        self.fields_name = fields_name
        self.fields_type = fields_type
        self.shipper_type = shipper_type
        self.kafka_config = kafka_config
        self.dest_type = dest_type
        self.log_store = log_store
        self.rate_limit = rate_limit
        self.client_count = client_count

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
        if self.bos_path is not None:
            result['BOSPath'] = self.bos_path
        if self.partition_format_ts is not None:
            result['partitionFormatTS'] = self.partition_format_ts
        if self.partition_format_log_stream is not None:
            result['partitionFormatLogStream'] = self.partition_format_log_stream
        if self.max_object_size is not None:
            result['maxObjectSize'] = self.max_object_size
        if self.compress_type is not None:
            result['compressType'] = self.compress_type
        if self.deliver_interval is not None:
            result['deliverInterval'] = self.deliver_interval
        if self.storage_format is not None:
            result['storageFormat'] = self.storage_format
        if self.csv_headline is not None:
            result['csvHeadline'] = self.csv_headline
        if self.csv_delimiter is not None:
            result['csvDelimiter'] = self.csv_delimiter
        if self.csv_quote is not None:
            result['csvQuote'] = self.csv_quote
        if self.null_identifier is not None:
            result['nullIdentifier'] = self.null_identifier
        if self.selected_column_name is not None:
            result['selectedColumnName'] = self.selected_column_name
        if self.selected_column_type is not None:
            result['selectedColumnType'] = self.selected_column_type
        if self.fields_name is not None:
            result['fieldsName'] = self.fields_name
        if self.fields_type is not None:
            result['fieldsType'] = self.fields_type
        if self.shipper_type is not None:
            result['shipperType'] = self.shipper_type
        if self.kafka_config is not None:
            result['kafkaConfig'] = self.kafka_config
        if self.dest_type is not None:
            result['destType'] = self.dest_type
        if self.log_store is not None:
            result['logStore'] = self.log_store
        if self.rate_limit is not None:
            result['rateLimit'] = self.rate_limit
        if self.client_count is not None:
            result['clientCount'] = self.client_count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DestConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('BOSPath') is not None:
            self.bos_path = m.get('BOSPath')
        if m.get('partitionFormatTS') is not None:
            self.partition_format_ts = m.get('partitionFormatTS')
        if m.get('partitionFormatLogStream') is not None:
            self.partition_format_log_stream = m.get('partitionFormatLogStream')
        if m.get('maxObjectSize') is not None:
            self.max_object_size = m.get('maxObjectSize')
        if m.get('compressType') is not None:
            self.compress_type = m.get('compressType')
        if m.get('deliverInterval') is not None:
            self.deliver_interval = m.get('deliverInterval')
        if m.get('storageFormat') is not None:
            self.storage_format = m.get('storageFormat')
        if m.get('csvHeadline') is not None:
            self.csv_headline = m.get('csvHeadline')
        if m.get('csvDelimiter') is not None:
            self.csv_delimiter = m.get('csvDelimiter')
        if m.get('csvQuote') is not None:
            self.csv_quote = m.get('csvQuote')
        if m.get('nullIdentifier') is not None:
            self.null_identifier = m.get('nullIdentifier')
        if m.get('selectedColumnName') is not None:
            self.selected_column_name = m.get('selectedColumnName')
        if m.get('selectedColumnType') is not None:
            self.selected_column_type = m.get('selectedColumnType')
        if m.get('fieldsName') is not None:
            self.fields_name = m.get('fieldsName')
        if m.get('fieldsType') is not None:
            self.fields_type = m.get('fieldsType')
        if m.get('shipperType') is not None:
            self.shipper_type = m.get('shipperType')
        if m.get('kafkaConfig') is not None:
            self.kafka_config = m.get('kafkaConfig')
        if m.get('destType') is not None:
            self.dest_type = m.get('destType')
        if m.get('logStore') is not None:
            self.log_store = m.get('logStore')
        if m.get('rateLimit') is not None:
            self.rate_limit = m.get('rateLimit')
        if m.get('clientCount') is not None:
            self.client_count = m.get('clientCount')
        return self
