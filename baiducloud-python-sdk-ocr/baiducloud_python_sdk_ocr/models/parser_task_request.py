"""
Request entity for ParserTaskRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ParserTaskRequest(AbstractModel):
    """
    Request entity for ParserTaskRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        file_name,
        file_data=None,
        file_url=None,
        recognize_formula=None,
        analysis_chart=None,
        angle_adjust=None,
        parse_image_layout=None,
        language_type=None,
        switch_digital_width=None,
        html_table_format=None,
        return_doc_chunks=None,
    ):
        """
        Initialize ParserTaskRequest request entity.

        :param file_data: file_data parameter
        :type file_data: str (optional)

        :param file_url: file_url parameter
        :type file_url: str (optional)

        :param file_name: 文件名，请保证文件名后缀正确，例如 \\\"1.pdf\\\"
        :type file_name: str (required)

        :param recognize_formula: 是否对版式类型文档进行公式识别。可选值：true：是；false：否
        :type recognize_formula: bool (optional)

        :param analysis_chart: 是否对统计图表进行解析。可选值：true：是；false：否
        :type analysis_chart: bool (optional)

        :param angle_adjust: 是否对图片进行矫正。可选值：true：是；false：否
        :type angle_adjust: bool (optional)

        :param parse_image_layout: 是否返回文档中的图片位置信息。可选值：true：是；false：否
        :type parse_image_layout: bool (optional)

        :param language_type: language_type parameter
        :type language_type: str (optional)

        :param switch_digital_width: switch_digital_width parameter
        :type switch_digital_width: str (optional)

        :param html_table_format: 是否将识别出的表格转换为 HTML 格式返回，默认为 true。可选值：true：是；false：否
        :type html_table_format: bool (optional)

        :param return_doc_chunks: return_doc_chunks parameter
        :type return_doc_chunks: str (optional)
        """
        super().__init__()
        self.file_data = file_data
        self.file_url = file_url
        self.file_name = file_name
        self.recognize_formula = recognize_formula
        self.analysis_chart = analysis_chart
        self.angle_adjust = angle_adjust
        self.parse_image_layout = parse_image_layout
        self.language_type = language_type
        self.switch_digital_width = switch_digital_width
        self.html_table_format = html_table_format
        self.return_doc_chunks = return_doc_chunks

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.file_data is not None:
            result['file_data'] = self.file_data
        if self.file_url is not None:
            result['file_url'] = self.file_url
        if self.file_name is not None:
            result['file_name'] = self.file_name
        if self.recognize_formula is not None:
            result['recognize_formula'] = self.recognize_formula
        if self.analysis_chart is not None:
            result['analysis_chart'] = self.analysis_chart
        if self.angle_adjust is not None:
            result['angle_adjust'] = self.angle_adjust
        if self.parse_image_layout is not None:
            result['parse_image_layout'] = self.parse_image_layout
        if self.language_type is not None:
            result['language_type'] = self.language_type
        if self.switch_digital_width is not None:
            result['switch_digital_width'] = self.switch_digital_width
        if self.html_table_format is not None:
            result['html_table_format'] = self.html_table_format
        if self.return_doc_chunks is not None:
            result['return_doc_chunks'] = self.return_doc_chunks
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ParserTaskRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('file_data') is not None:
            self.file_data = m.get('file_data')
        if m.get('file_url') is not None:
            self.file_url = m.get('file_url')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        if m.get('recognize_formula') is not None:
            self.recognize_formula = m.get('recognize_formula')
        if m.get('analysis_chart') is not None:
            self.analysis_chart = m.get('analysis_chart')
        if m.get('angle_adjust') is not None:
            self.angle_adjust = m.get('angle_adjust')
        if m.get('parse_image_layout') is not None:
            self.parse_image_layout = m.get('parse_image_layout')
        if m.get('language_type') is not None:
            self.language_type = m.get('language_type')
        if m.get('switch_digital_width') is not None:
            self.switch_digital_width = m.get('switch_digital_width')
        if m.get('html_table_format') is not None:
            self.html_table_format = m.get('html_table_format')
        if m.get('return_doc_chunks') is not None:
            self.return_doc_chunks = m.get('return_doc_chunks')
        return self
