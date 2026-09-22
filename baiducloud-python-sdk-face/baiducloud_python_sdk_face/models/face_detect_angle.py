"""
FaceDetectAngle information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FaceDetectAngle(AbstractModel):
    """
    FaceDetectAngle
    """

    def __init__(self, yaw=None, pitch=None, roll=None):
        """
        Initialize FaceDetectAngle instance.

        :param yaw:
        :type yaw: float (optional)

        :param pitch:
        :type pitch: float (optional)

        :param roll:
        :type roll: float (optional)
        """
        super().__init__()
        self.yaw = yaw
        self.pitch = pitch
        self.roll = roll

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
        if self.yaw is not None:
            result['yaw'] = self.yaw
        if self.pitch is not None:
            result['pitch'] = self.pitch
        if self.roll is not None:
            result['roll'] = self.roll
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceDetectAngle

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('yaw') is not None:
            self.yaw = m.get('yaw')
        if m.get('pitch') is not None:
            self.pitch = m.get('pitch')
        if m.get('roll') is not None:
            self.roll = m.get('roll')
        return self
