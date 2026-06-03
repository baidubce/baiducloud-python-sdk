"""
Request entity for CreateL2PolicyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CreateL2PolicyRequest(AbstractModel):
    """
    Request entity for CreateL2PolicyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        policy_name,
        path,
        expired_time,
        type,
        execute_time=None,
        bucket_name=None,
        bucket_prefix=None,
    ):
        """
        Initialize CreateL2PolicyRequest request entity.

        :param instance_id: 创建规则的pfs实例短id
        :type instance_id: str (required)

        :param policy_name: policy_name parameter
        :type policy_name: str (required)

        :param path: 规则对应的路径，以\"/\"开头，非\"/\"结尾
        :type path: str (required)

        :param expired_time: 规则的过期时间，单位天，1 ～ 365*5
        :type expired_time: int (required)

        :param type: 规则的类型：<br>0：表示数据删除<br>1：表示数据转存
        :type type: int (required)

        :param execute_time: 规则的执行时间点，0～23整数，默认为0，范围在：0 ～ 23
        :type execute_time: int (optional)

        :param bucket_name: 数据转存对应的bucket，当type为数据转存时，该字段必须声明
        :type bucket_name: str (optional)

        :param bucket_prefix: 数据转存对应的prefix，当type为数据转存时，该字段必须声明prefix非\"/'开头，以\"/\"结尾
        :type bucket_prefix: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.policy_name = policy_name
        self.path = path
        self.expired_time = expired_time
        self.type = type
        self.execute_time = execute_time
        self.bucket_name = bucket_name
        self.bucket_prefix = bucket_prefix

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
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.path is not None:
            result['path'] = self.path
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
        if self.type is not None:
            result['type'] = self.type
        if self.execute_time is not None:
            result['executeTime'] = self.execute_time
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.bucket_prefix is not None:
            result['bucketPrefix'] = self.bucket_prefix
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateL2PolicyRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('executeTime') is not None:
            self.execute_time = m.get('executeTime')
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('bucketPrefix') is not None:
            self.bucket_prefix = m.get('bucketPrefix')
        return self
