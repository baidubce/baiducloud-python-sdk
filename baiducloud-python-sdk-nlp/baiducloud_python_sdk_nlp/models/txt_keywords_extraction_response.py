"""
Request entity for TxtKeywordsExtractionResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_nlp.models.txt_keywords_extraction_result import TxtKeywordsExtractionResult


class TxtKeywordsExtractionResponse(BceResponse):
    """
    TxtKeywordsExtractionResponse
    """

    def __init__(self, error_code=None, error_msg=None, log_id=None, results=None):
        """
        Initialize TxtKeywordsExtractionResponse response.

        :param error_code: 错误码
        :type error_code: int (optional)

        :param error_msg: 错误信息
        :type error_msg: str (optional)

        :param log_id: 请求唯一标识码
        :type log_id: int (optional)

        :param results: 关键词提取结果的数组集合
        :type results: List[TxtKeywordsExtractionResult] (optional)
        """
        super().__init__()
        self.error_code = error_code
        self.error_msg = error_msg
        self.log_id = log_id
        self.results = results

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
        if self.results is not None:
            result['results'] = [i.to_dict() for i in self.results]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TxtKeywordsExtractionResponse

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
        if m.get('results') is not None:
            self.results = [TxtKeywordsExtractionResult().from_dict(i) for i in m.get('results')]
        return self
