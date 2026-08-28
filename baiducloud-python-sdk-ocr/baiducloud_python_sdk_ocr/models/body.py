"""
Body information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.table_point import TablePoint

from baiducloud_python_sdk_ocr.models.table_content import TableContent


class Body(AbstractModel):
    """
    Body
    """

    def __init__(
        self, cell_location=None, row_start=None, row_end=None, col_start=None, col_end=None, words=None, contents=None
    ):
        """
        Initialize Body instance.

        :param cell_location: 单元格四角点x,y坐标
        :type cell_location: List[TablePoint] (optional)

        :param row_start: 单元格行起始编号，横线编号从0开始
        :type row_start: int (optional)

        :param row_end: 单元格行终止编号
        :type row_end: int (optional)

        :param col_start: 单元格列起始编号，竖线编号从0开始
        :type col_start: int (optional)

        :param col_end: 单元格列终止编号
        :type col_end: int (optional)

        :param words: 单元格文字内容
        :type words: str (optional)

        :param contents: 单元格内文字内容，分行显示，当请求参数 cell_contents = true 时返回
        :type contents: List[TableContent] (optional)
        """
        super().__init__()
        self.cell_location = cell_location
        self.row_start = row_start
        self.row_end = row_end
        self.col_start = col_start
        self.col_end = col_end
        self.words = words
        self.contents = contents

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
        if self.cell_location is not None:
            result['cell_location'] = [i.to_dict() for i in self.cell_location]
        if self.row_start is not None:
            result['row_start'] = self.row_start
        if self.row_end is not None:
            result['row_end'] = self.row_end
        if self.col_start is not None:
            result['col_start'] = self.col_start
        if self.col_end is not None:
            result['col_end'] = self.col_end
        if self.words is not None:
            result['words'] = self.words
        if self.contents is not None:
            result['contents'] = [i.to_dict() for i in self.contents]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Body

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cell_location') is not None:
            self.cell_location = [TablePoint().from_dict(i) for i in m.get('cell_location')]
        if m.get('row_start') is not None:
            self.row_start = m.get('row_start')
        if m.get('row_end') is not None:
            self.row_end = m.get('row_end')
        if m.get('col_start') is not None:
            self.col_start = m.get('col_start')
        if m.get('col_end') is not None:
            self.col_end = m.get('col_end')
        if m.get('words') is not None:
            self.words = m.get('words')
        if m.get('contents') is not None:
            self.contents = [TableContent().from_dict(i) for i in m.get('contents')]
        return self
