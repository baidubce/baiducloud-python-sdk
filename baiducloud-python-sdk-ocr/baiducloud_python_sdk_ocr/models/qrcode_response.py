"""
Request entity for QrcodeResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ocr.models.codes_result import CodesResult


class QrcodeResponse(BceResponse):
    """
    QrcodeResponse
    """

    def __init__(self, error_code=None, error_msg=None, log_id=None, codes_result_num=None, codes_result=None):
        """
        Initialize QrcodeResponse response.

        :param error_code: 错误码
        :type error_code: int (optional)

        :param error_msg: 错误信息
        :type error_msg: str (optional)

        :param log_id: 唯一的log id，用于问题定位
        :type log_id: int (optional)

        :param codes_result_num: 识别结果数，表示codes_result的元素个数
        :type codes_result_num: int (optional)

        :param codes_result: 定位和识别结果数组
        :type codes_result: List[CodesResult] (optional)
        """
        super().__init__()
        self.error_code = error_code
        self.error_msg = error_msg
        self.log_id = log_id
        self.codes_result_num = codes_result_num
        self.codes_result = codes_result

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
        if self.codes_result_num is not None:
            result['codes_result_num'] = self.codes_result_num
        if self.codes_result is not None:
            result['codes_result'] = [i.to_dict() for i in self.codes_result]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QrcodeResponse

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
        if m.get('codes_result_num') is not None:
            self.codes_result_num = m.get('codes_result_num')
        if m.get('codes_result') is not None:
            self.codes_result = [CodesResult().from_dict(i) for i in m.get('codes_result')]
        return self
