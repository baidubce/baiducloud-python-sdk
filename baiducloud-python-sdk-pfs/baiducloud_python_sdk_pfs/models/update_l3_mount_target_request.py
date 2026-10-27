"""
Request entity for UpdateL3MountTargetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateL3MountTargetRequest(AbstractModel):
    """
    Request entity for UpdateL3MountTargetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, mount_target_id, admission_status=None, name=None, access_group_name=None):
        """
        Initialize UpdateL3MountTargetRequest request entity.

        :param instance_id: PFS 实例 ID
        :type instance_id: str (required)

        :param mount_target_id: 挂载点 ID
        :type mount_target_id: str (required)

        :param admission_status: 传入该值时更新挂载点禁用状态，传 1 禁用、传 0 启用；不传表示不修改状态
        :type admission_status: int (optional)

        :param name: 传入该值时更新挂载点名称，长度 1~128 个字符，不可为空串；不传表示不改名
        :type name: str (optional)

        :param access_group_name: 传入该值时更新绑定的权限组；不传表示不修改
        :type access_group_name: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.mount_target_id = mount_target_id
        self.admission_status = admission_status
        self.name = name
        self.access_group_name = access_group_name

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
        if self.mount_target_id is not None:
            result['mountTargetId'] = self.mount_target_id
        if self.admission_status is not None:
            result['admissionStatus'] = self.admission_status
        if self.name is not None:
            result['name'] = self.name
        if self.access_group_name is not None:
            result['accessGroupName'] = self.access_group_name
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateL3MountTargetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('mountTargetId') is not None:
            self.mount_target_id = m.get('mountTargetId')
        if m.get('admissionStatus') is not None:
            self.admission_status = m.get('admissionStatus')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('accessGroupName') is not None:
            self.access_group_name = m.get('accessGroupName')
        return self
