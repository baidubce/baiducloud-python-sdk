"""
Request entity for CreatePodmonitorResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class CreatePodmonitorResponse(BceResponse):
    """
    CreatePodmonitorResponse
    """

    def __init__(self, pod_monitor_name=None):
        """
        Initialize CreatePodmonitorResponse response.

        :param pod_monitor_name: Pod Monitor名称
        :type pod_monitor_name: str (optional)
        """
        super().__init__()
        self.pod_monitor_name = pod_monitor_name

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
        if self.pod_monitor_name is not None:
            result['podMonitorName'] = self.pod_monitor_name
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreatePodmonitorResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('podMonitorName') is not None:
            self.pod_monitor_name = m.get('podMonitorName')
        return self
