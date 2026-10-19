"""
ResourceInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ResourceInfo(AbstractModel):
    """
    ResourceInfo
    """

    def __init__(
        self,
        name=None,
        extra=None,
        parent_uuid=None,
        group_id=None,
        account_id=None,
        user_id=None,
        create_time=None,
        update_time=None,
        delete_time=None,
        bind_time=None,
    ):
        """
        Initialize ResourceInfo instance.

        :param name: 资源分组名称。
        :type name: str (optional)

        :param extra: 扩展信息。
        :type extra: str (optional)

        :param parent_uuid: 上级资源 ID。
        :type parent_uuid: str (optional)

        :param group_id: 分组 ID。
        :type group_id: str (optional)

        :param account_id: 账户ID。
        :type account_id: str (optional)

        :param user_id: 用户ID。
        :type user_id: str (optional)

        :param create_time: create_time attribute
        :type create_time: object (optional)

        :param update_time: update_time attribute
        :type update_time: object (optional)

        :param delete_time: delete_time attribute
        :type delete_time: object (optional)

        :param bind_time: bind_time attribute
        :type bind_time: object (optional)
        """
        super().__init__()
        self.name = name
        self.extra = extra
        self.parent_uuid = parent_uuid
        self.group_id = group_id
        self.account_id = account_id
        self.user_id = user_id
        self.create_time = create_time
        self.update_time = update_time
        self.delete_time = delete_time
        self.bind_time = bind_time

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
        if self.name is not None:
            result['name'] = self.name
        if self.extra is not None:
            result['extra'] = self.extra
        if self.parent_uuid is not None:
            result['parentUuid'] = self.parent_uuid
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.delete_time is not None:
            result['deleteTime'] = self.delete_time
        if self.bind_time is not None:
            result['bindTime'] = self.bind_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ResourceInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('parentUuid') is not None:
            self.parent_uuid = m.get('parentUuid')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('deleteTime') is not None:
            self.delete_time = m.get('deleteTime')
        if m.get('bindTime') is not None:
            self.bind_time = m.get('bindTime')
        return self
