"""
Request entity for UpdateBlbModifyProtectionRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateBlbModifyProtectionRequest(AbstractModel):
    """
    Request entity for UpdateBlbModifyProtectionRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, blb_id, allow_modify, client_token=None, modification_protection_reason=None):
        """
        Initialize UpdateBlbModifyProtectionRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param allow_modify: true表示允许修改（关闭保护）；false表示不允许修改（开启保护）
        :type allow_modify: bool (required)

        :param modification_protection_reason: 保护原因，长度0-128字符
        :type modification_protection_reason: str (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.client_token = client_token
        self.allow_modify = allow_modify
        self.modification_protection_reason = modification_protection_reason

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
        if self.allow_modify is not None:
            result['allowModify'] = self.allow_modify
        if self.modification_protection_reason is not None:
            result['modificationProtectionReason'] = self.modification_protection_reason
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateBlbModifyProtectionRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('allowModify') is not None:
            self.allow_modify = m.get('allowModify')
        if m.get('modificationProtectionReason') is not None:
            self.modification_protection_reason = m.get('modificationProtectionReason')
        return self
