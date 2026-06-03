"""
ReplicationTrigger information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_ccr.models.replication_settings import ReplicationSettings


class ReplicationTrigger(AbstractModel):
    """
    ReplicationTrigger
    """

    def __init__(self, trigger_settings=None, type=None):
        """
        Initialize ReplicationTrigger instance.

        :param trigger_settings: trigger_settings attribute
        :type trigger_settings: ReplicationSettings (optional)

        :param type: 迁移规则触发类型，有效值为 `manual`、`event_based` 和 `scheduled`
        :type type: str (optional)
        """
        super().__init__()
        self.trigger_settings = trigger_settings
        self.type = type

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
        if self.trigger_settings is not None:
            result['triggerSettings'] = self.trigger_settings.to_dict()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ReplicationTrigger

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('triggerSettings') is not None:
            self.trigger_settings = ReplicationSettings().from_dict(m.get('triggerSettings'))
        if m.get('type') is not None:
            self.type = m.get('type')
        return self
