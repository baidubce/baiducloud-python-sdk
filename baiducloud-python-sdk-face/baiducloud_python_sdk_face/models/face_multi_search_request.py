"""
Request entity for FaceMultiSearchRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FaceMultiSearchRequest(AbstractModel):
    """
    Request entity for FaceMultiSearchRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        image,
        image_type,
        group_id_list,
        max_face_num=None,
        match_threshold=None,
        quality_control=None,
        liveness_control=None,
        spoofing_control=None,
        max_user_num=None,
    ):
        """
        Initialize FaceMultiSearchRequest request entity.

        :param image: 图片信息，数据大小应小于10M，分辨率应小于1920×1080
        :type image: str (required)

        :param image_type: 图片类型
        :type image_type: str (required)

        :param group_id_list: 从指定的group中进行查找，逗号分隔，上限10个
        :type group_id_list: str (required)

        :param max_face_num: 最多处理人脸的数目，默认1（仅检测面积最大的人脸），最大值10
        :type max_face_num: int (optional)

        :param match_threshold: 匹配阈值，score低于此阈值的用户不会返回，最大100最小0默认80，推荐使用默认阈值80
        :type match_threshold: int (optional)

        :param quality_control: 质量控制
        :type quality_control: str (optional)

        :param liveness_control: 活体控制
        :type liveness_control: str (optional)

        :param spoofing_control: 合成图控制
        :type spoofing_control: str (optional)

        :param max_user_num: 识别返回的最大用户数，默认为1，最大20个
        :type max_user_num: int (optional)
        """
        super().__init__()
        self.image = image
        self.image_type = image_type
        self.group_id_list = group_id_list
        self.max_face_num = max_face_num
        self.match_threshold = match_threshold
        self.quality_control = quality_control
        self.liveness_control = liveness_control
        self.spoofing_control = spoofing_control
        self.max_user_num = max_user_num

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
        if self.max_face_num is not None:
            result['max_face_num'] = self.max_face_num
        if self.match_threshold is not None:
            result['match_threshold'] = self.match_threshold
        if self.quality_control is not None:
            result['quality_control'] = self.quality_control
        if self.liveness_control is not None:
            result['liveness_control'] = self.liveness_control
        if self.spoofing_control is not None:
            result['spoofing_control'] = self.spoofing_control
        if self.max_user_num is not None:
            result['max_user_num'] = self.max_user_num
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceMultiSearchRequest

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
        if m.get('max_face_num') is not None:
            self.max_face_num = m.get('max_face_num')
        if m.get('match_threshold') is not None:
            self.match_threshold = m.get('match_threshold')
        if m.get('quality_control') is not None:
            self.quality_control = m.get('quality_control')
        if m.get('liveness_control') is not None:
            self.liveness_control = m.get('liveness_control')
        if m.get('spoofing_control') is not None:
            self.spoofing_control = m.get('spoofing_control')
        if m.get('max_user_num') is not None:
            self.max_user_num = m.get('max_user_num')
        return self
