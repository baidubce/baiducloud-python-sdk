"""
Request entity for FaceDeleteRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FaceDeleteRequest(AbstractModel):
    """
    Request entity for FaceDeleteRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, user_id, group_id, face_token, log_id):
        """
        Initialize FaceDeleteRequest request entity.

        :param user_id: 用户ID（由数字、字母、下划线组成），长度限制48B
        :type user_id: str (required)

        :param group_id: 用户组ID（由数字、字母、下划线组成） 长度限制48B，删除指定group_id中的user_id信息
        :type group_id: str (required)

        :param face_token: 需要删除的人脸图片token，（由数字、字母、下划线组成）长度限制64B
        :type face_token: str (required)

        :param log_id: 请求标识码，随机数，唯一
        :type log_id: int (required)
        """
        super().__init__()
        self.user_id = user_id
        self.group_id = group_id
        self.face_token = face_token
        self.log_id = log_id

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
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.face_token is not None:
            result['face_token'] = self.face_token
        if self.log_id is not None:
            result['log_id'] = self.log_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceDeleteRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('face_token') is not None:
            self.face_token = m.get('face_token')
        if m.get('log_id') is not None:
            self.log_id = m.get('log_id')
        return self
