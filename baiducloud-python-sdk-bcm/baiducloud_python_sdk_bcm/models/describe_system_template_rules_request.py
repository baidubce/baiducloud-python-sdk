"""
Request entity for DescribeSystemTemplateRulesRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DescribeSystemTemplateRulesRequest(AbstractModel):
    """
    Request entity for DescribeSystemTemplateRulesRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, scope, resource_type, sub_resource_type=None, source=None):
        """
        Initialize DescribeSystemTemplateRulesRequest request entity.

        :param scope: 云产品类型
        :type scope: str (required)

        :param resource_type: 资源类型
        :type resource_type: str (required)

        :param sub_resource_type: 子资源类型
        :type sub_resource_type: str (optional)

        :param source: 规则来源
        :type source: str (optional)
        """
        super().__init__()
        self.scope = scope
        self.resource_type = resource_type
        self.sub_resource_type = sub_resource_type
        self.source = source

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
        if self.scope is not None:
            result['scope'] = self.scope
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.sub_resource_type is not None:
            result['subResourceType'] = self.sub_resource_type
        if self.source is not None:
            result['source'] = self.source
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescribeSystemTemplateRulesRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('subResourceType') is not None:
            self.sub_resource_type = m.get('subResourceType')
        if m.get('source') is not None:
            self.source = m.get('source')
        return self
