"""
Request entity for QueryCsnDetailResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_csn.models.tag_model import TagModel


class QueryCsnDetailResponse(BceResponse):
    """
    QueryCsnDetailResponse
    """

    def __init__(
        self,
        name=None,
        description=None,
        csn_id=None,
        status=None,
        instance_num=None,
        csn_bp_num=None,
        created_time=None,
        tags=None,
    ):
        """
        Initialize QueryCsnDetailResponse response.

        :param name: 云智能网的名称
        :type name: str (optional)

        :param description: 云智能网的描述
        :type description: str (optional)

        :param csn_id: 云智能网的ID
        :type csn_id: str (optional)

        :param status: 云智能网的状态
        :type status: str (optional)

        :param instance_num: 云智能网加载的网络实例数量
        :type instance_num: int (optional)

        :param csn_bp_num: 云智能网绑定的带宽包数量
        :type csn_bp_num: int (optional)

        :param created_time: 云智能网的创建时间
        :type created_time: str (optional)

        :param tags: 云智能网绑定的标签信息
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.name = name
        self.description = description
        self.csn_id = csn_id
        self.status = status
        self.instance_num = instance_num
        self.csn_bp_num = csn_bp_num
        self.created_time = created_time
        self.tags = tags

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
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.csn_id is not None:
            result['csnId'] = self.csn_id
        if self.status is not None:
            result['status'] = self.status
        if self.instance_num is not None:
            result['instanceNum'] = self.instance_num
        if self.csn_bp_num is not None:
            result['csnBpNum'] = self.csn_bp_num
        if self.created_time is not None:
            result['createdTime'] = self.created_time
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryCsnDetailResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('csnId') is not None:
            self.csn_id = m.get('csnId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('instanceNum') is not None:
            self.instance_num = m.get('instanceNum')
        if m.get('csnBpNum') is not None:
            self.csn_bp_num = m.get('csnBpNum')
        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
