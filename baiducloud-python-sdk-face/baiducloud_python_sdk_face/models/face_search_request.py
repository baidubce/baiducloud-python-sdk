"""
Request entity for FaceSearchRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FaceSearchRequest(AbstractModel):
    """
    Request entity for FaceSearchRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        image,
        image_type,
        group_id_list,
        quality_control=None,
        liveness_control=None,
        spoofing_control=None,
        user_id=None,
        max_user_num=None,
        face_sort_type=None,
        match_threshold=None,
    ):
        """
        Initialize FaceSearchRequest request entity.

        :param image: 图片信息，base64时编码后不超过2M，分辨率应小于1920×1080
        :type image: str (required)

        :param image_type: 图片类型
        :type image_type: str (required)

        :param group_id_list: 从指定的group中进行查找，逗号分隔，上限10个
        :type group_id_list: str (required)

        :param quality_control: 图片质量控制
        :type quality_control: str (optional)

        :param liveness_control: 活体检测控制
        :type liveness_control: str (optional)

        :param spoofing_control: 合成图控制
        :type spoofing_control: str (optional)

        :param user_id: 当需要对特定用户进行比对时，指定user_id进行比对（即人脸认证功能）
        :type user_id: str (optional)

        :param max_user_num: 查找后返回的用户数量，默认为1，最多返回50个
        :type max_user_num: int (optional)

        :param face_sort_type: 人脸检测排序类型
        :type face_sort_type: int (optional)

        :param match_threshold: 匹配阈值，score低于此阈值的用户不会返回，最大100最小0默认0，推荐设置80
        :type match_threshold: int (optional)
        """
        super().__init__()
        self.image = image
        self.image_type = image_type
        self.group_id_list = group_id_list
        self.quality_control = quality_control
        self.liveness_control = liveness_control
        self.spoofing_control = spoofing_control
        self.user_id = user_id
        self.max_user_num = max_user_num
        self.face_sort_type = face_sort_type
        self.match_threshold = match_threshold

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
        if self.group_id_list is not None:
            result['group_id_list'] = self.group_id_list
        if self.quality_control is not None:
            result['quality_control'] = self.quality_control
        if self.liveness_control is not None:
            result['liveness_control'] = self.liveness_control
        if self.spoofing_control is not None:
            result['spoofing_control'] = self.spoofing_control
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.max_user_num is not None:
            result['max_user_num'] = self.max_user_num
        if self.face_sort_type is not None:
            result['face_sort_type'] = self.face_sort_type
        if self.match_threshold is not None:
            result['match_threshold'] = self.match_threshold
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceSearchRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('image_type') is not None:
            self.image_type = m.get('image_type')
        if m.get('group_id_list') is not None:
            self.group_id_list = m.get('group_id_list')
        if m.get('quality_control') is not None:
            self.quality_control = m.get('quality_control')
        if m.get('liveness_control') is not None:
            self.liveness_control = m.get('liveness_control')
        if m.get('spoofing_control') is not None:
            self.spoofing_control = m.get('spoofing_control')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('max_user_num') is not None:
            self.max_user_num = m.get('max_user_num')
        if m.get('face_sort_type') is not None:
            self.face_sort_type = m.get('face_sort_type')
        if m.get('match_threshold') is not None:
            self.match_threshold = m.get('match_threshold')
        return self
