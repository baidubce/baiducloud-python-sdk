"""
Request entity for ModifyVolumeChargeTypeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.billing import Billing


class ModifyVolumeChargeTypeRequest(AbstractModel):
    """
    Request entity for ModifyVolumeChargeTypeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, volume_id, billing=None, effective_type=None):
        """
        Initialize ModifyVolumeChargeTypeRequest request entity.

        :param volume_id: volume_id parameter
        :type volume_id: str (required)

        :param billing: billing parameter
        :type billing: Billing (optional)

        :param effective_type: effective_type parameter
        :type effective_type: str (optional)
        """
        super().__init__()
        self.volume_id = volume_id
        self.billing = billing
        self.effective_type = effective_type

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
        if self.effective_type is not None:
            result['effectiveType'] = self.effective_type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyVolumeChargeTypeRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('volumeId') is not None:
            self.volume_id = m.get('volumeId')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('effectiveType') is not None:
            self.effective_type = m.get('effectiveType')
        return self
