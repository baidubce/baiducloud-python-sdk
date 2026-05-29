"""
FileSystemModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FileSystemModel(AbstractModel):
    """
    FileSystemModel
    """

    def __init__(
        self,
        fs_id=None,
        fs_name=None,
        vpc_id=None,
        type=None,
        protocol=None,
        fs_usage=None,
        zone=None,
        status=None,
        kms_key_id=None,
        create_time=None,
        capacity_quota=None,
        mount_target_list=None,
        tags=None,
    ):
        """
        Initialize FileSystemModel instance.

        :param fs_id:
        :type fs_id: str (optional)

        :param fs_name:
        :type fs_name: str (optional)

        :param vpc_id:
        :type vpc_id: str (optional)

        :param type:
        :type type: str (optional)

        :param protocol:
        :type protocol: str (optional)

        :param fs_usage:
        :type fs_usage: str (optional)

        :param zone:
        :type zone: str (optional)

        :param status:
        :type status: str (optional)

        :param kms_key_id:
        :type kms_key_id: str (optional)

        :param create_time:
        :type create_time: str (optional)

        :param capacity_quota:
        :type capacity_quota: int (optional)

        :param mount_target_list:
        :type mount_target_list: List[object] (optional)

        :param tags:
        :type tags: List[object] (optional)
        """
        super().__init__()
        self.fs_id = fs_id
        self.fs_name = fs_name
        self.vpc_id = vpc_id
        self.type = type
        self.protocol = protocol
        self.fs_usage = fs_usage
        self.zone = zone
        self.status = status
        self.kms_key_id = kms_key_id
        self.create_time = create_time
        self.capacity_quota = capacity_quota
        self.mount_target_list = mount_target_list
        self.tags = tags

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
        if self.fs_id is not None:
            result['fsId'] = self.fs_id
        if self.fs_name is not None:
            result['fsName'] = self.fs_name
        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id
        if self.type is not None:
            result['type'] = self.type
        if self.protocol is not None:
            result['protocol'] = self.protocol
        if self.fs_usage is not None:
            result['fsUsage'] = self.fs_usage
        if self.zone is not None:
            result['zone'] = self.zone
        if self.status is not None:
            result['status'] = self.status
        if self.kms_key_id is not None:
            result['KMSKeyId'] = self.kms_key_id
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.capacity_quota is not None:
            result['capacityQuota'] = self.capacity_quota
        if self.mount_target_list is not None:
            result['mountTargetList'] = self.mount_target_list
        if self.tags is not None:
            result['tags'] = self.tags
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FileSystemModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('fsId') is not None:
            self.fs_id = m.get('fsId')
        if m.get('fsName') is not None:
            self.fs_name = m.get('fsName')
        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')
        if m.get('fsUsage') is not None:
            self.fs_usage = m.get('fsUsage')
        if m.get('zone') is not None:
            self.zone = m.get('zone')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('KMSKeyId') is not None:
            self.kms_key_id = m.get('KMSKeyId')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('capacityQuota') is not None:
            self.capacity_quota = m.get('capacityQuota')
        if m.get('mountTargetList') is not None:
            self.mount_target_list = m.get('mountTargetList')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        return self
