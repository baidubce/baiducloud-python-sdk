"""
Request entity for FaceDetectRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FaceDetectRequest(AbstractModel):
    """
    Request entity for FaceDetectRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        image,
        image_type,
        face_field=None,
        max_face_num=None,
        face_type=None,
        liveness_control=None,
        face_sort_type=None,
        display_corp_image=None,
    ):
        """
        Initialize FaceDetectRequest request entity.

        :param image: 图片信息（总数据大小应小于10M，分辨率应小于1920×1080），图片上传方式根据image_type来判断
        :type image: str (required)

        :param image_type: 图片类型
        :type image_type: str (required)

        :param face_field: face_field parameter
        :type face_field: str (optional)

        :param max_face_num: 最多处理人脸的数目，默认值为1，根据人脸检测排序类型检测图片中排序第一的人脸（默认为人脸面积最大的人脸），最大值20
        :type max_face_num: int (optional)

        :param face_type: 人脸类型
        :type face_type: str (optional)

        :param liveness_control: 活体控制
        :type liveness_control: str (optional)

        :param face_sort_type: 人脸检测排序类型
        :type face_sort_type: int (optional)

        :param display_corp_image: 是否显示检测人脸的裁剪图base64值：0-不显示（默认）；1-显示（max_face_num上限按5计算）
        :type display_corp_image: int (optional)
        """
        super().__init__()
        self.image = image
        self.image_type = image_type
        self.face_field = face_field
        self.max_face_num = max_face_num
        self.face_type = face_type
        self.liveness_control = liveness_control
        self.face_sort_type = face_sort_type
        self.display_corp_image = display_corp_image

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.image is not None:
            result['image'] = self.image
        if self.image_type is not None:
            result['image_type'] = self.image_type
        if self.face_field is not None:
            result['face_field'] = self.face_field
        if self.max_face_num is not None:
            result['max_face_num'] = self.max_face_num
        if self.face_type is not None:
            result['face_type'] = self.face_type
        if self.liveness_control is not None:
            result['liveness_control'] = self.liveness_control
        if self.face_sort_type is not None:
            result['face_sort_type'] = self.face_sort_type
        if self.display_corp_image is not None:
            result['display_corp_image'] = self.display_corp_image
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceDetectRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('image_type') is not None:
            self.image_type = m.get('image_type')
        if m.get('face_field') is not None:
            self.face_field = m.get('face_field')
        if m.get('max_face_num') is not None:
            self.max_face_num = m.get('max_face_num')
        if m.get('face_type') is not None:
            self.face_type = m.get('face_type')
        if m.get('liveness_control') is not None:
            self.liveness_control = m.get('liveness_control')
        if m.get('face_sort_type') is not None:
            self.face_sort_type = m.get('face_sort_type')
        if m.get('display_corp_image') is not None:
            self.display_corp_image = m.get('display_corp_image')
        return self
