"""
Request entity for ClearInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ClearInstanceRequest(AbstractModel):
    """
    Request entity for ClearInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, password, db_index=None, is_flush_expired=None, is_defer=None):
        """
        Initialize ClearInstanceRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param password: password parameter
        :type password: str (required)

        :param db_index: 数据库索引，取值为：[0,255]
        :type db_index: int (optional)

        :param is_flush_expired: true=只清理过期数据, false=清理所有数据
        :type is_flush_expired: bool (optional)

        :param is_defer: is_defer parameter
        :type is_defer: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.password = password
        self.db_index = db_index
        self.is_flush_expired = is_flush_expired
        self.is_defer = is_defer

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
        if self.password is not None:
            result['password'] = self.password
        if self.db_index is not None:
            result['dbIndex'] = self.db_index
        if self.is_flush_expired is not None:
            result['isFlushExpired'] = self.is_flush_expired
        if self.is_defer is not None:
            result['isDefer'] = self.is_defer
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ClearInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('dbIndex') is not None:
            self.db_index = m.get('dbIndex')
        if m.get('isFlushExpired') is not None:
            self.is_flush_expired = m.get('isFlushExpired')
        if m.get('isDefer') is not None:
            self.is_defer = m.get('isDefer')
        return self
