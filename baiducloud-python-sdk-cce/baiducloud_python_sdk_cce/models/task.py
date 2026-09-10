"""
Task information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Task(AbstractModel):
    """
    Task
    """

    def __init__(
        self, id=None, type=None, description=None, start_time=None, finish_time=None, phase=None, processes=None
    ):
        """
        Initialize Task instance.

        :param id:
        :type id: str (optional)

        :param type:
        :type type: str (optional)

        :param description:
        :type description: str (optional)

        :param start_time:
        :type start_time: str (optional)

        :param finish_time:
        :type finish_time: str (optional)

        :param phase:
        :type phase: str (optional)

        :param processes:
        :type processes: List[object] (optional)
        """
        super().__init__()
        self.id = id
        self.type = type
        self.description = description
        self.start_time = start_time
        self.finish_time = finish_time
        self.phase = phase
        self.processes = processes

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
        if self.type is not None:
            result['type'] = self.type
        if self.description is not None:
            result['description'] = self.description
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.finish_time is not None:
            result['finishTime'] = self.finish_time
        if self.phase is not None:
            result['phase'] = self.phase
        if self.processes is not None:
            result['processes'] = self.processes
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Task

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('finishTime') is not None:
            self.finish_time = m.get('finishTime')
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('processes') is not None:
            self.processes = m.get('processes')
        return self
