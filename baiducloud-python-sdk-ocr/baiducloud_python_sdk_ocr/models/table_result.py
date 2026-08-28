"""
TableResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.doc_analysis_office_point import DocAnalysisOfficePoint

from baiducloud_python_sdk_ocr.models.table_header import TableHeader

from baiducloud_python_sdk_ocr.models.table_body import TableBody

from baiducloud_python_sdk_ocr.models.table_footer import TableFooter


class TableResult(AbstractModel):
    """
    TableResult
    """

    def __init__(self, table_location=None, header=None, body=None, footer=None):
        """
        Initialize TableResult instance.

        :param table_location: 单个表格位置，四角点的x,y坐标
        :type table_location: List[DocAnalysisOfficePoint] (optional)

        :param header: 表头信息
        :type header: List[TableHeader] (optional)

        :param body: 单元格信息
        :type body: List[TableBody] (optional)

        :param footer: 表尾信息
        :type footer: List[TableFooter] (optional)
        """
        super().__init__()
        self.table_location = table_location
        self.header = header
        self.body = body
        self.footer = footer

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
        if self.table_location is not None:
            result['table_location'] = [i.to_dict() for i in self.table_location]
        if self.header is not None:
            result['header'] = [i.to_dict() for i in self.header]
        if self.body is not None:
            result['body'] = [i.to_dict() for i in self.body]
        if self.footer is not None:
            result['footer'] = [i.to_dict() for i in self.footer]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TableResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('table_location') is not None:
            self.table_location = [DocAnalysisOfficePoint().from_dict(i) for i in m.get('table_location')]
        if m.get('header') is not None:
            self.header = [TableHeader().from_dict(i) for i in m.get('header')]
        if m.get('body') is not None:
            self.body = [TableBody().from_dict(i) for i in m.get('body')]
        if m.get('footer') is not None:
            self.footer = [TableFooter().from_dict(i) for i in m.get('footer')]
        return self
