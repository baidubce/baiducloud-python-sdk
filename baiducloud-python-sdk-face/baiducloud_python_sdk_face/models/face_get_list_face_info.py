"""
FaceGetListFaceInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FaceGetListFaceInfo(AbstractModel):
    """
    FaceGetListFaceInfo
    """

    def __init__(self, ctime=None, face_token=None):
        """
        Initialize FaceGetListFaceInfo instance.

        :param ctime: 人脸创建时间
        :type ctime: str (optional)

        :param face_token: 人脸标识
        :type face_token: str (optional)
        """
        super().__init__()
        self.ctime = ctime
        self.face_token = face_token

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
        if self.ctime is not None:
            result['ctime'] = self.ctime
        if self.face_token is not None:
            result['face_token'] = self.face_token
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceGetListFaceInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ctime') is not None:
            self.ctime = m.get('ctime')
        if m.get('face_token') is not None:
            self.face_token = m.get('face_token')
        return self
