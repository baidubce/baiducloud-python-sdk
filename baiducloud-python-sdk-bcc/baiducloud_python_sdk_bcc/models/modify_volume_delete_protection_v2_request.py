"""
Request entity for ModifyVolumeDeleteProtectionV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyVolumeDeleteProtectionV2Request(AbstractModel):
    """
    Request entity for ModifyVolumeDeleteProtectionV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, volume_ids, enable_delete_protection):
        """
        Initialize ModifyVolumeDeleteProtectionV2Request request entity.

        :param volume_ids: 磁盘ID
        :type volume_ids: List[str] (required)

        :param enable_delete_protection: 是否开启磁盘释放保护，true为开启，false为关闭
        :type enable_delete_protection: bool (required)
        """
        super().__init__()
        self.volume_ids = volume_ids
        self.enable_delete_protection = enable_delete_protection

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.volume_ids is not None:
            result['volumeIds'] = self.volume_ids
        if self.enable_delete_protection is not None:
            result['enableDeleteProtection'] = self.enable_delete_protection
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyVolumeDeleteProtectionV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('volumeIds') is not None:
            self.volume_ids = m.get('volumeIds')
        if m.get('enableDeleteProtection') is not None:
            self.enable_delete_protection = m.get('enableDeleteProtection')
        return self
