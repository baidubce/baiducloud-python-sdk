"""
Request entity for DeleteElasticityAssuranceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteElasticityAssuranceRequest(AbstractModel):
    """
    Request entity for DeleteElasticityAssuranceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, elasticity_assurance_ids):
        """
        Initialize DeleteElasticityAssuranceRequest request entity.

        :param elasticity_assurance_ids: 待释放的弹性保障 ID，单次最多100个
        :type elasticity_assurance_ids: List[str] (required)
        """
        super().__init__()
        self.elasticity_assurance_ids = elasticity_assurance_ids

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteElasticityAssuranceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('elasticityAssuranceIds') is not None:
            self.elasticity_assurance_ids = m.get('elasticityAssuranceIds')
        return self
