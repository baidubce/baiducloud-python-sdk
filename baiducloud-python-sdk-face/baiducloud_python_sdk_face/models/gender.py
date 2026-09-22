"""
Gender information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Gender(AbstractModel):
    """
    Gender
    """

    def __init__(self, type=None, probability=None):
        """
        Initialize Gender instance.

        :param type: male:男性 female:女性
        :type type: str (optional)

        :param probability: 性别置信度，范围0~1
        :type probability: float (optional)
        """
        super().__init__()
        self.type = type
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
        if self.type is not None:
            result['type'] = self.type
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
        :rtype: Gender

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('probability') is not None:
            self.probability = m.get('probability')
        return self
