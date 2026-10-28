"""
Request entity for RenewElasticityAssuranceResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class RenewElasticityAssuranceResponse(BceResponse):
    """
    RenewElasticityAssuranceResponse
    """

    def __init__(self, order_id=None, elasticity_assurance_ids=None):
        """
        Initialize RenewElasticityAssuranceResponse response.

        :param order_id: 续费弹性保障的订单号
        :type order_id: str (optional)

        :param elasticity_assurance_ids: 弹性保障的id集合
        :type elasticity_assurance_ids: List[str] (optional)
        """
        super().__init__()
        self.order_id = order_id
        self.elasticity_assurance_ids = elasticity_assurance_ids

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.elasticity_assurance_ids is not None:
            result['elasticityAssuranceIds'] = self.elasticity_assurance_ids
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RenewElasticityAssuranceResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('elasticityAssuranceIds') is not None:
            self.elasticity_assurance_ids = m.get('elasticityAssuranceIds')
        return self
