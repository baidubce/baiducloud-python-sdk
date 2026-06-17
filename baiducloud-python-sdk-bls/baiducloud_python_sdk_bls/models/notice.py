"""
Notice information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bls.models.disable_time import DisableTime


class Notice(AbstractModel):
    """
    Notice
    """

    def __init__(self, id=None, name=None, members=None, methods=None, callbacks=None, disable_times=None):
        """
        Initialize Notice instance.

        :param id: 报警模板id
        :type id: str (optional)

        :param name: 报警模板名称
        :type name: str (optional)

        :param members: 报警模板用户列表
        :type members: List[str] (optional)

        :param methods: 报警模板通知方式，取值：EMAIL: 邮件，SMS: 短信， PHONE: 电话
        :type methods: List[str] (optional)

        :param callbacks: 报警模板回调地址
        :type callbacks: List[str] (optional)

        :param disable_times: 屏蔽时间
        :type disable_times: List[DisableTime] (optional)
        """
        super().__init__()
        self.id = id
        self.name = name
        self.members = members
        self.methods = methods
        self.callbacks = callbacks
        self.disable_times = disable_times

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
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.members is not None:
            result['members'] = self.members
        if self.methods is not None:
            result['methods'] = self.methods
        if self.callbacks is not None:
            result['callbacks'] = self.callbacks
        if self.disable_times is not None:
            result['disableTimes'] = [i.to_dict() for i in self.disable_times]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Notice

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('members') is not None:
            self.members = m.get('members')
        if m.get('methods') is not None:
            self.methods = m.get('methods')
        if m.get('callbacks') is not None:
            self.callbacks = m.get('callbacks')
        if m.get('disableTimes') is not None:
            self.disable_times = [DisableTime().from_dict(i) for i in m.get('disableTimes')]
        return self
