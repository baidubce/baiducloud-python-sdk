"""
Request entity for QueryAssociationRelationResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_csn.models.csn_rt_association import CsnRtAssociation


class QueryAssociationRelationResponse(BceResponse):
    """
    QueryAssociationRelationResponse
    """

    def __init__(self, associations=None):
        """
        Initialize QueryAssociationRelationResponse response.

        :param associations: 包含查询结果的列表
        :type associations: List[CsnRtAssociation] (optional)
        """
        super().__init__()
        self.associations = associations

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
        if self.associations is not None:
            result['associations'] = [i.to_dict() for i in self.associations]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryAssociationRelationResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('associations') is not None:
            self.associations = [CsnRtAssociation().from_dict(i) for i in m.get('associations')]
        return self
