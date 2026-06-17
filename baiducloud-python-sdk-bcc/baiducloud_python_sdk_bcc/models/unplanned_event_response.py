"""
UnplannedEventResponse information
"""

from baiducloud_python_sdk_core.bce_response import BceResponse

from baiducloud_python_sdk_bcc.models.tag_model import TagModel

from baiducloud_python_sdk_bcc.models.operation_record_response import OperationRecordResponse

from baiducloud_python_sdk_bcc.models.issue_response import IssueResponse

from baiducloud_python_sdk_bcc.models.issue_disk_info_response import IssueDiskInfoResponse


class UnplannedEventResponse(BceResponse):
    """
    UnplannedEventResponse
    """

    def __init__(
        self,
        server_event_id=None,
        server_event_type=None,
        server_event_status=None,
        instance_id=None,
        product_category=None,
        instance_spec=None,
        instance_name=None,
        private_ip=None,
        tags=None,
        server_event_created_time=None,
        server_event_ended_time=None,
        maintenance_options=None,
        support_maintenance_options=None,
        authorized_maintenance_operation=None,
        associated_planned_maintenance_server_event_ids=None,
        associated_unplanned_maintenance_server_event_ids=None,
        execute_time=None,
        server_event_logs=None,
        has_fast_repair_stock=None,
        failures=None,
        issue_disk_infos=None,
    ):
        """
        Initialize UnplannedEventResponse instance.

        :param server_event_id: 事件id（非预期事件列表、非预期事件记录列表接口返回）
        :type server_event_id: str (optional)

        :param server_event_type: server_event_type attribute
        :type server_event_type: str (optional)

        :param server_event_status: server_event_status attribute
        :type server_event_status: str (optional)

        :param instance_id: 故障实例ID（非预期事件列表、非预期事件记录列表接口返回）
        :type instance_id: str (optional)

        :param product_category: 故障实例产品类型（非预期事件列表、非预期事件记录列表接口返回）
        :type product_category: str (optional)

        :param instance_spec: 故障实例规格（非预期事件列表、非预期事件记录列表接口返回）
        :type instance_spec: str (optional)

        :param instance_name: 故障实例名（非预期事件列表、非预期事件记录列表接口返回）
        :type instance_name: str (optional)

        :param private_ip: 故障实例的内网IP。（非预期事件列表、非预期事件记录列表接口返回）
        :type private_ip: str (optional)

        :param tags: 故障实例的标签信息（非预期事件列表、非预期事件记录列表接口返回）
        :type tags: List[TagModel] (optional)

        :param server_event_created_time: server_event_created_time attribute
        :type server_event_created_time: str (optional)

        :param server_event_ended_time: server_event_ended_time attribute
        :type server_event_ended_time: str (optional)

        :param maintenance_options: 该事件支持的运维操作，可能支持的类型：Repair、Reboot（非预期事件列表、非预期事件记录列表接口返回）
        :type maintenance_options: List[str] (optional)

        :param support_maintenance_options: support_maintenance_options attribute
        :type support_maintenance_options: List[str] (optional)

        :param authorized_maintenance_operation: 该事件已授权的维修方式，与授权时使用的方式一致（非预期事件列表、非预期事件记录列表接口返回）
        :type authorized_maintenance_operation: str (optional)

        :param associated_planned_maintenance_server_event_ids: 多事件情况下该实例关联计划内运维事件ID列表（非预期事件列表、非预期事件记录列表接口返回）
        :type associated_planned_maintenance_server_event_ids: List[str] (optional)

        :param associated_unplanned_maintenance_server_event_ids: 多事件情况下该实例关联非预期运维事件ID列表（非预期事件列表、非预期事件记录列表接口返回）
        :type associated_unplanned_maintenance_server_event_ids: List[str] (optional)

        :param execute_time: execute_time attribute
        :type execute_time: str (optional)

        :param server_event_logs: 操作日志，包括用户授权、运维、验收等操作记录。（非预期事件列表、非预期事件记录列表接口返回）
        :type server_event_logs: List[OperationRecordResponse] (optional)

        :param has_fast_repair_stock: 是否有快速维修库存（非预期事件列表、非预期事件记录列表接口返回）
        :type has_fast_repair_stock: bool (optional)

        :param failures: 故障事项（非预期事件列表、非预期事件记录列表接口返回）
        :type failures: List[IssueResponse] (optional)

        :param issue_disk_infos: 故障磁盘信息（非预期事件列表、非预期事件记录列表接口返回）
        :type issue_disk_infos: List[IssueDiskInfoResponse] (optional)
        """
        super().__init__()
        self.server_event_id = server_event_id
        self.server_event_type = server_event_type
        self.server_event_status = server_event_status
        self.instance_id = instance_id
        self.product_category = product_category
        self.instance_spec = instance_spec
        self.instance_name = instance_name
        self.private_ip = private_ip
        self.tags = tags
        self.server_event_created_time = server_event_created_time
        self.server_event_ended_time = server_event_ended_time
        self.maintenance_options = maintenance_options
        self.support_maintenance_options = support_maintenance_options
        self.authorized_maintenance_operation = authorized_maintenance_operation
        self.associated_planned_maintenance_server_event_ids = associated_planned_maintenance_server_event_ids
        self.associated_unplanned_maintenance_server_event_ids = associated_unplanned_maintenance_server_event_ids
        self.execute_time = execute_time
        self.server_event_logs = server_event_logs
        self.has_fast_repair_stock = has_fast_repair_stock
        self.failures = failures
        self.issue_disk_infos = issue_disk_infos

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        Includes metadata from the parent BceResponse class.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.metadata is not None:
            result['metadata'] = dict(self.metadata)
        if self.server_event_id is not None:
            result['serverEventId'] = self.server_event_id
        if self.server_event_type is not None:
            result['serverEventType'] = self.server_event_type
        if self.server_event_status is not None:
            result['serverEventStatus'] = self.server_event_status
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.product_category is not None:
            result['productCategory'] = self.product_category
        if self.instance_spec is not None:
            result['instanceSpec'] = self.instance_spec
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.private_ip is not None:
            result['privateIp'] = self.private_ip
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.server_event_created_time is not None:
            result['serverEventCreatedTime'] = self.server_event_created_time
        if self.server_event_ended_time is not None:
            result['serverEventEndedTime'] = self.server_event_ended_time
        if self.maintenance_options is not None:
            result['maintenanceOptions'] = self.maintenance_options
        if self.support_maintenance_options is not None:
            result['supportMaintenanceOptions'] = self.support_maintenance_options
        if self.authorized_maintenance_operation is not None:
            result['authorizedMaintenanceOperation'] = self.authorized_maintenance_operation
        if self.associated_planned_maintenance_server_event_ids is not None:
            result['associatedPlannedMaintenanceServerEventIds'] = self.associated_planned_maintenance_server_event_ids
        if self.associated_unplanned_maintenance_server_event_ids is not None:
            result['associatedUnplannedMaintenanceServerEventIds'] = (
                self.associated_unplanned_maintenance_server_event_ids
            )
        if self.execute_time is not None:
            result['executeTime'] = self.execute_time
        if self.server_event_logs is not None:
            result['serverEventLogs'] = [i.to_dict() for i in self.server_event_logs]
        if self.has_fast_repair_stock is not None:
            result['hasFastRepairStock'] = self.has_fast_repair_stock
        if self.failures is not None:
            result['failures'] = [i.to_dict() for i in self.failures]
        if self.issue_disk_infos is not None:
            result['issueDiskInfos'] = [i.to_dict() for i in self.issue_disk_infos]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UnplannedEventResponse

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('serverEventId') is not None:
            self.server_event_id = m.get('serverEventId')
        if m.get('serverEventType') is not None:
            self.server_event_type = m.get('serverEventType')
        if m.get('serverEventStatus') is not None:
            self.server_event_status = m.get('serverEventStatus')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('productCategory') is not None:
            self.product_category = m.get('productCategory')
        if m.get('instanceSpec') is not None:
            self.instance_spec = m.get('instanceSpec')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('privateIp') is not None:
            self.private_ip = m.get('privateIp')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        if m.get('serverEventCreatedTime') is not None:
            self.server_event_created_time = m.get('serverEventCreatedTime')
        if m.get('serverEventEndedTime') is not None:
            self.server_event_ended_time = m.get('serverEventEndedTime')
        if m.get('maintenanceOptions') is not None:
            self.maintenance_options = m.get('maintenanceOptions')
        if m.get('supportMaintenanceOptions') is not None:
            self.support_maintenance_options = m.get('supportMaintenanceOptions')
        if m.get('authorizedMaintenanceOperation') is not None:
            self.authorized_maintenance_operation = m.get('authorizedMaintenanceOperation')
        if m.get('associatedPlannedMaintenanceServerEventIds') is not None:
            self.associated_planned_maintenance_server_event_ids = m.get('associatedPlannedMaintenanceServerEventIds')
        if m.get('associatedUnplannedMaintenanceServerEventIds') is not None:
            self.associated_unplanned_maintenance_server_event_ids = m.get(
                'associatedUnplannedMaintenanceServerEventIds'
            )
        if m.get('executeTime') is not None:
            self.execute_time = m.get('executeTime')
        if m.get('serverEventLogs') is not None:
            self.server_event_logs = [OperationRecordResponse().from_dict(i) for i in m.get('serverEventLogs')]
        if m.get('hasFastRepairStock') is not None:
            self.has_fast_repair_stock = m.get('hasFastRepairStock')
        if m.get('failures') is not None:
            self.failures = [IssueResponse().from_dict(i) for i in m.get('failures')]
        if m.get('issueDiskInfos') is not None:
            self.issue_disk_infos = [IssueDiskInfoResponse().from_dict(i) for i in m.get('issueDiskInfos')]
        return self
