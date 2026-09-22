"""
Deploy information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class Deploy(AbstractModel):
    """
    Deploy
    """

    def __init__(
        self,
        scs_instance_count=None,
        scs_instancelds=None,
        name=None,
        strategy=None,
        concurrency=None,
        deploy_set_id=None,
        desc=None,
    ):
        """
        Initialize Deploy instance.

        :param scs_instance_count: 部署集绑定的实例数量。
        :type scs_instance_count: int (optional)

        :param scs_instancelds: 部署集绑定的SCS集群ID列表。
        :type scs_instancelds: List[str] (optional)

        :param name: 部署集名称。
        :type name: str (optional)

        :param strategy: 策略。默认值：HOST_HA。
        :type strategy: str (optional)

        :param concurrency: 并发度。
        :type concurrency: int (optional)

        :param deploy_set_id: 部署集ID。
        :type deploy_set_id: str (optional)

        :param desc: 备注。
        :type desc: str (optional)
        """
        super().__init__()
        self.scs_instance_count = scs_instance_count
        self.scs_instancelds = scs_instancelds
        self.name = name
        self.strategy = strategy
        self.concurrency = concurrency
        self.deploy_set_id = deploy_set_id
        self.desc = desc

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
        if self.scs_instance_count is not None:
            result['scsInstanceCount'] = self.scs_instance_count
        if self.scs_instancelds is not None:
            result['scsInstancelds'] = self.scs_instancelds
        if self.name is not None:
            result['name'] = self.name
        if self.strategy is not None:
            result['strategy'] = self.strategy
        if self.concurrency is not None:
            result['concurrency'] = self.concurrency
        if self.deploy_set_id is not None:
            result['deploySetId'] = self.deploy_set_id
        if self.desc is not None:
            result['desc'] = self.desc
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: Deploy

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('scsInstanceCount') is not None:
            self.scs_instance_count = m.get('scsInstanceCount')
        if m.get('scsInstancelds') is not None:
            self.scs_instancelds = m.get('scsInstancelds')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('strategy') is not None:
            self.strategy = m.get('strategy')
        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')
        if m.get('deploySetId') is not None:
            self.deploy_set_id = m.get('deploySetId')
        if m.get('desc') is not None:
            self.desc = m.get('desc')
        return self
