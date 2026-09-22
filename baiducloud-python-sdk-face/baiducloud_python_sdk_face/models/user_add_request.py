"""
Request entity for UserAddRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UserAddRequest(AbstractModel):
    """
    Request entity for UserAddRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        image,
        image_type,
        group_id,
        user_id,
        user_info=None,
        quality_control=None,
        liveness_control=None,
        spoofing_control=None,
        action_type=None,
        face_sort_type=None,
    ):
        """
        Initialize UserAddRequest request entity.

        :param image: image parameter
        :type image: str (required)

        :param image_type: 图片类型
        :type image_type: str (required)

        :param group_id: group_id parameter
        :type group_id: str (required)

        :param user_id: 用户ID，由数字、字母、下划线组成，长度限制48B
        :type user_id: str (required)

        :param user_info: 用户资料，长度限制256B
        :type user_info: str (optional)

        :param quality_control: 图片质量控制
        :type quality_control: str (optional)

        :param liveness_control: 活体检测控制
        :type liveness_control: str (optional)

        :param spoofing_control: 合成图控制
        :type spoofing_control: str (optional)

        :param action_type: 操作方式
        :type action_type: str (optional)

        :param face_sort_type: 人脸检测排序类型
        :type face_sort_type: int (optional)
        """
        super().__init__()
        self.image = image
        self.image_type = image_type
        self.group_id = group_id
        self.user_id = user_id
        self.user_info = user_info
        self.quality_control = quality_control
        self.liveness_control = liveness_control
        self.spoofing_control = spoofing_control
        self.action_type = action_type
        self.face_sort_type = face_sort_type

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
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_info is not None:
            result['user_info'] = self.user_info
        if self.quality_control is not None:
            result['quality_control'] = self.quality_control
        if self.liveness_control is not None:
            result['liveness_control'] = self.liveness_control
        if self.spoofing_control is not None:
            result['spoofing_control'] = self.spoofing_control
        if self.action_type is not None:
            result['action_type'] = self.action_type
        if self.face_sort_type is not None:
            result['face_sort_type'] = self.face_sort_type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UserAddRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('image_type') is not None:
            self.image_type = m.get('image_type')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_info') is not None:
            self.user_info = m.get('user_info')
        if m.get('quality_control') is not None:
            self.quality_control = m.get('quality_control')
        if m.get('liveness_control') is not None:
            self.liveness_control = m.get('liveness_control')
        if m.get('spoofing_control') is not None:
            self.spoofing_control = m.get('spoofing_control')
        if m.get('action_type') is not None:
            self.action_type = m.get('action_type')
        if m.get('face_sort_type') is not None:
            self.face_sort_type = m.get('face_sort_type')
        return self
