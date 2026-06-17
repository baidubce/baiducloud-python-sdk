"""
CreateDownloadResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateDownloadResult(AbstractModel):
    """
    CreateDownloadResult
    """

    def __init__(self, uuid=None):
        """
        Initialize CreateDownloadResult instance.

        :param uuid:
        :type uuid: str (optional)
        """
        super().__init__()
        self.uuid = uuid

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
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateDownloadResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self
