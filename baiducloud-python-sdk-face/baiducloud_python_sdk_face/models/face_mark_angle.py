"""
FaceMarkAngle information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FaceMarkAngle(AbstractModel):
    """
    FaceMarkAngle
    """

    def __init__(self, yaw=None, pitch=None, roll=None):
        """
        Initialize FaceMarkAngle instance.

        :param yaw: 三维旋转之左右旋转角[-90(左), 90(右)]
        :type yaw: float (optional)

        :param pitch: 三维旋转之俯仰角度[-90(上), 90(下)]
        :type pitch: float (optional)

        :param roll: 平面内旋转角[-180(逆时针), 180(顺时针)]
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
        :rtype: FaceMarkAngle

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
