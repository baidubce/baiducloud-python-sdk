"""
Request entity for NatUnBindEipRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class NatUnBindEipRequest(AbstractModel):
    """
    Request entity for NatUnBindEipRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, nat_id, bind_eips, client_token=None):
        """
        Initialize NatUnBindEipRequest request entity.

        :param nat_id: nat_id parameter
        :type nat_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param bind_eips: 解绑的EIP列表
        :type bind_eips: List[str] (required)
        """
        super().__init__()
        self.nat_id = nat_id
        self.client_token = client_token
        self.bind_eips = bind_eips

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
        if self.bind_eips is not None:
            result['bindEips'] = self.bind_eips
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: NatUnBindEipRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('natId') is not None:
            self.nat_id = m.get('natId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('bindEips') is not None:
            self.bind_eips = m.get('bindEips')
        return self
