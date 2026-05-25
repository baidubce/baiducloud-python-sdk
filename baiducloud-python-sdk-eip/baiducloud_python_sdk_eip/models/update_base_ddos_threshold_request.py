"""
Request entity for UpdateBaseDdosThresholdRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateBaseDdosThresholdRequest(AbstractModel):
    """
    Request entity for UpdateBaseDdosThresholdRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, ip, threshold_type, ip_clean_mbps, ip_clean_pps, client_token=None):
        """
        Initialize UpdateBaseDdosThresholdRequest request entity.

        :param ip: ip parameter
        :type ip: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param threshold_type: 清洗阈值设置类型，包含按带宽上限 (bandwidth)、智能阈值 (auto) 和手动设置 (manual)
        :type threshold_type: str (required)

        :param ip_clean_mbps: 每秒流量带宽Mbps，最小值为120Mbps，最大值为5000Mbps (当清洗阈值设置类型为manual时必填)
        :type ip_clean_mbps: int (required)

        :param ip_clean_pps: 每秒报文数pps，最小值为58594pps，最大值为4882813pps (当清洗阈值设置类型为manual时必填)
        :type ip_clean_pps: int (required)
        """
        super().__init__()
        self.ip = ip
        self.client_token = client_token
        self.threshold_type = threshold_type
        self.ip_clean_mbps = ip_clean_mbps
        self.ip_clean_pps = ip_clean_pps

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
        if self.threshold_type is not None:
            result['thresholdType'] = self.threshold_type
        if self.ip_clean_mbps is not None:
            result['ipCleanMbps'] = self.ip_clean_mbps
        if self.ip_clean_pps is not None:
            result['ipCleanPps'] = self.ip_clean_pps
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateBaseDdosThresholdRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('thresholdType') is not None:
            self.threshold_type = m.get('thresholdType')
        if m.get('ipCleanMbps') is not None:
            self.ip_clean_mbps = m.get('ipCleanMbps')
        if m.get('ipCleanPps') is not None:
            self.ip_clean_pps = m.get('ipCleanPps')
        return self
