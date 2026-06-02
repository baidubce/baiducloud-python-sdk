"""
Request entity for CreateFilesetRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateFilesetRequest(AbstractModel):
    """
    Request entity for CreateFilesetRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        fileset_name,
        fileset_path,
        block_quota=None,
        files_quota=None,
        qps_limit=None,
        bandwidth_limit_mb=None,
    ):
        """
        Initialize CreateFilesetRequest request entity.

        :param instance_id: 创建fileset的pfs实例短id
        :type instance_id: str (required)

        :param fileset_name: fileset_name parameter
        :type fileset_name: str (required)

        :param fileset_path: fileset_path parameter
        :type fileset_path: str (required)

        :param block_quota: block_quota parameter
        :type block_quota: int (optional)

        :param files_quota: files_quota parameter
        :type files_quota: int (optional)

        :param qps_limit: qps_limit parameter
        :type qps_limit: int (optional)

        :param bandwidth_limit_mb: bandwidth_limit_mb parameter
        :type bandwidth_limit_mb: int (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.fileset_name = fileset_name
        self.fileset_path = fileset_path
        self.block_quota = block_quota
        self.files_quota = files_quota
        self.qps_limit = qps_limit
        self.bandwidth_limit_mb = bandwidth_limit_mb

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.fileset_name is not None:
            result['filesetName'] = self.fileset_name
        if self.fileset_path is not None:
            result['filesetPath'] = self.fileset_path
        if self.block_quota is not None:
            result['blockQuota'] = self.block_quota
        if self.files_quota is not None:
            result['filesQuota'] = self.files_quota
        if self.qps_limit is not None:
            result['qpsLimit'] = self.qps_limit
        if self.bandwidth_limit_mb is not None:
            result['bandwidthLimitMb'] = self.bandwidth_limit_mb
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateFilesetRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('filesetName') is not None:
            self.fileset_name = m.get('filesetName')
        if m.get('filesetPath') is not None:
            self.fileset_path = m.get('filesetPath')
        if m.get('blockQuota') is not None:
            self.block_quota = m.get('blockQuota')
        if m.get('filesQuota') is not None:
            self.files_quota = m.get('filesQuota')
        if m.get('qpsLimit') is not None:
            self.qps_limit = m.get('qpsLimit')
        if m.get('bandwidthLimitMb') is not None:
            self.bandwidth_limit_mb = m.get('bandwidthLimitMb')
        return self
