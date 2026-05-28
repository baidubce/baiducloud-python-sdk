"""
Request entity for AttachCsnInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AttachCsnInstanceRequest(AbstractModel):
    """
    Request entity for AttachCsnInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, csn_id, instance_type, instance_id, instance_region, client_token=None, instance_account_id=None
    ):
        """
        Initialize AttachCsnInstanceRequest request entity.

        :param csn_id: csn_id parameter
        :type csn_id: str (required)

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param instance_type: instance_type parameter
        :type instance_type: str (required)

        :param instance_id: 加载的实例ID
        :type instance_id: str (required)

        :param instance_region: 加载的实例所属的region
        :type instance_region: str (required)

        :param instance_account_id: 跨账号加载网络实例场景下，网络实例所属账号的ID
        :type instance_account_id: str (optional)
        """
        super().__init__()
        self.csn_id = csn_id
        self.client_token = client_token
        self.instance_type = instance_type
        self.instance_id = instance_id
        self.instance_region = instance_region
        self.instance_account_id = instance_account_id

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
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_region is not None:
            result['instanceRegion'] = self.instance_region
        if self.instance_account_id is not None:
            result['instanceAccountId'] = self.instance_account_id
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AttachCsnInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('csnId') is not None:
            self.csn_id = m.get('csnId')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceRegion') is not None:
            self.instance_region = m.get('instanceRegion')
        if m.get('instanceAccountId') is not None:
            self.instance_account_id = m.get('instanceAccountId')
        return self
