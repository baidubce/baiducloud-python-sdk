"""
Request entity for DocAnalysisOfficeResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ocr.models.doc_analysis_office_result import DocAnalysisOfficeResult
from baiducloud_python_sdk_ocr.models.doc_analysis_office_layout import DocAnalysisOfficeLayout
from baiducloud_python_sdk_ocr.models.doc_analysis_office_section import DocAnalysisOfficeSection
from baiducloud_python_sdk_ocr.models.table_result import TableResult
from baiducloud_python_sdk_ocr.models.seal_recog_result import SealRecogResult
from baiducloud_python_sdk_ocr.models.formula_result import FormulaResult


class DocAnalysisOfficeResponse(BceResponse):
    """
    DocAnalysisOfficeResponse
    """

    def __init__(
        self,
        error_code=None,
        error_msg=None,
        log_id=None,
        img_direction=None,
        results_num=None,
        results=None,
        layouts_num=None,
        layouts=None,
        sec_rows=None,
        sec_cols=None,
        sections=None,
        table_num=None,
        tables_result=None,
        seal_recog_num=None,
        seal_recog_results=None,
        formula_result=None,
        underline=None,
        pdf_file_size=None,
        ofd_file_size=None,
    ):
        """
        Initialize DocAnalysisOfficeResponse response.

        :param error_code: 错误码
        :type error_code: int (optional)

        :param error_msg: 错误信息
        :type error_msg: str (optional)

        :param log_id: 唯一的log id，用于问题定位
        :type log_id: int (optional)

        :param img_direction: img_direction field
        :type img_direction: int (optional)

        :param results_num: 识别结果数，表示results的元素个数
        :type results_num: int (optional)

        :param results: 识别结果数组
        :type results: List[DocAnalysisOfficeResult] (optional)

        :param layouts_num: 版面分析结果数，layout_analysis=true时返回
        :type layouts_num: int (optional)

        :param layouts: 文档版面模块数组，layout_analysis=true时返回
        :type layouts: List[DocAnalysisOfficeLayout] (optional)

        :param sec_rows: 将所有的版面中的「栏:section」内容表示成 M x N 的网格，sec_rows = M
        :type sec_rows: int (optional)

        :param sec_cols: 将所有的版面中的「分栏」内容表示成 M x N 的网格，sec_cols = N
        :type sec_cols: int (optional)

        :param sections: 一张图片中包含的5大版面属性，layout_analysis=true时返回
        :type sections: List[DocAnalysisOfficeSection] (optional)

        :param table_num: 检测到的表格数量，当recg_tables=true时返回
        :type table_num: int (optional)

        :param tables_result: 每个表格的内容数组，当recg_tables=true时返回
        :type tables_result: List[TableResult] (optional)

        :param seal_recog_num: 识别到的印章结果数，当recog_seal=true时返回
        :type seal_recog_num: int (optional)

        :param seal_recog_results: 印章内容数组，当recog_seal=true时返回
        :type seal_recog_results: List[SealRecogResult] (optional)

        :param formula_result: 识别到的公式数组，当 recg_formula=true 时返回
        :type formula_result: List[FormulaResult] (optional)

        :param underline: 识别到的下划线数组
        :type underline: List[object] (optional)

        :param pdf_file_size: 传入PDF文件的总页数，当 pdf_file 参数有效时返回该字段
        :type pdf_file_size: int (optional)

        :param ofd_file_size: 传入OFD文件的总页数，当 ofd_file 参数有效时返回该字段
        :type ofd_file_size: str (optional)
        """
        super().__init__()
        self.error_code = error_code
        self.error_msg = error_msg
        self.log_id = log_id
        self.img_direction = img_direction
        self.results_num = results_num
        self.results = results
        self.layouts_num = layouts_num
        self.layouts = layouts
        self.sec_rows = sec_rows
        self.sec_cols = sec_cols
        self.sections = sections
        self.table_num = table_num
        self.tables_result = tables_result
        self.seal_recog_num = seal_recog_num
        self.seal_recog_results = seal_recog_results
        self.formula_result = formula_result
        self.underline = underline
        self.pdf_file_size = pdf_file_size
        self.ofd_file_size = ofd_file_size

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
        if self.table_num is not None:
            result['table_num'] = self.table_num
        if self.tables_result is not None:
            result['tables_result'] = [i.to_dict() for i in self.tables_result]
        if self.seal_recog_num is not None:
            result['seal_recog_num'] = self.seal_recog_num
        if self.seal_recog_results is not None:
            result['seal_recog_results'] = [i.to_dict() for i in self.seal_recog_results]
        if self.formula_result is not None:
            result['formula_result'] = [i.to_dict() for i in self.formula_result]
        if self.underline is not None:
            result['underline'] = self.underline
        if self.pdf_file_size is not None:
            result['pdf_file_size'] = self.pdf_file_size
        if self.ofd_file_size is not None:
            result['ofd_file_size'] = self.ofd_file_size
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DocAnalysisOfficeResponse

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
            self.results = [DocAnalysisOfficeResult().from_dict(i) for i in m.get('results')]
        if m.get('layouts_num') is not None:
            self.layouts_num = m.get('layouts_num')
        if m.get('layouts') is not None:
            self.layouts = [DocAnalysisOfficeLayout().from_dict(i) for i in m.get('layouts')]
        if m.get('sec_rows') is not None:
            self.sec_rows = m.get('sec_rows')
        if m.get('sec_cols') is not None:
            self.sec_cols = m.get('sec_cols')
        if m.get('sections') is not None:
            self.sections = [DocAnalysisOfficeSection().from_dict(i) for i in m.get('sections')]
        if m.get('table_num') is not None:
            self.table_num = m.get('table_num')
        if m.get('tables_result') is not None:
            self.tables_result = [TableResult().from_dict(i) for i in m.get('tables_result')]
        if m.get('seal_recog_num') is not None:
            self.seal_recog_num = m.get('seal_recog_num')
        if m.get('seal_recog_results') is not None:
            self.seal_recog_results = [SealRecogResult().from_dict(i) for i in m.get('seal_recog_results')]
        if m.get('formula_result') is not None:
            self.formula_result = [FormulaResult().from_dict(i) for i in m.get('formula_result')]
        if m.get('underline') is not None:
            self.underline = m.get('underline')
        if m.get('pdf_file_size') is not None:
            self.pdf_file_size = m.get('pdf_file_size')
        if m.get('ofd_file_size') is not None:
            self.ofd_file_size = m.get('ofd_file_size')
        return self
