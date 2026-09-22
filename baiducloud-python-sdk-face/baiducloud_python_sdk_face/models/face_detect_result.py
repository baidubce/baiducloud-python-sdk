"""
FaceDetectResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_face.models.face_detect_face_info import FaceDetectFaceInfo


class FaceDetectResult(AbstractModel):
    """
    FaceDetectResult
    """

    def __init__(self, face_num=None, face_list=None, corp_image_base64=None):
        """
        Initialize FaceDetectResult instance.

        :param face_num: 检测到的图片中的人脸数量
        :type face_num: int (optional)

        :param face_list: 人脸信息列表
        :type face_list: List[FaceDetectFaceInfo] (optional)

        :param corp_image_base64: 检测人脸框的人脸图片base64值
        :type corp_image_base64: str (optional)
        """
        super().__init__()
        self.face_num = face_num
        self.face_list = face_list
        self.corp_image_base64 = corp_image_base64

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
        if self.face_num is not None:
            result['face_num'] = self.face_num
        if self.face_list is not None:
            result['face_list'] = [i.to_dict() for i in self.face_list]
        if self.corp_image_base64 is not None:
            result['corp_image_base64'] = self.corp_image_base64
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceDetectResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('face_num') is not None:
            self.face_num = m.get('face_num')
        if m.get('face_list') is not None:
            self.face_list = [FaceDetectFaceInfo().from_dict(i) for i in m.get('face_list')]
        if m.get('corp_image_base64') is not None:
            self.corp_image_base64 = m.get('corp_image_base64')
        return self
