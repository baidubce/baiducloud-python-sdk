"""
AlarmTarget information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel

from baiducloud_python_sdk_bcm.models.target_instance import TargetInstance

from baiducloud_python_sdk_bcm.models.dimension import Dimension


class AlarmTarget(AbstractModel):
    """
    AlarmTarget
    """

    def __init__(
        self,
        type=None,
        instances=None,
        region=None,
        tags=None,
        instance_groups=None,
        including_dimensions=None,
        excluding_dimensions=None,
    ):
        """
        Initialize AlarmTarget instance.

        :param type: 目标类型，可选值：ALL_INSTANCES / INSTANCES / TAGS / INSTANCE_GROUPS
        :type type: str (optional)

        :param instances: 当type=INSTANCES时必填，报警实例列表
        :type instances: List[TargetInstance] (optional)

        :param region: 当type=INSTANCES时必填，实例所属region
        :type region: str (optional)

        :param tags: 当type=TAGS时必填，报警实例标签列表
        :type tags: List[Dimension] (optional)

        :param instance_groups: 当type=INSTANCE_GROUPS时必填，实例组ID列表
        :type instance_groups: List[str] (optional)

        :param including_dimensions: 必须包含的维度列表
        :type including_dimensions: List[str] (optional)

        :param excluding_dimensions: 必须排除的维度列表
        :type excluding_dimensions: List[str] (optional)
        """
        super().__init__()
        self.type = type
        self.instances = instances
        self.region = region
        self.tags = tags
        self.instance_groups = instance_groups
        self.including_dimensions = including_dimensions
        self.excluding_dimensions = excluding_dimensions

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
        if self.type is not None:
            result['type'] = self.type
        if self.instances is not None:
            result['instances'] = [i.to_dict() for i in self.instances]
        if self.region is not None:
            result['region'] = self.region
        if self.tags is not None:
            result['tags'] = [i.to_dict() for i in self.tags]
        if self.instance_groups is not None:
            result['instanceGroups'] = self.instance_groups
        if self.including_dimensions is not None:
            result['includingDimensions'] = self.including_dimensions
        if self.excluding_dimensions is not None:
            result['excludingDimensions'] = self.excluding_dimensions
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: AlarmTarget

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('instances') is not None:
            self.instances = [TargetInstance().from_dict(i) for i in m.get('instances')]
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('tags') is not None:
            self.tags = [Dimension().from_dict(i) for i in m.get('tags')]
        if m.get('instanceGroups') is not None:
            self.instance_groups = m.get('instanceGroups')
        if m.get('includingDimensions') is not None:
            self.including_dimensions = m.get('includingDimensions')
        if m.get('excludingDimensions') is not None:
            self.excluding_dimensions = m.get('excludingDimensions')
        return self
