"""
EphemeralDisk information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class EphemeralDisk(AbstractModel):
    """
    EphemeralDisk
    """

    def __init__(self, storage_type=None, size_in_gb=None):
        """
        Initialize EphemeralDisk instance.

        :param storage_type: 本地盘类型
        :type storage_type: str (optional)

        :param size_in_gb: 本地盘大小
        :type size_in_gb: int (optional)
        """
        super().__init__()
        self.storage_type = storage_type
        self.size_in_gb = size_in_gb

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
        if self.storage_type is not None:
            result['storageType'] = self.storage_type
        if self.size_in_gb is not None:
            result['sizeInGB'] = self.size_in_gb
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EphemeralDisk

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('storageType') is not None:
            self.storage_type = m.get('storageType')
        if m.get('sizeInGB') is not None:
            self.size_in_gb = m.get('sizeInGB')
        return self
