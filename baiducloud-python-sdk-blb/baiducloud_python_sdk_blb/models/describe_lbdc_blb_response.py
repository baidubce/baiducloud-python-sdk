"""
Request entity for DescribeLbdcBlbResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_blb.models.associate_blb_model import AssociateBlbModel


class DescribeLbdcBlbResponse(BceResponse):
    """
    DescribeLbdcBlbResponse
    """

    def __init__(self, blb_list=None):
        """
        Initialize DescribeLbdcBlbResponse response.

        :param blb_list: 包含查询结果的BLB列表
        :type blb_list: List[AssociateBlbModel] (optional)
        """
        super().__init__()
        self.blb_list = blb_list

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
        if self.blb_list is not None:
            result['blbList'] = [i.to_dict() for i in self.blb_list]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeLbdcBlbResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbList') is not None:
            self.blb_list = [AssociateBlbModel().from_dict(i) for i in m.get('blbList')]
        return self
