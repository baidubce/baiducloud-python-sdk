"""
Request entity for UpdateSnicEsgRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateSnicEsgRequest(AbstractModel):
    """
    Request entity for UpdateSnicEsgRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, endpoint_id, enterprise_security_group_ids, client_token=None):
        """
        Initialize UpdateSnicEsgRequest request entity.

        :param endpoint_id: endpoint_id parameter
        :type endpoint_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param enterprise_security_group_ids: 企业安全组的ID列表
        :type enterprise_security_group_ids: List[str] (required)
        """
        super().__init__()
        self.endpoint_id = endpoint_id
        self.client_token = client_token
        self.enterprise_security_group_ids = enterprise_security_group_ids

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
        if self.enterprise_security_group_ids is not None:
            result['enterpriseSecurityGroupIds'] = self.enterprise_security_group_ids
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateSnicEsgRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('endpointId') is not None:
            self.endpoint_id = m.get('endpointId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('enterpriseSecurityGroupIds') is not None:
            self.enterprise_security_group_ids = m.get('enterpriseSecurityGroupIds')
        return self
