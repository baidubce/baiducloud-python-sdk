"""
Request entity for GetAcceleratorFilterDetailResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ccr.models.accelerator_filter import AcceleratorFilter


class GetAcceleratorFilterDetailResponse(BceResponse):
    """
    GetAcceleratorFilterDetailResponse
    """

    def __init__(
        self, creation_time=None, description=None, enabled=None, filters=None, id=None, name=None, update_time=None
    ):
        """
        Initialize GetAcceleratorFilterDetailResponse response.

        :param creation_time: 镜像按需加载规则创建时间
        :type creation_time: str (optional)

        :param description: 备注
        :type description: str (optional)

        :param enabled: 镜像按需加载规则是否开启
        :type enabled: bool (optional)

        :param filters: 触发规则
        :type filters: List[AcceleratorFilter] (optional)

        :param id: 镜像按需加载规则ID
        :type id: int (optional)

        :param name: 镜像按需加载规则名称
        :type name: str (optional)

        :param update_time: 镜像按需加载规则更新时间
        :type update_time: str (optional)
        """
        super().__init__()
        self.creation_time = creation_time
        self.description = description
        self.enabled = enabled
        self.filters = filters
        self.id = id
        self.name = name
        self.update_time = update_time

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.description is not None:
            result['description'] = self.description
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.filters is not None:
            result['filters'] = [i.to_dict() for i in self.filters]
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetAcceleratorFilterDetailResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('filters') is not None:
            self.filters = [AcceleratorFilter().from_dict(i) for i in m.get('filters')]
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self
