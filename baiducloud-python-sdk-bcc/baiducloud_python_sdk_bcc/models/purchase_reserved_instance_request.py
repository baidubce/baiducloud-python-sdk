"""
Request entity for PurchaseReservedInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.billing import Billing
from baiducloud_python_sdk_bcc.models.cds_custom_period import CdsCustomPeriod


class PurchaseReservedInstanceRequest(AbstractModel):
    """
    Request entity for PurchaseReservedInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, billing, related_renew_flag=None, cds_custom_period=None):
        """
        Initialize PurchaseReservedInstanceRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param related_renew_flag: related_renew_flag parameter
        :type related_renew_flag: str (optional)

        :param billing: billing parameter
        :type billing: Billing (required)

        :param cds_custom_period: cds_custom_period parameter
        :type cds_custom_period: List[CdsCustomPeriod] (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.related_renew_flag = related_renew_flag
        self.billing = billing
        self.cds_custom_period = cds_custom_period

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
        if self.cds_custom_period is not None:
            result['cdsCustomPeriod'] = [i.to_dict() for i in self.cds_custom_period]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PurchaseReservedInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('relatedRenewFlag') is not None:
            self.related_renew_flag = m.get('relatedRenewFlag')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('cdsCustomPeriod') is not None:
            self.cds_custom_period = [CdsCustomPeriod().from_dict(i) for i in m.get('cdsCustomPeriod')]
        return self
