"""
Request entity for FaceEditAttrRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FaceEditAttrRequest(AbstractModel):
    """
    Request entity for FaceEditAttrRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, image, image_type, action_type, target=None, quality_control=None, face_location=None):
        """
        Initialize FaceEditAttrRequest request entity.

        :param image: image parameter
        :type image: str (required)

        :param image_type: 图片类型
        :type image_type: str (required)

        :param action_type: 人脸编辑方式
        :type action_type: str (required)

        :param target: target parameter
        :type target: int (optional)

        :param quality_control: 质量控制
        :type quality_control: str (optional)

        :param face_location: face_location parameter
        :type face_location: str (optional)
        """
        super().__init__()
        self.image = image
        self.image_type = image_type
        self.action_type = action_type
        self.target = target
        self.quality_control = quality_control
        self.face_location = face_location

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
        if self.action_type is not None:
            result['action_type'] = self.action_type
        if self.target is not None:
            result['target'] = self.target
        if self.quality_control is not None:
            result['quality_control'] = self.quality_control
        if self.face_location is not None:
            result['face_location'] = self.face_location
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceEditAttrRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('image_type') is not None:
            self.image_type = m.get('image_type')
        if m.get('action_type') is not None:
            self.action_type = m.get('action_type')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('quality_control') is not None:
            self.quality_control = m.get('quality_control')
        if m.get('face_location') is not None:
            self.face_location = m.get('face_location')
        return self
