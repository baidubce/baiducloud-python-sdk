"""
TbspIpCleanModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TbspIpCleanModel(AbstractModel):
    """
    TbspIpCleanModel
    """

    def __init__(
        self,
        ip=None,
        eip_name=None,
        eip_id=None,
        threshold_type=None,
        ip_clean_mbps=None,
        ip_clean_pps=None,
        protect_level=None,
        turn_off_begin_time=None,
        turn_off_end_time=None,
    ):
        """
        Initialize TbspIpCleanModel instance.

        :param ip: DDoS增强防护包防护对象IP地址
        :type ip: str (optional)

        :param eip_name: DDoS增强防护包防护对象IP名称
        :type eip_name: str (optional)

        :param eip_id: DDoS增强防护包防护对象EIP ID
        :type eip_id: str (optional)

        :param threshold_type: DDoS增强防护包IP清洗阈值类型，包含按带宽上限 (bandwidth)、智能阈值 (auto) 和手动设置 (manual)
        :type threshold_type: str (optional)

        :param ip_clean_mbps: 清洗阈值每秒流量带宽Mbps
        :type ip_clean_mbps: int (optional)

        :param ip_clean_pps: 清洗阈值每秒报文数pps
        :type ip_clean_pps: int (optional)

        :param protect_level: 防护等级，1（宽松）、2（适中）、3（严格）
        :type protect_level: str (optional)

        :param turn_off_begin_time: 关闭防护IP清洗起始时间
        :type turn_off_begin_time: str (optional)

        :param turn_off_end_time: 关闭防护IP清洗终止时间
        :type turn_off_end_time: str (optional)
        """
        super().__init__()
        self.ip = ip
        self.eip_name = eip_name
        self.eip_id = eip_id
        self.threshold_type = threshold_type
        self.ip_clean_mbps = ip_clean_mbps
        self.ip_clean_pps = ip_clean_pps
        self.protect_level = protect_level
        self.turn_off_begin_time = turn_off_begin_time
        self.turn_off_end_time = turn_off_end_time

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
        if self.eip_name is not None:
            result['eipName'] = self.eip_name
        if self.eip_id is not None:
            result['eipId'] = self.eip_id
        if self.threshold_type is not None:
            result['thresholdType'] = self.threshold_type
        if self.ip_clean_mbps is not None:
            result['ipCleanMbps'] = self.ip_clean_mbps
        if self.ip_clean_pps is not None:
            result['ipCleanPps'] = self.ip_clean_pps
        if self.protect_level is not None:
            result['protectLevel'] = self.protect_level
        if self.turn_off_begin_time is not None:
            result['turnOffBeginTime'] = self.turn_off_begin_time
        if self.turn_off_end_time is not None:
            result['turnOffEndTime'] = self.turn_off_end_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TbspIpCleanModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('eipName') is not None:
            self.eip_name = m.get('eipName')
        if m.get('eipId') is not None:
            self.eip_id = m.get('eipId')
        if m.get('thresholdType') is not None:
            self.threshold_type = m.get('thresholdType')
        if m.get('ipCleanMbps') is not None:
            self.ip_clean_mbps = m.get('ipCleanMbps')
        if m.get('ipCleanPps') is not None:
            self.ip_clean_pps = m.get('ipCleanPps')
        if m.get('protectLevel') is not None:
            self.protect_level = m.get('protectLevel')
        if m.get('turnOffBeginTime') is not None:
            self.turn_off_begin_time = m.get('turnOffBeginTime')
        if m.get('turnOffEndTime') is not None:
            self.turn_off_end_time = m.get('turnOffEndTime')
        return self
