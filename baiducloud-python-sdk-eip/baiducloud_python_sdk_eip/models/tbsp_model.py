
from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_eip.models.tbsp_ip_model import TbspIpModel

from baiducloud_python_sdk_eip.models.tbsp_attack_record_model import TbspAttackRecordModel

from baiducloud_python_sdk_eip.models.tag_model import TagModel


class TbspModel(AbstractModel):
    """
    TbspModel
    """
    def __init__(self, name=None, id=None, defense_line_type=None, defense_count_quota=None, ip_list=None, ip_total_count=None, auto_renew_switch=None, product_status=None, create_time=None, expire_time=None, defense_enable=None, attacking_record_list=None, attacking_record_total_count=None, tags=None):
        super().__init__()
        self.name = name
        self.id = id
        self.defense_line_type = defense_line_type
        self.defense_count_quota = defense_count_quota
        self.ip_list = ip_list
        self.ip_total_count = ip_total_count
        self.auto_renew_switch = auto_renew_switch
        self.product_status = product_status
        self.create_time = create_time
        self.expire_time = expire_time
        self.defense_enable = defense_enable
        self.attacking_record_list = attacking_record_list
        self.attacking_record_total_count = attacking_record_total_count
        self.tags = tags

    def to_dict(self):
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.id is not None:
            result['id'] = self.id
        if self.defense_line_type is not None:
            result['defenseLineType'] = self.defense_line_type
        if self.defense_count_quota is not None:
            result['defenseCountQuota'] = self.defense_count_quota
        if self.ip_list is not None:
            result['ipList'] = [i.to_dict() for i in self.ip_list]
        if self.ip_total_count is not None:
            result['ipTotalCount'] = self.ip_total_count
        if self.auto_renew_switch is not None:
            result['autoRenewSwitch'] = self.auto_renew_switch
        if self.product_status is not None:
            result['productStatus'] = self.product_status
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.defense_enable is not None:
            result['defenseEnable'] = self.defense_enable
        if self.attacking_record_list is not None:
            result['attackingRecordList'] = [i.to_dict() for i in self.attacking_record_list]
        if self.attacking_record_total_count is not None:
            result['attackingRecordTotalCount'] = self.attacking_record_total_count
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result


    def from_dict(self, m):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('defenseLineType') is not None:
            self.defense_line_type = m.get('defenseLineType')
        if m.get('defenseCountQuota') is not None:
            self.defense_count_quota = m.get('defenseCountQuota')
        if m.get('ipList') is not None:
            self.ip_list = [
            TbspIpModel().from_dict(i)
            for i in m.get('ipList')
            ]
        if m.get('ipTotalCount') is not None:
            self.ip_total_count = m.get('ipTotalCount')
        if m.get('autoRenewSwitch') is not None:
            self.auto_renew_switch = m.get('autoRenewSwitch')
        if m.get('productStatus') is not None:
            self.product_status = m.get('productStatus')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('defenseEnable') is not None:
            self.defense_enable = m.get('defenseEnable')
        if m.get('attackingRecordList') is not None:
            self.attacking_record_list = [
            TbspAttackRecordModel().from_dict(i)
            for i in m.get('attackingRecordList')
            ]
        if m.get('attackingRecordTotalCount') is not None:
            self.attacking_record_total_count = m.get('attackingRecordTotalCount')
        if m.get('tags') is not None:
            self.tags = [
            TagModel().from_dict(i)
            for i in m.get('tags')
            ]
        return self
