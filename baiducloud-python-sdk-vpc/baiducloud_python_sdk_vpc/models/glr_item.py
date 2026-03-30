"""
GlrItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class GlrItem(AbstractModel):
    """
    GlrItem
    """

    def __init__(
        self,
        glr_id=None,
        ip_version=None,
        name=None,
        description=None,
        service_type=None,
        sub_service_type=None,
        resource_id=None,
        direction=None,
        cidr=None,
        bandwidth=None,
        enable=None,
        created_time=None,
        updated_time=None,
    ):
        """
        Initialize GlrItem instance.

        :param glr_id: 限速规则ID
        :type glr_id: str (optional)

        :param ip_version: IP协议版本，取值\"4\"
        :type ip_version: str (optional)

        :param name: 限速规则名称
        :type name: str (optional)

        :param description: 描述信息
        :type description: str (optional)

        :param service_type: 服务类型： <br>perrconn-对等连接 <br>et-专线网关 <br> csn-云智能网
        :type service_type: str (optional)

        :param sub_service_type: 子服务类型，当serviceType是csn时该字段存在值：<br>LOCAL 实例带宽 <br> PEER_CLOUD 云间互通 <br>PEER_EDGE 云边互通
        :type sub_service_type: str (optional)

        :param resource_id: 资源ID
        :type resource_id: str (optional)

        :param direction: 流量方向
        :type direction: str (optional)

        :param cidr: CIDR
        :type cidr: str (optional)

        :param bandwidth: 带宽
        :type bandwidth: int (optional)

        :param enable: 是否启用
        :type enable: bool (optional)

        :param created_time: 创建时间
        :type created_time: str (optional)

        :param updated_time: 修改时间
        :type updated_time: str (optional)
        """
        super().__init__()
        self.glr_id = glr_id
        self.ip_version = ip_version
        self.name = name
        self.description = description
        self.service_type = service_type
        self.sub_service_type = sub_service_type
        self.resource_id = resource_id
        self.direction = direction
        self.cidr = cidr
        self.bandwidth = bandwidth
        self.enable = enable
        self.created_time = created_time
        self.updated_time = updated_time

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
        if self.glr_id is not None:
            result['glrId'] = self.glr_id
        if self.ip_version is not None:
            result['ipVersion'] = self.ip_version
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.service_type is not None:
            result['serviceType'] = self.service_type
        if self.sub_service_type is not None:
            result['subServiceType'] = self.sub_service_type
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.direction is not None:
            result['direction'] = self.direction
        if self.cidr is not None:
            result['cidr'] = self.cidr
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        if self.enable is not None:
            result['enable'] = self.enable
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.updated_time is not None:
            result['updatedTime'] = self.updated_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GlrItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('glrId') is not None:
            self.glr_id = m.get('glrId')
        if m.get('ipVersion') is not None:
            self.ip_version = m.get('ipVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('serviceType') is not None:
            self.service_type = m.get('serviceType')
        if m.get('subServiceType') is not None:
            self.sub_service_type = m.get('subServiceType')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('direction') is not None:
            self.direction = m.get('direction')
        if m.get('cidr') is not None:
            self.cidr = m.get('cidr')
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')
        return self
