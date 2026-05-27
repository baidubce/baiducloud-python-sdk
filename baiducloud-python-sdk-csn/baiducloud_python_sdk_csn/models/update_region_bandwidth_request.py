"""
Request entity for UpdateRegionBandwidthRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateRegionBandwidthRequest(AbstractModel):
    """
    Request entity for UpdateRegionBandwidthRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, csn_bp_id, local_region, peer_region, bandwidth, client_token=None):
        """
        Initialize UpdateRegionBandwidthRequest request entity.

        :param csn_bp_id: csn_bp_id parameter
        :type csn_bp_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param local_region: 地域带宽的本端region，该值不能改变
        :type local_region: str (required)

        :param peer_region: 地域带宽的对端region，该值不能改变
        :type peer_region: str (required)

        :param bandwidth: 更新的地域带宽的带宽值
        :type bandwidth: int (required)
        """
        super().__init__()
        self.csn_bp_id = csn_bp_id
        self.client_token = client_token
        self.local_region = local_region
        self.peer_region = peer_region
        self.bandwidth = bandwidth

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
        if self.local_region is not None:
            result['localRegion'] = self.local_region
        if self.peer_region is not None:
            result['peerRegion'] = self.peer_region
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateRegionBandwidthRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('csnBpId') is not None:
            self.csn_bp_id = m.get('csnBpId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('localRegion') is not None:
            self.local_region = m.get('localRegion')
        if m.get('peerRegion') is not None:
            self.peer_region = m.get('peerRegion')
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        return self
