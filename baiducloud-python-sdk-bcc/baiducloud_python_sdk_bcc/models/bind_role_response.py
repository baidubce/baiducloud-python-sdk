"""
Request entity for BindRoleResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.instance_pass_role_fail_model import InstancePassRoleFailModel
from baiducloud_python_sdk_bcc.models.instance_role_association_model import InstanceRoleAssociationModel


class BindRoleResponse(BceResponse):
    """
    BindRoleResponse
    """

    def __init__(self, fail_instances=None, instance_role_associations=None):
        """
        Initialize BindRoleResponse response.

        :param fail_instances: 实例绑定角色失败列表
        :type fail_instances: List[InstancePassRoleFailModel] (optional)

        :param instance_role_associations: 实例绑定角色成功列表
        :type instance_role_associations: List[InstanceRoleAssociationModel] (optional)
        """
        super().__init__()
        self.fail_instances = fail_instances
        self.instance_role_associations = instance_role_associations

    def to_dict(self):
        """
        Convert the response instance to a dictionary representation.

        Includes metadata from the parent BceResponse class.
        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the response
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.fail_instances is not None:
            result['failInstances'] = [i.to_dict() for i in self.fail_instances]
        if self.instance_role_associations is not None:
            result['instanceRoleAssociations'] = [i.to_dict() for i in self.instance_role_associations]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: BindRoleResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('failInstances') is not None:
            self.fail_instances = [InstancePassRoleFailModel().from_dict(i) for i in m.get('failInstances')]
        if m.get('instanceRoleAssociations') is not None:
            self.instance_role_associations = [
                InstanceRoleAssociationModel().from_dict(i) for i in m.get('instanceRoleAssociations')
            ]
        return self
