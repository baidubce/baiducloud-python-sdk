"""
AdditionalAttributesModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AdditionalAttributesModel(AbstractModel):
    """
    AdditionalAttributesModel
    """

    def __init__(self, gzip_json=None):
        """
        Initialize AdditionalAttributesModel instance.

        :param gzip_json: 是否启用gzipJSON压缩,字符串类型,取值 \"on\" 或 \"off\"
        :type gzip_json: str (optional)
        """
        super().__init__()
        self.gzip_json = gzip_json

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
        if self.gzip_json is not None:
            result['gzipJson'] = self.gzip_json
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AdditionalAttributesModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('gzipJson') is not None:
            self.gzip_json = m.get('gzipJson')
        return self
