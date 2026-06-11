"""
Request entity for RetrieveTheDatasetVersionListV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RetrieveTheDatasetVersionListV2Request(AbstractModel):
    """
    Request entity for RetrieveTheDatasetVersionListV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, dataset_id, page_number=None, page_size=None):
        """
        Initialize RetrieveTheDatasetVersionListV2Request request entity.

        :param dataset_id: dataset_id parameter
        :type dataset_id: str (required)

        :param page_number: page_number parameter
        :type page_number: int (optional)

        :param page_size: page_size parameter
        :type page_size: int (optional)
        """
        super().__init__()
        self.dataset_id = dataset_id
        self.page_number = page_number
        self.page_size = page_size

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
        :rtype: RetrieveTheDatasetVersionListV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self
