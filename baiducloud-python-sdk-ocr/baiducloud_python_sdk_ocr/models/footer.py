"""
Footer information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.table_point import TablePoint


class Footer(AbstractModel):
    """
    Footer
    """

    def __init__(self, location=None, words=None):
        """
        Initialize Footer instance.

        :param location: 表尾位置，四角点 x,y 坐标
        :type location: List[TablePoint] (optional)

        :param words: 表尾信息，按行拆分
        :type words: str (optional)
        """
        super().__init__()
        self.location = location
        self.words = words

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
        if self.location is not None:
            result['location'] = [i.to_dict() for i in self.location]
        if self.words is not None:
            result['words'] = self.words
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Footer

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('location') is not None:
            self.location = [TablePoint().from_dict(i) for i in m.get('location')]
        if m.get('words') is not None:
            self.words = m.get('words')
        return self
