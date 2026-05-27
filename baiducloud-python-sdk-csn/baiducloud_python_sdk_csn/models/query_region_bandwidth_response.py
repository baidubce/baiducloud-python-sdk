"""
QueryRegionBandwidthResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse

from baiducloud_python_sdk_csn.models.csn_bp_limit import CsnBpLimit


class QueryRegionBandwidthResponse(BceResponse):
    """
    QueryRegionBandwidthResponse
    """

    def __init__(self, bp_limits=None):
        """
        Initialize QueryRegionBandwidthResponse instance.

        :param bp_limits: 地域带宽列表
        :type bp_limits: List[CsnBpLimit] (optional)
        """
        super().__init__()
        self.bp_limits = bp_limits

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.bp_limits is not None:
            result['bpLimits'] = [i.to_dict() for i in self.bp_limits]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryRegionBandwidthResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('bpLimits') is not None:
            self.bp_limits = [CsnBpLimit().from_dict(i) for i in m.get('bpLimits')]
        return self
