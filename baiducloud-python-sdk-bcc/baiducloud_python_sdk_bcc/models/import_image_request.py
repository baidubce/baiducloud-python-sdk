"""
Request entity for ImportImageRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class ImportImageRequest(AbstractModel):
    """
    Request entity for ImportImageRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, os_name, os_arch, os_type, os_version, name, bos_url, detection=None, generation_type=None):
        """
        Initialize ImportImageRequest request entity.

        :param os_name: 操作系统名称
        :type os_name: str (required)

        :param os_arch: 操作系统位数
        :type os_arch: str (required)

        :param os_type: 操作系统类型
        :type os_type: str (required)

        :param os_version: 操作系统版本
        :type os_version: str (required)

        :param name: 镜像名称,支持大小写字母、数字、中文以及-_ /.特殊字符，必须以字母开头，长度1-65。
        :type name: str (required)

        :param bos_url: bos镜像地址
        :type bos_url: str (required)

        :param detection: detection parameter
        :type detection: bool (optional)

        :param generation_type: 导入的镜像适用于BCC还是EBC，枚举值：BCC、EBC，默认BCC
        :type generation_type: str (optional)
        """
        super().__init__()
        self.os_name = os_name
        self.os_arch = os_arch
        self.os_type = os_type
        self.os_version = os_version
        self.name = name
        self.bos_url = bos_url
        self.detection = detection
        self.generation_type = generation_type

    def to_dict(self):
        """
        Convert the request entity to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the request
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.os_name is not None:
            result['osName'] = self.os_name
        if self.os_arch is not None:
            result['osArch'] = self.os_arch
        if self.os_type is not None:
            result['osType'] = self.os_type
        if self.os_version is not None:
            result['osVersion'] = self.os_version
        if self.name is not None:
            result['name'] = self.name
        if self.bos_url is not None:
            result['bosUrl'] = self.bos_url
        if self.detection is not None:
            result['detection'] = self.detection
        if self.generation_type is not None:
            result['generationType'] = self.generation_type
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: ImportImageRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('osName') is not None:
            self.os_name = m.get('osName')
        if m.get('osArch') is not None:
            self.os_arch = m.get('osArch')
        if m.get('osType') is not None:
            self.os_type = m.get('osType')
        if m.get('osVersion') is not None:
            self.os_version = m.get('osVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('bosUrl') is not None:
            self.bos_url = m.get('bosUrl')
        if m.get('detection') is not None:
            self.detection = m.get('detection')
        if m.get('generationType') is not None:
            self.generation_type = m.get('generationType')
        return self
