"""
Request entity for BillingChangePreToPostBlbRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class BillingChangePreToPostBlbRequest(AbstractModel):
    """
    Request entity for BillingChangePreToPostBlbRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, blb_id, client_token=None, billing_method=None, performance_level=None, effective_immediately=None
    ):
        """
        Initialize BillingChangePreToPostBlbRequest request entity.

        :param blb_id: blb_id parameter
        :type blb_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param billing_method: 计费方式。\"BySpec\"表示按固定规格计费(默认值)，\"ByCapacityUnit\"表示按使用量计费。
        :type billing_method: str (optional)

        :param performance_level:
            性能规格参数，默认为当前实例的性能规格。取值如下：\"small1\"标准型1，\"small2\"标准型2，\"medium1\"增强型1，\"medium2\"增强型2，\"large1\"超大型1，
            \"large2\"超大型2，\"large3\"超大型3。仅后付费-按使用量支持\"unlimited\"不限速。
        :type performance_level: str (optional)

        :param effective_immediately: 是否立即生效，默认false。
        :type effective_immediately: bool (optional)
        """
        super().__init__()
        self.blb_id = blb_id
        self.client_token = client_token
        self.billing_method = billing_method
        self.performance_level = performance_level
        self.effective_immediately = effective_immediately

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
        if self.billing_method is not None:
            result['billingMethod'] = self.billing_method
        if self.performance_level is not None:
            result['performanceLevel'] = self.performance_level
        if self.effective_immediately is not None:
            result['effectiveImmediately'] = self.effective_immediately
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BillingChangePreToPostBlbRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('blbId') is not None:
            self.blb_id = m.get('blbId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('billingMethod') is not None:
            self.billing_method = m.get('billingMethod')
        if m.get('performanceLevel') is not None:
            self.performance_level = m.get('performanceLevel')
        if m.get('effectiveImmediately') is not None:
            self.effective_immediately = m.get('effectiveImmediately')
        return self
