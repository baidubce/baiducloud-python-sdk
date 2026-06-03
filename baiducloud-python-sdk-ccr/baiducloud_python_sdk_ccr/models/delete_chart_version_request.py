"""
Request entity for DeleteChartVersionRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteChartVersionRequest(AbstractModel):
    """
    Request entity for DeleteChartVersionRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, project_name, chart_name, chart_version):
        """
        Initialize DeleteChartVersionRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param project_name: project_name parameter
        :type project_name: str (required)

        :param chart_name: chart_name parameter
        :type chart_name: str (required)

        :param chart_version: chart_version parameter
        :type chart_version: str (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.project_name = project_name
        self.chart_name = chart_name
        self.chart_version = chart_version

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
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeleteChartVersionRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        if m.get('chartName') is not None:
            self.chart_name = m.get('chartName')
        if m.get('chartVersion') is not None:
            self.chart_version = m.get('chartVersion')
        return self
