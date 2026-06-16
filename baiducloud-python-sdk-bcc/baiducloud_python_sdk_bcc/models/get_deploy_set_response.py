"""
Request entity for GetDeploySetResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_bcc.models.az_intstance_statis_detail import AzIntstanceStatisDetail


class GetDeploySetResponse(BceResponse):
    """
    GetDeploySetResponse
    """

    def __init__(
        self,
        short_id=None,
        uuid=None,
        instance_total=None,
        instance_count=None,
        bcc_instance_cnt=None,
        bbc_instance_cnt=None,
        az_intstance_statis_list=None,
    ):
        """
        Initialize GetDeploySetResponse response.

        :param short_id: 部署集短id
        :type short_id: str (optional)

        :param uuid: 部署集长id
        :type uuid: str (optional)

        :param instance_total: 当前部署集strategy类型下指定可用区配额
        :type instance_total: int (optional)

        :param instance_count: 部署集关联实例数量
        :type instance_count: int (optional)

        :param bcc_instance_cnt: 部署集关联bcc实例数量
        :type bcc_instance_cnt: int (optional)

        :param bbc_instance_cnt: 部署集关联bbc实例数量
        :type bbc_instance_cnt: int (optional)

        :param az_intstance_statis_list: 可用区实例统计列表
        :type az_intstance_statis_list: List[AzIntstanceStatisDetail] (optional)
        """
        super().__init__()
        self.short_id = short_id
        self.uuid = uuid
        self.instance_total = instance_total
        self.instance_count = instance_count
        self.bcc_instance_cnt = bcc_instance_cnt
        self.bbc_instance_cnt = bbc_instance_cnt
        self.az_intstance_statis_list = az_intstance_statis_list

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
        if self.short_id is not None:
            result['shortId'] = self.short_id
        if self.uuid is not None:
            result['uuid'] = self.uuid
        if self.instance_total is not None:
            result['instanceTotal'] = self.instance_total
        if self.instance_count is not None:
            result['instanceCount'] = self.instance_count
        if self.bcc_instance_cnt is not None:
            result['bccInstanceCnt'] = self.bcc_instance_cnt
        if self.bbc_instance_cnt is not None:
            result['bbcInstanceCnt'] = self.bbc_instance_cnt
        if self.az_intstance_statis_list is not None:
            result['azIntstanceStatisList'] = [i.to_dict() for i in self.az_intstance_statis_list]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: GetDeploySetResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('shortId') is not None:
            self.short_id = m.get('shortId')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        if m.get('instanceTotal') is not None:
            self.instance_total = m.get('instanceTotal')
        if m.get('instanceCount') is not None:
            self.instance_count = m.get('instanceCount')
        if m.get('bccInstanceCnt') is not None:
            self.bcc_instance_cnt = m.get('bccInstanceCnt')
        if m.get('bbcInstanceCnt') is not None:
            self.bbc_instance_cnt = m.get('bbcInstanceCnt')
        if m.get('azIntstanceStatisList') is not None:
            self.az_intstance_statis_list = [
                AzIntstanceStatisDetail().from_dict(i) for i in m.get('azIntstanceStatisList')
            ]
        return self
