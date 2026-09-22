"""
FaceDetectFaceInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_face.models.face_detect_location import FaceDetectLocation

from baiducloud_python_sdk_face.models.face_detect_angle import FaceDetectAngle

from baiducloud_python_sdk_face.models.face_detect_type_probability import FaceDetectTypeProbability

from baiducloud_python_sdk_face.models.face_detect_type_probability import FaceDetectTypeProbability

from baiducloud_python_sdk_face.models.face_detect_type_probability import FaceDetectTypeProbability

from baiducloud_python_sdk_face.models.face_detect_type_probability import FaceDetectTypeProbability

from baiducloud_python_sdk_face.models.mask_info import MaskInfo

from baiducloud_python_sdk_face.models.face_detect_point import FaceDetectPoint

from baiducloud_python_sdk_face.models.face_detect_point import FaceDetectPoint

from baiducloud_python_sdk_face.models.face_detect_quality import FaceDetectQuality

from baiducloud_python_sdk_face.models.face_detect_liveness import FaceDetectLiveness

from baiducloud_python_sdk_face.models.face_detect_type_probability import FaceDetectTypeProbability

from baiducloud_python_sdk_face.models.eye_status import EyeStatus

from baiducloud_python_sdk_face.models.face_detect_type_probability import FaceDetectTypeProbability


class FaceDetectFaceInfo(AbstractModel):
    """
    FaceDetectFaceInfo
    """

    def __init__(
        self,
        location=None,
        angle=None,
        age=None,
        expression=None,
        gender=None,
        glasses=None,
        emotion=None,
        mask=None,
        landmark=None,
        landmark72=None,
        landmark150=None,
        quality=None,
        liveness=None,
        spoofing=None,
        face_token=None,
        face_probability=None,
        face_shape=None,
        eye_status=None,
        face_type=None,
        not_spoofing=None,
    ):
        """
        Initialize FaceDetectFaceInfo instance.

        :param location: location attribute
        :type location: FaceDetectLocation (optional)

        :param angle: angle attribute
        :type angle: FaceDetectAngle (optional)

        :param age: 年龄，face_field包含age时返回
        :type age: float (optional)

        :param expression: expression attribute
        :type expression: FaceDetectTypeProbability (optional)

        :param gender: gender attribute
        :type gender: FaceDetectTypeProbability (optional)

        :param glasses: glasses attribute
        :type glasses: FaceDetectTypeProbability (optional)

        :param emotion: emotion attribute
        :type emotion: FaceDetectTypeProbability (optional)

        :param mask: mask attribute
        :type mask: MaskInfo (optional)

        :param landmark: 4个关键点位置，face_field包含landmark时返回
        :type landmark: List[FaceDetectPoint] (optional)

        :param landmark72: 72个特征点位置，face_field包含landmark时返回
        :type landmark72: List[FaceDetectPoint] (optional)

        :param landmark150: 150个特征点位置，face_field包含landmark150时返回
        :type landmark150: object (optional)

        :param quality: quality attribute
        :type quality: FaceDetectQuality (optional)

        :param liveness: liveness attribute
        :type liveness: FaceDetectLiveness (optional)

        :param spoofing: 判断图片是合成图的概率
        :type spoofing: float (optional)

        :param face_token: 人脸图片的唯一标识，有效期60min
        :type face_token: str (optional)

        :param face_probability: 人脸置信度，范围0~1
        :type face_probability: float (optional)

        :param face_shape: face_shape attribute
        :type face_shape: FaceDetectTypeProbability (optional)

        :param eye_status: eye_status attribute
        :type eye_status: EyeStatus (optional)

        :param face_type: face_type attribute
        :type face_type: FaceDetectTypeProbability (optional)

        :param not_spoofing: 判断图片不是合成图的概率
        :type not_spoofing: float (optional)
        """
        super().__init__()
        self.location = location
        self.angle = angle
        self.age = age
        self.expression = expression
        self.gender = gender
        self.glasses = glasses
        self.emotion = emotion
        self.mask = mask
        self.landmark = landmark
        self.landmark72 = landmark72
        self.landmark150 = landmark150
        self.quality = quality
        self.liveness = liveness
        self.spoofing = spoofing
        self.face_token = face_token
        self.face_probability = face_probability
        self.face_shape = face_shape
        self.eye_status = eye_status
        self.face_type = face_type
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
        if self.location is not None:
            result['location'] = self.location.to_dict()
        if self.angle is not None:
            result['angle'] = self.angle.to_dict()
        if self.age is not None:
            result['age'] = self.age
        if self.expression is not None:
            result['expression'] = self.expression.to_dict()
        if self.gender is not None:
            result['gender'] = self.gender.to_dict()
        if self.glasses is not None:
            result['glasses'] = self.glasses.to_dict()
        if self.emotion is not None:
            result['emotion'] = self.emotion.to_dict()
        if self.mask is not None:
            result['mask'] = self.mask.to_dict()
        if self.landmark is not None:
            result['landmark'] = [i.to_dict() for i in self.landmark]
        if self.landmark72 is not None:
            result['landmark72'] = [i.to_dict() for i in self.landmark72]
        if self.landmark150 is not None:
            result['landmark150'] = self.landmark150
        if self.quality is not None:
            result['quality'] = self.quality.to_dict()
        if self.liveness is not None:
            result['liveness'] = self.liveness.to_dict()
        if self.spoofing is not None:
            result['spoofing'] = self.spoofing
        if self.face_token is not None:
            result['face_token'] = self.face_token
        if self.face_probability is not None:
            result['face_probability'] = self.face_probability
        if self.face_shape is not None:
            result['face_shape'] = self.face_shape.to_dict()
        if self.eye_status is not None:
            result['eye_status'] = self.eye_status.to_dict()
        if self.face_type is not None:
            result['face_type'] = self.face_type.to_dict()
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
        :rtype: FaceDetectFaceInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('location') is not None:
            self.location = FaceDetectLocation().from_dict(m.get('location'))
        if m.get('angle') is not None:
            self.angle = FaceDetectAngle().from_dict(m.get('angle'))
        if m.get('age') is not None:
            self.age = m.get('age')
        if m.get('expression') is not None:
            self.expression = FaceDetectTypeProbability().from_dict(m.get('expression'))
        if m.get('gender') is not None:
            self.gender = FaceDetectTypeProbability().from_dict(m.get('gender'))
        if m.get('glasses') is not None:
            self.glasses = FaceDetectTypeProbability().from_dict(m.get('glasses'))
        if m.get('emotion') is not None:
            self.emotion = FaceDetectTypeProbability().from_dict(m.get('emotion'))
        if m.get('mask') is not None:
            self.mask = MaskInfo().from_dict(m.get('mask'))
        if m.get('landmark') is not None:
            self.landmark = [FaceDetectPoint().from_dict(i) for i in m.get('landmark')]
        if m.get('landmark72') is not None:
            self.landmark72 = [FaceDetectPoint().from_dict(i) for i in m.get('landmark72')]
        if m.get('landmark150') is not None:
            self.landmark150 = m.get('landmark150')
        if m.get('quality') is not None:
            self.quality = FaceDetectQuality().from_dict(m.get('quality'))
        if m.get('liveness') is not None:
            self.liveness = FaceDetectLiveness().from_dict(m.get('liveness'))
        if m.get('spoofing') is not None:
            self.spoofing = m.get('spoofing')
        if m.get('face_token') is not None:
            self.face_token = m.get('face_token')
        if m.get('face_probability') is not None:
            self.face_probability = m.get('face_probability')
        if m.get('face_shape') is not None:
            self.face_shape = FaceDetectTypeProbability().from_dict(m.get('face_shape'))
        if m.get('eye_status') is not None:
            self.eye_status = EyeStatus().from_dict(m.get('eye_status'))
        if m.get('face_type') is not None:
            self.face_type = FaceDetectTypeProbability().from_dict(m.get('face_type'))
        if m.get('not_spoofing') is not None:
            self.not_spoofing = m.get('not_spoofing')
        return self
