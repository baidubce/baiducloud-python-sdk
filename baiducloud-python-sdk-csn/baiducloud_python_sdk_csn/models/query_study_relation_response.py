"""
Request entity for QueryStudyRelationResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_csn.models.csn_rt_propagation import CsnRtPropagation


class QueryStudyRelationResponse(BceResponse):
    """
    QueryStudyRelationResponse
    """

    def __init__(self, propagations=None):
        """
        Initialize QueryStudyRelationResponse response.

        :param propagations: 包含查询结果的列表
        :type propagations: List[CsnRtPropagation] (optional)
        """
        super().__init__()
        self.propagations = propagations

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.propagations is not None:
            result['propagations'] = [i.to_dict() for i in self.propagations]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryStudyRelationResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('propagations') is not None:
            self.propagations = [CsnRtPropagation().from_dict(i) for i in m.get('propagations')]
        return self
