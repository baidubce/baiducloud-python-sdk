"""
Request entity for RenewElasticityAssuranceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RenewElasticityAssuranceRequest(AbstractModel):
    """
    Request entity for RenewElasticityAssuranceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, elasticity_assurance_ids, period):
        """
        Initialize RenewElasticityAssuranceRequest request entity.

        :param elasticity_assurance_ids: 弹性保障id集合，最多100个
        :type elasticity_assurance_ids: List[str] (required)

        :param period: 弹性保障续费时长，单位为月，允许值：1~9、12、24、36、48、60
        :type period: str (required)
        """
        super().__init__()
        self.elasticity_assurance_ids = elasticity_assurance_ids
        self.period = period

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
        if self.period is not None:
            result['period'] = self.period
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RenewElasticityAssuranceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('elasticityAssuranceIds') is not None:
            self.elasticity_assurance_ids = m.get('elasticityAssuranceIds')
        if m.get('period') is not None:
            self.period = m.get('period')
        return self
