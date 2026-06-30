"""
Request entity for CreateImageCacheRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bci.models.origin_image import OriginImage
from baiducloud_python_sdk_bci.models.image_registry_credential import ImageRegistryCredential


class CreateImageCacheRequest(AbstractModel):
    """
    Request entity for CreateImageCacheRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        image_cache_name,
        origin_images,
        subnet_id,
        security_group_id,
        zone_name,
        temporary_storage_size,
        need_eip,
        eip_ip=None,
        auto_match_image_cache=None,
        image_registry_secrets=None,
    ):
        """
        Initialize CreateImageCacheRequest request entity.

        :param image_cache_name: 镜像缓存名称
        :type image_cache_name: str (required)

        :param origin_images: 原始镜像数组，每个对象包含镜像地址和版本信息
        :type origin_images: List[OriginImage] (required)

        :param subnet_id: 子网ID
        :type subnet_id: str (required)

        :param security_group_id: 安全组ID
        :type security_group_id: str (required)

        :param zone_name: 可用区名称
        :type zone_name: str (required)

        :param temporary_storage_size: 临时存储大小（单位：GB）
        :type temporary_storage_size: int (required)

        :param need_eip: 是否需要弹性公网IP
        :type need_eip: bool (required)

        :param eip_ip: 弹性公网IP地址，needEip为true时必须提供
        :type eip_ip: str (optional)

        :param auto_match_image_cache: 是否自动匹配镜像缓存
        :type auto_match_image_cache: bool (optional)

        :param image_registry_secrets: 镜像仓库凭据
        :type image_registry_secrets: List[ImageRegistryCredential] (optional)
        """
        super().__init__()
        self.image_cache_name = image_cache_name
        self.origin_images = origin_images
        self.subnet_id = subnet_id
        self.security_group_id = security_group_id
        self.zone_name = zone_name
        self.temporary_storage_size = temporary_storage_size
        self.need_eip = need_eip
        self.eip_ip = eip_ip
        self.auto_match_image_cache = auto_match_image_cache
        self.image_registry_secrets = image_registry_secrets

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
        if self.image_cache_name is not None:
            result['imageCacheName'] = self.image_cache_name
        if self.origin_images is not None:
            result['originImages'] = [i.to_dict() for i in self.origin_images]
        if self.subnet_id is not None:
            result['subnetId'] = self.subnet_id
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.temporary_storage_size is not None:
            result['temporaryStorageSize'] = self.temporary_storage_size
        if self.need_eip is not None:
            result['needEip'] = self.need_eip
        if self.eip_ip is not None:
            result['eipIp'] = self.eip_ip
        if self.auto_match_image_cache is not None:
            result['autoMatchImageCache'] = self.auto_match_image_cache
        if self.image_registry_secrets is not None:
            result['imageRegistrySecrets'] = [i.to_dict() for i in self.image_registry_secrets]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateImageCacheRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('imageCacheName') is not None:
            self.image_cache_name = m.get('imageCacheName')
        if m.get('originImages') is not None:
            self.origin_images = [OriginImage().from_dict(i) for i in m.get('originImages')]
        if m.get('subnetId') is not None:
            self.subnet_id = m.get('subnetId')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('temporaryStorageSize') is not None:
            self.temporary_storage_size = m.get('temporaryStorageSize')
        if m.get('needEip') is not None:
            self.need_eip = m.get('needEip')
        if m.get('eipIp') is not None:
            self.eip_ip = m.get('eipIp')
        if m.get('autoMatchImageCache') is not None:
            self.auto_match_image_cache = m.get('autoMatchImageCache')
        if m.get('imageRegistrySecrets') is not None:
            self.image_registry_secrets = [
                ImageRegistryCredential().from_dict(i) for i in m.get('imageRegistrySecrets')
            ]
        return self
