"""
Bucket information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Bucket(AbstractModel):
    """
    Bucket
    """

    def __init__(self, key=None, doc_count=None):
        """
        Initialize Bucket instance.

        :param key: key attribute
        :type key: int (optional)

        :param doc_count: 时间区间内的文档数量
        :type doc_count: int (optional)
        """
        super().__init__()
        self.key = key
        self.doc_count = doc_count

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
        if self.key is not None:
            result['key'] = self.key
        if self.doc_count is not None:
            result['doc_count'] = self.doc_count
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Bucket

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('doc_count') is not None:
            self.doc_count = m.get('doc_count')
        return self
