"""
HkMacauTaiwanExitentrypermitResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse

from baiducloud_python_sdk_ocr.models.hk_macau_taiwan_exitentrypermit_result import HkMacauTaiwanExitentrypermitResult


class HkMacauTaiwanExitentrypermitResponse(BceResponse):
    """
    HkMacauTaiwanExitentrypermitResponse
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
        Initialize HkMacauTaiwanExitentrypermitResponse instance.

        :param error_code: 错误码
        :type error_code: int (optional)

        :param error_msg: 错误信息
        :type error_msg: str (optional)

        :param log_id: 唯一的log id，用于问题定位
        :type log_id: int (optional)

        :param pdf_file_size: PDF文件总页数（可选）
        :type pdf_file_size: int (optional)

        :param words_result_num: 识别结果数
        :type words_result_num: int (optional)

        :param words_result: words_result attribute
        :type words_result: HkMacauTaiwanExitentrypermitResult (optional)
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
            result['words_result'] = self.words_result.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HkMacauTaiwanExitentrypermitResponse

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
            self.words_result = HkMacauTaiwanExitentrypermitResult().from_dict(m.get('words_result'))
        return self
