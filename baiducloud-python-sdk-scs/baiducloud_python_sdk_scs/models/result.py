"""
Result information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_scs.models.parameters import Parameters


class Result(AbstractModel):
    """
    Result
    """

    def __init__(
        self,
        template_id=None,
        template_show_id=None,
        template_name=None,
        parameters_num=None,
        cluster_type=None,
        engine=None,
        engine_version=None,
        template_type=None,
        need_reboot=None,
        comment=None,
        create_time=None,
        update_time=None,
        parameters=None,
        cache_cluster_show_id=None,
        cache_cluster_name=None,
        availability_zone=None,
        version=None,
        status=None,
        apply_time=None,
        conf_name=None,
        conf_default=None,
        conf_value=None,
        conf_type=None,
        conf_range=None,
        conf_module=None,
        conf_desc=None,
        conf_redis_version=None,
        conf_cache_version=None,
        leader_name=None,
        leader_show_id=None,
        leader_region=None,
        group_id=None,
        group_name=None,
        group_status=None,
        cluster_num=None,
        group_create_time=None,
        forbid_write=None,
        group_type=None,
    ):
        """
        Initialize Result instance.

        :param template_id: 参数模板数字ID
        :type template_id: int (optional)

        :param template_show_id: 参数模板ID
        :type template_show_id: str (optional)

        :param template_name: 参数模板名称
        :type template_name: str (optional)

        :param parameters_num: 参数模板参数数量
        :type parameters_num: int (optional)

        :param cluster_type: 集群类型
        :type cluster_type: str (optional)

        :param engine: 引擎类型
        :type engine: str (optional)

        :param engine_version: 引擎版本
        :type engine_version: str (optional)

        :param template_type: 参数模板类型（1为自定义参数模板）
        :type template_type: int (optional)

        :param need_reboot: 该参数是否需要重启，0：不需要，1：需要
        :type need_reboot: int (optional)

        :param comment: 备注
        :type comment: str (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param update_time: 更新时间
        :type update_time: str (optional)

        :param parameters: 参数列表
        :type parameters: List[Parameters] (optional)

        :param cache_cluster_show_id: 集群ID
        :type cache_cluster_show_id: str (optional)

        :param cache_cluster_name: 集群名称
        :type cache_cluster_name: str (optional)

        :param availability_zone: 可用区
        :type availability_zone: str (optional)

        :param version: 集群版本
        :type version: int (optional)

        :param status: 集群状态
        :type status: str (optional)

        :param apply_time: 应用时间
        :type apply_time: str (optional)

        :param conf_name: 参数名称
        :type conf_name: str (optional)

        :param conf_default: 参数默认值
        :type conf_default: str (optional)

        :param conf_value: 参数值
        :type conf_value: str (optional)

        :param conf_type: 参数类型（1:单选类型 2.数字类型 3.多选类型 4.多选类型，单值）
        :type conf_type: int (optional)

        :param conf_range: conf_range attribute
        :type conf_range: str (optional)

        :param conf_module: 1:redis 2:proxy 3.redis+proxy 4.metaserver
        :type conf_module: int (optional)

        :param conf_desc: 配置对用户展示含义(转码后的一串字符)
        :type conf_desc: str (optional)

        :param conf_redis_version: 参数对应的redis版本。例如：2.6、3.2、 4.0、5.0、 all(所有版本都适配)
        :type conf_redis_version: str (optional)

        :param conf_cache_version: 生效redis version（和VERSION_TYPE保持一致）
        :type conf_cache_version: int (optional)

        :param leader_name: 主角色的名称
        :type leader_name: str (optional)

        :param leader_show_id: 主角色的ID
        :type leader_show_id: str (optional)

        :param leader_region: 主角色的地域
        :type leader_region: str (optional)

        :param group_id: 实例组ID
        :type group_id: str (optional)

        :param group_name: 实例组名称
        :type group_name: str (optional)

        :param group_status: 实例组状态
        :type group_status: str (optional)

        :param cluster_num: 实例组的集群数量
        :type cluster_num: int (optional)

        :param group_create_time: 实例组创建时间
        :type group_create_time: str (optional)

        :param forbid_write: 禁写标志（0 未禁写， 1 禁写）
        :type forbid_write: int (optional)

        :param group_type: 实例组类型。标准版：standalone；集群版：bdrp
        :type group_type: str (optional)
        """
        super().__init__()
        self.template_id = template_id
        self.template_show_id = template_show_id
        self.template_name = template_name
        self.parameters_num = parameters_num
        self.cluster_type = cluster_type
        self.engine = engine
        self.engine_version = engine_version
        self.template_type = template_type
        self.need_reboot = need_reboot
        self.comment = comment
        self.create_time = create_time
        self.update_time = update_time
        self.parameters = parameters
        self.cache_cluster_show_id = cache_cluster_show_id
        self.cache_cluster_name = cache_cluster_name
        self.availability_zone = availability_zone
        self.version = version
        self.status = status
        self.apply_time = apply_time
        self.conf_name = conf_name
        self.conf_default = conf_default
        self.conf_value = conf_value
        self.conf_type = conf_type
        self.conf_range = conf_range
        self.conf_module = conf_module
        self.conf_desc = conf_desc
        self.conf_redis_version = conf_redis_version
        self.conf_cache_version = conf_cache_version
        self.leader_name = leader_name
        self.leader_show_id = leader_show_id
        self.leader_region = leader_region
        self.group_id = group_id
        self.group_name = group_name
        self.group_status = group_status
        self.cluster_num = cluster_num
        self.group_create_time = group_create_time
        self.forbid_write = forbid_write
        self.group_type = group_type

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
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.template_show_id is not None:
            result['templateShowId'] = self.template_show_id
        if self.template_name is not None:
            result['templateName'] = self.template_name
        if self.parameters_num is not None:
            result['parametersNum'] = self.parameters_num
        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type
        if self.engine is not None:
            result['engine'] = self.engine
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.template_type is not None:
            result['templateType'] = self.template_type
        if self.need_reboot is not None:
            result['needReboot'] = self.need_reboot
        if self.comment is not None:
            result['comment'] = self.comment
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.parameters is not None:
            result['parameters'] = [i.to_dict() for i in self.parameters]
        if self.cache_cluster_show_id is not None:
            result['cacheClusterShowId'] = self.cache_cluster_show_id
        if self.cache_cluster_name is not None:
            result['cacheClusterName'] = self.cache_cluster_name
        if self.availability_zone is not None:
            result['availabilityZone'] = self.availability_zone
        if self.version is not None:
            result['version'] = self.version
        if self.status is not None:
            result['status'] = self.status
        if self.apply_time is not None:
            result['applyTime'] = self.apply_time
        if self.conf_name is not None:
            result['confName'] = self.conf_name
        if self.conf_default is not None:
            result['confDefault'] = self.conf_default
        if self.conf_value is not None:
            result['confValue'] = self.conf_value
        if self.conf_type is not None:
            result['confType'] = self.conf_type
        if self.conf_range is not None:
            result['confRange'] = self.conf_range
        if self.conf_module is not None:
            result['confModule'] = self.conf_module
        if self.conf_desc is not None:
            result['confDesc'] = self.conf_desc
        if self.conf_redis_version is not None:
            result['confRedisVersion'] = self.conf_redis_version
        if self.conf_cache_version is not None:
            result['confCacheVersion'] = self.conf_cache_version
        if self.leader_name is not None:
            result['leaderName'] = self.leader_name
        if self.leader_show_id is not None:
            result['leaderShowId'] = self.leader_show_id
        if self.leader_region is not None:
            result['leaderRegion'] = self.leader_region
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.group_status is not None:
            result['groupStatus'] = self.group_status
        if self.cluster_num is not None:
            result['clusterNum'] = self.cluster_num
        if self.group_create_time is not None:
            result['groupCreateTime'] = self.group_create_time
        if self.forbid_write is not None:
            result['forbidWrite'] = self.forbid_write
        if self.group_type is not None:
            result['groupType'] = self.group_type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Result

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('templateShowId') is not None:
            self.template_show_id = m.get('templateShowId')
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        if m.get('parametersNum') is not None:
            self.parameters_num = m.get('parametersNum')
        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')
        if m.get('engine') is not None:
            self.engine = m.get('engine')
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('templateType') is not None:
            self.template_type = m.get('templateType')
        if m.get('needReboot') is not None:
            self.need_reboot = m.get('needReboot')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('parameters') is not None:
            self.parameters = [Parameters().from_dict(i) for i in m.get('parameters')]
        if m.get('cacheClusterShowId') is not None:
            self.cache_cluster_show_id = m.get('cacheClusterShowId')
        if m.get('cacheClusterName') is not None:
            self.cache_cluster_name = m.get('cacheClusterName')
        if m.get('availabilityZone') is not None:
            self.availability_zone = m.get('availabilityZone')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('applyTime') is not None:
            self.apply_time = m.get('applyTime')
        if m.get('confName') is not None:
            self.conf_name = m.get('confName')
        if m.get('confDefault') is not None:
            self.conf_default = m.get('confDefault')
        if m.get('confValue') is not None:
            self.conf_value = m.get('confValue')
        if m.get('confType') is not None:
            self.conf_type = m.get('confType')
        if m.get('confRange') is not None:
            self.conf_range = m.get('confRange')
        if m.get('confModule') is not None:
            self.conf_module = m.get('confModule')
        if m.get('confDesc') is not None:
            self.conf_desc = m.get('confDesc')
        if m.get('confRedisVersion') is not None:
            self.conf_redis_version = m.get('confRedisVersion')
        if m.get('confCacheVersion') is not None:
            self.conf_cache_version = m.get('confCacheVersion')
        if m.get('leaderName') is not None:
            self.leader_name = m.get('leaderName')
        if m.get('leaderShowId') is not None:
            self.leader_show_id = m.get('leaderShowId')
        if m.get('leaderRegion') is not None:
            self.leader_region = m.get('leaderRegion')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('groupStatus') is not None:
            self.group_status = m.get('groupStatus')
        if m.get('clusterNum') is not None:
            self.cluster_num = m.get('clusterNum')
        if m.get('groupCreateTime') is not None:
            self.group_create_time = m.get('groupCreateTime')
        if m.get('forbidWrite') is not None:
            self.forbid_write = m.get('forbidWrite')
        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')
        return self
