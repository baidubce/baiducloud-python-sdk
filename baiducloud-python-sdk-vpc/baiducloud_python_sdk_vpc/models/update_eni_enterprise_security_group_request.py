"""
Request entity for UpdateEniEnterpriseSecurityGroupRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateEniEnterpriseSecurityGroupRequest(AbstractModel):
    """
    Request entity for UpdateEniEnterpriseSecurityGroupRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, eni_id, enterprise_security_group_ids, client_token=None):
        """
        Initialize UpdateEniEnterpriseSecurityGroupRequest request entity.

        :param eni_id: eni_id parameter
        :type eni_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param enterprise_security_group_ids: 企业安全组的ID列表
        :type enterprise_security_group_ids: List[str] (required)
        """
        super().__init__()
        self.eni_id = eni_id
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
        :rtype: UpdateEniEnterpriseSecurityGroupRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('eniId') is not None:
            self.eni_id = m.get('eniId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('enterpriseSecurityGroupIds') is not None:
            self.enterprise_security_group_ids = m.get('enterpriseSecurityGroupIds')
        return self
