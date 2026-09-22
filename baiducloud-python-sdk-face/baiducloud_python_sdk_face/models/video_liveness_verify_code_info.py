"""
VideoLivenessVerifyCodeInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class VideoLivenessVerifyCodeInfo(AbstractModel):
    """
    VideoLivenessVerifyCodeInfo
    """

    def __init__(self, create=None, identify=None, similarity=None):
        """
        Initialize VideoLivenessVerifyCodeInfo instance.

        :param create: 生成的验证码
        :type create: str (optional)

        :param identify: 验证码的语音识别结果
        :type identify: str (optional)

        :param similarity: 验证码相似度，取值0~1，1代表完全一致，0代表完全不一致，推荐阈值0.75
        :type similarity: float (optional)
        """
        super().__init__()
        self.create = create
        self.identify = identify
        self.similarity = similarity

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
        if self.create is not None:
            result['create'] = self.create
        if self.identify is not None:
            result['identify'] = self.identify
        if self.similarity is not None:
            result['similarity'] = self.similarity
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VideoLivenessVerifyCodeInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('create') is not None:
            self.create = m.get('create')
        if m.get('identify') is not None:
            self.identify = m.get('identify')
        if m.get('similarity') is not None:
            self.similarity = m.get('similarity')
        return self
