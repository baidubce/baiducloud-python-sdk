"""
Instance information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ccr.models.logical_tag import LogicalTag


class Instance(AbstractModel):
    """
    Instance
    """

    def __init__(
        self,
        id=None,
        name=None,
        instance_type=None,
        public_url=None,
        private_url=None,
        custom_domains=None,
        region=None,
        status=None,
        create_time=None,
        expire_time=None,
        tags=None,
    ):
        """
        Initialize Instance instance.

        :param id: 实例 ID
        :type id: str (optional)

        :param name: 实例名称
        :type name: str (optional)

        :param instance_type: 实例类型。<br>`BASIC`：基础版；`STANDARD`：标准版；`ADVANCED`：高级版
        :type instance_type: str (optional)

        :param public_url: 公网访问地址
        :type public_url: str (optional)

        :param private_url: 内网访问地址
        :type private_url: str (optional)

        :param custom_domains: 自定义域名信息
        :type custom_domains: List[str] (optional)

        :param region: 地域
        :type region: str (optional)

        :param status: 实例状态
        :type status: str (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param expire_time: 到期时间
        :type expire_time: str (optional)

        :param tags: 标签键值对信息
        :type tags: List[LogicalTag] (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.instance_type = instance_type
        self.public_url = public_url
        self.private_url = private_url
        self.custom_domains = custom_domains
        self.region = region
        self.status = status
        self.create_time = create_time
        self.expire_time = expire_time
        self.tags = tags

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
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.public_url is not None:
            result['publicURL'] = self.public_url
        if self.private_url is not None:
            result['privateURL'] = self.private_url
        if self.custom_domains is not None:
            result['customDomains'] = self.custom_domains
        if self.region is not None:
            result['region'] = self.region
        if self.status is not None:
            result['status'] = self.status
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Instance

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('publicURL') is not None:
            self.public_url = m.get('publicURL')
        if m.get('privateURL') is not None:
            self.private_url = m.get('privateURL')
        if m.get('customDomains') is not None:
            self.custom_domains = m.get('customDomains')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('tags') is not None:
            self.tags = [LogicalTag().from_dict(i) for i in m.get('tags')]
        return self
