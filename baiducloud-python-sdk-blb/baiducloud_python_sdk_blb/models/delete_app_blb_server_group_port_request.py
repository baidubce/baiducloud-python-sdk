"""
Request entity for DeleteAppBlbServerGroupPortRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteAppBlbServerGroupPortRequest(AbstractModel):
    """
    Request entity for DeleteAppBlbServerGroupPortRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, blb_id, sg_id, port_id_list, client_token=None):
        """
        Initialize DeleteAppBlbServerGroupPortRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param sg_id: 要删除的端口所在服务器组id
        :type sg_id: str (required)

        :param port_id_list: 所有待释放的端口id，一起组成一个数组
        :type port_id_list: List[str] (required)
        """
        super().__init__()
        self.blb_id = blb_id
        self.client_token = client_token
        self.sg_id = sg_id
        self.port_id_list = port_id_list

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
        if self.sg_id is not None:
            result['sgId'] = self.sg_id
        if self.port_id_list is not None:
            result['portIdList'] = self.port_id_list
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteAppBlbServerGroupPortRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('sgId') is not None:
            self.sg_id = m.get('sgId')
        if m.get('portIdList') is not None:
            self.port_id_list = m.get('portIdList')
        return self
