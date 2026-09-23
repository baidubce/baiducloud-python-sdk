"""
SentimentClassifyItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SentimentClassifyItem(AbstractModel):
    """
    SentimentClassifyItem
    """

    def __init__(self, sentiment=None, confidence=None, positive_prob=None, negative_prob=None):
        """
        Initialize SentimentClassifyItem instance.

        :param sentiment: 表示情感极性分类结果，0:负向，1:中性，2:正向
        :type sentiment: int (optional)

        :param confidence: 表示分类的置信度，取值范围[0,1]
        :type confidence: float (optional)

        :param positive_prob: 表示属于积极类别的概率，取值范围[0,1]
        :type positive_prob: float (optional)

        :param negative_prob: 表示属于消极类别的概率，取值范围[0,1]
        :type negative_prob: float (optional)
        """
        super().__init__()
        self.sentiment = sentiment
        self.confidence = confidence
        self.positive_prob = positive_prob
        self.negative_prob = negative_prob

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
        if self.sentiment is not None:
            result['sentiment'] = self.sentiment
        if self.confidence is not None:
            result['confidence'] = self.confidence
        if self.positive_prob is not None:
            result['positive_prob'] = self.positive_prob
        if self.negative_prob is not None:
            result['negative_prob'] = self.negative_prob
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SentimentClassifyItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('sentiment') is not None:
            self.sentiment = m.get('sentiment')
        if m.get('confidence') is not None:
            self.confidence = m.get('confidence')
        if m.get('positive_prob') is not None:
            self.positive_prob = m.get('positive_prob')
        if m.get('negative_prob') is not None:
            self.negative_prob = m.get('negative_prob')
        return self
