"""
TransformOptions information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TransformOptions(AbstractModel):
    """
    TransformOptions
    """

    def __init__(self, auto_correct_angle=None, size_compress=None):
        """
        Initialize TransformOptions instance.

        :param auto_correct_angle: 图片自动矫正
        :type auto_correct_angle: bool (optional)

        :param size_compress: 结果图大小压缩
        :type size_compress: bool (optional)
        """
        super().__init__()
        self.auto_correct_angle = auto_correct_angle
        self.size_compress = size_compress

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
        if self.auto_correct_angle is not None:
            result['auto_correct_angle'] = self.auto_correct_angle
        if self.size_compress is not None:
            result['size_compress'] = self.size_compress
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TransformOptions

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('auto_correct_angle') is not None:
            self.auto_correct_angle = m.get('auto_correct_angle')
        if m.get('size_compress') is not None:
            self.size_compress = m.get('size_compress')
        return self
