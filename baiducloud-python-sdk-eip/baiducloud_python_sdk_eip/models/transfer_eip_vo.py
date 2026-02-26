
from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TransferEipVo(AbstractModel):
    """
    TransferEipVo
    """
    def __init__(self, transfer_id=None, transfer_type=None, user_id=None, to_user_id=None, instance_id=None, instance_name=None, instance_ip=None, instance_type=None, instance_bandwidth=None, status=None, create_time=None, update_time=None):
        super().__init__()
        self.transfer_id = transfer_id
        self.transfer_type = transfer_type
        self.user_id = user_id
        self.to_user_id = to_user_id
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_ip = instance_ip
        self.instance_type = instance_type
        self.instance_bandwidth = instance_bandwidth
        self.status = status
        self.create_time = create_time
        self.update_time = update_time

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.transfer_id is not None:
            result['transferId'] = self.transfer_id
        if self.transfer_type is not None:
            result['transferType'] = self.transfer_type
        if self.user_id is not None:
            result['userId'] = self.user_id
        if self.to_user_id is not None:
            result['toUserId'] = self.to_user_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.instance_ip is not None:
            result['instanceIp'] = self.instance_ip
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.instance_bandwidth is not None:
            result['instanceBandwidth'] = self.instance_bandwidth
        if self.status is not None:
            result['status'] = self.status
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('transferId') is not None:
            self.transfer_id = m.get('transferId')
        if m.get('transferType') is not None:
            self.transfer_type = m.get('transferType')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        if m.get('toUserId') is not None:
            self.to_user_id = m.get('toUserId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('instanceIp') is not None:
            self.instance_ip = m.get('instanceIp')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('instanceBandwidth') is not None:
            self.instance_bandwidth = m.get('instanceBandwidth')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self
