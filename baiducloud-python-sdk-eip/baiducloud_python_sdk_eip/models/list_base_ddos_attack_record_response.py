"""
Request entity for ListBaseDdosAttackRecordResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_eip.models.ddos_attack_record_model import DdosAttackRecordModel


class ListBaseDdosAttackRecordResponse(BceResponse):
    """
    ListBaseDdosAttackRecordResponse
    """

    def __init__(self, attack_record_list=None):
        """
        Initialize ListBaseDdosAttackRecordResponse response.

        :param attack_record_list: 基础防护攻击记录列表
        :type attack_record_list: List[DdosAttackRecordModel] (optional)
        """
        super().__init__()
        self.attack_record_list = attack_record_list

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
        if self.attack_record_list is not None:
            result['attackRecordList'] = [i.to_dict() for i in self.attack_record_list]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ListBaseDdosAttackRecordResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('attackRecordList') is not None:
            self.attack_record_list = [DdosAttackRecordModel().from_dict(i) for i in m.get('attackRecordList')]
        return self
