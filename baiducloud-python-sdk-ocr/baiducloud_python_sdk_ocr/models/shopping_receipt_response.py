"""
Request entity for ShoppingReceiptResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ocr.models.shopping_receipt_words_result import ShoppingReceiptWordsResult


class ShoppingReceiptResponse(BceResponse):
    """
    ShoppingReceiptResponse
    """

    def __init__(self, log_id=None, error_code=None, error_msg=None, pdf_file_size=None, words_result=None):
        """
        Initialize ShoppingReceiptResponse response.

        :param log_id: 唯一的log id，用于问题定位
        :type log_id: int (optional)

        :param error_code: 错误码
        :type error_code: int (optional)

        :param error_msg: 错误信息
        :type error_msg: str (optional)

        :param pdf_file_size: 传入PDF文件的总页数，当pdf_file参数有效时返回该字段
        :type pdf_file_size: int (optional)

        :param words_result: 识别结果
        :type words_result: List[ShoppingReceiptWordsResult] (optional)
        """
        super().__init__()
        self.log_id = log_id
        self.error_code = error_code
        self.error_msg = error_msg
        self.pdf_file_size = pdf_file_size
        self.words_result = words_result

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
        if self.log_id is not None:
            result['log_id'] = self.log_id
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.pdf_file_size is not None:
            result['pdf_file_size'] = self.pdf_file_size
        if self.words_result is not None:
            result['words_result'] = [i.to_dict() for i in self.words_result]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ShoppingReceiptResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('log_id') is not None:
            self.log_id = m.get('log_id')
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_msg') is not None:
            self.error_msg = m.get('error_msg')
        if m.get('pdf_file_size') is not None:
            self.pdf_file_size = m.get('pdf_file_size')
        if m.get('words_result') is not None:
            self.words_result = [ShoppingReceiptWordsResult().from_dict(i) for i in m.get('words_result')]
        return self
