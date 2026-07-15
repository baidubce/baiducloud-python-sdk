"""
Output information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Output(AbstractModel):
    """
    Output
    """

    def __init__(self, exit_code=None, stderr=None, stdout=None, is_truncated=None):
        """
        Initialize Output instance.

        :param exit_code: 退出码
        :type exit_code: int (optional)

        :param stderr: 标准错误
        :type stderr: str (optional)

        :param stdout: 标准输出
        :type stdout: str (optional)

        :param is_truncated: 标准输出或标准错误是否由于过长（超过4KB）而被截断
        :type is_truncated: bool (optional)
        """
        super().__init__()
        self.exit_code = exit_code
        self.stderr = stderr
        self.stdout = stdout
        self.is_truncated = is_truncated

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
        if self.exit_code is not None:
            result['exitCode'] = self.exit_code
        if self.stderr is not None:
            result['stderr'] = self.stderr
        if self.stdout is not None:
            result['stdout'] = self.stdout
        if self.is_truncated is not None:
            result['isTruncated'] = self.is_truncated
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Output

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('exitCode') is not None:
            self.exit_code = m.get('exitCode')
        if m.get('stderr') is not None:
            self.stderr = m.get('stderr')
        if m.get('stdout') is not None:
            self.stdout = m.get('stdout')
        if m.get('isTruncated') is not None:
            self.is_truncated = m.get('isTruncated')
        return self
