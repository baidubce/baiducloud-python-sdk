"""
Request entity for EipBandwidthScalingCapacityRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class EipBandwidthScalingCapacityRequest(AbstractModel):
    """
    Request entity for EipBandwidthScalingCapacityRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, eip, new_bandwidth_in_mbps, client_token=None):
        """
        Initialize EipBandwidthScalingCapacityRequest request entity.

        :param eip: eip parameter
        :type eip: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param new_bandwidth_in_mbps:
            公网带宽，单位为Mbps。对于预付费(prepay)以及按带宽(bandwidth)类型的EIP，限制为1~200之间的整数，对于按流量(traffic)类型的EIP，限制为1~1000之间的整数。
        :type new_bandwidth_in_mbps: int (required)
        """
        super().__init__()
        self.eip = eip
        self.client_token = client_token
        self.new_bandwidth_in_mbps = new_bandwidth_in_mbps

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
        if self.new_bandwidth_in_mbps is not None:
            result['newBandwidthInMbps'] = self.new_bandwidth_in_mbps
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EipBandwidthScalingCapacityRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('newBandwidthInMbps') is not None:
            self.new_bandwidth_in_mbps = m.get('newBandwidthInMbps')
        return self
