"""
PeerConnStatus information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PeerConnStatus(AbstractModel):
    """
    PeerConnStatus
    """

    def __init__(
        self,
        creating=None,
        consulting=None,
        consult_failed=None,
        active=None,
        down=None,
        starting=None,
        stopping=None,
        deleting=None,
        deleted=None,
        expired=None,
        error=None,
        updating=None,
    ):
        """
        Initialize PeerConnStatus instance.

        :param creating: 创建中
        :type creating: str (optional)

        :param consulting: 协商中
        :type consulting: str (optional)

        :param consult_failed: 协商失败
        :type consult_failed: str (optional)

        :param active: 可用
        :type active: str (optional)

        :param down: 不可用
        :type down: str (optional)

        :param starting: 启动中
        :type starting: str (optional)

        :param stopping: 停止中
        :type stopping: str (optional)

        :param deleting: 删除中
        :type deleting: str (optional)

        :param deleted: 已删除
        :type deleted: str (optional)

        :param expired: 已到期
        :type expired: str (optional)

        :param error: 异常
        :type error: str (optional)

        :param updating: 更新中
        :type updating: str (optional)
        """
        super().__init__()
        self.creating = creating
        self.consulting = consulting
        self.consult_failed = consult_failed
        self.active = active
        self.down = down
        self.starting = starting
        self.stopping = stopping
        self.deleting = deleting
        self.deleted = deleted
        self.expired = expired
        self.error = error
        self.updating = updating

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
        if self.creating is not None:
            result['creating'] = self.creating
        if self.consulting is not None:
            result['consulting'] = self.consulting
        if self.consult_failed is not None:
            result['consult_failed'] = self.consult_failed
        if self.active is not None:
            result['active'] = self.active
        if self.down is not None:
            result['down'] = self.down
        if self.starting is not None:
            result['starting'] = self.starting
        if self.stopping is not None:
            result['stopping'] = self.stopping
        if self.deleting is not None:
            result['deleting'] = self.deleting
        if self.deleted is not None:
            result['deleted'] = self.deleted
        if self.expired is not None:
            result['expired'] = self.expired
        if self.error is not None:
            result['error'] = self.error
        if self.updating is not None:
            result['updating'] = self.updating
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PeerConnStatus

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('creating') is not None:
            self.creating = m.get('creating')
        if m.get('consulting') is not None:
            self.consulting = m.get('consulting')
        if m.get('consult_failed') is not None:
            self.consult_failed = m.get('consult_failed')
        if m.get('active') is not None:
            self.active = m.get('active')
        if m.get('down') is not None:
            self.down = m.get('down')
        if m.get('starting') is not None:
            self.starting = m.get('starting')
        if m.get('stopping') is not None:
            self.stopping = m.get('stopping')
        if m.get('deleting') is not None:
            self.deleting = m.get('deleting')
        if m.get('deleted') is not None:
            self.deleted = m.get('deleted')
        if m.get('expired') is not None:
            self.expired = m.get('expired')
        if m.get('error') is not None:
            self.error = m.get('error')
        if m.get('updating') is not None:
            self.updating = m.get('updating')
        return self
