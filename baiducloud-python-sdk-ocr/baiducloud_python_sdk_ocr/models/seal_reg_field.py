"""
SealRegField information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SealRegField(AbstractModel):
    """
    SealRegField
    """

    def __init__(self, words=None, flatten_image=None, probability=None):
        """
        Initialize SealRegField instance.

        :param words: 识别内容
        :type words: str (optional)

        :param flatten_image: 主字段展平图的 base64 编码，即章内上环弯曲文字切片后拼接图片，flatten_image=true 时返回
        :type flatten_image: str (optional)

        :param probability: 识别内容的置信度
        :type probability: float (optional)
        """
        super().__init__()
        self.words = words
        self.flatten_image = flatten_image
        self.probability = probability

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
        if self.words is not None:
            result['words'] = self.words
        if self.flatten_image is not None:
            result['flatten_image'] = self.flatten_image
        if self.probability is not None:
            result['probability'] = self.probability
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SealRegField

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('words') is not None:
            self.words = m.get('words')
        if m.get('flatten_image') is not None:
            self.flatten_image = m.get('flatten_image')
        if m.get('probability') is not None:
            self.probability = m.get('probability')
        return self
