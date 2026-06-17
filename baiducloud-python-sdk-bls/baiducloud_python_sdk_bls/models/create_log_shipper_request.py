"""
Request entity for CreateLogShipperRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bls.models.dest_config import DestConfig


class CreateLogShipperRequest(AbstractModel):
    """
    Request entity for CreateLogShipperRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, log_store_name, log_shipper_name, dest_config, project=None, start_time=None, dest_type=None):
        """
        Initialize CreateLogShipperRequest request entity.

        :param project: 日志组名称，默认default
        :type project: str (optional)

        :param log_store_name: 日志集名称
        :type log_store_name: str (required)

        :param log_shipper_name: 投递任务名称
        :type log_shipper_name: str (required)

        :param start_time: 投递开始时间
        :type start_time: str (optional)

        :param dest_type: 投递目的端类型，支持BOS/KAFKA
        :type dest_type: str (optional)

        :param dest_config: dest_config parameter
        :type dest_config: DestConfig (required)
        """
        super().__init__()
        self.project = project
        self.log_store_name = log_store_name
        self.log_shipper_name = log_shipper_name
        self.start_time = start_time
        self.dest_type = dest_type
        self.dest_config = dest_config

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
        if self.project is not None:
            result['project'] = self.project
        if self.log_store_name is not None:
            result['logStoreName'] = self.log_store_name
        if self.log_shipper_name is not None:
            result['logShipperName'] = self.log_shipper_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.dest_type is not None:
            result['destType'] = self.dest_type
        if self.dest_config is not None:
            result['destConfig'] = self.dest_config.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateLogShipperRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        if m.get('logShipperName') is not None:
            self.log_shipper_name = m.get('logShipperName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('destType') is not None:
            self.dest_type = m.get('destType')
        if m.get('destConfig') is not None:
            self.dest_config = DestConfig().from_dict(m.get('destConfig'))
        return self
