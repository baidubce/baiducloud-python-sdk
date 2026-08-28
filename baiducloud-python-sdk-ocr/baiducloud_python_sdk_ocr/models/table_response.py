"""
Request entity for TableResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ocr.models.tables_result import TablesResult


class TableResponse(BceResponse):
    """
    TableResponse
    """

    def __init__(
        self,
        error_code=None,
        error_msg=None,
        log_id=None,
        table_num=None,
        tables_result=None,
        pdf_file_size=None,
        excel_file=None,
    ):
        """
        Initialize TableResponse response.

        :param error_code: 错误码
        :type error_code: int (optional)

        :param error_msg: 错误信息
        :type error_msg: str (optional)

        :param log_id: 日志id，用于问题定位
        :type log_id: int (optional)

        :param table_num: 检测到的表格数量
        :type table_num: int (optional)

        :param tables_result: 表格内容
        :type tables_result: List[TablesResult] (optional)

        :param pdf_file_size: 传入PDF文件的总页数，当 pdf_file 参数有效时返回该字段
        :type pdf_file_size: int (optional)

        :param excel_file: 图像内表格转换为excel文件的base64编码，当 return_excel 参数为true时返回该字段
        :type excel_file: str (optional)
        """
        super().__init__()
        self.error_code = error_code
        self.error_msg = error_msg
        self.log_id = log_id
        self.table_num = table_num
        self.tables_result = tables_result
        self.pdf_file_size = pdf_file_size
        self.excel_file = excel_file

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
        if self.table_num is not None:
            result['table_num'] = self.table_num
        if self.tables_result is not None:
            result['tables_result'] = [i.to_dict() for i in self.tables_result]
        if self.pdf_file_size is not None:
            result['pdf_file_size'] = self.pdf_file_size
        if self.excel_file is not None:
            result['excel_file'] = self.excel_file
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TableResponse

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
        if m.get('table_num') is not None:
            self.table_num = m.get('table_num')
        if m.get('tables_result') is not None:
            self.tables_result = [TablesResult().from_dict(i) for i in m.get('tables_result')]
        if m.get('pdf_file_size') is not None:
            self.pdf_file_size = m.get('pdf_file_size')
        if m.get('excel_file') is not None:
            self.excel_file = m.get('excel_file')
        return self
