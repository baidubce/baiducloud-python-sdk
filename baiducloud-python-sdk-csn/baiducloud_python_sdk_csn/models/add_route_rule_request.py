"""
Request entity for AddRouteRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AddRouteRuleRequest(AbstractModel):
    """
    Request entity for AddRouteRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, csn_rt_id, attach_id, dest_address, route_type, client_token=None):
        """
        Initialize AddRouteRuleRequest request entity.

        :param csn_rt_id: csn_rt_id parameter
        :type csn_rt_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param attach_id: 网络实例在云智能网中的身份的ID
        :type attach_id: str (required)

        :param dest_address: 路由的目的地址，当前只支持0.0.0.0/0
        :type dest_address: str (required)

        :param route_type: 路由类型，当前只支持custom
        :type route_type: str (required)
        """
        super().__init__()
        self.csn_rt_id = csn_rt_id
        self.client_token = client_token
        self.attach_id = attach_id
        self.dest_address = dest_address
        self.route_type = route_type

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
        if self.attach_id is not None:
            result['attachId'] = self.attach_id
        if self.dest_address is not None:
            result['destAddress'] = self.dest_address
        if self.route_type is not None:
            result['routeType'] = self.route_type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AddRouteRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('csnRtId') is not None:
            self.csn_rt_id = m.get('csnRtId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('attachId') is not None:
            self.attach_id = m.get('attachId')
        if m.get('destAddress') is not None:
            self.dest_address = m.get('destAddress')
        if m.get('routeType') is not None:
            self.route_type = m.get('routeType')
        return self
