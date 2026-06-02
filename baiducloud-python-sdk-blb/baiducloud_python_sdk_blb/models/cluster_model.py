"""
ClusterModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ClusterModel(AbstractModel):
    """
    ClusterModel
    """

    def __init__(
        self, id=None, name=None, type=None, status=None, ccu_count=None, create_time=None, expire_time=None, desc=None
    ):
        """
        Initialize ClusterModel instance.

        :param id: 集群id
        :type id: str (optional)

        :param name: 集群名称
        :type name: str (optional)

        :param type: 集群类型
        :type type: str (optional)

        :param status: 集群状态
        :type status: str (optional)

        :param ccu_count: 集群性能容量
        :type ccu_count: int (optional)

        :param create_time: 集群创建时间
        :type create_time: str (optional)

        :param expire_time: 集群失效时间
        :type expire_time: str (optional)

        :param desc: 描述
        :type desc: str (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.type = type
        self.status = status
        self.ccu_count = ccu_count
        self.create_time = create_time
        self.expire_time = expire_time
        self.desc = desc

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
        if self.type is not None:
            result['type'] = self.type
        if self.status is not None:
            result['status'] = self.status
        if self.ccu_count is not None:
            result['ccuCount'] = self.ccu_count
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.desc is not None:
            result['desc'] = self.desc
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ClusterModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('ccuCount') is not None:
            self.ccu_count = m.get('ccuCount')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        return self
