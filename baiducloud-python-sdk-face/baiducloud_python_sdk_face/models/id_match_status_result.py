"""
IdMatchStatusResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class IdMatchStatusResult(AbstractModel):
    """
    IdMatchStatusResult
    """

    def __init__(self, verify_status=None, is_newest=None, is_losted=None, is_expired=None, hjzt=None):
        """
        Initialize IdMatchStatusResult instance.

        :param verify_status: verify_status attribute
        :type verify_status: int (optional)

        :param is_newest: 证件是否最新，1 最新、0 非最新
        :type is_newest: int (optional)

        :param is_losted: 证件是否挂失，1 挂失、0 非挂失
        :type is_losted: int (optional)

        :param is_expired: 证件是否过期，1 过期、0 非过期
        :type is_expired: int (optional)

        :param hjzt: hjzt attribute
        :type hjzt: int (optional)
        """
        super().__init__()
        self.verify_status = verify_status
        self.is_newest = is_newest
        self.is_losted = is_losted
        self.is_expired = is_expired
        self.hjzt = hjzt

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
        if self.verify_status is not None:
            result['verify_status'] = self.verify_status
        if self.is_newest is not None:
            result['isNewest'] = self.is_newest
        if self.is_losted is not None:
            result['isLosted'] = self.is_losted
        if self.is_expired is not None:
            result['isExpired'] = self.is_expired
        if self.hjzt is not None:
            result['hjzt'] = self.hjzt
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: IdMatchStatusResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('verify_status') is not None:
            self.verify_status = m.get('verify_status')
        if m.get('isNewest') is not None:
            self.is_newest = m.get('isNewest')
        if m.get('isLosted') is not None:
            self.is_losted = m.get('isLosted')
        if m.get('isExpired') is not None:
            self.is_expired = m.get('isExpired')
        if m.get('hjzt') is not None:
            self.hjzt = m.get('hjzt')
        return self
