"""
ReplicationRegistry information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ccr.models.registry_credential import RegistryCredential


class ReplicationRegistry(AbstractModel):
    """
    ReplicationRegistry
    """

    def __init__(
        self,
        creation_time=None,
        credential=None,
        description=None,
        id=None,
        insecure=None,
        name=None,
        status=None,
        type=None,
        update_time=None,
        url=None,
        region=None,
    ):
        """
        Initialize ReplicationRegistry instance.

        :param creation_time: Registry 创建时间
        :type creation_time: str (optional)

        :param credential: credential attribute
        :type credential: RegistryCredential (optional)

        :param description: Registry 描述
        :type description: str (optional)

        :param id: Registry ID
        :type id: int (optional)

        :param insecure: 当 Harbor 尝试访问服务器时，是否验证证书
        :type insecure: bool (optional)

        :param name: Registry 名称
        :type name: str (optional)

        :param status: Registry 健康状态
        :type status: str (optional)

        :param type: Registry 类型，可选值：`docker-hub`、`docker-registry`、`harbor`
        :type type: str (optional)

        :param update_time: Registry 更新时间
        :type update_time: str (optional)

        :param url: Registry 地址
        :type url: str (optional)

        :param region: Registry 所在地区
        :type region: str (optional)
        """
        super().__init__()
        self.creation_time = creation_time
        self.credential = credential
        self.description = description
        self.id = id
        self.insecure = insecure
        self.name = name
        self.status = status
        self.type = type
        self.update_time = update_time
        self.url = url
        self.region = region

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
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.credential is not None:
            result['credential'] = self.credential.to_dict()
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.insecure is not None:
            result['insecure'] = self.insecure
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.url is not None:
            result['url'] = self.url
        if self.region is not None:
            result['region'] = self.region
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ReplicationRegistry

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('credential') is not None:
            self.credential = RegistryCredential().from_dict(m.get('credential'))
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('insecure') is not None:
            self.insecure = m.get('insecure')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('region') is not None:
            self.region = m.get('region')
        return self
