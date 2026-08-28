"""
DocClassifyWordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.doc_classify_location import DocClassifyLocation


class DocClassifyWordsResult(AbstractModel):
    """
    DocClassifyWordsResult
    """

    def __init__(self, type=None, probablity=None, location=None):
        """
        Initialize DocClassifyWordsResult instance.

        :param type: 类别信息
        :type type: str (optional)

        :param probablity: 分类置信度
        :type probablity: float (optional)

        :param location: location attribute
        :type location: DocClassifyLocation (optional)
        """
        super().__init__()
        self.type = type
        self.probablity = probablity
        self.location = location

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
        if self.probablity is not None:
            result['probablity'] = self.probablity
        if self.location is not None:
            result['location'] = self.location.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DocClassifyWordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('probablity') is not None:
            self.probablity = m.get('probablity')
        if m.get('location') is not None:
            self.location = DocClassifyLocation().from_dict(m.get('location'))
        return self
