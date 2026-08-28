"""
DivorceCertificateResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class DivorceCertificateResponse(BceResponse):
    """
    DivorceCertificateResponse
    """

    def __init__(
        self,
        error_code=None,
        error_msg=None,
        log_id=None,
        pdf_file_size=None,
        words_result_num=None,
        words_result=None,
    ):
        """
        Initialize DivorceCertificateResponse instance.

        :param error_code: 错误码
        :type error_code: int (optional)

        :param error_msg: 错误信息
        :type error_msg: str (optional)

        :param log_id: 唯一的log id，用于问题定位
        :type log_id: int (optional)

        :param pdf_file_size: 传入PDF文件的总页数，当pdf_file参数有效时返回该字段
        :type pdf_file_size: int (optional)

        :param words_result_num: 识别结果数，表示words_result的元素个数
        :type words_result_num: int (optional)

        :param words_result: 识别结果，key为字段名（如：姓名_男、身份证件号_女等），value为识别内容数组
        :type words_result: object (optional)
        """
        super().__init__()
        self.error_code = error_code
        self.error_msg = error_msg
        self.log_id = log_id
        self.pdf_file_size = pdf_file_size
        self.words_result_num = words_result_num
        self.words_result = words_result

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
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
        if self.pdf_file_size is not None:
            result['pdf_file_size'] = self.pdf_file_size
        if self.words_result_num is not None:
            result['words_result_num'] = self.words_result_num
        if self.words_result is not None:
            result['words_result'] = self.words_result
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DivorceCertificateResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('log_id') is not None:
            self.log_id = m.get('log_id')
        if m.get('pdf_file_size') is not None:
            self.pdf_file_size = m.get('pdf_file_size')
        if m.get('words_result_num') is not None:
            self.words_result_num = m.get('words_result_num')
        if m.get('words_result') is not None:
            self.words_result = m.get('words_result')
        return self
