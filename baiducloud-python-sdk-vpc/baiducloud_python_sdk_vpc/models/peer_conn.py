"""
PeerConn information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PeerConn(AbstractModel):
    """
    PeerConn
    """

    def __init__(
        self,
        peer_conn_id=None,
        role=None,
        status=None,
        bandwidth_in_mbps=None,
        description=None,
        local_if_id=None,
        local_if_name=None,
        local_vpc_id=None,
        local_region=None,
        peer_vpc_id=None,
        peer_region=None,
        peer_account_id=None,
        payment_timing=None,
        dns_status=None,
        created_time=None,
        expired_time=None,
    ):
        """
        Initialize PeerConn instance.

        :param peer_conn_id: 对等连接的ID
        :type peer_conn_id: str (optional)

        :param role: 对等连接角色 initiator发起端 acceptor接收端
        :type role: str (optional)

        :param status: 对等连接状态
        :type status: str (optional)

        :param bandwidth_in_mbps: 对等连接的带宽
        :type bandwidth_in_mbps: str (optional)

        :param description: 对等连接备注
        :type description: str (optional)

        :param local_if_id: 对等连接本端接口ID
        :type local_if_id: str (optional)

        :param local_if_name: 对等连接本端接口名称
        :type local_if_name: str (optional)

        :param local_vpc_id: 对等连接本端VPC的ID
        :type local_vpc_id: str (optional)

        :param local_region: 对等连接本端区域
        :type local_region: str (optional)

        :param peer_vpc_id: 对等连接对端VPC的ID
        :type peer_vpc_id: str (optional)

        :param peer_region: 对等连接对端区域
        :type peer_region: str (optional)

        :param peer_account_id: 对等连接对端的账户ID
        :type peer_account_id: str (optional)

        :param payment_timing: 对等连接的付费类型
        :type payment_timing: str (optional)

        :param dns_status: DNS同步状态
        :type dns_status: str (optional)

        :param created_time: 对等连接的创建时间
        :type created_time: str (optional)

        :param expired_time: 过期时间，只有预付费产品此参数才有值
        :type expired_time: str (optional)
        """
        super().__init__()
        self.peer_conn_id = peer_conn_id
        self.role = role
        self.status = status
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.description = description
        self.local_if_id = local_if_id
        self.local_if_name = local_if_name
        self.local_vpc_id = local_vpc_id
        self.local_region = local_region
        self.peer_vpc_id = peer_vpc_id
        self.peer_region = peer_region
        self.peer_account_id = peer_account_id
        self.payment_timing = payment_timing
        self.dns_status = dns_status
        self.created_time = created_time
        self.expired_time = expired_time

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
        if self.peer_conn_id is not None:
            result['peerConnId'] = self.peer_conn_id
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.description is not None:
            result['description'] = self.description
        if self.local_if_id is not None:
            result['localIfId'] = self.local_if_id
        if self.local_if_name is not None:
            result['localIfName'] = self.local_if_name
        if self.local_vpc_id is not None:
            result['localVpcId'] = self.local_vpc_id
        if self.local_region is not None:
            result['localRegion'] = self.local_region
        if self.peer_vpc_id is not None:
            result['peerVpcId'] = self.peer_vpc_id
        if self.peer_region is not None:
            result['peerRegion'] = self.peer_region
        if self.peer_account_id is not None:
            result['peerAccountId'] = self.peer_account_id
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.dns_status is not None:
            result['dnsStatus'] = self.dns_status
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PeerConn

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('peerConnId') is not None:
            self.peer_conn_id = m.get('peerConnId')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('localIfId') is not None:
            self.local_if_id = m.get('localIfId')
        if m.get('localIfName') is not None:
            self.local_if_name = m.get('localIfName')
        if m.get('localVpcId') is not None:
            self.local_vpc_id = m.get('localVpcId')
        if m.get('localRegion') is not None:
            self.local_region = m.get('localRegion')
        if m.get('peerVpcId') is not None:
            self.peer_vpc_id = m.get('peerVpcId')
        if m.get('peerRegion') is not None:
            self.peer_region = m.get('peerRegion')
        if m.get('peerAccountId') is not None:
            self.peer_account_id = m.get('peerAccountId')
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('dnsStatus') is not None:
            self.dns_status = m.get('dnsStatus')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        return self
