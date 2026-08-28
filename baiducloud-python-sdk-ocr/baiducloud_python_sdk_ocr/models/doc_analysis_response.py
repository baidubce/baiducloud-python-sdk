"""
Request entity for DocAnalysisResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ocr.models.doc_analysis_result import DocAnalysisResult
from baiducloud_python_sdk_ocr.models.doc_analysis_formula_result import DocAnalysisFormulaResult
from baiducloud_python_sdk_ocr.models.doc_analysis_words_result import DocAnalysisWordsResult
from baiducloud_python_sdk_ocr.models.doc_analysis_layout import DocAnalysisLayout
from baiducloud_python_sdk_ocr.models.doc_analysis_section import DocAnalysisSection
from baiducloud_python_sdk_ocr.models.long_division import LongDivision
from baiducloud_python_sdk_ocr.models.underline import Underline


class DocAnalysisResponse(BceResponse):
    """
    DocAnalysisResponse
    """

    def __init__(
        self,
        error_code=None,
        error_msg=None,
        log_id=None,
        img_direction=None,
        results_num=None,
        results=None,
        formula_result=None,
        words_result=None,
        layouts_num=None,
        layouts=None,
        sec_rows=None,
        sec_cols=None,
        sections=None,
        long_division=None,
        long_division_num=None,
        underline=None,
        pdf_file_size=None,
    ):
        """
        Initialize DocAnalysisResponse response.

        :param error_code: 错误码
        :type error_code: int (optional)

        :param error_msg: 错误描述信息
        :type error_msg: str (optional)

        :param log_id: 唯一的log id，用于问题定位
        :type log_id: int (optional)

        :param img_direction: img_direction field
        :type img_direction: int (optional)

        :param results_num: 识别结果数，表示results的元素个数
        :type results_num: int (optional)

        :param results: 识别结果数组
        :type results: List[DocAnalysisResult] (optional)

        :param formula_result: 识别结果中的公式数组，recg_formula=true时返回
        :type formula_result: List[DocAnalysisFormulaResult] (optional)

        :param words_result: 将普通文字和公式融合后的识别结果数组，recg_formula=true时返回
        :type words_result: List[DocAnalysisWordsResult] (optional)

        :param layouts_num: 版面分析结果数，表示layout的元素个数
        :type layouts_num: int (optional)

        :param layouts: 每个「栏：section」里面的文档版面模块数组，包含表格、图、段落文本、标题、目录等5个模块
        :type layouts: List[DocAnalysisLayout] (optional)

        :param sec_rows: 将所有的版面中的「栏:section」内容表示成M×N的网格，sec_rows=M
        :type sec_rows: int (optional)

        :param sec_cols: 将所有的版面中的「分栏」内容表示成M×N的网格，sec_cols=N
        :type sec_cols: int (optional)

        :param sections: 一张图片中包含的5大版面属性，包含：栏、页眉、页脚、页码、脚注
        :type sections: List[DocAnalysisSection] (optional)

        :param long_division: 手写竖式识别结果，当recg_long_division=true时返回
        :type long_division: List[LongDivision] (optional)

        :param long_division_num: 手写竖式识别结果数，表示long_division的元素个数，当recg_long_division=true时返回
        :type long_division_num: int (optional)

        :param underline: 识别到的下划线结果，当disp_underline_analysis=true时返回
        :type underline: List[Underline] (optional)

        :param pdf_file_size: 传入PDF文件的总页数，当pdf_file参数有效时返回该字段
        :type pdf_file_size: int (optional)
        """
        super().__init__()
        self.error_code = error_code
        self.error_msg = error_msg
        self.log_id = log_id
        self.img_direction = img_direction
        self.results_num = results_num
        self.results = results
        self.formula_result = formula_result
        self.words_result = words_result
        self.layouts_num = layouts_num
        self.layouts = layouts
        self.sec_rows = sec_rows
        self.sec_cols = sec_cols
        self.sections = sections
        self.long_division = long_division
        self.long_division_num = long_division_num
        self.underline = underline
        self.pdf_file_size = pdf_file_size

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.log_id is not None:
            result['log_id'] = self.log_id
        if self.img_direction is not None:
            result['img_direction'] = self.img_direction
        if self.results_num is not None:
            result['results_num'] = self.results_num
        if self.results is not None:
            result['results'] = [i.to_dict() for i in self.results]
        if self.formula_result is not None:
            result['formula_result'] = [i.to_dict() for i in self.formula_result]
        if self.words_result is not None:
            result['words_result'] = [i.to_dict() for i in self.words_result]
        if self.layouts_num is not None:
            result['layouts_num'] = self.layouts_num
        if self.layouts is not None:
            result['layouts'] = [i.to_dict() for i in self.layouts]
        if self.sec_rows is not None:
            result['sec_rows'] = self.sec_rows
        if self.sec_cols is not None:
            result['sec_cols'] = self.sec_cols
        if self.sections is not None:
            result['sections'] = [i.to_dict() for i in self.sections]
        if self.long_division is not None:
            result['long_division'] = [i.to_dict() for i in self.long_division]
        if self.long_division_num is not None:
            result['long_division_num'] = self.long_division_num
        if self.underline is not None:
            result['underline'] = [i.to_dict() for i in self.underline]
        if self.pdf_file_size is not None:
            result['pdf_file_size'] = self.pdf_file_size
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DocAnalysisResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('log_id') is not None:
            self.log_id = m.get('log_id')
        if m.get('img_direction') is not None:
            self.img_direction = m.get('img_direction')
        if m.get('results_num') is not None:
            self.results_num = m.get('results_num')
        if m.get('results') is not None:
            self.results = [DocAnalysisResult().from_dict(i) for i in m.get('results')]
        if m.get('formula_result') is not None:
            self.formula_result = [DocAnalysisFormulaResult().from_dict(i) for i in m.get('formula_result')]
        if m.get('words_result') is not None:
            self.words_result = [DocAnalysisWordsResult().from_dict(i) for i in m.get('words_result')]
        if m.get('layouts_num') is not None:
            self.layouts_num = m.get('layouts_num')
        if m.get('layouts') is not None:
            self.layouts = [DocAnalysisLayout().from_dict(i) for i in m.get('layouts')]
        if m.get('sec_rows') is not None:
            self.sec_rows = m.get('sec_rows')
        if m.get('sec_cols') is not None:
            self.sec_cols = m.get('sec_cols')
        if m.get('sections') is not None:
            self.sections = [DocAnalysisSection().from_dict(i) for i in m.get('sections')]
        if m.get('long_division') is not None:
            self.long_division = [LongDivision().from_dict(i) for i in m.get('long_division')]
        if m.get('long_division_num') is not None:
            self.long_division_num = m.get('long_division_num')
        if m.get('underline') is not None:
            self.underline = [Underline().from_dict(i) for i in m.get('underline')]
        if m.get('pdf_file_size') is not None:
            self.pdf_file_size = m.get('pdf_file_size')
        return self
