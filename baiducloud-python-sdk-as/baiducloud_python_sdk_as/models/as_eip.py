"""
AsEip information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AsEip(AbstractModel):
    """
    AsEip
    """

    def __init__(self, bandwidth_in_mbps=None, address=None, eip_id=None, eip_status=None, eip_allocation_id=None):
        """
        Initialize AsEip instance.

        :param bandwidth_in_mbps: 最大带宽
        :type bandwidth_in_mbps: int (optional)

        :param address: 公网IP
        :type address: str (optional)

        :param eip_id: EIP的ID
        :type eip_id: str (optional)

        :param eip_status: EIP状态
        :type eip_status: str (optional)

        :param eip_allocation_id: 弹性公网IP-实例ID
        :type eip_allocation_id: str (optional)
        """
        super().__init__()
        self.bandwidth_in_mbps = bandwidth_in_mbps
        self.address = address
        self.eip_id = eip_id
        self.eip_status = eip_status
        self.eip_allocation_id = eip_allocation_id

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
        if self.bandwidth_in_mbps is not None:
            result['bandwidthInMbps'] = self.bandwidth_in_mbps
        if self.address is not None:
            result['address'] = self.address
        if self.eip_id is not None:
            result['eipId'] = self.eip_id
        if self.eip_status is not None:
            result['eipStatus'] = self.eip_status
        if self.eip_allocation_id is not None:
            result['eipAllocationId'] = self.eip_allocation_id
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AsEip

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('bandwidthInMbps') is not None:
            self.bandwidth_in_mbps = m.get('bandwidthInMbps')
        if m.get('address') is not None:
            self.address = m.get('address')
        if m.get('eipId') is not None:
            self.eip_id = m.get('eipId')
        if m.get('eipStatus') is not None:
            self.eip_status = m.get('eipStatus')
        if m.get('eipAllocationId') is not None:
            self.eip_allocation_id = m.get('eipAllocationId')
        return self
