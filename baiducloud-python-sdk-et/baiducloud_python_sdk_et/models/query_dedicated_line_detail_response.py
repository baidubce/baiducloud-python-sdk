"""
Request entity for QueryDedicatedLineDetailResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_et.models.tag_model import TagModel


class QueryDedicatedLineDetailResponse(BceResponse):
    """
    QueryDedicatedLineDetailResponse
    """

    def __init__(
        self,
        id=None,
        name=None,
        description=None,
        status=None,
        expire_time=None,
        isp=None,
        intf_type=None,
        ap_type=None,
        ap_addr=None,
        link_delay=None,
        user_name=None,
        user_phone=None,
        user_email=None,
        user_idc=None,
        tags=None,
    ):
        """
        Initialize QueryDedicatedLineDetailResponse response.

        :param id: 专线ID
        :type id: str (optional)

        :param name: 名称
        :type name: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param status: status field
        :type status: str (optional)

        :param expire_time: 到期时间
        :type expire_time: str (optional)

        :param isp: isp field
        :type isp: str (optional)

        :param intf_type: 接口规格，取值：1G/10G/100G
        :type intf_type: str (optional)

        :param ap_type: 接入类型
        :type ap_type: str (optional)

        :param ap_addr: 接入点
        :type ap_addr: str (optional)

        :param link_delay: 端口延迟down时间
        :type link_delay: int (optional)

        :param user_name: 用户名称
        :type user_name: str (optional)

        :param user_phone: 用户手机
        :type user_phone: str (optional)

        :param user_email: 用户邮箱
        :type user_email: str (optional)

        :param user_idc: 对端地址
        :type user_idc: str (optional)

        :param tags: 专线绑定的标签列表
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.description = description
        self.status = status
        self.expire_time = expire_time
        self.isp = isp
        self.intf_type = intf_type
        self.ap_type = ap_type
        self.ap_addr = ap_addr
        self.link_delay = link_delay
        self.user_name = user_name
        self.user_phone = user_phone
        self.user_email = user_email
        self.user_idc = user_idc
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
        if self.description is not None:
            result['description'] = self.description
        if self.status is not None:
            result['status'] = self.status
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
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
        :rtype: QueryDedicatedLineDetailResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
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
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
