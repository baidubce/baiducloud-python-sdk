"""
Request entity for CreateParameterTemplateRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_scs.models.parameters import Parameters


class CreateParameterTemplateRequest(AbstractModel):
    """
    Request entity for CreateParameterTemplateRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, name, engine, engine_version, cluster_type, template_type, parameters, comment=None):
        """
        Initialize CreateParameterTemplateRequest request entity.

        :param name: 模板名称，格式要求：大小写字母、数字、中文以及-_/.特殊字符，必须以字母或者中文开头，长度1-65
        :type name: str (required)

        :param engine: 引擎（当前仅支持redis）
        :type engine: str (required)

        :param engine_version: 引擎版本
        :type engine_version: str (required)

        :param cluster_type: 集群类型（master_slave\\cluster）
        :type cluster_type: str (required)

        :param template_type: 模板类型（1、自定义参数模板）
        :type template_type: int (required)

        :param comment: 备注
        :type comment: str (optional)

        :param parameters: 参数列表，系统模版内的数据，和引擎及引擎版本有关
        :type parameters: List[Parameters] (required)
        """
        super().__init__()
        self.name = name
        self.engine = engine
        self.engine_version = engine_version
        self.cluster_type = cluster_type
        self.template_type = template_type
        self.comment = comment
        self.parameters = parameters

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
        if self.name is not None:
            result['name'] = self.name
        if self.engine is not None:
            result['engine'] = self.engine
        if self.engine_version is not None:
            result['engineVersion'] = self.engine_version
        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type
        if self.template_type is not None:
            result['templateType'] = self.template_type
        if self.comment is not None:
            result['comment'] = self.comment
        if self.parameters is not None:
            result['parameters'] = [i.to_dict() for i in self.parameters]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateParameterTemplateRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('engine') is not None:
            self.engine = m.get('engine')
        if m.get('engineVersion') is not None:
            self.engine_version = m.get('engineVersion')
        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')
        if m.get('templateType') is not None:
            self.template_type = m.get('templateType')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('parameters') is not None:
            self.parameters = [Parameters().from_dict(i) for i in m.get('parameters')]
        return self
