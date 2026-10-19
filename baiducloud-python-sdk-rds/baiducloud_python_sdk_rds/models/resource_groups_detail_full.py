"""
ResourceGroupsDetailFull information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rds.models.resource_info import ResourceInfo

from baiducloud_python_sdk_rds.models.tag import Tag


class ResourceGroupsDetailFull(AbstractModel):
    """
    ResourceGroupsDetailFull
    """

    def __init__(
        self,
        groups=None,
        name=None,
        type=None,
        region=None,
        id=None,
        uuid=None,
        summary=None,
        url=None,
        account_id=None,
        user_id=None,
        tags=None,
        res_uuid=None,
    ):
        """
        Initialize ResourceGroupsDetailFull instance.

        :param groups: 集合ResourceInfo列表。
        :type groups: List[ResourceInfo] (optional)

        :param name: 资源名称。
        :type name: str (optional)

        :param type: 资源类型（产品类型）默认为RDS。
        :type type: str (optional)

        :param region: 资源所属区域。
        :type region: str (optional)

        :param id: 资源短 ID。
        :type id: str (optional)

        :param uuid: 资源长 ID。
        :type uuid: str (optional)

        :param summary: 日志。
        :type summary: str (optional)

        :param url: URL。
        :type url: str (optional)

        :param account_id: 账户ID。
        :type account_id: str (optional)

        :param user_id: 用户ID。
        :type user_id: str (optional)

        :param tags: 分组标签。
        :type tags: List[Tag] (optional)

        :param res_uuid: 资源记录ID。
        :type res_uuid: str (optional)
        """
        super().__init__()
        self.groups = groups
        self.name = name
        self.type = type
        self.region = region
        self.id = id
        self.uuid = uuid
        self.summary = summary
        self.url = url
        self.account_id = account_id
        self.user_id = user_id
        self.tags = tags
        self.res_uuid = res_uuid

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
        if self.groups is not None:
            result['groups'] = [i.to_dict() for i in self.groups]
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.region is not None:
            result['region'] = self.region
        if self.id is not None:
            result['id'] = self.id
        if self.uuid is not None:
            result['uuid'] = self.uuid
        if self.summary is not None:
            result['summary'] = self.summary
        if self.url is not None:
            result['url'] = self.url
        if self.account_id is not None:
            result['accountId'] = self.account_id
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.res_uuid is not None:
            result['resUuid'] = self.res_uuid
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ResourceGroupsDetailFull

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('groups') is not None:
            self.groups = [ResourceInfo().from_dict(i) for i in m.get('groups')]
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        if m.get('resUuid') is not None:
            self.res_uuid = m.get('resUuid')
        return self
