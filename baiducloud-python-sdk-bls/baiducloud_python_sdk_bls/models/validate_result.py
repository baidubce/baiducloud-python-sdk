"""
ValidateResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bls.models.log_store import LogStore


class ValidateResult(AbstractModel):
    """
    ValidateResult
    """

    def __init__(self, log_store=None, valid=None, reason=None, columns=None, column_types=None):
        """
        Initialize ValidateResult instance.

        :param log_store: log_store attribute
        :type log_store: LogStore (optional)

        :param valid: 是否通过校验
        :type valid: bool (optional)

        :param reason: 若校验失败，返回失败原因
        :type reason: str (optional)

        :param columns: 若校验通过，返回列名称列表
        :type columns: List[str] (optional)

        :param column_types: 若校验通过，返回列类型列表
        :type column_types: List[str] (optional)
        """
        super().__init__()
        self.log_store = log_store
        self.valid = valid
        self.reason = reason
        self.columns = columns
        self.column_types = column_types

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
        if self.log_store is not None:
            result['logStore'] = self.log_store.to_dict()
        if self.valid is not None:
            result['valid'] = self.valid
        if self.reason is not None:
            result['reason'] = self.reason
        if self.columns is not None:
            result['columns'] = self.columns
        if self.column_types is not None:
            result['columnTypes'] = self.column_types
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ValidateResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('logStore') is not None:
            self.log_store = LogStore().from_dict(m.get('logStore'))
        if m.get('valid') is not None:
            self.valid = m.get('valid')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('columns') is not None:
            self.columns = m.get('columns')
        if m.get('columnTypes') is not None:
            self.column_types = m.get('columnTypes')
        return self
