"""
NodeTypeItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class NodeTypeItem(AbstractModel):
    """
    NodeTypeItem
    """

    def __init__(
        self,
        node_type=None,
        instance_flavor=None,
        cpu_num=None,
        network_throughput_in_gbps=None,
        peak_qps=None,
        max_connections=None,
        allowed_node_num_list=None,
        min_disk_flavor=None,
        max_disk_flavor=None,
    ):
        """
        Initialize NodeTypeItem instance.

        :param node_type: 节点规格
        :type node_type: str (optional)

        :param instance_flavor: 节点容量
        :type instance_flavor: int (optional)

        :param cpu_num: cpu数量
        :type cpu_num: int (optional)

        :param network_throughput_in_gbps: 网络吞吐
        :type network_throughput_in_gbps: float (optional)

        :param peak_qps: 参考最大Qps
        :type peak_qps: int (optional)

        :param max_connections: 最大连接数
        :type max_connections: int (optional)

        :param allowed_node_num_list: 允许的分片数量
        :type allowed_node_num_list: List[int] (optional)

        :param min_disk_flavor: Pegadb规格最小的磁盘大小，单位GB。
        :type min_disk_flavor: int (optional)

        :param max_disk_flavor: Pegadb规格最小的磁盘大小，单位GB。
        :type max_disk_flavor: int (optional)
        """
        super().__init__()
        self.node_type = node_type
        self.instance_flavor = instance_flavor
        self.cpu_num = cpu_num
        self.network_throughput_in_gbps = network_throughput_in_gbps
        self.peak_qps = peak_qps
        self.max_connections = max_connections
        self.allowed_node_num_list = allowed_node_num_list
        self.min_disk_flavor = min_disk_flavor
        self.max_disk_flavor = max_disk_flavor

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
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.instance_flavor is not None:
            result['instanceFlavor'] = self.instance_flavor
        if self.cpu_num is not None:
            result['cpuNum'] = self.cpu_num
        if self.network_throughput_in_gbps is not None:
            result['networkThroughputInGbps'] = self.network_throughput_in_gbps
        if self.peak_qps is not None:
            result['peakQps'] = self.peak_qps
        if self.max_connections is not None:
            result['maxConnections'] = self.max_connections
        if self.allowed_node_num_list is not None:
            result['allowedNodeNumList'] = self.allowed_node_num_list
        if self.min_disk_flavor is not None:
            result['minDiskFlavor'] = self.min_disk_flavor
        if self.max_disk_flavor is not None:
            result['maxDiskFlavor'] = self.max_disk_flavor
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: NodeTypeItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('instanceFlavor') is not None:
            self.instance_flavor = m.get('instanceFlavor')
        if m.get('cpuNum') is not None:
            self.cpu_num = m.get('cpuNum')
        if m.get('networkThroughputInGbps') is not None:
            self.network_throughput_in_gbps = m.get('networkThroughputInGbps')
        if m.get('peakQps') is not None:
            self.peak_qps = m.get('peakQps')
        if m.get('maxConnections') is not None:
            self.max_connections = m.get('maxConnections')
        if m.get('allowedNodeNumList') is not None:
            self.allowed_node_num_list = m.get('allowedNodeNumList')
        if m.get('minDiskFlavor') is not None:
            self.min_disk_flavor = m.get('minDiskFlavor')
        if m.get('maxDiskFlavor') is not None:
            self.max_disk_flavor = m.get('maxDiskFlavor')
        return self
