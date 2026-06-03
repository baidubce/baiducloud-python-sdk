"""
Request entity for UpdateL2PolicyRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateL2PolicyRequest(AbstractModel):
    """
    Request entity for UpdateL2PolicyRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        instance_id,
        policy_id,
        new_policy_name,
        expired_time=None,
        execute_time=None,
        bucket_name=None,
        bucket_prefix=None,
    ):
        """
        Initialize UpdateL2PolicyRequest request entity.

        :param instance_id: policyId对应的pfs实例短id
        :type instance_id: str (required)

        :param policy_id: 需要修改policyId
        :type policy_id: str (required)

        :param new_policy_name: new_policy_name parameter
        :type new_policy_name: str (required)

        :param expired_time: 规则的过期时间，单位天，1 ～ 365*5
        :type expired_time: int (optional)

        :param execute_time: 规则的执行时间点，0～23整数，默认为0，范围在：0 ～ 23
        :type execute_time: int (optional)

        :param bucket_name: 数据转存对应的bucket
        :type bucket_name: str (optional)

        :param bucket_prefix: 数据转存对应的prefix，非\"/\"开头，以\"/\"结尾
        :type bucket_prefix: str (optional)
        """
        super().__init__()
        self.instance_id = instance_id
        self.policy_id = policy_id
        self.new_policy_name = new_policy_name
        self.expired_time = expired_time
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
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.new_policy_name is not None:
            result['newPolicyName'] = self.new_policy_name
        if self.expired_time is not None:
            result['expiredTime'] = self.expired_time
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
        :rtype: UpdateL2PolicyRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('newPolicyName') is not None:
            self.new_policy_name = m.get('newPolicyName')
        if m.get('expiredTime') is not None:
            self.expired_time = m.get('expiredTime')
        if m.get('executeTime') is not None:
            self.execute_time = m.get('executeTime')
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('bucketPrefix') is not None:
            self.bucket_prefix = m.get('bucketPrefix')
        return self
