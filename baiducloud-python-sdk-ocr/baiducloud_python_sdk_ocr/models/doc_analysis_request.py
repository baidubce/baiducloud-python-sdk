"""
Request entity for DocAnalysisRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DocAnalysisRequest(AbstractModel):
    """
    Request entity for DocAnalysisRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        image=None,
        url=None,
        pdf_file=None,
        pdf_file_num=None,
        language_type=None,
        result_type=None,
        detect_direction=None,
        line_probability=None,
        disp_line_poly=None,
        words_type=None,
        layout_analysis=None,
        recg_formula=None,
        recg_long_division=None,
        disp_underline_analysis=None,
        recg_alter=None,
    ):
        """
        Initialize DocAnalysisRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param pdf_file: pdf_file parameter
        :type pdf_file: str (optional)

        :param pdf_file_num: 需要识别的PDF文件的对应页码，当pdf_file参数有效时，识别传入页码的对应页面内容，若不传入，则默认识别第1页
        :type pdf_file_num: int (optional)

        :param language_type: 识别语言类型，默认为CHN_ENG。可选值包括：<br/>CHN_ENG：中英文；ENG：英文
        :type language_type: str (optional)

        :param result_type: result_type parameter
        :type result_type: str (optional)

        :param detect_direction: detect_direction parameter
        :type detect_direction: bool (optional)

        :param line_probability: 是否返回每行识别结果的置信度。默认为false
        :type line_probability: bool (optional)

        :param disp_line_poly: 是否返回每行的四角点坐标。默认为false
        :type disp_line_poly: bool (optional)

        :param words_type: words_type parameter
        :type words_type: str (optional)

        :param layout_analysis: layout_analysis parameter
        :type layout_analysis: bool (optional)

        :param recg_formula: recg_formula parameter
        :type recg_formula: bool (optional)

        :param recg_long_division: recg_long_division parameter
        :type recg_long_division: bool (optional)

        :param disp_underline_analysis: disp_underline_analysis parameter
        :type disp_underline_analysis: bool (optional)

        :param recg_alter: recg_alter parameter
        :type recg_alter: bool (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.pdf_file = pdf_file
        self.pdf_file_num = pdf_file_num
        self.language_type = language_type
        self.result_type = result_type
        self.detect_direction = detect_direction
        self.line_probability = line_probability
        self.disp_line_poly = disp_line_poly
        self.words_type = words_type
        self.layout_analysis = layout_analysis
        self.recg_formula = recg_formula
        self.recg_long_division = recg_long_division
        self.disp_underline_analysis = disp_underline_analysis
        self.recg_alter = recg_alter

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
        if self.image is not None:
            result['image'] = self.image
        if self.url is not None:
            result['url'] = self.url
        if self.pdf_file is not None:
            result['pdf_file'] = self.pdf_file
        if self.pdf_file_num is not None:
            result['pdf_file_num'] = self.pdf_file_num
        if self.language_type is not None:
            result['language_type'] = self.language_type
        if self.result_type is not None:
            result['result_type'] = self.result_type
        if self.detect_direction is not None:
            result['detect_direction'] = self.detect_direction
        if self.line_probability is not None:
            result['line_probability'] = self.line_probability
        if self.disp_line_poly is not None:
            result['disp_line_poly'] = self.disp_line_poly
        if self.words_type is not None:
            result['words_type'] = self.words_type
        if self.layout_analysis is not None:
            result['layout_analysis'] = self.layout_analysis
        if self.recg_formula is not None:
            result['recg_formula'] = self.recg_formula
        if self.recg_long_division is not None:
            result['recg_long_division'] = self.recg_long_division
        if self.disp_underline_analysis is not None:
            result['disp_underline_analysis'] = self.disp_underline_analysis
        if self.recg_alter is not None:
            result['recg_alter'] = self.recg_alter
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DocAnalysisRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('pdf_file') is not None:
            self.pdf_file = m.get('pdf_file')
        if m.get('pdf_file_num') is not None:
            self.pdf_file_num = m.get('pdf_file_num')
        if m.get('language_type') is not None:
            self.language_type = m.get('language_type')
        if m.get('result_type') is not None:
            self.result_type = m.get('result_type')
        if m.get('detect_direction') is not None:
            self.detect_direction = m.get('detect_direction')
        if m.get('line_probability') is not None:
            self.line_probability = m.get('line_probability')
        if m.get('disp_line_poly') is not None:
            self.disp_line_poly = m.get('disp_line_poly')
        if m.get('words_type') is not None:
            self.words_type = m.get('words_type')
        if m.get('layout_analysis') is not None:
            self.layout_analysis = m.get('layout_analysis')
        if m.get('recg_formula') is not None:
            self.recg_formula = m.get('recg_formula')
        if m.get('recg_long_division') is not None:
            self.recg_long_division = m.get('recg_long_division')
        if m.get('disp_underline_analysis') is not None:
            self.disp_underline_analysis = m.get('disp_underline_analysis')
        if m.get('recg_alter') is not None:
            self.recg_alter = m.get('recg_alter')
        return self
