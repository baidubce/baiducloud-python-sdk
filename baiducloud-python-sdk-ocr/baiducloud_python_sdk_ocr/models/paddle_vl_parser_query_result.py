"""
PaddleVlParserQueryResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PaddleVlParserQueryResult(AbstractModel):
    """
    PaddleVlParserQueryResult
    """

    def __init__(self, task_id=None, status=None, task_error=None, markdown_url=None, parse_result_url=None):
        """
        Initialize PaddleVlParserQueryResult instance.

        :param task_id: 任务ID
        :type task_id: str (optional)

        :param status: 任务状态
        :type status: str (optional)

        :param task_error: 解析报错信息，包含任务失败、额度不够
        :type task_error: str (optional)

        :param markdown_url: 文档解析结果的markdown格式链接，链接有效期30天
        :type markdown_url: str (optional)

        :param parse_result_url: 文档解析结果的bos链接，链接有效期30天
        :type parse_result_url: str (optional)
        """
        super().__init__()
        self.task_id = task_id
        self.status = status
        self.task_error = task_error
        self.markdown_url = markdown_url
        self.parse_result_url = parse_result_url

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.task_id is not None:
            result['task_id'] = self.task_id
        if self.status is not None:
            result['status'] = self.status
        if self.task_error is not None:
            result['task_error'] = self.task_error
        if self.markdown_url is not None:
            result['markdown_url'] = self.markdown_url
        if self.parse_result_url is not None:
            result['parse_result_url'] = self.parse_result_url
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PaddleVlParserQueryResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('task_error') is not None:
            self.task_error = m.get('task_error')
        if m.get('markdown_url') is not None:
            self.markdown_url = m.get('markdown_url')
        if m.get('parse_result_url') is not None:
            self.parse_result_url = m.get('parse_result_url')
        return self
