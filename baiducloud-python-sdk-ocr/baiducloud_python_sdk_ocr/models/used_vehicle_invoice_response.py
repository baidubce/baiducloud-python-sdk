"""
Request entity for UsedVehicleInvoiceResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ocr.models.used_vehicle_invoice_word_result import UsedVehicleInvoiceWordResult


class UsedVehicleInvoiceResponse(BceResponse):
    """
    UsedVehicleInvoiceResponse
    """

    def __init__(self, error_code=None, error_msg=None, log_id=None, direction=None, word_result=None):
        """
        Initialize UsedVehicleInvoiceResponse response.

        :param error_code: 错误码
        :type error_code: int (optional)

        :param error_msg: 错误描述信息
        :type error_msg: str (optional)

        :param log_id: 唯一的log id，用于问题定位
        :type log_id: int (optional)

        :param direction: 图像方向，-1：未定义，0：正向，1：逆时针90度，2：逆时针180度，3：逆时针270度
        :type direction: str (optional)

        :param word_result: word_result field
        :type word_result: UsedVehicleInvoiceWordResult (optional)
        """
        super().__init__()
        self.error_code = error_code
        self.error_msg = error_msg
        self.log_id = log_id
        self.direction = direction
        self.word_result = word_result

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
        if self.direction is not None:
            result['direction'] = self.direction
        if self.word_result is not None:
            result['word_result'] = self.word_result.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UsedVehicleInvoiceResponse

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
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('word_result') is not None:
            self.word_result = UsedVehicleInvoiceWordResult().from_dict(m.get('word_result'))
        return self
