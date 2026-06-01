"""
Request entity for UpdateServiceConfigRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_apm.models.sample_config import SampleConfig
from baiducloud_python_sdk_apm.models.logging_config import LoggingConfig
from baiducloud_python_sdk_apm.models.service_request_config import ServiceRequestConfig
from baiducloud_python_sdk_apm.models.service_topo_config import ServiceTopoConfig
from baiducloud_python_sdk_apm.models.mllm_resource_dump_config import MllmResourceDumpConfig


class UpdateServiceConfigRequest(AbstractModel):
    """
    Request entity for UpdateServiceConfigRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        service_names,
        sample_config=None,
        logging_config=None,
        request_config=None,
        topo_config=None,
        mllm_resource_dump_config=None,
    ):
        """
        Initialize UpdateServiceConfigRequest request entity.

        :param service_names: 应用名列表，支持将配置同时更新到多个服务
        :type service_names: List[str] (required)

        :param sample_config: sample_config parameter
        :type sample_config: SampleConfig (optional)

        :param logging_config: logging_config parameter
        :type logging_config: LoggingConfig (optional)

        :param request_config: request_config parameter
        :type request_config: ServiceRequestConfig (optional)

        :param topo_config: topo_config parameter
        :type topo_config: ServiceTopoConfig (optional)

        :param mllm_resource_dump_config: mllm_resource_dump_config parameter
        :type mllm_resource_dump_config: MllmResourceDumpConfig (optional)
        """
        super().__init__()
        self.service_names = service_names
        self.sample_config = sample_config
        self.logging_config = logging_config
        self.request_config = request_config
        self.topo_config = topo_config
        self.mllm_resource_dump_config = mllm_resource_dump_config

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
        if self.service_names is not None:
            result['serviceNames'] = self.service_names
        if self.sample_config is not None:
            result['sampleConfig'] = self.sample_config.to_dict()
        if self.logging_config is not None:
            result['loggingConfig'] = self.logging_config.to_dict()
        if self.request_config is not None:
            result['requestConfig'] = self.request_config.to_dict()
        if self.topo_config is not None:
            result['topoConfig'] = self.topo_config.to_dict()
        if self.mllm_resource_dump_config is not None:
            result['mllmResourceDumpConfig'] = self.mllm_resource_dump_config.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateServiceConfigRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('serviceNames') is not None:
            self.service_names = m.get('serviceNames')
        if m.get('sampleConfig') is not None:
            self.sample_config = SampleConfig().from_dict(m.get('sampleConfig'))
        if m.get('loggingConfig') is not None:
            self.logging_config = LoggingConfig().from_dict(m.get('loggingConfig'))
        if m.get('requestConfig') is not None:
            self.request_config = ServiceRequestConfig().from_dict(m.get('requestConfig'))
        if m.get('topoConfig') is not None:
            self.topo_config = ServiceTopoConfig().from_dict(m.get('topoConfig'))
        if m.get('mllmResourceDumpConfig') is not None:
            self.mllm_resource_dump_config = MllmResourceDumpConfig().from_dict(m.get('mllmResourceDumpConfig'))
        return self
