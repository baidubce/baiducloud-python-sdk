"""
Request entity for PurchaseReservedVolumeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.billing import Billing


class PurchaseReservedVolumeRequest(AbstractModel):
    """
    Request entity for PurchaseReservedVolumeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, volume_id, billing, instance_id=None):
        """
        Initialize PurchaseReservedVolumeRequest request entity.

        :param volume_id: volume_id parameter
        :type volume_id: str (required)

        :param billing: billing parameter
        :type billing: Billing (required)

        :param instance_id: 未挂载磁盘预期挂载到的预付费BCC实例ID，磁盘未挂载状态下必传，已挂载状态下可不传或传当前挂载的实例ID
        :type instance_id: str (optional)
        """
        super().__init__()
        self.volume_id = volume_id
        self.billing = billing
        self.instance_id = instance_id

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
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PurchaseReservedVolumeRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('volumeId') is not None:
            self.volume_id = m.get('volumeId')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        return self
