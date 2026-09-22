"""
FaceRegResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_face.models.face_location import FaceLocation


class FaceRegResult(AbstractModel):
    """
    FaceRegResult
    """

    def __init__(self, location=None, face_token=None):
        """
        Initialize FaceRegResult instance.

        :param location: location attribute
        :type location: FaceLocation (optional)

        :param face_token: 人脸图片的唯一标识，有效期永久
        :type face_token: str (optional)
        """
        super().__init__()
        self.location = location
        self.face_token = face_token

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
        if self.location is not None:
            result['location'] = self.location.to_dict()
        if self.face_token is not None:
            result['face_token'] = self.face_token
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceRegResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('location') is not None:
            self.location = FaceLocation().from_dict(m.get('location'))
        if m.get('face_token') is not None:
            self.face_token = m.get('face_token')
        return self
