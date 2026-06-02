"""
Request entity for DescribeLbdcResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_blb.models.tag_model import TagModel


class DescribeLbdcResponse(BceResponse):
    """
    DescribeLbdcResponse
    """

    def __init__(
        self,
        id=None,
        name=None,
        type=None,
        status=None,
        ccu_count=None,
        create_time=None,
        expire_time=None,
        total_connect_count=None,
        new_connect_cps=None,
        network_in_bps=None,
        network_out_bps=None,
        https_qps=None,
        http_qps=None,
        http_new_connect_cps=None,
        https_new_connect_cps=None,
        ssl_new_connect_cps=None,
        tags=None,
    ):
        """
        Initialize DescribeLbdcResponse response.

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

        :param total_connect_count: 并发连接数
        :type total_connect_count: int (optional)

        :param new_connect_cps: 新建连接速度，四层集群专有
        :type new_connect_cps: int (optional)

        :param network_in_bps: 网络输入带宽
        :type network_in_bps: int (optional)

        :param network_out_bps: 网络输出带宽
        :type network_out_bps: int (optional)

        :param https_qps: https的qps
        :type https_qps: int (optional)

        :param http_qps: http的qps
        :type http_qps: int (optional)

        :param http_new_connect_cps: http新建速度
        :type http_new_connect_cps: int (optional)

        :param https_new_connect_cps: https新建速度
        :type https_new_connect_cps: int (optional)

        :param ssl_new_connect_cps: ssl新建速度
        :type ssl_new_connect_cps: int (optional)

        :param tags: 标签
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.type = type
        self.status = status
        self.ccu_count = ccu_count
        self.create_time = create_time
        self.expire_time = expire_time
        self.total_connect_count = total_connect_count
        self.new_connect_cps = new_connect_cps
        self.network_in_bps = network_in_bps
        self.network_out_bps = network_out_bps
        self.https_qps = https_qps
        self.http_qps = http_qps
        self.http_new_connect_cps = http_new_connect_cps
        self.https_new_connect_cps = https_new_connect_cps
        self.ssl_new_connect_cps = ssl_new_connect_cps
        self.tags = tags

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
        if self.total_connect_count is not None:
            result['totalConnectCount'] = self.total_connect_count
        if self.new_connect_cps is not None:
            result['newConnectCps'] = self.new_connect_cps
        if self.network_in_bps is not None:
            result['networkInBps'] = self.network_in_bps
        if self.network_out_bps is not None:
            result['networkOutBps'] = self.network_out_bps
        if self.https_qps is not None:
            result['httpsQps'] = self.https_qps
        if self.http_qps is not None:
            result['httpQps'] = self.http_qps
        if self.http_new_connect_cps is not None:
            result['httpNewConnectCps'] = self.http_new_connect_cps
        if self.https_new_connect_cps is not None:
            result['httpsNewConnectCps'] = self.https_new_connect_cps
        if self.ssl_new_connect_cps is not None:
            result['sslNewConnectCps'] = self.ssl_new_connect_cps
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeLbdcResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
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
        if m.get('totalConnectCount') is not None:
            self.total_connect_count = m.get('totalConnectCount')
        if m.get('newConnectCps') is not None:
            self.new_connect_cps = m.get('newConnectCps')
        if m.get('networkInBps') is not None:
            self.network_in_bps = m.get('networkInBps')
        if m.get('networkOutBps') is not None:
            self.network_out_bps = m.get('networkOutBps')
        if m.get('httpsQps') is not None:
            self.https_qps = m.get('httpsQps')
        if m.get('httpQps') is not None:
            self.http_qps = m.get('httpQps')
        if m.get('httpNewConnectCps') is not None:
            self.http_new_connect_cps = m.get('httpNewConnectCps')
        if m.get('httpsNewConnectCps') is not None:
            self.https_new_connect_cps = m.get('httpsNewConnectCps')
        if m.get('sslNewConnectCps') is not None:
            self.ssl_new_connect_cps = m.get('sslNewConnectCps')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
