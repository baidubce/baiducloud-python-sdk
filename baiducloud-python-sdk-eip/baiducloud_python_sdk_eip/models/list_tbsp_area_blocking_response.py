"""
Request entity for ListTbspAreaBlockingResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_eip.models.tbsp_area_blocking_model import TbspAreaBlockingModel


class ListTbspAreaBlockingResponse(BceResponse):
    """
    ListTbspAreaBlockingResponse
    """

    def __init__(self, area_blocking_list=None, id=None):
        """
        Initialize ListTbspAreaBlockingResponse response.

        :param area_blocking_list: 包含查询结果的列表
        :type area_blocking_list: List[TbspAreaBlockingModel] (optional)

        :param id: DDoS增强防护包ID
        :type id: str (optional)
        """
        super().__init__()
        self.area_blocking_list = area_blocking_list
        self.id = id

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
            result['metadata'] = self.metadata
        if self.area_blocking_list is not None:
            result['areaBlockingList'] = [i.to_dict() for i in self.area_blocking_list]
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListTbspAreaBlockingResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('areaBlockingList') is not None:
            self.area_blocking_list = [TbspAreaBlockingModel().from_dict(i) for i in m.get('areaBlockingList')]
        if m.get('id') is not None:
            self.id = m.get('id')
        return self
