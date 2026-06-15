"""
Request entity for RebuildInstanceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class RebuildInstanceRequest(AbstractModel):
    """
    Request entity for RebuildInstanceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        image_id,
        keep_image_login=None,
        is_preserve_data=None,
        admin_pass=None,
        is_open_host_eye=None,
        sys_root_size=None,
        keypair_id=None,
        data_partition_type=None,
        root_partition_type=None,
        raid_id=None,
        user_data=None,
        use_last_user_data=None,
        clean_last_user_data=None,
    ):
        """
        Initialize RebuildInstanceRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param image_id: 待指定的镜像ID
        :type image_id: str (required)

        :param keep_image_login: keep_image_login parameter
        :type keep_image_login: bool (optional)

        :param is_preserve_data: 仅对ebc实例本地盘生效。是否保留数据重装，当值为true时，raidId和sysRootSize字段不生效
        :type is_preserve_data: bool (optional)

        :param admin_pass: 机器密码，密码需要加密传输，详见密码加密传输规范，必须传递adminPass、keypairId其中一个参数
        :type admin_pass: str (optional)

        :param is_open_host_eye: 是否开启主机安全，默认true
        :type is_open_host_eye: bool (optional)

        :param sys_root_size: 仅对ebc实例生效。系统盘大小
        :type sys_root_size: int (optional)

        :param keypair_id: 待重装实例所要绑定的密钥对ID，必须传递adminPass、keypairId其中一个参数
        :type keypair_id: str (optional)

        :param data_partition_type: 仅对ebc实例生效。数据盘分区格式
        :type data_partition_type: str (optional)

        :param root_partition_type: 仅对ebc实例生效。系统盘分区格式
        :type root_partition_type: str (optional)

        :param raid_id: raid_id parameter
        :type raid_id: str (optional)

        :param user_data: 待重装的自定义脚本
        :type user_data: str (optional)

        :param use_last_user_data: 在重装实例时是否使用上一次的 userData
        :type use_last_user_data: bool (optional)

        :param clean_last_user_data: 清空历史userData，默认false，即默认重装历史userData（包括gpu驱动和CFS文件系统）
        :type clean_last_user_data: bool (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.image_id = image_id
        self.keep_image_login = keep_image_login
        self.is_preserve_data = is_preserve_data
        self.admin_pass = admin_pass
        self.is_open_host_eye = is_open_host_eye
        self.sys_root_size = sys_root_size
        self.keypair_id = keypair_id
        self.data_partition_type = data_partition_type
        self.root_partition_type = root_partition_type
        self.raid_id = raid_id
        self.user_data = user_data
        self.use_last_user_data = use_last_user_data
        self.clean_last_user_data = clean_last_user_data

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
        if self.image_id is not None:
            result['imageId'] = self.image_id
        if self.keep_image_login is not None:
            result['keepImageLogin'] = self.keep_image_login
        if self.is_preserve_data is not None:
            result['isPreserveData'] = self.is_preserve_data
        if self.admin_pass is not None:
            result['adminPass'] = self.admin_pass
        if self.is_open_host_eye is not None:
            result['isOpenHostEye'] = self.is_open_host_eye
        if self.sys_root_size is not None:
            result['sysRootSize'] = self.sys_root_size
        if self.keypair_id is not None:
            result['keypairId'] = self.keypair_id
        if self.data_partition_type is not None:
            result['dataPartitionType'] = self.data_partition_type
        if self.root_partition_type is not None:
            result['rootPartitionType'] = self.root_partition_type
        if self.raid_id is not None:
            result['raidId'] = self.raid_id
        if self.user_data is not None:
            result['userData'] = self.user_data
        if self.use_last_user_data is not None:
            result['useLastUserData'] = self.use_last_user_data
        if self.clean_last_user_data is not None:
            result['cleanLastUserData'] = self.clean_last_user_data
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: RebuildInstanceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')
        if m.get('keepImageLogin') is not None:
            self.keep_image_login = m.get('keepImageLogin')
        if m.get('isPreserveData') is not None:
            self.is_preserve_data = m.get('isPreserveData')
        if m.get('adminPass') is not None:
            self.admin_pass = m.get('adminPass')
        if m.get('isOpenHostEye') is not None:
            self.is_open_host_eye = m.get('isOpenHostEye')
        if m.get('sysRootSize') is not None:
            self.sys_root_size = m.get('sysRootSize')
        if m.get('keypairId') is not None:
            self.keypair_id = m.get('keypairId')
        if m.get('dataPartitionType') is not None:
            self.data_partition_type = m.get('dataPartitionType')
        if m.get('rootPartitionType') is not None:
            self.root_partition_type = m.get('rootPartitionType')
        if m.get('raidId') is not None:
            self.raid_id = m.get('raidId')
        if m.get('userData') is not None:
            self.user_data = m.get('userData')
        if m.get('useLastUserData') is not None:
            self.use_last_user_data = m.get('useLastUserData')
        if m.get('cleanLastUserData') is not None:
            self.clean_last_user_data = m.get('cleanLastUserData')
        return self
