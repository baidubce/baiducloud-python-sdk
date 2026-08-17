"""
Request entity for MedicalRecordResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ocr.models.medical_record_words_result import MedicalRecordWordsResult


class MedicalRecordResponse(BceResponse):
    """
    MedicalRecordResponse
    """

    def __init__(
        self, error_code=None, error_msg=None, log_id=None, words_result_num=None, invoice_type=None, words_result=None
    ):
        """
        Initialize MedicalRecordResponse response.

        :param error_code: 错误码
        :type error_code: int (optional)

        :param error_msg: 错误描述信息
        :type error_msg: str (optional)

        :param log_id: 唯一的log id，用于问题定位
        :type log_id: int (optional)

        :param words_result_num: 识别结果数，表示words_result的元素个数
        :type words_result_num: int (optional)

        :param invoice_type: 票据种类
        :type invoice_type: str (optional)

        :param words_result: words_result field
        :type words_result: MedicalRecordWordsResult (optional)
        """
        super().__init__()
        self.error_code = error_code
        self.error_msg = error_msg
        self.log_id = log_id
        self.words_result_num = words_result_num
        self.invoice_type = invoice_type
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
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.log_id is not None:
            result['log_id'] = self.log_id
        if self.words_result_num is not None:
            result['words_result_num'] = self.words_result_num
        if self.invoice_type is not None:
            result['InvoiceType'] = self.invoice_type
        if self.words_result is not None:
            result['words_result'] = self.words_result.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MedicalRecordResponse

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
        if m.get('words_result_num') is not None:
            self.words_result_num = m.get('words_result_num')
        if m.get('InvoiceType') is not None:
            self.invoice_type = m.get('InvoiceType')
        if m.get('words_result') is not None:
            self.words_result = MedicalRecordWordsResult().from_dict(m.get('words_result'))
        return self
