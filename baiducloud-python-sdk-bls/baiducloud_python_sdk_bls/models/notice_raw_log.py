"""
NoticeRawLog information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bls.models.custom_target import CustomTarget


class NoticeRawLog(AbstractModel):
    """
    NoticeRawLog
    """

    def __init__(self, type=None, ref_target=None, custom_target=None, columns=None, limit=None):
        """
        Initialize NoticeRawLog instance.

        :param type: 配置类型，REF: 关联执行语句，CUSTOM: 自定义检索语句
        :type type: str (optional)

        :param ref_target: 引用的执行语句序号，从0开始计数，type=REF时必填
        :type ref_target: int (optional)

        :param custom_target: custom_target attribute
        :type custom_target: CustomTarget (optional)

        :param columns: 在原始日志中展示的字段名列表
        :type columns: List[str] (optional)

        :param limit: 展示的日志条数，最大值为5
        :type limit: int (optional)
        """
        super().__init__()
        self.type = type
        self.ref_target = ref_target
        self.custom_target = custom_target
        self.columns = columns
        self.limit = limit

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
        if self.type is not None:
            result['type'] = self.type
        if self.ref_target is not None:
            result['refTarget'] = self.ref_target
        if self.custom_target is not None:
            result['customTarget'] = self.custom_target.to_dict()
        if self.columns is not None:
            result['columns'] = self.columns
        if self.limit is not None:
            result['limit'] = self.limit
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: NoticeRawLog

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('refTarget') is not None:
            self.ref_target = m.get('refTarget')
        if m.get('customTarget') is not None:
            self.custom_target = CustomTarget().from_dict(m.get('customTarget'))
        if m.get('columns') is not None:
            self.columns = m.get('columns')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        return self
