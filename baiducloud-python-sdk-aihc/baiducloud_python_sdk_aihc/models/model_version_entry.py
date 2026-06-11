"""
ModelVersionEntry information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModelVersionEntry(AbstractModel):
    """
    ModelVersionEntry
    """

    def __init__(
        self,
        id=None,
        version=None,
        source=None,
        storage_bucket=None,
        storage_path=None,
        model_metrics=None,
        description=None,
    ):
        """
        Initialize ModelVersionEntry instance.

        :param id: 否
        :type id: str (optional)

        :param version: 否
        :type version: str (optional)

        :param source: 是
        :type source: str (optional)

        :param storage_bucket: 是
        :type storage_bucket: str (optional)

        :param storage_path: 是
        :type storage_path: str (optional)

        :param model_metrics: 否
        :type model_metrics: str (optional)

        :param description: 否
        :type description: str (optional)
        """
        super().__init__()
        self.id = id
        self.version = version
        self.source = source
        self.storage_bucket = storage_bucket
        self.storage_path = storage_path
        self.model_metrics = model_metrics
        self.description = description

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
        if self.version is not None:
            result['version'] = self.version
        if self.source is not None:
            result['source'] = self.source
        if self.storage_bucket is not None:
            result['storageBucket'] = self.storage_bucket
        if self.storage_path is not None:
            result['storagePath'] = self.storage_path
        if self.model_metrics is not None:
            result['modelMetrics'] = self.model_metrics
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModelVersionEntry

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('storageBucket') is not None:
            self.storage_bucket = m.get('storageBucket')
        if m.get('storagePath') is not None:
            self.storage_path = m.get('storagePath')
        if m.get('modelMetrics') is not None:
            self.model_metrics = m.get('modelMetrics')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self
