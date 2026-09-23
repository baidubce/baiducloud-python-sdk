"""
Request entity for EntityAnalysisRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class EntityAnalysisRequest(AbstractModel):
    """
    Request entity for EntityAnalysisRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, text, mention=None):
        """
        Initialize EntityAnalysisRequest request entity.

        :param text: 需要进行实体分析的文本，最多128个汉字
        :type text: str (required)

        :param mention: 输入需要指定分析的实体
        :type mention: str (optional)
        """
        super().__init__()
        self.text = text
        self.mention = mention

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.text is not None:
            result['text'] = self.text
        if self.mention is not None:
            result['mention'] = self.mention
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EntityAnalysisRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('mention') is not None:
            self.mention = m.get('mention')
        return self
