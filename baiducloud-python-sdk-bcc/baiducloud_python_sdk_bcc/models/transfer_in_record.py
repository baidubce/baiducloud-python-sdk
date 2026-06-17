"""
TransferInRecord information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcc.models.reserved_instance_info import ReservedInstanceInfo


class TransferInRecord(AbstractModel):
    """
    TransferInRecord
    """

    def __init__(
        self,
        transfer_record_id=None,
        grantor_user_id=None,
        status=None,
        reserved_instance_info=None,
        application_time=None,
        expire_time=None,
        end_time=None,
    ):
        """
        Initialize TransferInRecord instance.

        :param transfer_record_id: 券转移记录id
        :type transfer_record_id: str (optional)

        :param grantor_user_id: 转让人账号(脱敏处理)
        :type grantor_user_id: str (optional)

        :param status: 券转移记录状态
        :type status: str (optional)

        :param reserved_instance_info: reserved_instance_info attribute
        :type reserved_instance_info: ReservedInstanceInfo (optional)

        :param application_time: 券转移发起时间
        :type application_time: str (optional)

        :param expire_time: 券转移过期时间
        :type expire_time: str (optional)

        :param end_time: 券转移结束时间
        :type end_time: str (optional)
        """
        super().__init__()
        self.transfer_record_id = transfer_record_id
        self.grantor_user_id = grantor_user_id
        self.status = status
        self.reserved_instance_info = reserved_instance_info
        self.application_time = application_time
        self.expire_time = expire_time
        self.end_time = end_time

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
        if self.transfer_record_id is not None:
            result['transferRecordId'] = self.transfer_record_id
        if self.grantor_user_id is not None:
            result['grantorUserId'] = self.grantor_user_id
        if self.status is not None:
            result['status'] = self.status
        if self.reserved_instance_info is not None:
            result['reservedInstanceInfo'] = self.reserved_instance_info.to_dict()
        if self.application_time is not None:
            result['applicationTime'] = self.application_time
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TransferInRecord

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('transferRecordId') is not None:
            self.transfer_record_id = m.get('transferRecordId')
        if m.get('grantorUserId') is not None:
            self.grantor_user_id = m.get('grantorUserId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('reservedInstanceInfo') is not None:
            self.reserved_instance_info = ReservedInstanceInfo().from_dict(m.get('reservedInstanceInfo'))
        if m.get('applicationTime') is not None:
            self.application_time = m.get('applicationTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        return self
