"""
Request entity for NewModelVersionV2Request information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class NewModelVersionV2Request(AbstractModel):
    """
    Request entity for NewModelVersionV2Request operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, model_id, storage_bucket, storage_path, source, description=None, model_metrics=None):
        """
        Initialize NewModelVersionV2Request request entity.

        :param model_id: model_id parameter
        :type model_id: str (required)

        :param storage_bucket: 模型存储的BOS桶
        :type storage_bucket: str (required)

        :param storage_path: BOS桶中的存储路径
        :type storage_path: str (required)

        :param description: 描述
        :type description: str (optional)

        :param source: 该版本模型的来源UserUpload：用户上传
        :type source: str (required)

        :param model_metrics: model_metrics parameter
        :type model_metrics: str (optional)
        """
        super().__init__()
        self.model_id = model_id
        self.storage_bucket = storage_bucket
        self.storage_path = storage_path
        self.description = description
        self.source = source
        self.model_metrics = model_metrics

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
        if self.storage_bucket is not None:
            result['storageBucket'] = self.storage_bucket
        if self.storage_path is not None:
            result['storagePath'] = self.storage_path
        if self.description is not None:
            result['description'] = self.description
        if self.source is not None:
            result['source'] = self.source
        if self.model_metrics is not None:
            result['modelMetrics'] = self.model_metrics
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: NewModelVersionV2Request

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('modelId') is not None:
            self.model_id = m.get('modelId')
        if m.get('storageBucket') is not None:
            self.storage_bucket = m.get('storageBucket')
        if m.get('storagePath') is not None:
            self.storage_path = m.get('storagePath')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('modelMetrics') is not None:
            self.model_metrics = m.get('modelMetrics')
        return self
