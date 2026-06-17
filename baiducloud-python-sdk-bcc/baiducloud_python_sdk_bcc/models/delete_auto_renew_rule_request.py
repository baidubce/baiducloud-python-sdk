"""
Request entity for DeleteAutoRenewRuleRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteAutoRenewRuleRequest(AbstractModel):
    """
    Request entity for DeleteAutoRenewRuleRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, renew_eip=None):
        """
        Initialize DeleteAutoRenewRuleRequest request entity.

        :param instance_id: 实例ID
        :type instance_id: str (required)

        :param renew_eip: 是否合并关闭eip自动续费，默认为true。
        :type renew_eip: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.renew_eip = renew_eip

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.renew_eip is not None:
            result['renewEip'] = self.renew_eip
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteAutoRenewRuleRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('renewEip') is not None:
            self.renew_eip = m.get('renewEip')
        return self
