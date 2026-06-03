"""
Request entity for UpdateInstanceNameResponse information.
"""

from baiducloud_python_sdk_core.bce_response import BceResponse
from baiducloud_python_sdk_ccr.models.logical_tag import LogicalTag


class UpdateInstanceNameResponse(BceResponse):
    """
    UpdateInstanceNameResponse
    """

    def __init__(
        self,
        id=None,
        name=None,
        instance_type=None,
        public_url=None,
        region=None,
        status=None,
        create_time=None,
        tags=None,
    ):
        """
        Initialize UpdateInstanceNameResponse response.

        :param id: 实例ID
        :type id: str (optional)

        :param name: 实例名称
        :type name: str (optional)

        :param instance_type: 实例类型
        :type instance_type: str (optional)

        :param public_url: 公共访问地址
        :type public_url: str (optional)

        :param region: 地域
        :type region: str (optional)

        :param status: 实例状态
        :type status: str (optional)

        :param create_time: 创建时间
        :type create_time: str (optional)

        :param tags: tags field
        :type tags: LogicalTag (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.instance_type = instance_type
        self.public_url = public_url
        self.region = region
        self.status = status
        self.create_time = create_time
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
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.public_url is not None:
            result['publicURL'] = self.public_url
        if self.region is not None:
            result['region'] = self.region
        if self.status is not None:
            result['status'] = self.status
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.tags is not None:
            result['tags'] = self.tags.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the response instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing response data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateInstanceNameResponse

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('publicURL') is not None:
            self.public_url = m.get('publicURL')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('tags') is not None:
            self.tags = LogicalTag().from_dict(m.get('tags'))
        return self
