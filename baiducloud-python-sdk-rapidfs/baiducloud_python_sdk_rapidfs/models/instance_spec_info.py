"""
InstanceSpecInfo information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_rapidfs.models.stock_info import StockInfo


class InstanceSpecInfo(AbstractModel):
    """
    InstanceSpecInfo
    """

    def __init__(
        self,
        managed_mode=None,
        meta_spec=None,
        data_spec=None,
        min_capacity_ti_b=None,
        step_capacity_ti_b=None,
        max_capacity_ti_b=None,
        stock_infos=None,
    ):
        """
        Initialize InstanceSpecInfo instance.

        :param managed_mode: managed_mode attribute
        :type managed_mode: str (optional)

        :param meta_spec: meta_spec attribute
        :type meta_spec: str (optional)

        :param data_spec: data_spec attribute
        :type data_spec: str (optional)

        :param min_capacity_ti_b: 全部署模式下，某个数据规格的最小缓存容量，单位 TiB
        :type min_capacity_ti_b: int (optional)

        :param step_capacity_ti_b: 全部署模式下，某个数据规格的缓存步长容量，单位 TiB
        :type step_capacity_ti_b: int (optional)

        :param max_capacity_ti_b: 全部署模式下，某个数据规格的最大缓存容量，单位 TiB
        :type max_capacity_ti_b: int (optional)

        :param stock_infos: 可购容量信息，见StockInfo
        :type stock_infos: List[StockInfo] (optional)
        """
        super().__init__()
        self.managed_mode = managed_mode
        self.meta_spec = meta_spec
        self.data_spec = data_spec
        self.min_capacity_ti_b = min_capacity_ti_b
        self.step_capacity_ti_b = step_capacity_ti_b
        self.max_capacity_ti_b = max_capacity_ti_b
        self.stock_infos = stock_infos

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
        if self.managed_mode is not None:
            result['managedMode'] = self.managed_mode
        if self.meta_spec is not None:
            result['metaSpec'] = self.meta_spec
        if self.data_spec is not None:
            result['dataSpec'] = self.data_spec
        if self.min_capacity_ti_b is not None:
            result['minCapacityTiB'] = self.min_capacity_ti_b
        if self.step_capacity_ti_b is not None:
            result['stepCapacityTiB'] = self.step_capacity_ti_b
        if self.max_capacity_ti_b is not None:
            result['maxCapacityTiB'] = self.max_capacity_ti_b
        if self.stock_infos is not None:
            result['stockInfos'] = [i.to_dict() for i in self.stock_infos]
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: InstanceSpecInfo

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('managedMode') is not None:
            self.managed_mode = m.get('managedMode')
        if m.get('metaSpec') is not None:
            self.meta_spec = m.get('metaSpec')
        if m.get('dataSpec') is not None:
            self.data_spec = m.get('dataSpec')
        if m.get('minCapacityTiB') is not None:
            self.min_capacity_ti_b = m.get('minCapacityTiB')
        if m.get('stepCapacityTiB') is not None:
            self.step_capacity_ti_b = m.get('stepCapacityTiB')
        if m.get('maxCapacityTiB') is not None:
            self.max_capacity_ti_b = m.get('maxCapacityTiB')
        if m.get('stockInfos') is not None:
            self.stock_infos = [StockInfo().from_dict(i) for i in m.get('stockInfos')]
        return self
