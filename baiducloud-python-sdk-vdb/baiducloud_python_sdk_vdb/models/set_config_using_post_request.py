"""
Request entity for SetConfigUsingPOSTRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class SetConfigUsingPOSTRequest(AbstractModel):
    """
    Request entity for SetConfigUsingPOSTRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, instance_id, engine_type=None, auto_backup_config=None, auto_backup_enabled=None, is_encrypt=None
    ):
        """
        Initialize SetConfigUsingPOSTRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param engine_type: engine_type parameter
        :type engine_type: str (optional)

        :param auto_backup_config: auto_backup_config parameter
        :type auto_backup_config: str (optional)

        :param auto_backup_enabled: auto_backup_enabled parameter
        :type auto_backup_enabled: bool (optional)

        :param is_encrypt: is_encrypt parameter
        :type is_encrypt: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.engine_type = engine_type
        self.auto_backup_config = auto_backup_config
        self.auto_backup_enabled = auto_backup_enabled
        self.is_encrypt = is_encrypt

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
        if self.auto_backup_config is not None:
            result['autoBackupConfig'] = self.auto_backup_config
        if self.auto_backup_enabled is not None:
            result['autoBackupEnabled'] = self.auto_backup_enabled
        if self.is_encrypt is not None:
            result['isEncrypt'] = self.is_encrypt
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: SetConfigUsingPOSTRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')
        if m.get('autoBackupConfig') is not None:
            self.auto_backup_config = m.get('autoBackupConfig')
        if m.get('autoBackupEnabled') is not None:
            self.auto_backup_enabled = m.get('autoBackupEnabled')
        if m.get('isEncrypt') is not None:
            self.is_encrypt = m.get('isEncrypt')
        return self
