"""
EipMoveOutModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_eip.models.billing import Billing


class EipMoveOutModel(AbstractModel):
    """
    EipMoveOutModel
    """

    def __init__(self, eip=None, bandwidth_in_mbps=None, billing=None):
        """
        Initialize EipMoveOutModel instance.

        :param eip: 待移出的EIP IP地址
        :type eip: str (optional)

        :param bandwidth_in_mbps: 移出后的EIP带宽值，单位为Mbps（只有移出共享带宽原生的EIP需要此参数）
        :type bandwidth_in_mbps: int (optional)

        :param billing: billing attribute
        :type billing: Billing (optional)
        """
        super().__init__()
        self.eip = eip
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.billing = billing

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
        if self.eip is not None:
            result['eip'] = self.eip
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EipMoveOutModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eip') is not None:
            self.eip = m.get('eip')
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        return self
