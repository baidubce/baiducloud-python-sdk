"""
Step information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Step(AbstractModel):
    """
    Step
    """

    def __init__(
        self,
        step_name=None,
        step_status=None,
        ready=None,
        start_time=None,
        finished_time=None,
        cost_seconds=None,
        retry_count=None,
        err_info=None,
    ):
        """
        Initialize Step instance.

        :param step_name:
        :type step_name: str (optional)

        :param step_status:
        :type step_status: str (optional)

        :param ready:
        :type ready: bool (optional)

        :param start_time:
        :type start_time: str (optional)

        :param finished_time:
        :type finished_time: str (optional)

        :param cost_seconds:
        :type cost_seconds: int (optional)

        :param retry_count:
        :type retry_count: int (optional)

        :param err_info:
        :type err_info: object (optional)
        """
        super().__init__()
        self.step_name = step_name
        self.step_status = step_status
        self.ready = ready
        self.start_time = start_time
        self.finished_time = finished_time
        self.cost_seconds = cost_seconds
        self.retry_count = retry_count
        self.err_info = err_info

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
        if self.step_name is not None:
            result['stepName'] = self.step_name
        if self.step_status is not None:
            result['stepStatus'] = self.step_status
        if self.ready is not None:
            result['ready'] = self.ready
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.finished_time is not None:
            result['finishedTime'] = self.finished_time
        if self.cost_seconds is not None:
            result['costSeconds'] = self.cost_seconds
        if self.retry_count is not None:
            result['retryCount'] = self.retry_count
        if self.err_info is not None:
            result['errInfo'] = self.err_info
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Step

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('stepName') is not None:
            self.step_name = m.get('stepName')
        if m.get('stepStatus') is not None:
            self.step_status = m.get('stepStatus')
        if m.get('ready') is not None:
            self.ready = m.get('ready')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('finishedTime') is not None:
            self.finished_time = m.get('finishedTime')
        if m.get('costSeconds') is not None:
            self.cost_seconds = m.get('costSeconds')
        if m.get('retryCount') is not None:
            self.retry_count = m.get('retryCount')
        if m.get('errInfo') is not None:
            self.err_info = m.get('errInfo')
        return self
