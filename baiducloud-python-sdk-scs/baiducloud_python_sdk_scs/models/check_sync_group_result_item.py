"""
CheckSyncGroupResultItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CheckSyncGroupResultItem(AbstractModel):
    """
    CheckSyncGroupResultItem
    """

    def __init__(
        self,
        member_id=None,
        no_data=None,
        version=None,
        engine_version=None,
        cluster_status=None,
        shard_num=None,
        replication_num=None,
        flavor=None,
        not_joined=None,
        no_security_group=None,
        is_hit_x1=None,
        is_append_only_on=None,
        same_passwd=None,
        has_same_hash_tag_conf=None,
        has_set_pwd=None,
    ):
        """
        Initialize CheckSyncGroupResultItem instance.

        :param member_id: 成员实例展示ID
        :type member_id: str (optional)

        :param no_data: 是否没有数据
        :type no_data: bool (optional)

        :param version: 版本校验是否通过
        :type version: bool (optional)

        :param engine_version: 引擎版本是否符合要求
        :type engine_version: bool (optional)

        :param cluster_status: 集群状态校验是否通过
        :type cluster_status: bool (optional)

        :param shard_num: 分片数是否一致
        :type shard_num: bool (optional)

        :param replication_num: 副本数是否一致
        :type replication_num: bool (optional)

        :param flavor: 单分片容量是否一致
        :type flavor: bool (optional)

        :param not_joined: 是否已加入多活/热活实例组
        :type not_joined: bool (optional)

        :param no_security_group: 是否无VPC侧安全组
        :type no_security_group: bool (optional)

        :param is_hit_x1: 是否新架构（true：是，false：否）
        :type is_hit_x1: bool (optional)

        :param is_append_only_on: 是否开启AOF
        :type is_append_only_on: bool (optional)

        :param same_passwd: 密码是否一致
        :type same_passwd: bool (optional)

        :param has_same_hash_tag_conf: 是否具备相同的hashtag参数值
        :type has_same_hash_tag_conf: bool (optional)

        :param has_set_pwd: 是否设置了密码
        :type has_set_pwd: bool (optional)
        """
        super().__init__()
        self.member_id = member_id
        self.no_data = no_data
        self.version = version
        self.engine_version = engine_version
        self.cluster_status = cluster_status
        self.shard_num = shard_num
        self.replication_num = replication_num
        self.flavor = flavor
        self.not_joined = not_joined
        self.no_security_group = no_security_group
        self.is_hit_x1 = is_hit_x1
        self.is_append_only_on = is_append_only_on
        self.same_passwd = same_passwd
        self.has_same_hash_tag_conf = has_same_hash_tag_conf
        self.has_set_pwd = has_set_pwd

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
        if self.member_id is not None:
            result['memberId'] = self.member_id
        if self.no_data is not None:
            result['noData'] = self.no_data
        if self.version is not None:
            result['version'] = self.version
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.cluster_status is not None:
            result['clusterStatus'] = self.cluster_status
        if self.shard_num is not None:
            result['shardNum'] = self.shard_num
        if self.replication_num is not None:
            result['replicationNum'] = self.replication_num
        if self.flavor is not None:
            result['flavor'] = self.flavor
        if self.not_joined is not None:
            result['notJoined'] = self.not_joined
        if self.no_security_group is not None:
            result['noSecurityGroup'] = self.no_security_group
        if self.is_hit_x1 is not None:
            result['isHitX1'] = self.is_hit_x1
        if self.is_append_only_on is not None:
            result['isAppendOnlyOn'] = self.is_append_only_on
        if self.same_passwd is not None:
            result['samePasswd'] = self.same_passwd
        if self.has_same_hash_tag_conf is not None:
            result['hasSameHashTagConf'] = self.has_same_hash_tag_conf
        if self.has_set_pwd is not None:
            result['hasSetPwd'] = self.has_set_pwd
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CheckSyncGroupResultItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('memberId') is not None:
            self.member_id = m.get('memberId')
        if m.get('noData') is not None:
            self.no_data = m.get('noData')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('clusterStatus') is not None:
            self.cluster_status = m.get('clusterStatus')
        if m.get('shardNum') is not None:
            self.shard_num = m.get('shardNum')
        if m.get('replicationNum') is not None:
            self.replication_num = m.get('replicationNum')
        if m.get('flavor') is not None:
            self.flavor = m.get('flavor')
        if m.get('notJoined') is not None:
            self.not_joined = m.get('notJoined')
        if m.get('noSecurityGroup') is not None:
            self.no_security_group = m.get('noSecurityGroup')
        if m.get('isHitX1') is not None:
            self.is_hit_x1 = m.get('isHitX1')
        if m.get('isAppendOnlyOn') is not None:
            self.is_append_only_on = m.get('isAppendOnlyOn')
        if m.get('samePasswd') is not None:
            self.same_passwd = m.get('samePasswd')
        if m.get('hasSameHashTagConf') is not None:
            self.has_same_hash_tag_conf = m.get('hasSameHashTagConf')
        if m.get('hasSetPwd') is not None:
            self.has_set_pwd = m.get('hasSetPwd')
        return self
