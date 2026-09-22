"""
EyeStatus information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class EyeStatus(AbstractModel):
    """
    EyeStatus
    """

    def __init__(self, left_eye=None, right_eye=None):
        """
        Initialize EyeStatus instance.

        :param left_eye: 左眼状态，[0,1]，越接近0闭合可能性越大
        :type left_eye: float (optional)

        :param right_eye: 右眼状态，[0,1]，越接近0闭合可能性越大
        :type right_eye: float (optional)
        """
        super().__init__()
        self.left_eye = left_eye
        self.right_eye = right_eye

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
        if self.left_eye is not None:
            result['left_eye'] = self.left_eye
        if self.right_eye is not None:
            result['right_eye'] = self.right_eye
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EyeStatus

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('left_eye') is not None:
            self.left_eye = m.get('left_eye')
        if m.get('right_eye') is not None:
            self.right_eye = m.get('right_eye')
        return self
