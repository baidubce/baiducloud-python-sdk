"""
AddCacheNodeInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rapidfs.models.disk_info import DiskInfo

from baiducloud_python_sdk_rapidfs.models.bcc_cache_node_info import BCCCacheNodeInfo

from baiducloud_python_sdk_rapidfs.models.idc_cache_node_info import IDCCacheNodeInfo


class AddCacheNodeInfo(AbstractModel):
    """
    AddCacheNodeInfo
    """

    def __init__(self, ip=None, config=None, disk_infos=None, deploy_path=None, bcc_info=None, idc_info=None):
        """
        Initialize AddCacheNodeInfo instance.

        :param ip: 节点 ip
        :type ip: str (optional)

        :param config: config attribute
        :type config: str (optional)

        :param disk_infos: disk_infos attribute
        :type disk_infos: List[DiskInfo] (optional)

        :param deploy_path: cache 节点服务部署路径，默认 /home/.rapidfs/
        :type deploy_path: str (optional)

        :param bcc_info: bcc_info attribute
        :type bcc_info: BCCCacheNodeInfo (optional)

        :param idc_info: idc_info attribute
        :type idc_info: IDCCacheNodeInfo (optional)
        """
        super().__init__()
        self.ip = ip
        self.config = config
        self.disk_infos = disk_infos
        self.deploy_path = deploy_path
        self.bcc_info = bcc_info
        self.idc_info = idc_info

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
        if self.ip is not None:
            result['ip'] = self.ip
        if self.config is not None:
            result['config'] = self.config
        if self.disk_infos is not None:
            result['diskInfos'] = [i.to_dict() for i in self.disk_infos]
        if self.deploy_path is not None:
            result['deployPath'] = self.deploy_path
        if self.bcc_info is not None:
            result['bccInfo'] = self.bcc_info.to_dict()
        if self.idc_info is not None:
            result['idcInfo'] = self.idc_info.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AddCacheNodeInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('diskInfos') is not None:
            self.disk_infos = [DiskInfo().from_dict(i) for i in m.get('diskInfos')]
        if m.get('deployPath') is not None:
            self.deploy_path = m.get('deployPath')
        if m.get('bccInfo') is not None:
            self.bcc_info = BCCCacheNodeInfo().from_dict(m.get('bccInfo'))
        if m.get('idcInfo') is not None:
            self.idc_info = IDCCacheNodeInfo().from_dict(m.get('idcInfo'))
        return self
