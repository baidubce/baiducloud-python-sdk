"""
Request entity for UnbindVpcToRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_privatezone.models.vpc_region import VpcRegion


class UnbindVpcToRuleRequest(AbstractModel):
    """
    Request entity for UnbindVpcToRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, rule_id, vpc_regions, clien_token=None):
        """
        Initialize UnbindVpcToRuleRequest request entity.

        :param rule_id: rule_id parameter
        :type rule_id: str (required)

        :param clien_token: clien_token parameter
        :type clien_token: str (optional)

        :param vpc_regions: 要解绑的vpc信息
        :type vpc_regions: List[VpcRegion] (required)
        """
        super().__init__()
        self.rule_id = rule_id
        self.clien_token = clien_token
        self.vpc_regions = vpc_regions

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
        if self.vpc_regions is not None:
            result['vpcRegions'] = [i.to_dict() for i in self.vpc_regions]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UnbindVpcToRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('clienToken') is not None:
            self.clien_token = m.get('clienToken')
        if m.get('vpcRegions') is not None:
            self.vpc_regions = [VpcRegion().from_dict(i) for i in m.get('vpcRegions')]
        return self
