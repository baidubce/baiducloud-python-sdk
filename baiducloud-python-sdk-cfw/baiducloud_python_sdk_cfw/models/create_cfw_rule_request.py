"""
Request entity for CreateCfwRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_cfw.models.create_rule import CreateRule


class CreateCfwRuleRequest(AbstractModel):
    """
    Request entity for CreateCfwRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, cfw_id, cfw_rules):
        """
        Initialize CreateCfwRuleRequest request entity.

        :param cfw_id: cfw_id parameter
        :type cfw_id: str (required)

        :param cfw_rules: CFW规则列表
        :type cfw_rules: List[CreateRule] (required)
        """
        super().__init__()
        self.cfw_id = cfw_id
        self.cfw_rules = cfw_rules

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
        if self.cfw_rules is not None:
            result['cfwRules'] = [i.to_dict() for i in self.cfw_rules]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateCfwRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cfwId') is not None:
            self.cfw_id = m.get('cfwId')
        if m.get('cfwRules') is not None:
            self.cfw_rules = [CreateRule().from_dict(i) for i in m.get('cfwRules')]
        return self
