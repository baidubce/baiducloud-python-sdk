"""
FaceMergeResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FaceMergeResult(AbstractModel):
    """
    FaceMergeResult
    """

    def __init__(self, merge_image=None):
        """
        Initialize FaceMergeResult instance.

        :param merge_image: 融合图的BASE64值
        :type merge_image: str (optional)
        """
        super().__init__()
        self.merge_image = merge_image

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
        if self.merge_image is not None:
            result['merge_image'] = self.merge_image
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FaceMergeResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('merge_image') is not None:
            self.merge_image = m.get('merge_image')
        return self
