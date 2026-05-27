"""
CsnBpLimit information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CsnBpLimit(AbstractModel):
    """
    CsnBpLimit
    """

    def __init__(self, csn_bp_id=None, csn_id=None, local_region=None, peer_region=None, bandwidth=None):
        """
        Initialize CsnBpLimit instance.

        :param csn_bp_id: 带宽包的ID
        :type csn_bp_id: str (optional)

        :param csn_id: 云智能网的ID
        :type csn_id: str (optional)

        :param local_region: 地域带宽的本端region，云边互通场景中表示云端region
        :type local_region: str (optional)

        :param peer_region: 地域带宽的对端region，云边互通场景中表示边缘region
        :type peer_region: str (optional)

        :param bandwidth: 地域带宽的带宽值
        :type bandwidth: int (optional)
        """
        super().__init__()
        self.csn_bp_id = csn_bp_id
        self.csn_id = csn_id
        self.local_region = local_region
        self.peer_region = peer_region
        self.bandwidth = bandwidth

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
        if self.csn_bp_id is not None:
            result['csnBpId'] = self.csn_bp_id
        if self.csn_id is not None:
            result['csnId'] = self.csn_id
        if self.local_region is not None:
            result['localRegion'] = self.local_region
        if self.peer_region is not None:
            result['peerRegion'] = self.peer_region
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CsnBpLimit

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('csnBpId') is not None:
            self.csn_bp_id = m.get('csnBpId')
        if m.get('csnId') is not None:
            self.csn_id = m.get('csnId')
        if m.get('localRegion') is not None:
            self.local_region = m.get('localRegion')
        if m.get('peerRegion') is not None:
            self.peer_region = m.get('peerRegion')
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        return self
