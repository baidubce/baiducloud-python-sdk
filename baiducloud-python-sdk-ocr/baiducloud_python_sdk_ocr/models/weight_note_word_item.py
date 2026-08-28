"""
WeightNoteWordItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class WeightNoteWordItem(AbstractModel):
    """
    WeightNoteWordItem
    """

    def __init__(self, word=None, probability=None):
        """
        Initialize WeightNoteWordItem instance.

        :param word: 字段识别结果
        :type word: str (optional)

        :param probability: 字段识别结果置信度，当请求参数probability=true时返回
        :type probability: object (optional)
        """
        super().__init__()
        self.word = word
        self.probability = probability

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
        if self.word is not None:
            result['word'] = self.word
        if self.probability is not None:
            result['probability'] = self.probability
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: WeightNoteWordItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('word') is not None:
            self.word = m.get('word')
        if m.get('probability') is not None:
            self.probability = m.get('probability')
        return self
