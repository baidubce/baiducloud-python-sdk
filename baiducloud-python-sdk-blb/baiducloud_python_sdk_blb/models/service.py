"""
Service information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_blb.models.related_endpoint import RelatedEndpoint

from baiducloud_python_sdk_blb.models.auth import Auth


class Service(AbstractModel):
    """
    Service
    """

    def __init__(
        self,
        service_id=None,
        name=None,
        description=None,
        service_name=None,
        bind_type=None,
        instance_id=None,
        status=None,
        service=None,
        create_time=None,
        endpoint_count=None,
        endpoint_list=None,
        auth_list=None,
    ):
        """
        Initialize Service instance.

        :param service_id: 服务发布点的id
        :type service_id: str (optional)

        :param name: 服务发布点的名称
        :type name: str (optional)

        :param description: 描述
        :type description: str (optional)

        :param service_name: 服务名称
        :type service_name: str (optional)

        :param bind_type: 绑定服务类型，目前仅支持绑定BLB实例
        :type bind_type: str (optional)

        :param instance_id: 绑定实例ID
        :type instance_id: str (optional)

        :param status: status attribute
        :type status: str (optional)

        :param service: 服务发布点唯一对应域名
        :type service: str (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param endpoint_count: 关联的服务网卡数量
        :type endpoint_count: int (optional)

        :param endpoint_list: 关联的服务网卡列表
        :type endpoint_list: List[RelatedEndpoint] (optional)

        :param auth_list: 授权列表
        :type auth_list: List[Auth] (optional)
        """
        super().__init__()
        self.service_id = service_id
        self.name = name
        self.description = description
        self.service_name = service_name
        self.bind_type = bind_type
        self.instance_id = instance_id
        self.status = status
        self.service = service
        self.create_time = create_time
        self.endpoint_count = endpoint_count
        self.endpoint_list = endpoint_list
        self.auth_list = auth_list

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
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.bind_type is not None:
            result['bindType'] = self.bind_type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.status is not None:
            result['status'] = self.status
        if self.service is not None:
            result['service'] = self.service
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.endpoint_count is not None:
            result['endpointCount'] = self.endpoint_count
        if self.endpoint_list is not None:
            result['endpointList'] = [i.to_dict() for i in self.endpoint_list]
        if self.auth_list is not None:
            result['authList'] = [i.to_dict() for i in self.auth_list]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Service

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('bindType') is not None:
            self.bind_type = m.get('bindType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('endpointCount') is not None:
            self.endpoint_count = m.get('endpointCount')
        if m.get('endpointList') is not None:
            self.endpoint_list = [RelatedEndpoint().from_dict(i) for i in m.get('endpointList')]
        if m.get('authList') is not None:
            self.auth_list = [Auth().from_dict(i) for i in m.get('authList')]
        return self
