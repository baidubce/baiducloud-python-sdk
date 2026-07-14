"""
EipInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class EipInfo(AbstractModel):
    """
    EipInfo
    """

    def __init__(self, if_bind_eip=None, bandwidth_in_mbps=None, eip_product_type=None, purchase_type=None):
        """
        Initialize EipInfo instance.

        :param if_bind_eip: 是否绑定EIP
        :type if_bind_eip: bool (optional)

        :param bandwidth_in_mbps: EIP带宽
        :type bandwidth_in_mbps: int (optional)

        :param eip_product_type: EIP公网带宽计费类型，按带宽计费：bandwidth，按流量计费：netraffic
        :type eip_product_type: str (optional)

        :param purchase_type: 购买线路类型，标准型：BGP，增强型：BGP_S
        :type purchase_type: str (optional)
        """
        super().__init__()
        self.if_bind_eip = if_bind_eip
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.eip_product_type = eip_product_type
        self.purchase_type = purchase_type

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
        if self.if_bind_eip is not None:
            result['ifBindEip'] = self.if_bind_eip
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.eip_product_type is not None:
            result['eipProductType'] = self.eip_product_type
        if self.purchase_type is not None:
            result['purchaseType'] = self.purchase_type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: EipInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ifBindEip') is not None:
            self.if_bind_eip = m.get('ifBindEip')
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('eipProductType') is not None:
            self.eip_product_type = m.get('eipProductType')
        if m.get('purchaseType') is not None:
            self.purchase_type = m.get('purchaseType')
        return self
