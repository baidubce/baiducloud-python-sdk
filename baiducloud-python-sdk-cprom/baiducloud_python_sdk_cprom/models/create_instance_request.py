"""
Request entity for CreateInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateInstanceRequest(AbstractModel):
    """
    Request entity for CreateInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_name,
        instance_type=None,
        instance_spec=None,
        retention_period=None,
        need_grafana=None,
        grafana_name=None,
        grafana_admin_password=None,
    ):
        """
        Initialize CreateInstanceRequest request entity.

        :param instance_name: 实例名称
        :type instance_name: str (required)

        :param instance_type: 监控实例类型，默认为CCE，代表CCE型监控实例，可选值：CCE、BCM
        :type instance_type: str (optional)

        :param instance_spec: 实例规格类型，默认为基础版\"free-v1\"，可选值：advance-v1，advance-v2，free-v1
        :type instance_spec: str (optional)

        :param retention_period: 数据存储时长，默认值为 `15d`。
        :type retention_period: str (optional)

        :param need_grafana: 是否需要创建 Grafana。当前地域无 Grafana 实例时可创建，一个地域仅能创建一个 Grafana 实例。
        :type need_grafana: bool (optional)

        :param grafana_name: 当 `needGrafana=true` 时提供，Grafana 名称，默认值为 `admin`。
        :type grafana_name: str (optional)

        :param grafana_admin_password: grafana_admin_password parameter
        :type grafana_admin_password: str (optional)
        """
        super().__init__()
        self.instance_name = instance_name
        self.instance_type = instance_type
        self.instance_spec = instance_spec
        self.retention_period = retention_period
        self.need_grafana = need_grafana
        self.grafana_name = grafana_name
        self.grafana_admin_password = grafana_admin_password

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
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.instance_spec is not None:
            result['instanceSpec'] = self.instance_spec
        if self.retention_period is not None:
            result['retentionPeriod'] = self.retention_period
        if self.need_grafana is not None:
            result['needGrafana'] = self.need_grafana
        if self.grafana_name is not None:
            result['grafanaName'] = self.grafana_name
        if self.grafana_admin_password is not None:
            result['grafanaAdminPassword'] = self.grafana_admin_password
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('instanceSpec') is not None:
            self.instance_spec = m.get('instanceSpec')
        if m.get('retentionPeriod') is not None:
            self.retention_period = m.get('retentionPeriod')
        if m.get('needGrafana') is not None:
            self.need_grafana = m.get('needGrafana')
        if m.get('grafanaName') is not None:
            self.grafana_name = m.get('grafanaName')
        if m.get('grafanaAdminPassword') is not None:
            self.grafana_admin_password = m.get('grafanaAdminPassword')
        return self
