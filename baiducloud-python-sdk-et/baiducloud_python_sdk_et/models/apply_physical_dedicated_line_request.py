"""
Request entity for ApplyPhysicalDedicatedLineRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_et.models.billing import Billing
from baiducloud_python_sdk_et.models.reservation import Reservation
from baiducloud_python_sdk_et.models.tag_model import TagModel


class ApplyPhysicalDedicatedLineRequest(AbstractModel):
    """
    Request entity for ApplyPhysicalDedicatedLineRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        name,
        isp,
        intf_type,
        ap_type,
        ap_addr,
        user_name,
        user_phone,
        user_email,
        user_idc,
        client_token=None,
        description=None,
        link_delay=None,
        billing=None,
        auto_renew=None,
        tags=None,
    ):
        """
        Initialize ApplyPhysicalDedicatedLineRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 专线名称,大小写字母、数字以及-_ /.特殊字符，必须以字母开头，长度1-65
        :type name: str (required)

        :param description: 描述
        :type description: str (optional)

        :param isp: isp parameter
        :type isp: str (required)

        :param intf_type: 物理端口规格，取值：1G/10G/100G/40G/400G
        :type intf_type: str (required)

        :param ap_type: 线路类型，百度内部用户：BAIDU，外部用户：SINGLE
        :type ap_type: str (required)

        :param ap_addr: ap_addr parameter
        :type ap_addr: str (required)

        :param link_delay: 端口延迟down时间，单位ms
        :type link_delay: int (optional)

        :param user_name: 用户名称
        :type user_name: str (required)

        :param user_phone: 用户手机号码
        :type user_phone: str (required)

        :param user_email: 用户邮箱
        :type user_email: str (required)

        :param user_idc: user_idc parameter
        :type user_idc: str (required)

        :param billing: billing parameter
        :type billing: Billing (optional)

        :param auto_renew: auto_renew parameter
        :type auto_renew: Reservation (optional)

        :param tags: 待创建的标签键值对列表
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.description = description
        self.isp = isp
        self.intf_type = intf_type
        self.ap_type = ap_type
        self.ap_addr = ap_addr
        self.link_delay = link_delay
        self.user_name = user_name
        self.user_phone = user_phone
        self.user_email = user_email
        self.user_idc = user_idc
        self.billing = billing
        self.auto_renew = auto_renew
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
        if self.description is not None:
            result['description'] = self.description
        if self.isp is not None:
            result['isp'] = self.isp
        if self.intf_type is not None:
            result['intfType'] = self.intf_type
        if self.ap_type is not None:
            result['apType'] = self.ap_type
        if self.ap_addr is not None:
            result['apAddr'] = self.ap_addr
        if self.link_delay is not None:
            result['linkDelay'] = self.link_delay
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.user_phone is not None:
            result['userPhone'] = self.user_phone
        if self.user_email is not None:
            result['userEmail'] = self.user_email
        if self.user_idc is not None:
            result['userIdc'] = self.user_idc
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew.to_dict()
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
        :rtype: ApplyPhysicalDedicatedLineRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('isp') is not None:
            self.isp = m.get('isp')
        if m.get('intfType') is not None:
            self.intf_type = m.get('intfType')
        if m.get('apType') is not None:
            self.ap_type = m.get('apType')
        if m.get('apAddr') is not None:
            self.ap_addr = m.get('apAddr')
        if m.get('linkDelay') is not None:
            self.link_delay = m.get('linkDelay')
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('userPhone') is not None:
            self.user_phone = m.get('userPhone')
        if m.get('userEmail') is not None:
            self.user_email = m.get('userEmail')
        if m.get('userIdc') is not None:
            self.user_idc = m.get('userIdc')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('autoRenew') is not None:
            self.auto_renew = Reservation().from_dict(m.get('autoRenew'))
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
