"""
Request entity for CreateDatasetVersionRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateDatasetVersionRequest(AbstractModel):
    """
    Request entity for CreateDatasetVersionRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, dataset_id, storage_path, mount_path, description=None):
        """
        Initialize CreateDatasetVersionRequest request entity.

        :param dataset_id: dataset_id parameter
        :type dataset_id: str (required)

        :param description: 版本描述
        :type description: str (optional)

        :param storage_path: 存储路径
        :type storage_path: str (required)

        :param mount_path: 默认挂载路径
        :type mount_path: str (required)
        """
        super().__init__()
        self.dataset_id = dataset_id
        self.description = description
        self.storage_path = storage_path
        self.mount_path = mount_path

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
        if self.storage_path is not None:
            result['storagePath'] = self.storage_path
        if self.mount_path is not None:
            result['mountPath'] = self.mount_path
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateDatasetVersionRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('datasetId') is not None:
            self.dataset_id = m.get('datasetId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('storagePath') is not None:
            self.storage_path = m.get('storagePath')
        if m.get('mountPath') is not None:
            self.mount_path = m.get('mountPath')
        return self
