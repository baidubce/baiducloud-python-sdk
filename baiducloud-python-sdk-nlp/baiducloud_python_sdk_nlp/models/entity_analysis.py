"""
EntityAnalysis information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_nlp.models.category import Category


class EntityAnalysis(AbstractModel):
    """
    EntityAnalysis
    """

    def __init__(self, mention=None, category=None, confidence=None, desc=None, status=None):
        """
        Initialize EntityAnalysis instance.

        :param mention: 识别出的实体
        :type mention: str (optional)

        :param category: category attribute
        :type category: Category (optional)

        :param confidence: 实体关联至该百科内容的置信度
        :type confidence: float (optional)

        :param desc: 实体的简介
        :type desc: str (optional)

        :param status: 用于对关联结果进行标识，包括LINKED（正常关联）、NIL（无关联内容）
        :type status: str (optional)
        """
        super().__init__()
        self.mention = mention
        self.category = category
        self.confidence = confidence
        self.desc = desc
        self.status = status

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
        if self.mention is not None:
            result['mention'] = self.mention
        if self.category is not None:
            result['category'] = self.category.to_dict()
        if self.confidence is not None:
            result['confidence'] = self.confidence
        if self.desc is not None:
            result['desc'] = self.desc
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EntityAnalysis

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('mention') is not None:
            self.mention = m.get('mention')
        if m.get('category') is not None:
            self.category = Category().from_dict(m.get('category'))
        if m.get('confidence') is not None:
            self.confidence = m.get('confidence')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
