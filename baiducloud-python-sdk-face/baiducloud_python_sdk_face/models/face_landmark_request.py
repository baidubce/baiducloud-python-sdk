"""
Request entity for FaceLandmarkRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FaceLandmarkRequest(AbstractModel):
    """
    Request entity for FaceLandmarkRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image, image_type, max_face_num=None, face_field=None):
        """
        Initialize FaceLandmarkRequest request entity.

        :param image: 图片信息，数据大小应小于10M，分辨率应小于1920×1080
        :type image: str (required)

        :param image_type: 图片类型
        :type image_type: str (required)

        :param max_face_num: 最多处理人脸的数目，默认值为1（仅检测面积最大的人脸），最大值10
        :type max_face_num: int (optional)

        :param face_field: face_field parameter
        :type face_field: str (optional)
        """
        super().__init__()
        self.image = image
        self.image_type = image_type
        self.max_face_num = max_face_num
        self.face_field = face_field

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
        if self.max_face_num is not None:
            result['max_face_num'] = self.max_face_num
        if self.face_field is not None:
            result['face_field'] = self.face_field
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceLandmarkRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('image_type') is not None:
            self.image_type = m.get('image_type')
        if m.get('max_face_num') is not None:
            self.max_face_num = m.get('max_face_num')
        if m.get('face_field') is not None:
            self.face_field = m.get('face_field')
        return self
