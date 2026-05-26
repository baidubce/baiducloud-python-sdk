"""
Request entity for GetNatResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_vpc.models.session_config import SessionConfig
from baiducloud_python_sdk_vpc.models.tag_model import TagModel


class GetNatResponse(BceResponse):
    """
    GetNatResponse
    """

    def __init__(
        self,
        id=None,
        name=None,
        nat_type=None,
        vpc_id=None,
        spec=None,
        cu_num=None,
        bind_eips=None,
        status=None,
        ip_version=None,
        session_config=None,
        payment_timing=None,
        expired_time=None,
        create_time=None,
        tags=None,
        delete_protect=None,
    ):
        """
        Initialize GetNatResponse response.

        :param id: NAT网关的ID
        :type id: str (optional)

        :param name: NAT网关名称
        :type name: str (optional)

        :param nat_type: NAT网关类型，enhanced表示增强型，normal表示普通型
        :type nat_type: str (optional)

        :param vpc_id: NAT网关所属VPC的ID
        :type vpc_id: str (optional)

        :param spec: spec field
        :type spec: str (optional)

        :param cu_num: NAT网关的CU数量，仅适用于增强型NAT网关
        :type cu_num: int (optional)

        :param bind_eips: NAT网关绑定的EIP的IP地址列表，仅适用于增强型NAT网关
        :type bind_eips: List[str] (optional)

        :param status: NAT网关的状态
        :type status: str (optional)

        :param ip_version: NAT IP类型，v4/v6
        :type ip_version: str (optional)

        :param session_config: session_config field
        :type session_config: SessionConfig (optional)

        :param payment_timing: 付费方式 预付费Prepaid 后付费Postpaid
        :type payment_timing: str (optional)

        :param expired_time: 过期时间
        :type expired_time: str (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param tags: NAT网关绑定的标签列表
        :type tags: List[TagModel] (optional)

        :param delete_protect: 是否开启释放保护
        :type delete_protect: bool (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.nat_type = nat_type
        self.vpc_id = vpc_id
        self.spec = spec
        self.cu_num = cu_num
        self.bind_eips = bind_eips
        self.status = status
        self.ip_version = ip_version
        self.session_config = session_config
        self.payment_timing = payment_timing
        self.expired_time = expired_time
        self.create_time = create_time
        self.tags = tags
        self.delete_protect = delete_protect

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
        if self.nat_type is not None:
            result['natType'] = self.nat_type
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.spec is not None:
            result['spec'] = self.spec
        if self.cu_num is not None:
            result['cuNum'] = self.cu_num
        if self.bind_eips is not None:
            result['bindEips'] = self.bind_eips
        if self.status is not None:
            result['status'] = self.status
        if self.ip_version is not None:
            result['ipVersion'] = self.ip_version
        if self.session_config is not None:
            result['sessionConfig'] = self.session_config.to_dict()
        if self.payment_timing is not None:
            result['paymentTiming'] = self.payment_timing
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.delete_protect is not None:
            result['deleteProtect'] = self.delete_protect
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetNatResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('natType') is not None:
            self.nat_type = m.get('natType')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('cuNum') is not None:
            self.cu_num = m.get('cuNum')
        if m.get('bindEips') is not None:
            self.bind_eips = m.get('bindEips')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        if m.get('sessionConfig') is not None:
            self.session_config = SessionConfig().from_dict(m.get('sessionConfig'))
        if m.get('paymentTiming') is not None:
            self.payment_timing = m.get('paymentTiming')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('deleteProtect') is not None:
            self.delete_protect = m.get('deleteProtect')
        return self
