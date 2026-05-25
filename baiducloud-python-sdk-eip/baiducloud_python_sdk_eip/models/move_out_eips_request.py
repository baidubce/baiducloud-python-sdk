"""
Request entity for MoveOutEipsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_eip.models.eip_move_out_model import EipMoveOutModel


class MoveOutEipsRequest(AbstractModel):
    """
    Request entity for MoveOutEipsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, id, move_out_eips, client_token=None):
        """
        Initialize MoveOutEipsRequest request entity.

        :param id: id parameter
        :type id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param move_out_eips: 待移出EIP列表，包括IPv4 EIP和IPv6 EIP
        :type move_out_eips: List[EipMoveOutModel] (required)
        """
        super().__init__()
        self.id = id
        self.client_token = client_token
        self.move_out_eips = move_out_eips

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
        if self.move_out_eips is not None:
            result['moveOutEips'] = [i.to_dict() for i in self.move_out_eips]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MoveOutEipsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('moveOutEips') is not None:
            self.move_out_eips = [EipMoveOutModel().from_dict(i) for i in m.get('moveOutEips')]
        return self
