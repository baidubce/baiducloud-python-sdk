"""
Request entity for CreatePfsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_pfs.models.tag import Tag


class CreatePfsRequest(AbstractModel):
    """
    Request entity for CreatePfsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, instance_type, capacity, subnet_id, description=None, tags=None):
        """
        Initialize CreatePfsRequest request entity.

        :param name: name parameter
        :type name: str (required)

        :param instance_type: 可选类型包括：base、basic、baseX、plus、plus2、plusl2X
        :type instance_type: str (required)

        :param capacity: 购买文件系统存储容量大小，详情见容量限制表（单位GB）
        :type capacity: int (required)

        :param subnet_id: 子网短ID
        :type subnet_id: str (required)

        :param description: 实例描述
        :type description: str (optional)

        :param tags: 实例标签
        :type tags: List[Tag] (optional)
        """
        super().__init__()
        self.name = name
        self.instance_type = instance_type
        self.capacity = capacity
        self.subnet_id = subnet_id
        self.description = description
        self.tags = tags

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
        if self.name is not None:
            result['name'] = self.name
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.capacity is not None:
            result['capacity'] = self.capacity
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.description is not None:
            result['description'] = self.description
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreatePfsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('capacity') is not None:
            self.capacity = m.get('capacity')
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('tags') is not None:
            self.tags = [Tag().from_dict(i) for i in m.get('tags')]
        return self
