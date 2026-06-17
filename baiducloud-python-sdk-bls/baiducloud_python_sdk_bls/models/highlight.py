"""
Highlight information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Highlight(AbstractModel):
    """
    Highlight
    """

    def __init__(self, pre_tags=None, post_tags=None):
        """
        Initialize Highlight instance.

        :param pre_tags: 高亮的前置标识，默认@kibana-highlighted-field@
        :type pre_tags: List[str] (optional)

        :param post_tags: 高亮的后置标识，默认@/kibana-highlighted-field@
        :type post_tags: List[str] (optional)
        """
        super().__init__()
        self.pre_tags = pre_tags
        self.post_tags = post_tags

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
        if self.pre_tags is not None:
            result['pre_tags'] = self.pre_tags
        if self.post_tags is not None:
            result['post_tags'] = self.post_tags
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Highlight

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('pre_tags') is not None:
            self.pre_tags = m.get('pre_tags')
        if m.get('post_tags') is not None:
            self.post_tags = m.get('post_tags')
        return self
