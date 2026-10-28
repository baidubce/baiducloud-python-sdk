"""
Request entity for ModifyElasticityAssuranceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyElasticityAssuranceRequest(AbstractModel):
    """
    Request entity for ModifyElasticityAssuranceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, elasticity_assurance_ids, auto_renew, auto_renew_period=None):
        """
        Initialize ModifyElasticityAssuranceRequest request entity.

        :param elasticity_assurance_ids: 弹性保障id，单次最多100个
        :type elasticity_assurance_ids: List[str] (required)

        :param auto_renew: 是否自动续费, true：开启或修改自动续费；false：取消自动续费
        :type auto_renew: bool (required)

        :param auto_renew_period: auto_renew_period parameter
        :type auto_renew_period: int (optional)
        """
        super().__init__()
        self.elasticity_assurance_ids = elasticity_assurance_ids
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period

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
        if self.elasticity_assurance_ids is not None:
            result['elasticityAssuranceIds'] = self.elasticity_assurance_ids
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['autoRenewPeriod'] = self.auto_renew_period
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyElasticityAssuranceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('elasticityAssuranceIds') is not None:
            self.elasticity_assurance_ids = m.get('elasticityAssuranceIds')
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('autoRenewPeriod') is not None:
            self.auto_renew_period = m.get('autoRenewPeriod')
        return self
