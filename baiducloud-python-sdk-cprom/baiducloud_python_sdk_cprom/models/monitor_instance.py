"""
MonitorInstance information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_cprom.models.status import Status


class MonitorInstance(AbstractModel):
    """
    MonitorInstance
    """

    def __init__(
        self,
        instance_id=None,
        instance_name=None,
        instance_spec=None,
        instance_type=None,
        retention_period=None,
        create_time=None,
        grafana_id=None,
        grafana_name=None,
        status=None,
    ):
        """
        Initialize MonitorInstance instance.

        :param instance_id: 监控实例ID
        :type instance_id: str (optional)

        :param instance_name: 监控实例名字
        :type instance_name: str (optional)

        :param instance_spec: 实例规格类型，默认为基础版\"free-v1\"，可选值：advance-v1，advance-v2，free-v1
        :type instance_spec: str (optional)

        :param instance_type: 监控实例类型，默认为CCE，代表CCE型监控实例，可选值：CCE、BCM
        :type instance_type: str (optional)

        :param retention_period: 数据存储时长，示例格式: 15d
        :type retention_period: str (optional)

        :param create_time: 监控实例创建时间（0时区），格式: 2025-02-05T08:14:23Z
        :type create_time: str (optional)

        :param grafana_id: Grafana ID
        :type grafana_id: str (optional)

        :param grafana_name: Grafana名称
        :type grafana_name: str (optional)

        :param status: status attribute
        :type status: Status (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_spec = instance_spec
        self.instance_type = instance_type
        self.retention_period = retention_period
        self.create_time = create_time
        self.grafana_id = grafana_id
        self.grafana_name = grafana_name
        self.status = status

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.instance_spec is not None:
            result['instanceSpec'] = self.instance_spec
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.retention_period is not None:
            result['retentionPeriod'] = self.retention_period
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.grafana_id is not None:
            result['grafanaId'] = self.grafana_id
        if self.grafana_name is not None:
            result['grafanaName'] = self.grafana_name
        if self.status is not None:
            result['status'] = self.status.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MonitorInstance

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('instanceSpec') is not None:
            self.instance_spec = m.get('instanceSpec')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('retentionPeriod') is not None:
            self.retention_period = m.get('retentionPeriod')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('grafanaId') is not None:
            self.grafana_id = m.get('grafanaId')
        if m.get('grafanaName') is not None:
            self.grafana_name = m.get('grafanaName')
        if m.get('status') is not None:
            self.status = Status().from_dict(m.get('status'))
        return self
