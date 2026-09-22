"""
Request entity for GetHotGroupDetailResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_scs.models.leader import Leader
from baiducloud_python_sdk_scs.models.followers import Followers


class GetHotGroupDetailResponse(BceResponse):
    """
    GetHotGroupDetailResponse
    """

    def __init__(
        self,
        leader=None,
        followers=None,
        group_id=None,
        group_name=None,
        group_status=None,
        cluster_num=None,
        group_create_time=None,
        forbid_write=None,
        group_type=None,
    ):
        """
        Initialize GetHotGroupDetailResponse response.

        :param leader: leader field
        :type leader: Leader (optional)

        :param followers: 从角色信息
        :type followers: List[Followers] (optional)

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
        self.leader = leader
        self.followers = followers
        self.group_id = group_id
        self.group_name = group_name
        self.group_status = group_status
        self.cluster_num = cluster_num
        self.group_create_time = group_create_time
        self.forbid_write = forbid_write
        self.group_type = group_type

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
        if self.leader is not None:
            result['leader'] = self.leader.to_dict()
        if self.followers is not None:
            result['followers'] = [i.to_dict() for i in self.followers]
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
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetHotGroupDetailResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('leader') is not None:
            self.leader = Leader().from_dict(m.get('leader'))
        if m.get('followers') is not None:
            self.followers = [Followers().from_dict(i) for i in m.get('followers')]
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
