"""
RemoteCopyRequest information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RemoteCopyRequest(AbstractModel):
    """
    RemoteCopyRequest
    """

    def __init__(self, name=None, dest_region=None):
        """
        Initialize RemoteCopyRequest instance.

        :param name: 快照名称
        :type name: str (optional)

        :param dest_region: 待复制快照的目标区域
        :type dest_region: str (optional)
        """
        super().__init__()
        self.name = name
        self.dest_region = dest_region

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
        if self.name is not None:
            result['name'] = self.name
        if self.dest_region is not None:
            result['destRegion'] = self.dest_region
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RemoteCopyRequest

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('destRegion') is not None:
            self.dest_region = m.get('destRegion')
        return self
