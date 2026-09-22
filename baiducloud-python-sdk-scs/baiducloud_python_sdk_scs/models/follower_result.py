"""
FollowerResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class FollowerResult(AbstractModel):
    """
    FollowerResult
    """

    def __init__(
        self,
        follower_id=None,
        no_data=None,
        version=None,
        cluster_status=None,
        shard_num=None,
        replication_num=None,
        flavor=None,
        joined=None,
        no_passwd=None,
        no_security_group=None,
        is_hit_x1=None,
        no_tde=None,
        same_passwd=None,
        has_same_hash_tag_conf=None,
        has_set_pwd=None,
        is_not_cross_az_nearest=None,
    ):
        """
        Initialize FollowerResult instance.

        :param follower_id: 从角色ID
        :type follower_id: str (optional)

        :param no_data: 是否没有数据（true:是，false: 否）
        :type no_data: bool (optional)

        :param version: 版本是否为集群版（true:是，false：否）
        :type version: bool (optional)

        :param cluster_status: 集群状态是否是running（true:是，false：否）
        :type cluster_status: bool (optional)

        :param shard_num: 分片数是否和主一致（true:是，false：否）
        :type shard_num: bool (optional)

        :param replication_num: 副本数（true:是，false：否）（主角色副本数需为2）
        :type replication_num: bool (optional)

        :param flavor: 单分片容量（true:是，false：否）（主角色单分片在8G及以下）
        :type flavor: bool (optional)

        :param joined: 是否已加入热活实例组（true：是，false：否）
        :type joined: bool (optional)

        :param no_passwd: 是否无密码（true：是，false：否）
        :type no_passwd: bool (optional)

        :param no_security_group: 是否无VPC侧安全组（true：是， false：否）
        :type no_security_group: bool (optional)

        :param is_hit_x1: 是否是新架构（true:是 false：否）
        :type is_hit_x1: bool (optional)

        :param no_tde: 是否没有开通TDE（true:是 false：否）
        :type no_tde: bool (optional)

        :param same_passwd: 是否校验密码一致（true:是 false：否）
        :type same_passwd: bool (optional)

        :param has_same_hash_tag_conf: 是否具备相同的hashtag参数值（true:是 false：否）
        :type has_same_hash_tag_conf: bool (optional)

        :param has_set_pwd: 是否设置了密码（true:是 false：否）
        :type has_set_pwd: bool (optional)

        :param is_not_cross_az_nearest: 是否没有开通跨AZ就近访问（true:是 false：否）
        :type is_not_cross_az_nearest: bool (optional)
        """
        super().__init__()
        self.follower_id = follower_id
        self.no_data = no_data
        self.version = version
        self.cluster_status = cluster_status
        self.shard_num = shard_num
        self.replication_num = replication_num
        self.flavor = flavor
        self.joined = joined
        self.no_passwd = no_passwd
        self.no_security_group = no_security_group
        self.is_hit_x1 = is_hit_x1
        self.no_tde = no_tde
        self.same_passwd = same_passwd
        self.has_same_hash_tag_conf = has_same_hash_tag_conf
        self.has_set_pwd = has_set_pwd
        self.is_not_cross_az_nearest = is_not_cross_az_nearest

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
        if self.follower_id is not None:
            result['followerId'] = self.follower_id
        if self.no_data is not None:
            result['noData'] = self.no_data
        if self.version is not None:
            result['version'] = self.version
        if self.cluster_status is not None:
            result['clusterStatus'] = self.cluster_status
        if self.shard_num is not None:
            result['shardNum'] = self.shard_num
        if self.replication_num is not None:
            result['replicationNum'] = self.replication_num
        if self.flavor is not None:
            result['flavor'] = self.flavor
        if self.joined is not None:
            result['joined'] = self.joined
        if self.no_passwd is not None:
            result['noPasswd'] = self.no_passwd
        if self.no_security_group is not None:
            result['noSecurityGroup'] = self.no_security_group
        if self.is_hit_x1 is not None:
            result['isHitX1'] = self.is_hit_x1
        if self.no_tde is not None:
            result['noTde'] = self.no_tde
        if self.same_passwd is not None:
            result['samePasswd'] = self.same_passwd
        if self.has_same_hash_tag_conf is not None:
            result['hasSameHashTagConf'] = self.has_same_hash_tag_conf
        if self.has_set_pwd is not None:
            result['hasSetPwd'] = self.has_set_pwd
        if self.is_not_cross_az_nearest is not None:
            result['isNotCrossAzNearest'] = self.is_not_cross_az_nearest
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: FollowerResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('followerId') is not None:
            self.follower_id = m.get('followerId')
        if m.get('noData') is not None:
            self.no_data = m.get('noData')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('clusterStatus') is not None:
            self.cluster_status = m.get('clusterStatus')
        if m.get('shardNum') is not None:
            self.shard_num = m.get('shardNum')
        if m.get('replicationNum') is not None:
            self.replication_num = m.get('replicationNum')
        if m.get('flavor') is not None:
            self.flavor = m.get('flavor')
        if m.get('joined') is not None:
            self.joined = m.get('joined')
        if m.get('noPasswd') is not None:
            self.no_passwd = m.get('noPasswd')
        if m.get('noSecurityGroup') is not None:
            self.no_security_group = m.get('noSecurityGroup')
        if m.get('isHitX1') is not None:
            self.is_hit_x1 = m.get('isHitX1')
        if m.get('noTde') is not None:
            self.no_tde = m.get('noTde')
        if m.get('samePasswd') is not None:
            self.same_passwd = m.get('samePasswd')
        if m.get('hasSameHashTagConf') is not None:
            self.has_same_hash_tag_conf = m.get('hasSameHashTagConf')
        if m.get('hasSetPwd') is not None:
            self.has_set_pwd = m.get('hasSetPwd')
        if m.get('isNotCrossAzNearest') is not None:
            self.is_not_cross_az_nearest = m.get('isNotCrossAzNearest')
        return self
