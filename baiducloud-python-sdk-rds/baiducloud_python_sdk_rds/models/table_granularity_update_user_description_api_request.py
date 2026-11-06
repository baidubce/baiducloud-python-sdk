"""
Request entity for TableGranularityUpdateUserDescriptionApiRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TableGranularityUpdateUserDescriptionApiRequest(AbstractModel):
    """
    Request entity for TableGranularityUpdateUserDescriptionApiRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, user, host, remark):
        """
        Initialize TableGranularityUpdateUserDescriptionApiRequest request entity.

        :param instance_id: RDS 实例 ID
        :type instance_id: str (required)

        :param user: 账号名
        :type user: str (required)

        :param host: 来源主机
        :type host: str (required)

        :param remark: 新备注
        :type remark: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.user = user
        self.host = host
        self.remark = remark

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.user is not None:
            result['user'] = self.user
        if self.host is not None:
            result['host'] = self.host
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TableGranularityUpdateUserDescriptionApiRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('user') is not None:
            self.user = m.get('user')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self
