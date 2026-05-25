"""
Request entity for UnbindCfwRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_cfw.models.cfw_bind import CfwBind


class UnbindCfwRequest(AbstractModel):
    """
    Request entity for UnbindCfwRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, cfw_id, instance_type, instances):
        """
        Initialize UnbindCfwRequest request entity.

        :param cfw_id: cfw_id parameter
        :type cfw_id: str (required)

        :param instance_type: instance_type parameter
        :type instance_type: str (required)

        :param instances: 解绑实例信息
        :type instances: List[CfwBind] (required)
        """
        super().__init__()
        self.cfw_id = cfw_id
        self.instance_type = instance_type
        self.instances = instances

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
        if self.instances is not None:
            result['instances'] = [i.to_dict() for i in self.instances]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UnbindCfwRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('cfwId') is not None:
            self.cfw_id = m.get('cfwId')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('instances') is not None:
            self.instances = [CfwBind().from_dict(i) for i in m.get('instances')]
        return self
