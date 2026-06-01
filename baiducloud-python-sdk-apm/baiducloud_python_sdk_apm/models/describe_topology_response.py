"""
Request entity for DescribeTopologyResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_apm.models.topo_node import TopoNode
from baiducloud_python_sdk_apm.models.topo_edge import TopoEdge


class DescribeTopologyResponse(BceResponse):
    """
    DescribeTopologyResponse
    """

    def __init__(self, success=None, code=None, message=None, nodes=None, edges=None):
        """
        Initialize DescribeTopologyResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 状态码
        :type code: str (optional)

        :param message: 错误信息
        :type message: str (optional)

        :param nodes: 节点列表
        :type nodes: List[TopoNode] (optional)

        :param edges: 边列表
        :type edges: List[TopoEdge] (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.message = message
        self.nodes = nodes
        self.edges = edges

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
        if self.success is not None:
            result['success'] = self.success
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.nodes is not None:
            result['nodes'] = [i.to_dict() for i in self.nodes]
        if self.edges is not None:
            result['edges'] = [i.to_dict() for i in self.edges]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeTopologyResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('nodes') is not None:
            self.nodes = [TopoNode().from_dict(i) for i in m.get('nodes')]
        if m.get('edges') is not None:
            self.edges = [TopoEdge().from_dict(i) for i in m.get('edges')]
        return self
