"""
Request entity for DescribeAihcResourcePoolsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeAihcResourcePoolsRequest(AbstractModel):
    """
    Request entity for DescribeAihcResourcePoolsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, vpc_id, max_keys=None, marker=None):
        """
        Initialize DescribeAihcResourcePoolsRequest request entity.

        :param vpc_id: VPC ID，仅返回归属该 VPC 的资源池
        :type vpc_id: str (required)

        :param max_keys: 返回列表长度，有效范围 [1, 1000]，默认 100
        :type max_keys: int (optional)

        :param marker: 批量获取列表的查询的起始位置，取值为上一次返回的 nextMarker
        :type marker: str (optional)
        """
        super().__init__()
        self.vpc_id = vpc_id
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
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
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
        :rtype: DescribeAihcResourcePoolsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self
