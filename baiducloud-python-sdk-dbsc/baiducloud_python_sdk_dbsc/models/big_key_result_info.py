"""
BigKeyResultInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BigKeyResultInfo(AbstractModel):
    """
    BigKeyResultInfo
    """

    def __init__(self, db=None, element_count=None, encoding=None, expire_time=None, key=None, size=None, type=None):
        """
        Initialize BigKeyResultInfo instance.

        :param db: 数据库编号
        :type db: int (optional)

        :param element_count: 元素数量
        :type element_count: int (optional)

        :param encoding: 编码方式
        :type encoding: str (optional)

        :param expire_time: 过期时间
        :type expire_time: str (optional)

        :param key: 键
        :type key: str (optional)

        :param size: 占有内存
        :type size: int (optional)

        :param type: 数据类型
        :type type: str (optional)
        """
        super().__init__()
        self.db = db
        self.element_count = element_count
        self.encoding = encoding
        self.expire_time = expire_time
        self.key = key
        self.size = size
        self.type = type

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
        if self.db is not None:
            result['db'] = self.db
        if self.element_count is not None:
            result['elementCount'] = self.element_count
        if self.encoding is not None:
            result['encoding'] = self.encoding
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.key is not None:
            result['key'] = self.key
        if self.size is not None:
            result['size'] = self.size
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BigKeyResultInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('db') is not None:
            self.db = m.get('db')
        if m.get('elementCount') is not None:
            self.element_count = m.get('elementCount')
        if m.get('encoding') is not None:
            self.encoding = m.get('encoding')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self
