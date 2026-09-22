"""
FaceMultiFaceInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_face.models.face_multi_location import FaceMultiLocation

from baiducloud_python_sdk_face.models.face_multi_user_info import FaceMultiUserInfo


class FaceMultiFaceInfo(AbstractModel):
    """
    FaceMultiFaceInfo
    """

    def __init__(self, location=None, face_token=None, user_list=None):
        """
        Initialize FaceMultiFaceInfo instance.

        :param location: location attribute
        :type location: FaceMultiLocation (optional)

        :param face_token: 人脸图片的唯一标识，有效期60min
        :type face_token: str (optional)

        :param user_list: 匹配的用户信息列表
        :type user_list: List[FaceMultiUserInfo] (optional)
        """
        super().__init__()
        self.location = location
        self.face_token = face_token
        self.user_list = user_list

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
        if self.location is not None:
            result['location'] = self.location.to_dict()
        if self.face_token is not None:
            result['face_token'] = self.face_token
        if self.user_list is not None:
            result['user_list'] = [i.to_dict() for i in self.user_list]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceMultiFaceInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('location') is not None:
            self.location = FaceMultiLocation().from_dict(m.get('location'))
        if m.get('face_token') is not None:
            self.face_token = m.get('face_token')
        if m.get('user_list') is not None:
            self.user_list = [FaceMultiUserInfo().from_dict(i) for i in m.get('user_list')]
        return self
