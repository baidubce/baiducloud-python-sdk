"""
Request entity for DocAnalysisOfficeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DocAnalysisOfficeRequest(AbstractModel):
    """
    Request entity for DocAnalysisOfficeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        image=None,
        url=None,
        pdf_file=None,
        pdf_file_num=None,
        ofd_file=None,
        ofd_file_num=None,
        language_type=None,
        result_type=None,
        char_probability=None,
        detect_direction=None,
        line_probability=None,
        disp_line_poly=None,
        words_type=None,
        layout_analysis=None,
        recg_tables=None,
        recog_seal=None,
        recg_formula=None,
        erase_seal=None,
        disp_underline_analysis=None,
    ):
        """
        Initialize DocAnalysisOfficeRequest request entity.

        :param image: image parameter
        :type image: str (optional)

        :param url: url parameter
        :type url: str (optional)

        :param pdf_file: pdf_file parameter
        :type pdf_file: str (optional)

        :param pdf_file_num: pdf_file_num parameter
        :type pdf_file_num: int (optional)

        :param ofd_file: ofd_file parameter
        :type ofd_file: str (optional)

        :param ofd_file_num: ofd_file_num parameter
        :type ofd_file_num: int (optional)

        :param language_type: language_type parameter
        :type language_type: str (optional)

        :param result_type: result_type parameter
        :type result_type: str (optional)

        :param char_probability: char_probability parameter
        :type char_probability: bool (optional)

        :param detect_direction: detect_direction parameter
        :type detect_direction: bool (optional)

        :param line_probability: 是否返回每行识别结果的置信度。默认为false。可选值包括：true：返回；false：不返回
        :type line_probability: bool (optional)

        :param disp_line_poly: 是否返回每行的四角点坐标。默认为false。可选值包括：true：返回；false：不返回
        :type disp_line_poly: bool (optional)

        :param words_type: words_type parameter
        :type words_type: str (optional)

        :param layout_analysis: layout_analysis parameter
        :type layout_analysis: bool (optional)

        :param recg_tables: 是否识别并输出表格相关信息，包括单元格内容。默认为false。可选值包括：true：返回；false：不返回
        :type recg_tables: bool (optional)

        :param recog_seal: 是否识别并输出印章相关信息。默认为false。可选值包括：true：返回；false：不返回
        :type recog_seal: bool (optional)

        :param recg_formula: 是否检测并识别公式，公式以Latex格式返回。默认为false。可选值包括：true：返回；false：不返回
        :type recg_formula: bool (optional)

        :param erase_seal: 是否先擦除水印、印章后再识别文档。默认为false。可选值包括：true：返回；false：不返回
        :type erase_seal: bool (optional)

        :param disp_underline_analysis: 是否识别并输出下划线，默认false。可选值包括：true：返回；false：不返回
        :type disp_underline_analysis: bool (optional)
        """
        super().__init__()
        self.image = image
        self.url = url
        self.pdf_file = pdf_file
        self.pdf_file_num = pdf_file_num
        self.ofd_file = ofd_file
        self.ofd_file_num = ofd_file_num
        self.language_type = language_type
        self.result_type = result_type
        self.char_probability = char_probability
        self.detect_direction = detect_direction
        self.line_probability = line_probability
        self.disp_line_poly = disp_line_poly
        self.words_type = words_type
        self.layout_analysis = layout_analysis
        self.recg_tables = recg_tables
        self.recog_seal = recog_seal
        self.recg_formula = recg_formula
        self.erase_seal = erase_seal
        self.disp_underline_analysis = disp_underline_analysis

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
        if self.ofd_file is not None:
            result['ofd_file'] = self.ofd_file
        if self.ofd_file_num is not None:
            result['ofd_file_num'] = self.ofd_file_num
        if self.language_type is not None:
            result['language_type'] = self.language_type
        if self.result_type is not None:
            result['result_type'] = self.result_type
        if self.char_probability is not None:
            result['char_probability'] = self.char_probability
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
        if self.recg_tables is not None:
            result['recg_tables'] = self.recg_tables
        if self.recog_seal is not None:
            result['recog_seal'] = self.recog_seal
        if self.recg_formula is not None:
            result['recg_formula'] = self.recg_formula
        if self.erase_seal is not None:
            result['erase_seal'] = self.erase_seal
        if self.disp_underline_analysis is not None:
            result['disp_underline_analysis'] = self.disp_underline_analysis
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DocAnalysisOfficeRequest

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
        if m.get('ofd_file') is not None:
            self.ofd_file = m.get('ofd_file')
        if m.get('ofd_file_num') is not None:
            self.ofd_file_num = m.get('ofd_file_num')
        if m.get('language_type') is not None:
            self.language_type = m.get('language_type')
        if m.get('result_type') is not None:
            self.result_type = m.get('result_type')
        if m.get('char_probability') is not None:
            self.char_probability = m.get('char_probability')
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
        if m.get('recg_tables') is not None:
            self.recg_tables = m.get('recg_tables')
        if m.get('recog_seal') is not None:
            self.recog_seal = m.get('recog_seal')
        if m.get('recg_formula') is not None:
            self.recg_formula = m.get('recg_formula')
        if m.get('erase_seal') is not None:
            self.erase_seal = m.get('erase_seal')
        if m.get('disp_underline_analysis') is not None:
            self.disp_underline_analysis = m.get('disp_underline_analysis')
        return self
