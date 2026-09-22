"""
FaceMarkFaceInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_face.models.face_mark_location import FaceMarkLocation

from baiducloud_python_sdk_face.models.face_mark_angle import FaceMarkAngle

from baiducloud_python_sdk_face.models.gender import Gender

from baiducloud_python_sdk_face.models.face_mark_point import FaceMarkPoint


class FaceMarkFaceInfo(AbstractModel):
    """
    FaceMarkFaceInfo
    """

    def __init__(
        self,
        location=None,
        angle=None,
        age=None,
        gender=None,
        landmark72=None,
        landmark150=None,
        landmark201=None,
        face_token=None,
        face_probability=None,
    ):
        """
        Initialize FaceMarkFaceInfo instance.

        :param location: location attribute
        :type location: FaceMarkLocation (optional)

        :param angle: angle attribute
        :type angle: FaceMarkAngle (optional)

        :param age: 年龄，face_field包含age时返回
        :type age: float (optional)

        :param gender: gender attribute
        :type gender: Gender (optional)

        :param landmark72: 72个特征点位置，face_field包含landmark72时返回
        :type landmark72: List[FaceMarkPoint] (optional)

        :param landmark150: 150个特征点位置，face_field包含landmark150时返回
        :type landmark150: object (optional)

        :param landmark201: 201个特征点位置，face_field包含landmark201时返回
        :type landmark201: object (optional)

        :param face_token: 人脸标志
        :type face_token: str (optional)

        :param face_probability: 人脸置信度，范围0-1
        :type face_probability: float (optional)
        """
        super().__init__()
        self.location = location
        self.angle = angle
        self.age = age
        self.gender = gender
        self.landmark72 = landmark72
        self.landmark150 = landmark150
        self.landmark201 = landmark201
        self.face_token = face_token
        self.face_probability = face_probability

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
        if self.angle is not None:
            result['angle'] = self.angle.to_dict()
        if self.age is not None:
            result['age'] = self.age
        if self.gender is not None:
            result['gender'] = self.gender.to_dict()
        if self.landmark72 is not None:
            result['landmark72'] = [i.to_dict() for i in self.landmark72]
        if self.landmark150 is not None:
            result['landmark150'] = self.landmark150
        if self.landmark201 is not None:
            result['landmark201'] = self.landmark201
        if self.face_token is not None:
            result['face_token'] = self.face_token
        if self.face_probability is not None:
            result['face_probability'] = self.face_probability
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceMarkFaceInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('location') is not None:
            self.location = FaceMarkLocation().from_dict(m.get('location'))
        if m.get('angle') is not None:
            self.angle = FaceMarkAngle().from_dict(m.get('angle'))
        if m.get('age') is not None:
            self.age = m.get('age')
        if m.get('gender') is not None:
            self.gender = Gender().from_dict(m.get('gender'))
        if m.get('landmark72') is not None:
            self.landmark72 = [FaceMarkPoint().from_dict(i) for i in m.get('landmark72')]
        if m.get('landmark150') is not None:
            self.landmark150 = m.get('landmark150')
        if m.get('landmark201') is not None:
            self.landmark201 = m.get('landmark201')
        if m.get('face_token') is not None:
            self.face_token = m.get('face_token')
        if m.get('face_probability') is not None:
            self.face_probability = m.get('face_probability')
        return self
