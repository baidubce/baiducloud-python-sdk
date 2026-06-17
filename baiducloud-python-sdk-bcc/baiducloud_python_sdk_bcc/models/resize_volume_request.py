"""
Request entity for ResizeVolumeRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ResizeVolumeRequest(AbstractModel):
    """
    Request entity for ResizeVolumeRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, volume_id, new_cds_size_in_gb=None, new_extra_io=None, new_volume_type=None):
        """
        Initialize ResizeVolumeRequest request entity.

        :param volume_id: volume_id parameter
        :type volume_id: str (required)

        :param new_cds_size_in_gb: 新扩容CDS磁盘的容量大小，必须为大于当前CDS容量的整数，单位为GB，大小为0~32765GB的正整数。
        :type new_cds_size_in_gb: int (optional)

        :param new_extra_io: new_extra_io parameter
        :type new_extra_io: int (optional)

        :param new_volume_type: CDS支持对预付费和后付费云磁盘进行升配和降配。newVolumeType和newCdsSizeInGB不允许同时为空。
        :type new_volume_type: str (optional)
        """
        super().__init__()
        self.volume_id = volume_id
        self.new_cds_size_in_gb = new_cds_size_in_gb
        self.new_extra_io = new_extra_io
        self.new_volume_type = new_volume_type

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
        if self.new_cds_size_in_gb is not None:
            result['newCdsSizeInGB'] = self.new_cds_size_in_gb
        if self.new_extra_io is not None:
            result['newExtraIO'] = self.new_extra_io
        if self.new_volume_type is not None:
            result['newVolumeType'] = self.new_volume_type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ResizeVolumeRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('volumeId') is not None:
            self.volume_id = m.get('volumeId')
        if m.get('newCdsSizeInGB') is not None:
            self.new_cds_size_in_gb = m.get('newCdsSizeInGB')
        if m.get('newExtraIO') is not None:
            self.new_extra_io = m.get('newExtraIO')
        if m.get('newVolumeType') is not None:
            self.new_volume_type = m.get('newVolumeType')
        return self
