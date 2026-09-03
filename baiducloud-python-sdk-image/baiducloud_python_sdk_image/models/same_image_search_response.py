"""
SameImageSearchResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse

from baiducloud_python_sdk_image.models.search_result import SearchResult


class SameImageSearchResponse(BceResponse):
    """
    SameImageSearchResponse
    """

    def __init__(self, error_code=None, error_msg=None, log_id=None, result_num=None, result=None, has_more=None):
        """
        Initialize SameImageSearchResponse instance.

        :param error_code: 错误码
        :type error_code: int (optional)

        :param error_msg: 错误信息
        :type error_msg: str (optional)

        :param log_id: 唯一的log id，用于问题定位
        :type log_id: int (optional)

        :param result_num: 检索结果数
        :type result_num: int (optional)

        :param result: 结果数组
        :type result: List[SearchResult] (optional)

        :param has_more: 是否还有下一页
        :type has_more: bool (optional)
        """
        super().__init__()
        self.error_code = error_code
        self.error_msg = error_msg
        self.log_id = log_id
        self.result_num = result_num
        self.result = result
        self.has_more = has_more

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
        if self.result_num is not None:
            result['result_num'] = self.result_num
        if self.result is not None:
            result['result'] = [i.to_dict() for i in self.result]
        if self.has_more is not None:
            result['has_more'] = self.has_more
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SameImageSearchResponse

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
        if m.get('result_num') is not None:
            self.result_num = m.get('result_num')
        if m.get('result') is not None:
            self.result = [SearchResult().from_dict(i) for i in m.get('result')]
        if m.get('has_more') is not None:
            self.has_more = m.get('has_more')
        return self
