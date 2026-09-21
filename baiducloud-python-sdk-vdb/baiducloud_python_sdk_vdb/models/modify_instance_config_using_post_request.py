"""
Request entity for ModifyInstanceConfigUsingPOSTRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_vdb.models.instance_config_user_config import InstanceConfigUserConfig


class ModifyInstanceConfigUsingPOSTRequest(AbstractModel):
    """
    Request entity for ModifyInstanceConfigUsingPOSTRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id=None, reason=None, user_configs=None):
        """
        Initialize ModifyInstanceConfigUsingPOSTRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (optional)

        :param reason: reason parameter
        :type reason: str (optional)

        :param user_configs: user_configs parameter
        :type user_configs: List[InstanceConfigUserConfig] (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.reason = reason
        self.user_configs = user_configs

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
        if self.reason is not None:
            result['reason'] = self.reason
        if self.user_configs is not None:
            result['userConfigs'] = [i.to_dict() for i in self.user_configs]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyInstanceConfigUsingPOSTRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('userConfigs') is not None:
            self.user_configs = [InstanceConfigUserConfig().from_dict(i) for i in m.get('userConfigs')]
        return self
