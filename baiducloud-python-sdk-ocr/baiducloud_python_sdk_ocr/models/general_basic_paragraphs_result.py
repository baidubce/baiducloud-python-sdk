"""
GeneralBasicParagraphsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GeneralBasicParagraphsResult(AbstractModel):
    """
    GeneralBasicParagraphsResult
    """

    def __init__(self, words_result_idx=None):
        """
        Initialize GeneralBasicParagraphsResult instance.

        :param words_result_idx: 一个段落包含的行序号，当 paragraph=true 时返回该字段
        :type words_result_idx: List[int] (optional)
        """
        super().__init__()
        self.words_result_idx = words_result_idx

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
        if self.words_result_idx is not None:
            result['words_result_idx'] = self.words_result_idx
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GeneralBasicParagraphsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('words_result_idx') is not None:
            self.words_result_idx = m.get('words_result_idx')
        return self
