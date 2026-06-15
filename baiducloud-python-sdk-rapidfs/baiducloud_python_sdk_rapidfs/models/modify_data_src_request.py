"""
Request entity for ModifyDataSrcRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ModifyDataSrcRequest(AbstractModel):
    """
    Request entity for ModifyDataSrcRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        data_src_id,
        instance_id,
        client_token=None,
        keep_symlink=None,
        auth_group_id=None,
        description=None,
        quota_mi_b=None,
    ):
        """
        Initialize ModifyDataSrcRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param data_src_id: 待修改的数据源 ID
        :type data_src_id: str (required)

        :param instance_id: 所属 RapidFS 实例唯一 ID
        :type instance_id: str (required)

        :param keep_symlink: 是否保留 BOS 软链，保留软链会降低数据源导入效率，以及后续增量元数据同步效率
        :type keep_symlink: bool (optional)

        :param auth_group_id: 权限组Id
        :type auth_group_id: str (optional)

        :param description: 数据源描述信息，不超过256个字符
        :type description: str (optional)

        :param quota_mi_b: 该数据源的容量配额，表示该数据源的可用最大容量，不能超过实例的缓存总容量。-1 表示取消对数据源的容量限制
        :type quota_mi_b: int (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.data_src_id = data_src_id
        self.instance_id = instance_id
        self.keep_symlink = keep_symlink
        self.auth_group_id = auth_group_id
        self.description = description
        self.quota_mi_b = quota_mi_b

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
        if self.data_src_id is not None:
            result['dataSrcId'] = self.data_src_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.keep_symlink is not None:
            result['keepSymlink'] = self.keep_symlink
        if self.auth_group_id is not None:
            result['authGroupId'] = self.auth_group_id
        if self.description is not None:
            result['description'] = self.description
        if self.quota_mi_b is not None:
            result['quotaMiB'] = self.quota_mi_b
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ModifyDataSrcRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('dataSrcId') is not None:
            self.data_src_id = m.get('dataSrcId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('keepSymlink') is not None:
            self.keep_symlink = m.get('keepSymlink')
        if m.get('authGroupId') is not None:
            self.auth_group_id = m.get('authGroupId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('quotaMiB') is not None:
            self.quota_mi_b = m.get('quotaMiB')
        return self
