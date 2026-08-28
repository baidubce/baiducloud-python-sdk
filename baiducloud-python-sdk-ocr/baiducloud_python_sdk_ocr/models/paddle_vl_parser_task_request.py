"""
Request entity for PaddleVlParserTaskRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PaddleVlParserTaskRequest(AbstractModel):
    """
    Request entity for PaddleVlParserTaskRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        file_name,
        file_data=None,
        file_url=None,
        analysis_chart=None,
        merge_tables=None,
        relevel_titles=None,
        recognize_seal=None,
        return_span_boxes=None,
    ):
        """
        Initialize PaddleVlParserTaskRequest request entity.

        :param file_data: file_data parameter
        :type file_data: str (optional)

        :param file_url: file_url parameter
        :type file_url: str (optional)

        :param file_name: 文件名，请保证文件名后缀正确，例如 \\\"1.pdf\\\"
        :type file_name: str (required)

        :param analysis_chart: 是否对统计图表进行解析。可选值：true：是；false：否
        :type analysis_chart: bool (optional)

        :param merge_tables: 是否将跨页表格合并输出。可选值：true：是；false：否
        :type merge_tables: bool (optional)

        :param relevel_titles: 是否对段落标题（paragraph_title）进行分级。可选值：true：是；false：否
        :type relevel_titles: bool (optional)

        :param recognize_seal: 是否识别印章内容。可选值：true：是；false：否
        :type recognize_seal: bool (optional)

        :param return_span_boxes: 是否返回行坐标。可选值：true：是；false：否
        :type return_span_boxes: bool (optional)
        """
        super().__init__()
        self.file_data = file_data
        self.file_url = file_url
        self.file_name = file_name
        self.analysis_chart = analysis_chart
        self.merge_tables = merge_tables
        self.relevel_titles = relevel_titles
        self.recognize_seal = recognize_seal
        self.return_span_boxes = return_span_boxes

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
        if self.analysis_chart is not None:
            result['analysis_chart'] = self.analysis_chart
        if self.merge_tables is not None:
            result['merge_tables'] = self.merge_tables
        if self.relevel_titles is not None:
            result['relevel_titles'] = self.relevel_titles
        if self.recognize_seal is not None:
            result['recognize_seal'] = self.recognize_seal
        if self.return_span_boxes is not None:
            result['return_span_boxes'] = self.return_span_boxes
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PaddleVlParserTaskRequest

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
        if m.get('analysis_chart') is not None:
            self.analysis_chart = m.get('analysis_chart')
        if m.get('merge_tables') is not None:
            self.merge_tables = m.get('merge_tables')
        if m.get('relevel_titles') is not None:
            self.relevel_titles = m.get('relevel_titles')
        if m.get('recognize_seal') is not None:
            self.recognize_seal = m.get('recognize_seal')
        if m.get('return_span_boxes') is not None:
            self.return_span_boxes = m.get('return_span_boxes')
        return self
