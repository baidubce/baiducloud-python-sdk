"""
Request entity for DeleteAppBlbListenerRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_blb.models.port_type_model import PortTypeModel


class DeleteAppBlbListenerRequest(AbstractModel):
    """
    Request entity for DeleteAppBlbListenerRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, blb_id, client_token=None, port_list=None, port_type_list=None):
        """
        Initialize DeleteAppBlbListenerRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param port_list: 所有待释放的监听器的端口，一起组成一个数组
        :type port_list: List[int] (optional)

        :param port_type_list: port_type_list parameter
        :type port_type_list: List[PortTypeModel] (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.client_token = client_token
        self.port_list = port_list
        self.port_type_list = port_type_list

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
        if self.port_list is not None:
            result['portList'] = self.port_list
        if self.port_type_list is not None:
            result['portTypeList'] = [i.to_dict() for i in self.port_type_list]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteAppBlbListenerRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('portList') is not None:
            self.port_list = m.get('portList')
        if m.get('portTypeList') is not None:
            self.port_type_list = [PortTypeModel().from_dict(i) for i in m.get('portTypeList')]
        return self
