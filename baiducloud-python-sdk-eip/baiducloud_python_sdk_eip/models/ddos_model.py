"""
DdosModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DdosModel(AbstractModel):
    """
    DdosModel
    """

    def __init__(
        self,
        ip=None,
        status=None,
        bind_instance_type=None,
        bind_instance_id=None,
        ip_clean_mbps=None,
        ip_clean_pps=None,
        threshold_type=None,
        maximum_threshold=None,
    ):
        """
        Initialize DdosModel instance.

        :param ip: 公网IP
        :type ip: str (optional)

        :param status: 基础防护状，包含normal正常、flush清洗中、blackhole封禁中
        :type status: str (optional)

        :param bind_instance_type: 公网IP绑定实例类型，若处于未绑定状态，此项值为空
        :type bind_instance_type: str (optional)

        :param bind_instance_id: 公网IP绑定实例ID，若处于未绑定状态，此项值为空
        :type bind_instance_id: str (optional)

        :param ip_clean_mbps: 清洗阈值每秒流量带宽Mbps
        :type ip_clean_mbps: int (optional)

        :param ip_clean_pps: 清洗阈值每秒报文数pps
        :type ip_clean_pps: int (optional)

        :param threshold_type: 清洗阈值类型，包含按带宽上限 (bandwidth)、智能阈值 (auto) 和手动设置 (manual)
        :type threshold_type: str (optional)

        :param maximum_threshold: 最大防护阈值MB
        :type maximum_threshold: int (optional)
        """
        super().__init__()
        self.ip = ip
        self.status = status
        self.bind_instance_type = bind_instance_type
        self.bind_instance_id = bind_instance_id
        self.ip_clean_mbps = ip_clean_mbps
        self.ip_clean_pps = ip_clean_pps
        self.threshold_type = threshold_type
        self.maximum_threshold = maximum_threshold

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
        if self.ip is not None:
            result['ip'] = self.ip
        if self.status is not None:
            result['status'] = self.status
        if self.bind_instance_type is not None:
            result['bindInstanceType'] = self.bind_instance_type
        if self.bind_instance_id is not None:
            result['bindInstanceId'] = self.bind_instance_id
        if self.ip_clean_mbps is not None:
            result['ipCleanMbps'] = self.ip_clean_mbps
        if self.ip_clean_pps is not None:
            result['ipCleanPps'] = self.ip_clean_pps
        if self.threshold_type is not None:
            result['thresholdType'] = self.threshold_type
        if self.maximum_threshold is not None:
            result['maximumThreshold'] = self.maximum_threshold
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DdosModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('bindInstanceType') is not None:
            self.bind_instance_type = m.get('bindInstanceType')
        if m.get('bindInstanceId') is not None:
            self.bind_instance_id = m.get('bindInstanceId')
        if m.get('ipCleanMbps') is not None:
            self.ip_clean_mbps = m.get('ipCleanMbps')
        if m.get('ipCleanPps') is not None:
            self.ip_clean_pps = m.get('ipCleanPps')
        if m.get('thresholdType') is not None:
            self.threshold_type = m.get('thresholdType')
        if m.get('maximumThreshold') is not None:
            self.maximum_threshold = m.get('maximumThreshold')
        return self
