"""
Request entity for ResizeNatRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ResizeNatRequest(AbstractModel):
    """
    Request entity for ResizeNatRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, nat_id, cu_num, client_token=None):
        """
        Initialize ResizeNatRequest request entity.

        :param nat_id: nat_id parameter
        :type nat_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param cu_num: NAT网关变配的CU数量，取值1~100
        :type cu_num: int (required)
        """
        super().__init__()
        self.nat_id = nat_id
        self.client_token = client_token
        self.cu_num = cu_num

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
        if self.cu_num is not None:
            result['cuNum'] = self.cu_num
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ResizeNatRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('natId') is not None:
            self.nat_id = m.get('natId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('cuNum') is not None:
            self.cu_num = m.get('cuNum')
        return self
