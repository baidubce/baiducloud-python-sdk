"""
Request entity for CreateElasticityAssuranceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_bcc.models.tag_model import TagModel


class CreateElasticityAssuranceRequest(AbstractModel):
    """
    Request entity for CreateElasticityAssuranceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, zone_name, spec, capacity, period, elasticity_assurance_name=None, auto_renew=None, tags=None):
        """
        Initialize CreateElasticityAssuranceRequest request entity.

        :param elasticity_assurance_name: elasticity_assurance_name parameter
        :type elasticity_assurance_name: str (optional)

        :param zone_name: 可用区，例如cn-bj-a
        :type zone_name: str (required)

        :param spec: 弹性保障实例规格，例如bcc.g4.c2m8
        :type spec: str (required)

        :param capacity: 保障数量，最少为1，最大为100
        :type capacity: int (required)

        :param period: 弹性保障购买时长，支持1~9、12、24、36、48、60，单位默认为month，不可变更
        :type period: int (required)

        :param auto_renew: 自动续费开关，默认为false，续费时长与period一致
        :type auto_renew: bool (optional)

        :param tags: 待创建的标签列表
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.elasticity_assurance_name = elasticity_assurance_name
        self.zone_name = zone_name
        self.spec = spec
        self.capacity = capacity
        self.period = period
        self.auto_renew = auto_renew
        self.tags = tags

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
        if self.elasticity_assurance_name is not None:
            result['elasticityAssuranceName'] = self.elasticity_assurance_name
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.spec is not None:
            result['spec'] = self.spec
        if self.capacity is not None:
            result['capacity'] = self.capacity
        if self.period is not None:
            result['period'] = self.period
        if self.auto_renew is not None:
            result['autoRenew'] = self.auto_renew
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CreateElasticityAssuranceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('elasticityAssuranceName') is not None:
            self.elasticity_assurance_name = m.get('elasticityAssuranceName')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('capacity') is not None:
            self.capacity = m.get('capacity')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('autoRenew') is not None:
            self.auto_renew = m.get('autoRenew')
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
