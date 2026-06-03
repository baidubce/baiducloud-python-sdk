"""
Request entity for DescL2PolicyResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse


class DescL2PolicyResponse(BceResponse):
    """
    DescL2PolicyResponse
    """

    def __init__(
        self,
        request_id=None,
        policy_id=None,
        policy_name=None,
        instance_id=None,
        path=None,
        expired_time=None,
        create_time=None,
        execute_time=None,
        type=None,
        bos_path=None,
        status=None,
    ):
        """
        Initialize DescL2PolicyResponse response.

        :param request_id: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type request_id: str (optional)

        :param policy_id: 规则ID
        :type policy_id: str (optional)

        :param policy_name: 规则名字
        :type policy_name: str (optional)

        :param instance_id: 规则所属实例ID
        :type instance_id: str (optional)

        :param path: 规则生效路径
        :type path: str (optional)

        :param expired_time: 规则过期时间
        :type expired_time: int (optional)

        :param create_time: 规则创建时间
        :type create_time: str (optional)

        :param execute_time: 规则执行时间点
        :type execute_time: int (optional)

        :param type: policy类型。ttl or export
        :type type: int (optional)

        :param bos_path: 如果是导出类型，返回导出的bos bucket路径
        :type bos_path: str (optional)

        :param status: 规则当前状态：<br><li>0：生效中<br><li>1：运行中<br><li>2：删除中<br><li>3：失败
        :type status: int (optional)
        """
        super().__init__()
        self.request_id = request_id
        self.policy_id = policy_id
        self.policy_name = policy_name
        self.instance_id = instance_id
        self.path = path
        self.expired_time = expired_time
        self.create_time = create_time
        self.execute_time = execute_time
        self.type = type
        self.bos_path = bos_path
        self.status = status

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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.path is not None:
            result['path'] = self.path
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.execute_time is not None:
            result['executeTime'] = self.execute_time
        if self.type is not None:
            result['type'] = self.type
        if self.bos_path is not None:
            result['bosPath'] = self.bos_path
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DescL2PolicyResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('executeTime') is not None:
            self.execute_time = m.get('executeTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('bosPath') is not None:
            self.bos_path = m.get('bosPath')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
