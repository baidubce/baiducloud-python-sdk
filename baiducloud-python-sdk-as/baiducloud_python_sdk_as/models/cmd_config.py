"""
CmdConfig information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CmdConfig(AbstractModel):
    """
    CmdConfig
    """

    def __init__(
        self,
        has_decrease_cmd=None,
        dec_cmd_strategy=None,
        dec_cmd_data=None,
        dec_cmd_timeout=None,
        dec_cmd_manual=None,
        has_increase_cmd=None,
        inc_cmd_strategy=None,
        inc_cmd_data=None,
        inc_cmd_timeout=None,
        inc_cmd_manual=None,
    ):
        """
        Initialize CmdConfig instance.

        :param has_decrease_cmd: 是否配置缩容脚本
        :type has_decrease_cmd: bool (optional)

        :param dec_cmd_strategy: 缩容策略，不可为空，失败暂停缩容、失败继续缩容：Proceed、Pause
        :type dec_cmd_strategy: str (optional)

        :param dec_cmd_data: 缩容脚本
        :type dec_cmd_data: str (optional)

        :param dec_cmd_timeout: 缩容脚本超时时间
        :type dec_cmd_timeout: int (optional)

        :param dec_cmd_manual: 手动移出是否执行缩容脚本
        :type dec_cmd_manual: bool (optional)

        :param has_increase_cmd: 是否配置扩容脚本
        :type has_increase_cmd: bool (optional)

        :param inc_cmd_strategy: 缩容策略，不可为空，失败暂停缩容、失败继续缩容：Proceed、Pause
        :type inc_cmd_strategy: str (optional)

        :param inc_cmd_data: 扩容脚本
        :type inc_cmd_data: str (optional)

        :param inc_cmd_timeout: 扩容脚本超时时间
        :type inc_cmd_timeout: int (optional)

        :param inc_cmd_manual: 手动移入是否执行扩容脚本
        :type inc_cmd_manual: bool (optional)
        """
        super().__init__()
        self.has_decrease_cmd = has_decrease_cmd
        self.dec_cmd_strategy = dec_cmd_strategy
        self.dec_cmd_data = dec_cmd_data
        self.dec_cmd_timeout = dec_cmd_timeout
        self.dec_cmd_manual = dec_cmd_manual
        self.has_increase_cmd = has_increase_cmd
        self.inc_cmd_strategy = inc_cmd_strategy
        self.inc_cmd_data = inc_cmd_data
        self.inc_cmd_timeout = inc_cmd_timeout
        self.inc_cmd_manual = inc_cmd_manual

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
        if self.has_decrease_cmd is not None:
            result['hasDecreaseCmd'] = self.has_decrease_cmd
        if self.dec_cmd_strategy is not None:
            result['decCmdStrategy'] = self.dec_cmd_strategy
        if self.dec_cmd_data is not None:
            result['decCmdData'] = self.dec_cmd_data
        if self.dec_cmd_timeout is not None:
            result['decCmdTimeout'] = self.dec_cmd_timeout
        if self.dec_cmd_manual is not None:
            result['decCmdManual'] = self.dec_cmd_manual
        if self.has_increase_cmd is not None:
            result['hasIncreaseCmd'] = self.has_increase_cmd
        if self.inc_cmd_strategy is not None:
            result['incCmdStrategy'] = self.inc_cmd_strategy
        if self.inc_cmd_data is not None:
            result['incCmdData'] = self.inc_cmd_data
        if self.inc_cmd_timeout is not None:
            result['incCmdTimeout'] = self.inc_cmd_timeout
        if self.inc_cmd_manual is not None:
            result['incCmdManual'] = self.inc_cmd_manual
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CmdConfig

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('hasDecreaseCmd') is not None:
            self.has_decrease_cmd = m.get('hasDecreaseCmd')
        if m.get('decCmdStrategy') is not None:
            self.dec_cmd_strategy = m.get('decCmdStrategy')
        if m.get('decCmdData') is not None:
            self.dec_cmd_data = m.get('decCmdData')
        if m.get('decCmdTimeout') is not None:
            self.dec_cmd_timeout = m.get('decCmdTimeout')
        if m.get('decCmdManual') is not None:
            self.dec_cmd_manual = m.get('decCmdManual')
        if m.get('hasIncreaseCmd') is not None:
            self.has_increase_cmd = m.get('hasIncreaseCmd')
        if m.get('incCmdStrategy') is not None:
            self.inc_cmd_strategy = m.get('incCmdStrategy')
        if m.get('incCmdData') is not None:
            self.inc_cmd_data = m.get('incCmdData')
        if m.get('incCmdTimeout') is not None:
            self.inc_cmd_timeout = m.get('incCmdTimeout')
        if m.get('incCmdManual') is not None:
            self.inc_cmd_manual = m.get('incCmdManual')
        return self
