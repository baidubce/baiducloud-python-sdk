"""
Request entity for UpdateStrategyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateStrategyRequest(AbstractModel):
    """
    Request entity for UpdateStrategyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, policy_name, document, name=None, description=None):
        """
        Initialize UpdateStrategyRequest request entity.

        :param policy_name: policy_name parameter
        :type policy_name: str (required)

        :param name: 新策略名
        :type name: str (optional)

        :param description: 策略的描述
        :type description: str (optional)

        :param document: 策略内容，ACL格式序列化后得到的String
        :type document: str (required)
        """
        super().__init__()
        self.policy_name = policy_name
        self.name = name
        self.description = description
        self.document = document

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
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.document is not None:
            result['document'] = self.document
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateStrategyRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('document') is not None:
            self.document = m.get('document')
        return self
