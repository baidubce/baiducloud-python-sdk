"""
MachineSpecStatus information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class MachineSpecStatus(AbstractModel):
    """
    MachineSpecStatus
    """

    def __init__(self, machine_spec=None, status=None):
        """
        Initialize MachineSpecStatus instance.

        :param machine_spec:
        :type machine_spec: str (optional)

        :param status:
        :type status: str (optional)
        """
        super().__init__()
        self.machine_spec = machine_spec
        self.status = status

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
        if self.machine_spec is not None:
            result['machineSpec'] = self.machine_spec
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: MachineSpecStatus

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('machineSpec') is not None:
            self.machine_spec = m.get('machineSpec')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
