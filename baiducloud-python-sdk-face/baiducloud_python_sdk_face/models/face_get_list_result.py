"""
FaceGetListResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_face.models.face_get_list_face_info import FaceGetListFaceInfo


class FaceGetListResult(AbstractModel):
    """
    FaceGetListResult
    """

    def __init__(self, face_list=None):
        """
        Initialize FaceGetListResult instance.

        :param face_list: 人脸列表
        :type face_list: List[FaceGetListFaceInfo] (optional)
        """
        super().__init__()
        self.face_list = face_list

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
        if self.face_list is not None:
            result['face_list'] = [i.to_dict() for i in self.face_list]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceGetListResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('face_list') is not None:
            self.face_list = [FaceGetListFaceInfo().from_dict(i) for i in m.get('face_list')]
        return self
