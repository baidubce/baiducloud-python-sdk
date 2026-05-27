"""
Request entity for DeleteRouteRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteRouteRuleRequest(AbstractModel):
    """
    Request entity for DeleteRouteRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, csn_rt_id, csn_rt_rule_id, client_token=None):
        """
        Initialize DeleteRouteRuleRequest request entity.

        :param csn_rt_id: csn_rt_id parameter
        :type csn_rt_id: str (required)

        :param csn_rt_rule_id: csn_rt_rule_id parameter
        :type csn_rt_rule_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)
        """
        super().__init__()
        self.csn_rt_id = csn_rt_id
        self.csn_rt_rule_id = csn_rt_rule_id
        self.client_token = client_token

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteRouteRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('csnRtId') is not None:
            self.csn_rt_id = m.get('csnRtId')
        if m.get('csnRtRuleId') is not None:
            self.csn_rt_rule_id = m.get('csnRtRuleId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self
