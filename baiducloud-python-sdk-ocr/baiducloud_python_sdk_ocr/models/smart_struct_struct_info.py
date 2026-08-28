"""
SmartStructStructInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ocr.models.smart_struct_group import SmartStructGroup


class SmartStructStructInfo(AbstractModel):
    """
    SmartStructStructInfo
    """

    def __init__(self, group=None):
        """
        Initialize SmartStructStructInfo instance.

        :param group: key 文字行的信息
        :type group: List[SmartStructGroup] (optional)
        """
        super().__init__()
        self.group = group

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
        if self.group is not None:
            result['group'] = [i.to_dict() for i in self.group]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SmartStructStructInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('group') is not None:
            self.group = [SmartStructGroup().from_dict(i) for i in m.get('group')]
        return self
