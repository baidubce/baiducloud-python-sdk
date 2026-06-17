"""
ProcessConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ProcessConfig(AbstractModel):
    """
    ProcessConfig
    """

    def __init__(
        self,
        regex=None,
        separator=None,
        custom_separator=None,
        quote=None,
        kv_key_index=None,
        kv_value_index=None,
        sample_log=None,
        keys=None,
        data_type=None,
        discard_on_failure=None,
        keep_original=None,
    ):
        """
        Initialize ProcessConfig instance.

        :param regex: 处理类型是regex时必填；处理类型是kv时也必填
        :type regex: str (optional)

        :param separator: separator attribute
        :type separator: str (optional)

        :param custom_separator: 当separator为custom时必填
        :type custom_separator: str (optional)

        :param quote: 分隔符场景可指定引用符
        :type quote: str (optional)

        :param kv_key_index: kv解析时必填，用于指定key分组位置（从1开始）
        :type kv_key_index: int (optional)

        :param kv_value_index: kv解析时必填，用于指定value分组位置（从1开始）
        :type kv_value_index: int (optional)

        :param sample_log: 解析日志样例，主要用于console解析预览
        :type sample_log: str (optional)

        :param keys: 解析结果的列名
        :type keys: str (optional)

        :param data_type: data_type attribute
        :type data_type: str (optional)

        :param discard_on_failure: 日志解析失败是否丢弃，true:丢弃 false:返回原值
        :type discard_on_failure: bool (optional)

        :param keep_original: keep_original attribute
        :type keep_original: bool (optional)
        """
        super().__init__()
        self.regex = regex
        self.separator = separator
        self.custom_separator = custom_separator
        self.quote = quote
        self.kv_key_index = kv_key_index
        self.kv_value_index = kv_value_index
        self.sample_log = sample_log
        self.keys = keys
        self.data_type = data_type
        self.discard_on_failure = discard_on_failure
        self.keep_original = keep_original

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
        if self.regex is not None:
            result['regex'] = self.regex
        if self.separator is not None:
            result['separator'] = self.separator
        if self.custom_separator is not None:
            result['customSeparator'] = self.custom_separator
        if self.quote is not None:
            result['quote'] = self.quote
        if self.kv_key_index is not None:
            result['kvKeyIndex'] = self.kv_key_index
        if self.kv_value_index is not None:
            result['kvValueIndex'] = self.kv_value_index
        if self.sample_log is not None:
            result['sampleLog'] = self.sample_log
        if self.keys is not None:
            result['keys'] = self.keys
        if self.data_type is not None:
            result['dataType'] = self.data_type
        if self.discard_on_failure is not None:
            result['discardOnFailure'] = self.discard_on_failure
        if self.keep_original is not None:
            result['keepOriginal'] = self.keep_original
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ProcessConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('regex') is not None:
            self.regex = m.get('regex')
        if m.get('separator') is not None:
            self.separator = m.get('separator')
        if m.get('customSeparator') is not None:
            self.custom_separator = m.get('customSeparator')
        if m.get('quote') is not None:
            self.quote = m.get('quote')
        if m.get('kvKeyIndex') is not None:
            self.kv_key_index = m.get('kvKeyIndex')
        if m.get('kvValueIndex') is not None:
            self.kv_value_index = m.get('kvValueIndex')
        if m.get('sampleLog') is not None:
            self.sample_log = m.get('sampleLog')
        if m.get('keys') is not None:
            self.keys = m.get('keys')
        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')
        if m.get('discardOnFailure') is not None:
            self.discard_on_failure = m.get('discardOnFailure')
        if m.get('keepOriginal') is not None:
            self.keep_original = m.get('keepOriginal')
        return self
