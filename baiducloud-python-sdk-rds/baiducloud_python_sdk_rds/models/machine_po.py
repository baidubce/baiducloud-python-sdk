"""
MachinePO information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MachinePO(AbstractModel):
    """
    MachinePO
    """

    def __init__(
        self,
        id=None,
        updated_time=None,
        instance_id=None,
        machine_instance_id=None,
        machine_instance_name=None,
        machine_instance_status=None,
        available=None,
        instance_role=None,
        machine_type=None,
        azone=None,
    ):
        """
        Initialize MachinePO instance.

        :param id: dcc主机ID。
        :type id: int (optional)

        :param updated_time: updated_time attribute
        :type updated_time: datetime (optional)

        :param instance_id: 实例ID。
        :type instance_id: str (optional)

        :param machine_instance_id: 机器实例ID。
        :type machine_instance_id: str (optional)

        :param machine_instance_name: 机器实例名。
        :type machine_instance_name: str (optional)

        :param machine_instance_status: machine_instance_status attribute
        :type machine_instance_status: str (optional)

        :param available: 是否可用，true：是 false：否。
        :type available: bool (optional)

        :param instance_role: 实例角色。
        :type instance_role: str (optional)

        :param machine_type: 主机类型，默认只有dcc。
        :type machine_type: str (optional)

        :param azone: 实例的逻辑可用区。
        :type azone: str (optional)
        """
        super().__init__()
        self.id = id
        self.updated_time = updated_time
        self.instance_id = instance_id
        self.machine_instance_id = machine_instance_id
        self.machine_instance_name = machine_instance_name
        self.machine_instance_status = machine_instance_status
        self.available = available
        self.instance_role = instance_role
        self.machine_type = machine_type
        self.azone = azone

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.updated_time is not None:
            result['updatedTime'] = self.updated_time
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.machine_instance_id is not None:
            result['machineInstanceId'] = self.machine_instance_id
        if self.machine_instance_name is not None:
            result['machineInstanceName'] = self.machine_instance_name
        if self.machine_instance_status is not None:
            result['machineInstanceStatus'] = self.machine_instance_status
        if self.available is not None:
            result['available'] = self.available
        if self.instance_role is not None:
            result['instanceRole'] = self.instance_role
        if self.machine_type is not None:
            result['machineType'] = self.machine_type
        if self.azone is not None:
            result['azone'] = self.azone
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MachinePO

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('updatedTime') is not None:
            self.updated_time = m.get('updatedTime')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('machineInstanceId') is not None:
            self.machine_instance_id = m.get('machineInstanceId')
        if m.get('machineInstanceName') is not None:
            self.machine_instance_name = m.get('machineInstanceName')
        if m.get('machineInstanceStatus') is not None:
            self.machine_instance_status = m.get('machineInstanceStatus')
        if m.get('available') is not None:
            self.available = m.get('available')
        if m.get('instanceRole') is not None:
            self.instance_role = m.get('instanceRole')
        if m.get('machineType') is not None:
            self.machine_type = m.get('machineType')
        if m.get('azone') is not None:
            self.azone = m.get('azone')
        return self
