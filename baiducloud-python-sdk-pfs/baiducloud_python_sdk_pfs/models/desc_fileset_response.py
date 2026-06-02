"""
Request entity for DescFilesetResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class DescFilesetResponse(BceResponse):
    """
    DescFilesetResponse
    """

    def __init__(
        self,
        request_id=None,
        fileset_name=None,
        fileset_id=None,
        fileset_path=None,
        status=None,
        block_quota=None,
        block_usage=None,
        files_quota=None,
        files_usage=None,
        allocated_inode=None,
        ctime=None,
        qps_limit=None,
        bandwidth_limit_mb=None,
        parent_path=None,
    ):
        """
        Initialize DescFilesetResponse response.

        :param request_id: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type request_id: str (optional)

        :param fileset_name: fileset名称
        :type fileset_name: str (optional)

        :param fileset_id: fileset id
        :type fileset_id: str (optional)

        :param fileset_path: fileset path
        :type fileset_path: str (optional)

        :param status: status field
        :type status: int (optional)

        :param block_quota: 容量限制（单位GB）
        :type block_quota: int (optional)

        :param block_usage: 容量使用量（单位KB）
        :type block_usage: int (optional)

        :param files_quota: 文件数量限制
        :type files_quota: int (optional)

        :param files_usage: 文件使用量
        :type files_usage: int (optional)

        :param allocated_inode: 文件数预分配配额
        :type allocated_inode: int (optional)

        :param ctime: 创建时间
        :type ctime: str (optional)

        :param qps_limit: iops限制
        :type qps_limit: int (optional)

        :param bandwidth_limit_mb: 带宽限制
        :type bandwidth_limit_mb: int (optional)

        :param parent_path: 是否为父fileset<br><li> 1，表示子目录中有fileset<br><li>0，表示子目录中没有filset
        :type parent_path: bool (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.fileset_name = fileset_name
        self.fileset_id = fileset_id
        self.fileset_path = fileset_path
        self.status = status
        self.block_quota = block_quota
        self.block_usage = block_usage
        self.files_quota = files_quota
        self.files_usage = files_usage
        self.allocated_inode = allocated_inode
        self.ctime = ctime
        self.qps_limit = qps_limit
        self.bandwidth_limit_mb = bandwidth_limit_mb
        self.parent_path = parent_path

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.fileset_name is not None:
            result['filesetName'] = self.fileset_name
        if self.fileset_id is not None:
            result['filesetId'] = self.fileset_id
        if self.fileset_path is not None:
            result['filesetPath'] = self.fileset_path
        if self.status is not None:
            result['status'] = self.status
        if self.block_quota is not None:
            result['blockQuota'] = self.block_quota
        if self.block_usage is not None:
            result['blockUsage'] = self.block_usage
        if self.files_quota is not None:
            result['filesQuota'] = self.files_quota
        if self.files_usage is not None:
            result['filesUsage'] = self.files_usage
        if self.allocated_inode is not None:
            result['allocatedInode'] = self.allocated_inode
        if self.ctime is not None:
            result['ctime'] = self.ctime
        if self.qps_limit is not None:
            result['qpsLimit'] = self.qps_limit
        if self.bandwidth_limit_mb is not None:
            result['bandwidthLimitMb'] = self.bandwidth_limit_mb
        if self.parent_path is not None:
            result['parentPath'] = self.parent_path
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescFilesetResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('filesetName') is not None:
            self.fileset_name = m.get('filesetName')
        if m.get('filesetId') is not None:
            self.fileset_id = m.get('filesetId')
        if m.get('filesetPath') is not None:
            self.fileset_path = m.get('filesetPath')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('blockQuota') is not None:
            self.block_quota = m.get('blockQuota')
        if m.get('blockUsage') is not None:
            self.block_usage = m.get('blockUsage')
        if m.get('filesQuota') is not None:
            self.files_quota = m.get('filesQuota')
        if m.get('filesUsage') is not None:
            self.files_usage = m.get('filesUsage')
        if m.get('allocatedInode') is not None:
            self.allocated_inode = m.get('allocatedInode')
        if m.get('ctime') is not None:
            self.ctime = m.get('ctime')
        if m.get('qpsLimit') is not None:
            self.qps_limit = m.get('qpsLimit')
        if m.get('bandwidthLimitMb') is not None:
            self.bandwidth_limit_mb = m.get('bandwidthLimitMb')
        if m.get('parentPath') is not None:
            self.parent_path = m.get('parentPath')
        return self
