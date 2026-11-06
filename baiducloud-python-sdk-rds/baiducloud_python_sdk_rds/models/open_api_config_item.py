"""
OpenApiConfigItem information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class OpenApiConfigItem(AbstractModel):
    """
    OpenApiConfigItem
    """

    def __init__(
        self,
        name=None,
        default_value=None,
        value=None,
        pending_value=None,
        type=None,
        dynamic=None,
        modifiable=None,
        allowed_values=None,
        desc=None,
        etag=None,
        config_type=None,
        best_value=None,
        attention=None,
        if_cluster=None,
    ):
        """
        Initialize OpenApiConfigItem instance.

        :param name: 参数名
        :type name: str (optional)

        :param default_value: 参数的默认值
        :type default_value: str (optional)

        :param value: 当前参数值
        :type value: str (optional)

        :param pending_value: 待定值，默认为\"\"
        :type pending_value: str (optional)

        :param type: 参数类型：\"integer\"，\"string\"，\"float\"等
        :type type: str (optional)

        :param dynamic: 是否热加载，\"true\":为热加载参数，\"false\":为非热加载参数
        :type dynamic: str (optional)

        :param modifiable: 是否可修改参数，\"true\"：是，\"false\"：不是
        :type modifiable: str (optional)

        :param allowed_values: 可修改参数值
        :type allowed_values: str (optional)

        :param desc: 描述信息
        :type desc: str (optional)

        :param etag: 修改版本号，如V1
        :type etag: str (optional)

        :param config_type: config_type attribute
        :type config_type: str (optional)

        :param best_value: 建议实践值
        :type best_value: str (optional)

        :param attention: 注意事项
        :type attention: str (optional)

        :param if_cluster: 是否重启， true:是 、false：否
        :type if_cluster: bool (optional)
        """
        super().__init__()
        self.name = name
        self.default_value = default_value
        self.value = value
        self.pending_value = pending_value
        self.type = type
        self.dynamic = dynamic
        self.modifiable = modifiable
        self.allowed_values = allowed_values
        self.desc = desc
        self.etag = etag
        self.config_type = config_type
        self.best_value = best_value
        self.attention = attention
        self.if_cluster = if_cluster

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
        if self.name is not None:
            result['name'] = self.name
        if self.default_value is not None:
            result['defaultValue'] = self.default_value
        if self.value is not None:
            result['value'] = self.value
        if self.pending_value is not None:
            result['pendingValue'] = self.pending_value
        if self.type is not None:
            result['type'] = self.type
        if self.dynamic is not None:
            result['dynamic'] = self.dynamic
        if self.modifiable is not None:
            result['modifiable'] = self.modifiable
        if self.allowed_values is not None:
            result['allowedValues'] = self.allowed_values
        if self.desc is not None:
            result['desc'] = self.desc
        if self.etag is not None:
            result['etag'] = self.etag
        if self.config_type is not None:
            result['configType'] = self.config_type
        if self.best_value is not None:
            result['bestValue'] = self.best_value
        if self.attention is not None:
            result['attention'] = self.attention
        if self.if_cluster is not None:
            result['ifCluster'] = self.if_cluster
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: OpenApiConfigItem

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('defaultValue') is not None:
            self.default_value = m.get('defaultValue')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('pendingValue') is not None:
            self.pending_value = m.get('pendingValue')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('dynamic') is not None:
            self.dynamic = m.get('dynamic')
        if m.get('modifiable') is not None:
            self.modifiable = m.get('modifiable')
        if m.get('allowedValues') is not None:
            self.allowed_values = m.get('allowedValues')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('etag') is not None:
            self.etag = m.get('etag')
        if m.get('configType') is not None:
            self.config_type = m.get('configType')
        if m.get('bestValue') is not None:
            self.best_value = m.get('bestValue')
        if m.get('attention') is not None:
            self.attention = m.get('attention')
        if m.get('ifCluster') is not None:
            self.if_cluster = m.get('ifCluster')
        return self
