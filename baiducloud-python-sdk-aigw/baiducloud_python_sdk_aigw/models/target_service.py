"""
TargetService information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class TargetService(AbstractModel):
    """
    TargetService
    """

    def __init__(
        self,
        service_source=None,
        service_name=None,
        namespace=None,
        service_port=None,
        load_balance_algorithm=None,
        hash_type=None,
        hash_key=None,
        request_ratio=None,
        weight_factor=None,
        model_name=None,
        model_name_mode=None,
        specified_model_name=None,
    ):
        """
        Initialize TargetService instance.

        :param service_source: 服务来源：CCE、FIXED_IP、DNS_DOMAIN、CFC、AI_PROXY
        :type service_source: str (optional)

        :param service_name: 服务名称
        :type service_name: str (optional)

        :param namespace: CCE 服务所在命名空间
        :type namespace: str (optional)

        :param service_port: CCE 服务端口
        :type service_port: int (optional)

        :param load_balance_algorithm: 负载均衡算法
        :type load_balance_algorithm: str (optional)

        :param hash_type: 哈希类型
        :type hash_type: str (optional)

        :param hash_key: 哈希键
        :type hash_key: str (optional)

        :param request_ratio: ratio 策略的请求比例
        :type request_ratio: int (optional)

        :param weight_factor: 动态权重因子
        :type weight_factor: int (optional)

        :param model_name: model_name 策略的模型名称
        :type model_name: str (optional)

        :param model_name_mode: AI_PROXY 模型名称模式
        :type model_name_mode: str (optional)

        :param specified_model_name: AI_PROXY 指定的模型名称
        :type specified_model_name: str (optional)
        """
        super().__init__()
        self.service_source = service_source
        self.service_name = service_name
        self.namespace = namespace
        self.service_port = service_port
        self.load_balance_algorithm = load_balance_algorithm
        self.hash_type = hash_type
        self.hash_key = hash_key
        self.request_ratio = request_ratio
        self.weight_factor = weight_factor
        self.model_name = model_name
        self.model_name_mode = model_name_mode
        self.specified_model_name = specified_model_name

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
        if self.service_source is not None:
            result['serviceSource'] = self.service_source
        if self.service_name is not None:
            result['serviceName'] = self.service_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.service_port is not None:
            result['servicePort'] = self.service_port
        if self.load_balance_algorithm is not None:
            result['loadBalanceAlgorithm'] = self.load_balance_algorithm
        if self.hash_type is not None:
            result['hashType'] = self.hash_type
        if self.hash_key is not None:
            result['hashKey'] = self.hash_key
        if self.request_ratio is not None:
            result['requestRatio'] = self.request_ratio
        if self.weight_factor is not None:
            result['weightFactor'] = self.weight_factor
        if self.model_name is not None:
            result['modelName'] = self.model_name
        if self.model_name_mode is not None:
            result['modelNameMode'] = self.model_name_mode
        if self.specified_model_name is not None:
            result['specifiedModelName'] = self.specified_model_name
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: TargetService

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('serviceSource') is not None:
            self.service_source = m.get('serviceSource')
        if m.get('serviceName') is not None:
            self.service_name = m.get('serviceName')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('servicePort') is not None:
            self.service_port = m.get('servicePort')
        if m.get('loadBalanceAlgorithm') is not None:
            self.load_balance_algorithm = m.get('loadBalanceAlgorithm')
        if m.get('hashType') is not None:
            self.hash_type = m.get('hashType')
        if m.get('hashKey') is not None:
            self.hash_key = m.get('hashKey')
        if m.get('requestRatio') is not None:
            self.request_ratio = m.get('requestRatio')
        if m.get('weightFactor') is not None:
            self.weight_factor = m.get('weightFactor')
        if m.get('modelName') is not None:
            self.model_name = m.get('modelName')
        if m.get('modelNameMode') is not None:
            self.model_name_mode = m.get('modelNameMode')
        if m.get('specifiedModelName') is not None:
            self.specified_model_name = m.get('specifiedModelName')
        return self
