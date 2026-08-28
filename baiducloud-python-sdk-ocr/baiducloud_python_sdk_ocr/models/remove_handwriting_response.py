"""
Request entity for RemoveHandwritingResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class RemoveHandwritingResponse(BceResponse):
    """
    RemoveHandwritingResponse
    """

    def __init__(self, log_id=None, error_code=None, error_msg=None, image_processed=None, pdf_file_size=None):
        """
        Initialize RemoveHandwritingResponse response.

        :param log_id: 唯一的log id，用于问题定位
        :type log_id: int (optional)

        :param error_code: 错误码
        :type error_code: int (optional)

        :param error_msg: 错误信息
        :type error_msg: str (optional)

        :param image_processed: 返回处理后的图片，base64编码
        :type image_processed: str (optional)

        :param pdf_file_size: 传入PDF文件的总页数，当 pdf_file 参数有效时返回该字段
        :type pdf_file_size: int (optional)
        """
        super().__init__()
        self.log_id = log_id
        self.error_code = error_code
        self.error_msg = error_msg
        self.image_processed = image_processed
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
        if self.log_id is not None:
            result['log_id'] = self.log_id
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_msg is not None:
            result['error_msg'] = self.error_msg
        if self.image_processed is not None:
            result['image_processed'] = self.image_processed
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
        :rtype: RemoveHandwritingResponse

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
        if m.get('image_processed') is not None:
            self.image_processed = m.get('image_processed')
        if m.get('pdf_file_size') is not None:
            self.pdf_file_size = m.get('pdf_file_size')
        return self
