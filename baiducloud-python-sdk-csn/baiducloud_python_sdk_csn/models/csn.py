"""
Csn information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_csn.models.tag_model import TagModel


class Csn(AbstractModel):
    """
    Csn
    """

    def __init__(
        self,
        csn_id=None,
        name=None,
        description=None,
        status=None,
        instance_num=None,
        csn_bp_num=None,
        create_time=None,
        tags=None,
    ):
        """
        Initialize Csn instance.

        :param csn_id: CSN的ID
        :type csn_id: str (optional)

        :param name: CSN的名称
        :type name: str (optional)

        :param description: CSN的描述
        :type description: str (optional)

        :param status: CSN的状态
        :type status: str (optional)

        :param instance_num: CSN网络实例个数
        :type instance_num: int (optional)

        :param csn_bp_num: CSN带宽包个数
        :type csn_bp_num: int (optional)

        :param create_time: CSN的创建时间
        :type create_time: str (optional)

        :param tags: CSN绑定的标签集合
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.csn_id = csn_id
        self.name = name
        self.description = description
        self.status = status
        self.instance_num = instance_num
        self.csn_bp_num = csn_bp_num
        self.create_time = create_time
        self.tags = tags

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
        if self.csn_id is not None:
            result['csnId'] = self.csn_id
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.status is not None:
            result['status'] = self.status
        if self.instance_num is not None:
            result['instanceNum'] = self.instance_num
        if self.csn_bp_num is not None:
            result['csnBpNum'] = self.csn_bp_num
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Csn

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('csnId') is not None:
            self.csn_id = m.get('csnId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('instanceNum') is not None:
            self.instance_num = m.get('instanceNum')
        if m.get('csnBpNum') is not None:
            self.csn_bp_num = m.get('csnBpNum')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
