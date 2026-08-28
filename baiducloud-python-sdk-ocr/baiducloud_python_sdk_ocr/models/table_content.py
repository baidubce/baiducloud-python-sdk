"""
TableContent information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.table_point import TablePoint


class TableContent(AbstractModel):
    """
    TableContent
    """

    def __init__(self, poly_location=None, word=None):
        """
        Initialize TableContent instance.

        :param poly_location: 单元格内文字各行的四角点x,y坐标
        :type poly_location: List[TablePoint] (optional)

        :param word: 单元格内分行文字内容
        :type word: str (optional)
        """
        super().__init__()
        self.poly_location = poly_location
        self.word = word

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
        if self.poly_location is not None:
            result['poly_location'] = [i.to_dict() for i in self.poly_location]
        if self.word is not None:
            result['word'] = self.word
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TableContent

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('poly_location') is not None:
            self.poly_location = [TablePoint().from_dict(i) for i in m.get('poly_location')]
        if m.get('word') is not None:
            self.word = m.get('word')
        return self
