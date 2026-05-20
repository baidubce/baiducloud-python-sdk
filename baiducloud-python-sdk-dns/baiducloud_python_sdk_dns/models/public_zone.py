"""
PublicZone information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_dns.models.tag_model import TagModel


class PublicZone(AbstractModel):
    """
    PublicZone
    """

    def __init__(
        self, id=None, name=None, status=None, product_version=None, create_time=None, expire_time=None, tags=None
    ):
        """
        Initialize PublicZone instance.

        :param id: zone的id。
        :type id: str (optional)

        :param name: 域名名称。
        :type name: str (optional)

        :param status: status attribute
        :type status: str (optional)

        :param product_version: 产品版本，包含：基础版(free)、普惠版(discount)、企业版(flagship)。
        :type product_version: str (optional)

        :param create_time: 创建时间(北京时间)，比如：“2022-04-28 17:05:45”。
        :type create_time: str (optional)

        :param expire_time: 到期时间(北京时间)，比如：“2023-04-28 17:05:44”。
        :type expire_time: str (optional)

        :param tags: 标签键值对列表。
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.status = status
        self.product_version = product_version
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
        if self.status is not None:
            result['status'] = self.status
        if self.product_version is not None:
            result['productVersion'] = self.product_version
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
        :rtype: PublicZone

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('productVersion') is not None:
            self.product_version = m.get('productVersion')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
