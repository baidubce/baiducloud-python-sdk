"""
Request entity for DescribeCacheNodesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_rapidfs.models.filter import Filter


class DescribeCacheNodesRequest(AbstractModel):
    """
    Request entity for DescribeCacheNodesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, filters=None, max_keys=None, marker=None):
        """
        Initialize DescribeCacheNodesRequest request entity.

        :param instance_id: RapidFS 实例 ID
        :type instance_id: str (required)

        :param filters: filters parameter
        :type filters: List[Filter] (optional)

        :param max_keys: 返回列表长度，有效范围 [1, 1000]，默认 100
        :type max_keys: int (optional)

        :param marker: 批量获取列表的查询的起始位置，返回列表按 cacheNodeId 字典序排序，取值为上一次返回的 nextMarker
        :type marker: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.filters = filters
        self.max_keys = max_keys
        self.marker = marker

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
        if self.filters is not None:
            result['filters'] = [i.to_dict() for i in self.filters]
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeCacheNodesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('filters') is not None:
            self.filters = [Filter().from_dict(i) for i in m.get('filters')]
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self
