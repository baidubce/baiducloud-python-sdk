"""
BestImage information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BestImage(AbstractModel):
    """
    BestImage
    """

    def __init__(self, face_token=None, pic=None, liveness_score=None):
        """
        Initialize BestImage instance.

        :param face_token: 人脸图片的唯一标识
        :type face_token: str (optional)

        :param pic: base64编码后的图片信息
        :type pic: str (optional)

        :param liveness_score: 此图片的活体分数，范围[0,1]
        :type liveness_score: float (optional)
        """
        super().__init__()
        self.face_token = face_token
        self.pic = pic
        self.liveness_score = liveness_score

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
        if self.pic is not None:
            result['pic'] = self.pic
        if self.liveness_score is not None:
            result['liveness_score'] = self.liveness_score
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BestImage

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('face_token') is not None:
            self.face_token = m.get('face_token')
        if m.get('pic') is not None:
            self.pic = m.get('pic')
        if m.get('liveness_score') is not None:
            self.liveness_score = m.get('liveness_score')
        return self
