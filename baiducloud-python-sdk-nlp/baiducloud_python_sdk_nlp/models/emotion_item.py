"""
EmotionItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_nlp.models.emotion_subitem import EmotionSubitem


class EmotionItem(AbstractModel):
    """
    EmotionItem
    """

    def __init__(self, label=None, prob=None, subitems=None, replies=None):
        """
        Initialize EmotionItem instance.

        :param label: 情绪一级分类标签；pessimistic（负向情绪）、neutral（中性情绪）、optimistic（正向情绪）
        :type label: str (optional)

        :param prob: 情绪一级分类标签对应的概率
        :type prob: float (optional)

        :param subitems: 二级分析结果数组
        :type subitems: List[EmotionSubitem] (optional)

        :param replies: 参考回复话术，中性情绪下该项为空
        :type replies: List[str] (optional)
        """
        super().__init__()
        self.label = label
        self.prob = prob
        self.subitems = subitems
        self.replies = replies

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
        if self.label is not None:
            result['label'] = self.label
        if self.prob is not None:
            result['prob'] = self.prob
        if self.subitems is not None:
            result['subitems'] = [i.to_dict() for i in self.subitems]
        if self.replies is not None:
            result['replies'] = self.replies
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EmotionItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('prob') is not None:
            self.prob = m.get('prob')
        if m.get('subitems') is not None:
            self.subitems = [EmotionSubitem().from_dict(i) for i in m.get('subitems')]
        if m.get('replies') is not None:
            self.replies = m.get('replies')
        return self
