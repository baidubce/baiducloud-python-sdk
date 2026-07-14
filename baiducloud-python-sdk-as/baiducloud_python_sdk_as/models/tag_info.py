"""
TagInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TagInfo(AbstractModel):
    """
    TagInfo
    """

    def __init__(self, tag_key=None, tag_value=None):
        """
        Initialize TagInfo instance.

        :param tag_key: 键
        :type tag_key: str (optional)

        :param tag_value: 值
        :type tag_value: str (optional)
        """
        super().__init__()
        self.tag_key = tag_key
        self.tag_value = tag_value

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
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TagInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self
