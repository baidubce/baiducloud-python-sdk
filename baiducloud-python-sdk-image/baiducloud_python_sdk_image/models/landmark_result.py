"""
LandmarkResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class LandmarkResult(AbstractModel):
    """
    LandmarkResult
    """

    def __init__(self, landmark=None):
        """
        Initialize LandmarkResult instance.

        :param landmark: 地标名称
        :type landmark: str (optional)
        """
        super().__init__()
        self.landmark = landmark

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
        if self.landmark is not None:
            result['landmark'] = self.landmark
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: LandmarkResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('landmark') is not None:
            self.landmark = m.get('landmark')
        return self
