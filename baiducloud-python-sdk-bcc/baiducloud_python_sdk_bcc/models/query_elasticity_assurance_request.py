"""
Request entity for QueryElasticityAssuranceRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class QueryElasticityAssuranceRequest(AbstractModel):
    """
    Request entity for QueryElasticityAssuranceRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self,
        marker=None,
        max_keys=None,
        elasticity_assurance_ids=None,
        elasticity_assurance_name=None,
        zone_name=None,
        spec=None,
        status=None,
    ):
        """
        Initialize QueryElasticityAssuranceRequest request entity.

        :param marker: 批量获取列表的查询的起始位置，是一个由系统生成的字符串
        :type marker: str (optional)

        :param max_keys: 每页包含的最大数量，最大数量通常不超过1000，缺省值为1000
        :type max_keys: int (optional)

        :param elasticity_assurance_ids: 弹性保障的id集合
        :type elasticity_assurance_ids: List[str] (optional)

        :param elasticity_assurance_name: 弹性保障的名称
        :type elasticity_assurance_name: str (optional)

        :param zone_name: 可用区，例如：cn-bj-a
        :type zone_name: str (optional)

        :param spec: 实例规格，例如：bcc.g4.c2m8
        :type spec: str (optional)

        :param status: 弹性保障状态,可选值：CREATING/ACTIVE
        :type status: List[str] (optional)
        """
        super().__init__()
        self.marker = marker
        self.max_keys = max_keys
        self.elasticity_assurance_ids = elasticity_assurance_ids
        self.elasticity_assurance_name = elasticity_assurance_name
        self.zone_name = zone_name
        self.spec = spec
        self.status = status

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
        if self.marker is not None:
            result['marker'] = self.marker
        if self.max_keys is not None:
            result['maxKeys'] = self.max_keys
        if self.elasticity_assurance_ids is not None:
            result['elasticityAssuranceIds'] = self.elasticity_assurance_ids
        if self.elasticity_assurance_name is not None:
            result['elasticityAssuranceName'] = self.elasticity_assurance_name
        if self.zone_name is not None:
            result['zoneName'] = self.zone_name
        if self.spec is not None:
            result['spec'] = self.spec
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: QueryElasticityAssuranceRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('maxKeys') is not None:
            self.max_keys = m.get('maxKeys')
        if m.get('elasticityAssuranceIds') is not None:
            self.elasticity_assurance_ids = m.get('elasticityAssuranceIds')
        if m.get('elasticityAssuranceName') is not None:
            self.elasticity_assurance_name = m.get('elasticityAssuranceName')
        if m.get('zoneName') is not None:
            self.zone_name = m.get('zoneName')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
