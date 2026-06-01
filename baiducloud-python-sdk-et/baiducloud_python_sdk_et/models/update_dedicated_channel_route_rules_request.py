"""
Request entity for UpdateDedicatedChannelRouteRulesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateDedicatedChannelRouteRulesRequest(AbstractModel):
    """
    Request entity for UpdateDedicatedChannelRouteRulesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, et_id, et_channel_id, route_rule_id, description, client_token=None):
        """
        Initialize UpdateDedicatedChannelRouteRulesRequest request entity.

        :param et_id: et_id parameter
        :type et_id: str (required)

        :param et_channel_id: et_channel_id parameter
        :type et_channel_id: str (required)

        :param route_rule_id: route_rule_id parameter
        :type route_rule_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param description: 描述信息
        :type description: str (required)
        """
        super().__init__()
        self.et_id = et_id
        self.et_channel_id = et_channel_id
        self.route_rule_id = route_rule_id
        self.client_token = client_token
        self.description = description

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
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateDedicatedChannelRouteRulesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('etId') is not None:
            self.et_id = m.get('etId')
        if m.get('etChannelId') is not None:
            self.et_channel_id = m.get('etChannelId')
        if m.get('routeRuleId') is not None:
            self.route_rule_id = m.get('routeRuleId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
