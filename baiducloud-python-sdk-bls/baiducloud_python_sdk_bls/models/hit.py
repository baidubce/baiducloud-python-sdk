"""
Hit information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Hit(AbstractModel):
    """
    Hit
    """

    def __init__(self, index=None, id=None, score=None, sort=None, version=None, fields=None):
        """
        Initialize Hit instance.

        :param index: 项目和日志集信息 如何非default项目，使用 项目$日志集名称 的格式，defualt项目只有日志集名称
        :type index: str (optional)

        :param id: 日志集记录的ID  由offset和timestamp组成
        :type id: str (optional)

        :param score: 得分，目前都是0
        :type score: float (optional)

        :param sort: 排序字段，用于查找下一页, 目前都是单个元素
        :type sort: List[str] (optional)

        :param version: 版本，目前都是1
        :type version: int (optional)

        :param fields: 日志集字段信息
        :type fields: Dict[str, List[object]] (optional)
        """
        super().__init__()
        self.index = index
        self.id = id
        self.score = score
        self.sort = sort
        self.version = version
        self.fields = fields

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
        if self.index is not None:
            result['_index'] = self.index
        if self.id is not None:
            result['_id'] = self.id
        if self.score is not None:
            result['_score'] = self.score
        if self.sort is not None:
            result['sort'] = self.sort
        if self.version is not None:
            result['_version'] = self.version
        if self.fields is not None:
            result['fields'] = self.fields

        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Hit

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('_index') is not None:
            self.index = m.get('_index')
        if m.get('_id') is not None:
            self.id = m.get('_id')
        if m.get('_score') is not None:
            self.score = m.get('_score')
        if m.get('sort') is not None:
            self.sort = m.get('sort')
        if m.get('_version') is not None:
            self.version = m.get('_version')
        if m.get('fields') is not None:
            self.fields = m.get('fields')

        return self
