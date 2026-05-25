"""
Request entity for DeleteCfwRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteCfwRuleRequest(AbstractModel):
    """
    Request entity for DeleteCfwRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, cfw_id, cfw_rule_ids):
        """
        Initialize DeleteCfwRuleRequest request entity.

        :param cfw_id: cfw_id parameter
        :type cfw_id: str (required)

        :param cfw_rule_ids: 批量删除的CFW规则id
        :type cfw_rule_ids: List[str] (required)
        """
        super().__init__()
        self.cfw_id = cfw_id
        self.cfw_rule_ids = cfw_rule_ids

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
        if self.cfw_rule_ids is not None:
            result['cfwRuleIds'] = self.cfw_rule_ids
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteCfwRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cfwId') is not None:
            self.cfw_id = m.get('cfwId')
        if m.get('cfwRuleIds') is not None:
            self.cfw_rule_ids = m.get('cfwRuleIds')
        return self
