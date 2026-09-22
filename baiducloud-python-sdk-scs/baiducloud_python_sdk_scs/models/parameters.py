"""
Parameters information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Parameters(AbstractModel):
    """
    Parameters
    """

    def __init__(
        self,
        conf_name=None,
        conf_default=None,
        conf_value=None,
        conf_type=None,
        conf_range=None,
        conf_module=None,
        conf_desc=None,
        need_reboot=None,
        conf_redis_version=None,
        conf_cache_version=None,
        conf_user_visible=None,
    ):
        """
        Initialize Parameters instance.

        :param conf_name: 参数名称（可参考系统模版）
        :type conf_name: str (optional)

        :param conf_default: 参数默认值
        :type conf_default: str (optional)

        :param conf_value: 参数值（可修改对应的值，可参考系统模版在confRange的允许范围内修改）
        :type conf_value: str (optional)

        :param conf_type: 参数类型（可参考系统模版）
        :type conf_type: int (optional)

        :param conf_range: conf_range attribute
        :type conf_range: str (optional)

        :param conf_module: 可参考系统模版
        :type conf_module: int (optional)

        :param conf_desc: 配置对用户展示含义(转码后的一串字符)
        :type conf_desc: str (optional)

        :param need_reboot: 该参数是否需要重启，0：不需要，1：需要
        :type need_reboot: int (optional)

        :param conf_redis_version: 参数对应的redis版本。例如：2.6、3.2、 4.0、 all
        :type conf_redis_version: str (optional)

        :param conf_cache_version: 生效redis version（和VERSION_TYPE保持一致）
        :type conf_cache_version: int (optional)

        :param conf_user_visible: 用户是否可见（0 可见， 1 不可见）
        :type conf_user_visible: int (optional)
        """
        super().__init__()
        self.conf_name = conf_name
        self.conf_default = conf_default
        self.conf_value = conf_value
        self.conf_type = conf_type
        self.conf_range = conf_range
        self.conf_module = conf_module
        self.conf_desc = conf_desc
        self.need_reboot = need_reboot
        self.conf_redis_version = conf_redis_version
        self.conf_cache_version = conf_cache_version
        self.conf_user_visible = conf_user_visible

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
        if self.conf_name is not None:
            result['confName'] = self.conf_name
        if self.conf_default is not None:
            result['confDefault'] = self.conf_default
        if self.conf_value is not None:
            result['confValue'] = self.conf_value
        if self.conf_type is not None:
            result['confType'] = self.conf_type
        if self.conf_range is not None:
            result['confRange'] = self.conf_range
        if self.conf_module is not None:
            result['confModule'] = self.conf_module
        if self.conf_desc is not None:
            result['confDesc'] = self.conf_desc
        if self.need_reboot is not None:
            result['needReboot'] = self.need_reboot
        if self.conf_redis_version is not None:
            result['confRedisVersion'] = self.conf_redis_version
        if self.conf_cache_version is not None:
            result['confCacheVersion'] = self.conf_cache_version
        if self.conf_user_visible is not None:
            result['confUserVisible'] = self.conf_user_visible
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Parameters

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('confName') is not None:
            self.conf_name = m.get('confName')
        if m.get('confDefault') is not None:
            self.conf_default = m.get('confDefault')
        if m.get('confValue') is not None:
            self.conf_value = m.get('confValue')
        if m.get('confType') is not None:
            self.conf_type = m.get('confType')
        if m.get('confRange') is not None:
            self.conf_range = m.get('confRange')
        if m.get('confModule') is not None:
            self.conf_module = m.get('confModule')
        if m.get('confDesc') is not None:
            self.conf_desc = m.get('confDesc')
        if m.get('needReboot') is not None:
            self.need_reboot = m.get('needReboot')
        if m.get('confRedisVersion') is not None:
            self.conf_redis_version = m.get('confRedisVersion')
        if m.get('confCacheVersion') is not None:
            self.conf_cache_version = m.get('confCacheVersion')
        if m.get('confUserVisible') is not None:
            self.conf_user_visible = m.get('confUserVisible')
        return self
