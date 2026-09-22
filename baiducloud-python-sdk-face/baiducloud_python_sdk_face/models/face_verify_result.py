"""
FaceVerifyResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_face.models.thresholds import Thresholds

from baiducloud_python_sdk_face.models.face_verify_face_info import FaceVerifyFaceInfo


class FaceVerifyResult(AbstractModel):
    """
    FaceVerifyResult
    """

    def __init__(self, face_liveness=None, thresholds=None, face_list=None):
        """
        Initialize FaceVerifyResult instance.

        :param face_liveness: 所有图片的总体活体最高得分，范围【0~1】
        :type face_liveness: float (optional)

        :param thresholds: thresholds attribute
        :type thresholds: Thresholds (optional)

        :param face_list: 每张图片的详细信息描述，如果只上传一张图片，则只返回一个结果
        :type face_list: List[FaceVerifyFaceInfo] (optional)
        """
        super().__init__()
        self.face_liveness = face_liveness
        self.thresholds = thresholds
        self.face_list = face_list

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
        if self.face_liveness is not None:
            result['face_liveness'] = self.face_liveness
        if self.thresholds is not None:
            result['thresholds'] = self.thresholds.to_dict()
        if self.face_list is not None:
            result['face_list'] = [i.to_dict() for i in self.face_list]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceVerifyResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('face_liveness') is not None:
            self.face_liveness = m.get('face_liveness')
        if m.get('thresholds') is not None:
            self.thresholds = Thresholds().from_dict(m.get('thresholds'))
        if m.get('face_list') is not None:
            self.face_list = [FaceVerifyFaceInfo().from_dict(i) for i in m.get('face_list')]
        return self
