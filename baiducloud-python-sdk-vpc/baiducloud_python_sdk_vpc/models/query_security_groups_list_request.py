"""
Request entity for QuerySecurityGroupsListRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QuerySecurityGroupsListRequest(AbstractModel):
    """
    Request entity for QuerySecurityGroupsListRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        marker=None,
        max_keys=None,
        instance_id=None,
        vpc_id=None,
        security_group_id=None,
        security_group_ids=None,
    ):
        """
        Initialize QuerySecurityGroupsListRequest request entity.

        :param marker: marker parameter
        :type marker: str (optional)

        :param max_keys: max_keys parameter
        :type max_keys: int (optional)

        :param instance_id: instance_id parameter
        :type instance_id: str (optional)

        :param vpc_id: vpc_id parameter
        :type vpc_id: str (optional)

        :param security_group_id: security_group_id parameter
        :type security_group_id: str (optional)

        :param security_group_ids: security_group_ids parameter
        :type security_group_ids: str (optional)
        """
        super().__init__()
        self.marker = marker
        self.max_keys = max_keys
        self.instance_id = instance_id
        self.vpc_id = vpc_id
        self.security_group_id = security_group_id
        self.security_group_ids = security_group_ids

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QuerySecurityGroupsListRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('securityGroupIds') is not None:
            self.security_group_ids = m.get('securityGroupIds')
        return self
