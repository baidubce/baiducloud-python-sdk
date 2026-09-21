"""
Request entity for GetConfigUsingGETResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class GetConfigUsingGETResponse(BceResponse):
    """
    GetConfigUsingGETResponse
    """

    def __init__(self, auto_backup_config=None, auto_backup_enabled=None, is_encrypt=None):
        """
        Initialize GetConfigUsingGETResponse response.

        :param auto_backup_config: auto_backup_config field
        :type auto_backup_config: str (optional)

        :param auto_backup_enabled: auto_backup_enabled field
        :type auto_backup_enabled: bool (optional)

        :param is_encrypt: is_encrypt field
        :type is_encrypt: str (optional)
        """
        super().__init__()
        self.auto_backup_config = auto_backup_config
        self.auto_backup_enabled = auto_backup_enabled
        self.is_encrypt = is_encrypt

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.auto_backup_config is not None:
            result['autoBackupConfig'] = self.auto_backup_config
        if self.auto_backup_enabled is not None:
            result['autoBackupEnabled'] = self.auto_backup_enabled
        if self.is_encrypt is not None:
            result['isEncrypt'] = self.is_encrypt
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetConfigUsingGETResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('autoBackupConfig') is not None:
            self.auto_backup_config = m.get('autoBackupConfig')
        if m.get('autoBackupEnabled') is not None:
            self.auto_backup_enabled = m.get('autoBackupEnabled')
        if m.get('isEncrypt') is not None:
            self.is_encrypt = m.get('isEncrypt')
        return self
