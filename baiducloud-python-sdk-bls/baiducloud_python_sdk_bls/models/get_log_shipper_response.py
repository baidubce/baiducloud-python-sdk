"""
Request entity for GetLogShipperResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bls.models.dest_config import DestConfig


class GetLogShipperResponse(BceResponse):
    """
    GetLogShipperResponse
    """

    def __init__(
        self,
        success=None,
        code=None,
        status=None,
        log_shipper_name=None,
        project=None,
        log_store_name=None,
        start_time=None,
        dest_type=None,
        dest_config=None,
    ):
        """
        Initialize GetLogShipperResponse response.

        :param success: 请求是否成功
        :type success: bool (optional)

        :param code: 请求码，成功为OK，错误为具体的错误码
        :type code: str (optional)

        :param status: 运行状态, 可为运行中（Running）、异常（Abnormal）、已暂停（Paused）
        :type status: str (optional)

        :param log_shipper_name: 投递任务名称
        :type log_shipper_name: str (optional)

        :param project: 日志组名称
        :type project: str (optional)

        :param log_store_name: 日志集名称
        :type log_store_name: str (optional)

        :param start_time: 指定投递开始时间
        :type start_time: str (optional)

        :param dest_type: 目的端类型
        :type dest_type: str (optional)

        :param dest_config: dest_config field
        :type dest_config: DestConfig (optional)
        """
        super().__init__()
        self.success = success
        self.code = code
        self.status = status
        self.log_shipper_name = log_shipper_name
        self.project = project
        self.log_store_name = log_store_name
        self.start_time = start_time
        self.dest_type = dest_type
        self.dest_config = dest_config

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
        if self.success is not None:
            result['success'] = self.success
        if self.code is not None:
            result['code'] = self.code
        if self.status is not None:
            result['status'] = self.status
        if self.log_shipper_name is not None:
            result['logShipperName'] = self.log_shipper_name
        if self.project is not None:
            result['project'] = self.project
        if self.log_store_name is not None:
            result['logStoreName'] = self.log_store_name
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.dest_type is not None:
            result['destType'] = self.dest_type
        if self.dest_config is not None:
            result['destConfig'] = self.dest_config.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetLogShipperResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('logShipperName') is not None:
            self.log_shipper_name = m.get('logShipperName')
        if m.get('project') is not None:
            self.project = m.get('project')
        if m.get('logStoreName') is not None:
            self.log_store_name = m.get('logStoreName')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('destType') is not None:
            self.dest_type = m.get('destType')
        if m.get('destConfig') is not None:
            self.dest_config = DestConfig().from_dict(m.get('destConfig'))
        return self
