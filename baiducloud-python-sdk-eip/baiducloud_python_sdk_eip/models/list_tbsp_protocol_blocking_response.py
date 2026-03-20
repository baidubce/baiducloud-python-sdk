"""
Request entity for ListTbspProtocolBlockingResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_eip.models.tbsp_protocol_blocking_model import TbspProtocolBlockingModel


class ListTbspProtocolBlockingResponse(BceResponse):
    """
    ListTbspProtocolBlockingResponse
    """

    def __init__(self, protocol_blocking_list=None, id=None):
        """
        Initialize ListTbspProtocolBlockingResponse response.

        :param protocol_blocking_list: 包含查询结果的列表
        :type protocol_blocking_list: List[TbspProtocolBlockingModel] (optional)

        :param id: DDoS增强防护包ID
        :type id: str (optional)
        """
        super().__init__()
        self.protocol_blocking_list = protocol_blocking_list
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
        if self.protocol_blocking_list is not None:
            result['protocolBlockingList'] = [i.to_dict() for i in self.protocol_blocking_list]
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
        :rtype: ListTbspProtocolBlockingResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('protocolBlockingList') is not None:
            self.protocol_blocking_list = [
                TbspProtocolBlockingModel().from_dict(i) for i in m.get('protocolBlockingList')
            ]
        if m.get('id') is not None:
            self.id = m.get('id')
        return self
