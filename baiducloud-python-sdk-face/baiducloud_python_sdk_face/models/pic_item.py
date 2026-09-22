"""
PicItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PicItem(AbstractModel):
    """
    PicItem
    """

    def __init__(self, face_token=None, spoofing=None):
        """
        Initialize PicItem instance.

        :param face_token: 人脸图片的唯一标识
        :type face_token: str (optional)

        :param spoofing: 此图片的合成图分数，范围[0,1]
        :type spoofing: float (optional)
        """
        super().__init__()
        self.face_token = face_token
        self.spoofing = spoofing

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
        if self.face_token is not None:
            result['face_token'] = self.face_token
        if self.spoofing is not None:
            result['spoofing'] = self.spoofing
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PicItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('face_token') is not None:
            self.face_token = m.get('face_token')
        if m.get('spoofing') is not None:
            self.spoofing = m.get('spoofing')
        return self
