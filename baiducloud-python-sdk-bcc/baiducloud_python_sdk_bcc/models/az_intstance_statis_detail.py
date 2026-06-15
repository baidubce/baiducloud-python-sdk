"""
AzIntstanceStatisDetail information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class AzIntstanceStatisDetail(AbstractModel):
    """
    AzIntstanceStatisDetail
    """

    def __init__(
        self,
        zone_name=None,
        instance_count=None,
        instance_total=None,
        bcc_instance_cnt=None,
        bbc_instance_cnt=None,
        instance_ids=None,
        bcc_instance_ids=None,
        bbc_instance_ids=None,
    ):
        """
        Initialize AzIntstanceStatisDetail instance.

        :param zone_name: 可用区名称
        :type zone_name: str (optional)

        :param instance_count: 部署集关联的实例数量
        :type instance_count: int (optional)

        :param instance_total: 当前部署集strategy类型下指定可用区配额
        :type instance_total: int (optional)

        :param bcc_instance_cnt: 部署集关联的BCC实例数量
        :type bcc_instance_cnt: int (optional)

        :param bbc_instance_cnt: 部署集关联的BBC实例数量
        :type bbc_instance_cnt: int (optional)

        :param instance_ids: 部署集关联的实例列表（查询部署集详情返回）
        :type instance_ids: List[str] (optional)

        :param bcc_instance_ids: 部署集关联的BCC实例ID列表（查询部署集详情返回）
        :type bcc_instance_ids: List[str] (optional)

        :param bbc_instance_ids: 部署集关联的BBC实例数量（查询部署集详情返回）
        :type bbc_instance_ids: List[str] (optional)
        """
        super().__init__()
        self.zone_name = zone_name
        self.instance_count = instance_count
        self.instance_total = instance_total
        self.bcc_instance_cnt = bcc_instance_cnt
        self.bbc_instance_cnt = bbc_instance_cnt
        self.instance_ids = instance_ids
        self.bcc_instance_ids = bcc_instance_ids
        self.bbc_instance_ids = bbc_instance_ids

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
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.instance_count is not None:
            result['instanceCount'] = self.instance_count
        if self.instance_total is not None:
            result['instanceTotal'] = self.instance_total
        if self.bcc_instance_cnt is not None:
            result['bccInstanceCnt'] = self.bcc_instance_cnt
        if self.bbc_instance_cnt is not None:
            result['bbcInstanceCnt'] = self.bbc_instance_cnt
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.bcc_instance_ids is not None:
            result['bccInstanceIds'] = self.bcc_instance_ids
        if self.bbc_instance_ids is not None:
            result['bbcInstanceIds'] = self.bbc_instance_ids
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AzIntstanceStatisDetail

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('instanceCount') is not None:
            self.instance_count = m.get('instanceCount')
        if m.get('instanceTotal') is not None:
            self.instance_total = m.get('instanceTotal')
        if m.get('bccInstanceCnt') is not None:
            self.bcc_instance_cnt = m.get('bccInstanceCnt')
        if m.get('bbcInstanceCnt') is not None:
            self.bbc_instance_cnt = m.get('bbcInstanceCnt')
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('bccInstanceIds') is not None:
            self.bcc_instance_ids = m.get('bccInstanceIds')
        if m.get('bbcInstanceIds') is not None:
            self.bbc_instance_ids = m.get('bbcInstanceIds')
        return self
