"""
TagSelector information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_oos.models.tag_expression import TagExpression


class TagSelector(AbstractModel):
    """
    TagSelector
    """

    def __init__(self, expressions=None):
        """
        Initialize TagSelector instance.

        :param expressions: 标签匹配表达式列表
        :type expressions: List[TagExpression] (optional)
        """
        super().__init__()
        self.expressions = expressions

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
        if self.expressions is not None:
            result['expressions'] = [i.to_dict() for i in self.expressions]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TagSelector

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('expressions') is not None:
            self.expressions = [TagExpression().from_dict(i) for i in m.get('expressions')]
        return self
