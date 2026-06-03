"""
AihcResourcePoolInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AihcResourcePoolInfo(AbstractModel):
    """
    AihcResourcePoolInfo
    """

    def __init__(self, resource_pool_id=None, name=None, type=None, zones=None, bound_instance_ids=None):
        """
        Initialize AihcResourcePoolInfo instance.

        :param resource_pool_id: 百舸资源池 ID
        :type resource_pool_id: str (optional)

        :param name: 百舸资源池名称（排序键）
        :type name: str (optional)

        :param type: 百舸资源池类型
        :type type: str (optional)

        :param zones: 百舸资源池关联的可用区列表，由其子网自动聚合得出
        :type zones: List[str] (optional)

        :param bound_instance_ids: bound_instance_ids attribute
        :type bound_instance_ids: List[str] (optional)
        """
        super().__init__()
        self.resource_pool_id = resource_pool_id
        self.name = name
        self.type = type
        self.zones = zones
        self.bound_instance_ids = bound_instance_ids

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
        if self.resource_pool_id is not None:
            result['resourcePoolId'] = self.resource_pool_id
        if self.name is not None:
            result['name'] = self.name
        if self.type is not None:
            result['type'] = self.type
        if self.zones is not None:
            result['zones'] = self.zones
        if self.bound_instance_ids is not None:
            result['boundInstanceIds'] = self.bound_instance_ids
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AihcResourcePoolInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('resourcePoolId') is not None:
            self.resource_pool_id = m.get('resourcePoolId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('zones') is not None:
            self.zones = m.get('zones')
        if m.get('boundInstanceIds') is not None:
            self.bound_instance_ids = m.get('boundInstanceIds')
        return self
