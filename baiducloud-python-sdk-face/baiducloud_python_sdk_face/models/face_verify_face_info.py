"""
FaceVerifyFaceInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_face.models.face_verify_location import FaceVerifyLocation

from baiducloud_python_sdk_face.models.face_verify_angle import FaceVerifyAngle

from baiducloud_python_sdk_face.models.face_verify_type_probability import FaceVerifyTypeProbability

from baiducloud_python_sdk_face.models.face_verify_type_probability import FaceVerifyTypeProbability

from baiducloud_python_sdk_face.models.face_verify_type_probability import FaceVerifyTypeProbability

from baiducloud_python_sdk_face.models.face_verify_type_probability import FaceVerifyTypeProbability

from baiducloud_python_sdk_face.models.face_verify_type_probability import FaceVerifyTypeProbability

from baiducloud_python_sdk_face.models.face_verify_point import FaceVerifyPoint

from baiducloud_python_sdk_face.models.face_verify_point import FaceVerifyPoint

from baiducloud_python_sdk_face.models.face_verify_quality import FaceVerifyQuality

from baiducloud_python_sdk_face.models.face_verify_liveness import FaceVerifyLiveness


class FaceVerifyFaceInfo(AbstractModel):
    """
    FaceVerifyFaceInfo
    """

    def __init__(
        self,
        face_token=None,
        location=None,
        face_probability=None,
        angle=None,
        age=None,
        expression=None,
        face_shape=None,
        gender=None,
        glasses=None,
        face_type=None,
        landmark=None,
        landmark72=None,
        quality=None,
        liveness=None,
        beauty=None,
        spoofing=None,
        not_spoofing=None,
    ):
        """
        Initialize FaceVerifyFaceInfo instance.

        :param face_token: 人脸图片的唯一标识
        :type face_token: str (optional)

        :param location: location attribute
        :type location: FaceVerifyLocation (optional)

        :param face_probability: 人脸置信度，范围【0~1】，代表这是一张人脸的概率，0最小、1最大
        :type face_probability: float (optional)

        :param angle: angle attribute
        :type angle: FaceVerifyAngle (optional)

        :param age: 年龄，当face_field包含age时返回
        :type age: float (optional)

        :param expression: expression attribute
        :type expression: FaceVerifyTypeProbability (optional)

        :param face_shape: face_shape attribute
        :type face_shape: FaceVerifyTypeProbability (optional)

        :param gender: gender attribute
        :type gender: FaceVerifyTypeProbability (optional)

        :param glasses: glasses attribute
        :type glasses: FaceVerifyTypeProbability (optional)

        :param face_type: face_type attribute
        :type face_type: FaceVerifyTypeProbability (optional)

        :param landmark: 4个关键点位置，左眼中心、右眼中心、鼻尖、嘴中心。face_field包含landmark时返回
        :type landmark: List[FaceVerifyPoint] (optional)

        :param landmark72: 72个特征点位置，face_field包含landmark时返回
        :type landmark72: List[FaceVerifyPoint] (optional)

        :param quality: quality attribute
        :type quality: FaceVerifyQuality (optional)

        :param liveness: liveness attribute
        :type liveness: FaceVerifyLiveness (optional)

        :param beauty: 美丑打分，范围[0~100]，越大表示越美，face_field包含beauty时返回
        :type beauty: float (optional)

        :param spoofing: 判断图片是合成图的概率，face_field包含spoofing时返回
        :type spoofing: float (optional)

        :param not_spoofing: 判断图片不是合成图的概率
        :type not_spoofing: float (optional)
        """
        super().__init__()
        self.face_token = face_token
        self.location = location
        self.face_probability = face_probability
        self.angle = angle
        self.age = age
        self.expression = expression
        self.face_shape = face_shape
        self.gender = gender
        self.glasses = glasses
        self.face_type = face_type
        self.landmark = landmark
        self.landmark72 = landmark72
        self.quality = quality
        self.liveness = liveness
        self.beauty = beauty
        self.spoofing = spoofing
        self.not_spoofing = not_spoofing

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
        if self.face_token is not None:
            result['face_token'] = self.face_token
        if self.location is not None:
            result['location'] = self.location.to_dict()
        if self.face_probability is not None:
            result['face_probability'] = self.face_probability
        if self.angle is not None:
            result['angle'] = self.angle.to_dict()
        if self.age is not None:
            result['age'] = self.age
        if self.expression is not None:
            result['expression'] = self.expression.to_dict()
        if self.face_shape is not None:
            result['face_shape'] = self.face_shape.to_dict()
        if self.gender is not None:
            result['gender'] = self.gender.to_dict()
        if self.glasses is not None:
            result['glasses'] = self.glasses.to_dict()
        if self.face_type is not None:
            result['face_type'] = self.face_type.to_dict()
        if self.landmark is not None:
            result['landmark'] = [i.to_dict() for i in self.landmark]
        if self.landmark72 is not None:
            result['landmark72'] = [i.to_dict() for i in self.landmark72]
        if self.quality is not None:
            result['quality'] = self.quality.to_dict()
        if self.liveness is not None:
            result['liveness'] = self.liveness.to_dict()
        if self.beauty is not None:
            result['beauty'] = self.beauty
        if self.spoofing is not None:
            result['spoofing'] = self.spoofing
        if self.not_spoofing is not None:
            result['not_spoofing'] = self.not_spoofing
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceVerifyFaceInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('face_token') is not None:
            self.face_token = m.get('face_token')
        if m.get('location') is not None:
            self.location = FaceVerifyLocation().from_dict(m.get('location'))
        if m.get('face_probability') is not None:
            self.face_probability = m.get('face_probability')
        if m.get('angle') is not None:
            self.angle = FaceVerifyAngle().from_dict(m.get('angle'))
        if m.get('age') is not None:
            self.age = m.get('age')
        if m.get('expression') is not None:
            self.expression = FaceVerifyTypeProbability().from_dict(m.get('expression'))
        if m.get('face_shape') is not None:
            self.face_shape = FaceVerifyTypeProbability().from_dict(m.get('face_shape'))
        if m.get('gender') is not None:
            self.gender = FaceVerifyTypeProbability().from_dict(m.get('gender'))
        if m.get('glasses') is not None:
            self.glasses = FaceVerifyTypeProbability().from_dict(m.get('glasses'))
        if m.get('face_type') is not None:
            self.face_type = FaceVerifyTypeProbability().from_dict(m.get('face_type'))
        if m.get('landmark') is not None:
            self.landmark = [FaceVerifyPoint().from_dict(i) for i in m.get('landmark')]
        if m.get('landmark72') is not None:
            self.landmark72 = [FaceVerifyPoint().from_dict(i) for i in m.get('landmark72')]
        if m.get('quality') is not None:
            self.quality = FaceVerifyQuality().from_dict(m.get('quality'))
        if m.get('liveness') is not None:
            self.liveness = FaceVerifyLiveness().from_dict(m.get('liveness'))
        if m.get('beauty') is not None:
            self.beauty = m.get('beauty')
        if m.get('spoofing') is not None:
            self.spoofing = m.get('spoofing')
        if m.get('not_spoofing') is not None:
            self.not_spoofing = m.get('not_spoofing')
        return self
