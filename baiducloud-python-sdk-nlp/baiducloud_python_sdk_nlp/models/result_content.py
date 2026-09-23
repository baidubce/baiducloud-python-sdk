"""
ResultContent information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_nlp.models.txt_monet_result import TxtMonetResult


class ResultContent(AbstractModel):
    """
    ResultContent
    """

    def __init__(self, content=None, results=None):
        """
        Initialize ResultContent instance.

        :param content: 原文本内容
        :type content: str (optional)

        :param results: 针对原文本提出的所有query的返回结果列表
        :type results: List[TxtMonetResult] (optional)
        """
        super().__init__()
        self.content = content
        self.results = results

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
        if self.content is not None:
            result['content'] = self.content
        if self.results is not None:
            result['results'] = [i.to_dict() for i in self.results]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ResultContent

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('results') is not None:
            self.results = [TxtMonetResult().from_dict(i) for i in m.get('results')]
        return self
