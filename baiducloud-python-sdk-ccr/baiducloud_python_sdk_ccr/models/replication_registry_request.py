"""
ReplicationRegistryRequest information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ReplicationRegistryRequest(AbstractModel):
    """
    ReplicationRegistryRequest
    """

    def __init__(self, id=None):
        """
        Initialize ReplicationRegistryRequest instance.

        :param id: Registry ID
        :type id: int (optional)
        """
        super().__init__()
        self.id = id

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
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ReplicationRegistryRequest

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self
