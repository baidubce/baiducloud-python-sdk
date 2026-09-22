"""
FaceDetectQuality information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_face.models.face_detect_occlusion import FaceDetectOcclusion


class FaceDetectQuality(AbstractModel):
    """
    FaceDetectQuality
    """

    def __init__(self, occlusion=None, blur=None, illumination=None, completeness=None):
        """
        Initialize FaceDetectQuality instance.

        :param occlusion: occlusion attribute
        :type occlusion: FaceDetectOcclusion (optional)

        :param blur: 人脸模糊程度，[0~1]，0清晰，1模糊
        :type blur: float (optional)

        :param illumination: 脸部光照程度，[0~255]，越大光照越好
        :type illumination: float (optional)

        :param completeness: 人脸完整度，0-溢出图像边界，1-在边界内
        :type completeness: int (optional)
        """
        super().__init__()
        self.occlusion = occlusion
        self.blur = blur
        self.illumination = illumination
        self.completeness = completeness

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
        if self.occlusion is not None:
            result['occlusion'] = self.occlusion.to_dict()
        if self.blur is not None:
            result['blur'] = self.blur
        if self.illumination is not None:
            result['illumination'] = self.illumination
        if self.completeness is not None:
            result['completeness'] = self.completeness
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceDetectQuality

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('occlusion') is not None:
            self.occlusion = FaceDetectOcclusion().from_dict(m.get('occlusion'))
        if m.get('blur') is not None:
            self.blur = m.get('blur')
        if m.get('illumination') is not None:
            self.illumination = m.get('illumination')
        if m.get('completeness') is not None:
            self.completeness = m.get('completeness')
        return self
