"""
Request entity for DeleteCustomScrapeTaskRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class DeleteCustomScrapeTaskRequest(AbstractModel):
    """
    Request entity for DeleteCustomScrapeTaskRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, scrape_job_id, instance_id, agent_id):
        """
        Initialize DeleteCustomScrapeTaskRequest request entity.

        :param scrape_job_id: scrape_job_id parameter
        :type scrape_job_id: str (required)

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param agent_id: agent_id parameter
        :type agent_id: str (required)
        """
        super().__init__()
        self.scrape_job_id = scrape_job_id
        self.instance_id = instance_id
        self.agent_id = agent_id

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
        :rtype: DeleteCustomScrapeTaskRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('scrapeJobId') is not None:
            self.scrape_job_id = m.get('scrapeJobId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        return self
