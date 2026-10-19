"""
Request entity for RetrieveInstanceAutoScalingConfigResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class RetrieveInstanceAutoScalingConfigResponse(BceResponse):
    """
    RetrieveInstanceAutoScalingConfigResponse
    """

    def __init__(
        self, auto_resize_disk=None, free_space_threshold=None, disk_max_limit=None, extend_step_percent=None
    ):
        """
        Initialize RetrieveInstanceAutoScalingConfigResponse response.

        :param auto_resize_disk: 实例是否启用了存储自动扩容，0表示未启用，1表示已启用
        :type auto_resize_disk: int (optional)

        :param free_space_threshold: 可用空间阈值, 单位%
        :type free_space_threshold: int (optional)

        :param disk_max_limit: 自动扩容磁盘的上限,单位GB
        :type disk_max_limit: int (optional)

        :param extend_step_percent: 触发自动扩容时，目标磁盘大小增长百分比，单位%
        :type extend_step_percent: int (optional)
        """
        super().__init__()
        self.auto_resize_disk = auto_resize_disk
        self.free_space_threshold = free_space_threshold
        self.disk_max_limit = disk_max_limit
        self.extend_step_percent = extend_step_percent

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
        if self.auto_resize_disk is not None:
            result['autoResizeDisk'] = self.auto_resize_disk
        if self.free_space_threshold is not None:
            result['freeSpaceThreshold'] = self.free_space_threshold
        if self.disk_max_limit is not None:
            result['diskMaxLimit'] = self.disk_max_limit
        if self.extend_step_percent is not None:
            result['extendStepPercent'] = self.extend_step_percent
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RetrieveInstanceAutoScalingConfigResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('autoResizeDisk') is not None:
            self.auto_resize_disk = m.get('autoResizeDisk')
        if m.get('freeSpaceThreshold') is not None:
            self.free_space_threshold = m.get('freeSpaceThreshold')
        if m.get('diskMaxLimit') is not None:
            self.disk_max_limit = m.get('diskMaxLimit')
        if m.get('extendStepPercent') is not None:
            self.extend_step_percent = m.get('extendStepPercent')
        return self
