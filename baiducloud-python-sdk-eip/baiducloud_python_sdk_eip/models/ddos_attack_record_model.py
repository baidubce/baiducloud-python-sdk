"""
DdosAttackRecordModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DdosAttackRecordModel(AbstractModel):
    """
    DdosAttackRecordModel
    """

    def __init__(
        self,
        ip=None,
        start_time=None,
        end_time=None,
        attack_type=None,
        attack_peak_mbps=None,
        attack_peak_pps=None,
        attack_peak_qps=None,
        attack_status=None,
    ):
        """
        Initialize DdosAttackRecordModel instance.

        :param ip: 公网IP
        :type ip: str (optional)

        :param start_time: 攻击开始UTC时间
        :type start_time: str (optional)

        :param end_time: 攻击结束UTC时间
        :type end_time: str (optional)

        :param attack_type: 攻击类型
        :type attack_type: List[str] (optional)

        :param attack_peak_mbps: 攻击峰值每秒流量带宽Mbps
        :type attack_peak_mbps: int (optional)

        :param attack_peak_pps: 攻击峰值每秒报文数pps
        :type attack_peak_pps: int (optional)

        :param attack_peak_qps: 攻击峰值每秒服务请求数qps
        :type attack_peak_qps: int (optional)

        :param attack_status: 攻击状态，包含underway攻击中、ended攻击结束
        :type attack_status: str (optional)
        """
        super().__init__()
        self.ip = ip
        self.start_time = start_time
        self.end_time = end_time
        self.attack_type = attack_type
        self.attack_peak_mbps = attack_peak_mbps
        self.attack_peak_pps = attack_peak_pps
        self.attack_peak_qps = attack_peak_qps
        self.attack_status = attack_status

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
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.attack_type is not None:
            result['attackType'] = self.attack_type
        if self.attack_peak_mbps is not None:
            result['attackPeakMbps'] = self.attack_peak_mbps
        if self.attack_peak_pps is not None:
            result['attackPeakPps'] = self.attack_peak_pps
        if self.attack_peak_qps is not None:
            result['attackPeakQps'] = self.attack_peak_qps
        if self.attack_status is not None:
            result['attackStatus'] = self.attack_status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DdosAttackRecordModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('attackType') is not None:
            self.attack_type = m.get('attackType')
        if m.get('attackPeakMbps') is not None:
            self.attack_peak_mbps = m.get('attackPeakMbps')
        if m.get('attackPeakPps') is not None:
            self.attack_peak_pps = m.get('attackPeakPps')
        if m.get('attackPeakQps') is not None:
            self.attack_peak_qps = m.get('attackPeakQps')
        if m.get('attackStatus') is not None:
            self.attack_status = m.get('attackStatus')
        return self
