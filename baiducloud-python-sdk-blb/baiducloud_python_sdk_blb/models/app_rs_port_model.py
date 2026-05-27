"""
AppRsPortModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AppRsPortModel(AbstractModel):
    """
    AppRsPortModel
    """

    def __init__(
        self,
        listener_port=None,
        backend_port=None,
        port_type=None,
        health_check_port_type=None,
        status=None,
        port_id=None,
        policy_id=None,
    ):
        """
        Initialize AppRsPortModel instance.

        :param listener_port: 监听器端口(后端端口关联的监听器端口)
        :type listener_port: int (optional)

        :param backend_port: 后端开放的端口
        :type backend_port: str (optional)

        :param port_type: 端口协议类型(服务器组开放的端口类型，包含TCP、UDP、HTTP、HTTPS)
        :type port_type: str (optional)

        :param health_check_port_type: 健康检查端口协议类型(TCP、UDP、ICMP、HTTP、HTTPS)
        :type health_check_port_type: str (optional)

        :param status: 端口状态，\"Alive\"/\"Dead\"/\"Unknown\"
        :type status: str (optional)

        :param port_id: 端口id
        :type port_id: str (optional)

        :param policy_id: 对应策略id
        :type policy_id: str (optional)
        """
        super().__init__()
        self.listener_port = listener_port
        self.backend_port = backend_port
        self.port_type = port_type
        self.health_check_port_type = health_check_port_type
        self.status = status
        self.port_id = port_id
        self.policy_id = policy_id

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
        if self.listener_port is not None:
            result['listenerPort'] = self.listener_port
        if self.backend_port is not None:
            result['backendPort'] = self.backend_port
        if self.port_type is not None:
            result['portType'] = self.port_type
        if self.health_check_port_type is not None:
            result['healthCheckPortType'] = self.health_check_port_type
        if self.status is not None:
            result['status'] = self.status
        if self.port_id is not None:
            result['portId'] = self.port_id
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AppRsPortModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('listenerPort') is not None:
            self.listener_port = m.get('listenerPort')
        if m.get('backendPort') is not None:
            self.backend_port = m.get('backendPort')
        if m.get('portType') is not None:
            self.port_type = m.get('portType')
        if m.get('healthCheckPortType') is not None:
            self.health_check_port_type = m.get('healthCheckPortType')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('portId') is not None:
            self.port_id = m.get('portId')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        return self
