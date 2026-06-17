"""
DeploySetModel information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcc.models.az_intstance_statis_detail import AzIntstanceStatisDetail


class DeploySetModel(AbstractModel):
    """
    DeploySetModel
    """

    def __init__(
        self, deployset_id=None, name=None, desc=None, strategy=None, concurrency=None, az_intstance_statis_list=None
    ):
        """
        Initialize DeploySetModel instance.

        :param deployset_id: 部署集ID
        :type deployset_id: str (optional)

        :param name: 部署集名称
        :type name: str (optional)

        :param desc: 部署集描述
        :type desc: str (optional)

        :param strategy: 部署集策略（HOST_HA/RACK_HA/TOR_HA）
        :type strategy: str (optional)

        :param concurrency: 部署集并发度
        :type concurrency: int (optional)

        :param az_intstance_statis_list: 可用区实例数量统计列表
        :type az_intstance_statis_list: List[AzIntstanceStatisDetail] (optional)
        """
        super().__init__()
        self.deployset_id = deployset_id
        self.name = name
        self.desc = desc
        self.strategy = strategy
        self.concurrency = concurrency
        self.az_intstance_statis_list = az_intstance_statis_list

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
        if self.deployset_id is not None:
            result['deploysetId'] = self.deployset_id
        if self.name is not None:
            result['name'] = self.name
        if self.desc is not None:
            result['desc'] = self.desc
        if self.strategy is not None:
            result['strategy'] = self.strategy
        if self.concurrency is not None:
            result['concurrency'] = self.concurrency
        if self.az_intstance_statis_list is not None:
            result['azIntstanceStatisList'] = [i.to_dict() for i in self.az_intstance_statis_list]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: DeploySetModel

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('deploysetId') is not None:
            self.deployset_id = m.get('deploysetId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        if m.get('strategy') is not None:
            self.strategy = m.get('strategy')
        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')
        if m.get('azIntstanceStatisList') is not None:
            self.az_intstance_statis_list = [
                AzIntstanceStatisDetail().from_dict(i) for i in m.get('azIntstanceStatisList')
            ]
        return self
