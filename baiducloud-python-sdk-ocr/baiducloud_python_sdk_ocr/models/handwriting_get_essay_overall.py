"""
HandwritingGetEssayOverall information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class HandwritingGetEssayOverall(AbstractModel):
    """
    HandwritingGetEssayOverall
    """

    def __init__(self, title_text=None, content_text=None):
        """
        Initialize HandwritingGetEssayOverall instance.

        :param title_text: 作文题目文本
        :type title_text: str (optional)

        :param content_text: 作文正文文本
        :type content_text: str (optional)
        """
        super().__init__()
        self.title_text = title_text
        self.content_text = content_text

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
        if self.title_text is not None:
            result['titleText'] = self.title_text
        if self.content_text is not None:
            result['contentText'] = self.content_text
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: HandwritingGetEssayOverall

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('titleText') is not None:
            self.title_text = m.get('titleText')
        if m.get('contentText') is not None:
            self.content_text = m.get('contentText')
        return self
