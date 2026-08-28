"""
Request entity for WebImageLocResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ocr.models.web_image_loc_words_result import WebImageLocWordsResult


class WebImageLocResponse(BceResponse):
    """
    WebImageLocResponse
    """

    def __init__(
        self,
        error_code=None,
        error_msg=None,
        log_id=None,
        direction=None,
        words_result=None,
        words_result_num=None,
        pdf_file_size=None,
    ):
        """
        Initialize WebImageLocResponse response.

        :param error_code: 错误码
        :type error_code: int (optional)

        :param error_msg: 错误信息
        :type error_msg: str (optional)

        :param log_id: 唯一的log id，用于问题定位
        :type log_id: int (optional)

        :param direction: 图像方向，当 detect_direction=true 时返回该字段
        :type direction: int (optional)

        :param words_result: 识别结果数组
        :type words_result: List[WebImageLocWordsResult] (optional)

        :param words_result_num: 识别结果数，表示words_result的元素个数
        :type words_result_num: int (optional)

        :param pdf_file_size: 传入PDF文件的总页数，当 pdf_file 参数有效时返回该字段
        :type pdf_file_size: int (optional)
        """
        super().__init__()
        self.error_code = error_code
        self.error_msg = error_msg
        self.log_id = log_id
        self.direction = direction
        self.words_result = words_result
        self.words_result_num = words_result_num
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
        if self.direction is not None:
            result['direction'] = self.direction
        if self.words_result is not None:
            result['words_result'] = [i.to_dict() for i in self.words_result]
        if self.words_result_num is not None:
            result['words_result_num'] = self.words_result_num
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
        :rtype: WebImageLocResponse

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
        if m.get('words_result') is not None:
            self.words_result = [WebImageLocWordsResult().from_dict(i) for i in m.get('words_result')]
        if m.get('words_result_num') is not None:
            self.words_result_num = m.get('words_result_num')
        if m.get('pdf_file_size') is not None:
            self.pdf_file_size = m.get('pdf_file_size')
        return self
