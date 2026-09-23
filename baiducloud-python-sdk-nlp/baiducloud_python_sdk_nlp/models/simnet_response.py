"""
Request entity for SimnetResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_nlp.models.texts import Texts


class SimnetResponse(BceResponse):
    """
    SimnetResponse
    """

    def __init__(self, error_code=None, error_msg=None, log_id=None, score=None, texts=None):
        """
        Initialize SimnetResponse response.

        :param error_code: 错误码
        :type error_code: int (optional)

        :param error_msg: 错误信息
        :type error_msg: str (optional)

        :param log_id: 随机数，请求唯一标识码
        :type log_id: int (optional)

        :param score: 相似度结果取值(0,1]，分数越高说明相似度越高
        :type score: float (optional)

        :param texts: texts field
        :type texts: Texts (optional)
        """
        super().__init__()
        self.error_code = error_code
        self.error_msg = error_msg
        self.log_id = log_id
        self.score = score
        self.texts = texts

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
        if self.score is not None:
            result['score'] = self.score
        if self.texts is not None:
            result['texts'] = self.texts.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SimnetResponse

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
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('texts') is not None:
            self.texts = Texts().from_dict(m.get('texts'))
        return self
