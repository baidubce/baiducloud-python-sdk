"""
Request entity for CreateInstanceSyncRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_ccr.models.replication_sync_trigger_request import ReplicationSyncTriggerRequest


class CreateInstanceSyncRequest(AbstractModel):
    """
    Request entity for CreateInstanceSyncRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        dest_instance_id,
        name,
        override,
        src_project_name,
        trigger,
        description=None,
        dest_project_name=None,
        src_repository=None,
        src_tag=None,
        sync_type=None,
    ):
        """
        Initialize CreateInstanceSyncRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param description: 同步规则备注
        :type description: str (optional)

        :param dest_instance_id: 同步目标实例ID
        :type dest_instance_id: str (required)

        :param dest_project_name: 同步目标命名空间
        :type dest_project_name: str (optional)

        :param name: 同步规则名称
        :type name: str (required)

        :param override: 是否覆盖目标实例已有的同名镜像
        :type override: bool (required)

        :param src_project_name: 源实例命名空间
        :type src_project_name: str (required)

        :param src_repository: 源仓库名称
        :type src_repository: str (optional)

        :param src_tag: 源镜像版本
        :type src_tag: str (optional)

        :param sync_type: 同步类型
        :type sync_type: str (optional)

        :param trigger: trigger parameter
        :type trigger: ReplicationSyncTriggerRequest (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.description = description
        self.dest_instance_id = dest_instance_id
        self.dest_project_name = dest_project_name
        self.name = name
        self.override = override
        self.src_project_name = src_project_name
        self.src_repository = src_repository
        self.src_tag = src_tag
        self.sync_type = sync_type
        self.trigger = trigger

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
        if self.description is not None:
            result['description'] = self.description
        if self.dest_instance_id is not None:
            result['destInstanceId'] = self.dest_instance_id
        if self.dest_project_name is not None:
            result['destProjectName'] = self.dest_project_name
        if self.name is not None:
            result['name'] = self.name
        if self.override is not None:
            result['override'] = self.override
        if self.src_project_name is not None:
            result['srcProjectName'] = self.src_project_name
        if self.src_repository is not None:
            result['srcRepository'] = self.src_repository
        if self.src_tag is not None:
            result['srcTag'] = self.src_tag
        if self.sync_type is not None:
            result['syncType'] = self.sync_type
        if self.trigger is not None:
            result['trigger'] = self.trigger.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateInstanceSyncRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('destInstanceId') is not None:
            self.dest_instance_id = m.get('destInstanceId')
        if m.get('destProjectName') is not None:
            self.dest_project_name = m.get('destProjectName')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('override') is not None:
            self.override = m.get('override')
        if m.get('srcProjectName') is not None:
            self.src_project_name = m.get('srcProjectName')
        if m.get('srcRepository') is not None:
            self.src_repository = m.get('srcRepository')
        if m.get('srcTag') is not None:
            self.src_tag = m.get('srcTag')
        if m.get('syncType') is not None:
            self.sync_type = m.get('syncType')
        if m.get('trigger') is not None:
            self.trigger = ReplicationSyncTriggerRequest().from_dict(m.get('trigger'))
        return self
