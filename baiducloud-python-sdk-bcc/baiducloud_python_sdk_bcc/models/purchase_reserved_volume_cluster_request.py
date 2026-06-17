"""
Request entity for PurchaseReservedVolumeClusterRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.billing import Billing


class PurchaseReservedVolumeClusterRequest(AbstractModel):
    """
    Request entity for PurchaseReservedVolumeClusterRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, cluster_id, billing):
        """
        Initialize PurchaseReservedVolumeClusterRequest request entity.

        :param cluster_id: cluster_id parameter
        :type cluster_id: str (required)

        :param billing: billing parameter
        :type billing: Billing (required)
        """
        super().__init__()
        self.cluster_id = cluster_id
        self.billing = billing

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PurchaseReservedVolumeClusterRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        return self
