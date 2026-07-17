"""
Request entity for UpdateActionRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_cloudassistant.models.action import Action
from baiducloud_python_sdk_cloudassistant.models.target import Target
from baiducloud_python_sdk_cloudassistant.models.target_selector import TargetSelector


class UpdateActionRequest(AbstractModel):
    """
    Request entity for UpdateActionRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, execution, action, parameters=None, target_selector_type=None, targets=None, target_selector=None
    ):
        """
        Initialize UpdateActionRequest request entity.

        :param execution: 执行动作。SAVE(仅保存），RUN（仅执行），SAVE_AND_RUN（保存并执行）
        :type execution: str (required)

        :param action: action parameter
        :type action: Action (required)

        :param parameters: 执行命令时的参数值，仅在命令有参数时需要
        :type parameters: Dict[str, str] (optional)

        :param target_selector_type: target_selector_type parameter
        :type target_selector_type: str (optional)

        :param targets: 实例ID列表，仅在targetSelectorType为INSTANCES_LIST时需要
        :type targets: List[Target] (optional)

        :param target_selector: target_selector parameter
        :type target_selector: TargetSelector (optional)
        """
        super().__init__()
        self.execution = execution
        self.action = action
        self.parameters = parameters
        self.target_selector_type = target_selector_type
        self.targets = targets
        self.target_selector = target_selector

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
        if self.execution is not None:
            result['execution'] = self.execution
        if self.action is not None:
            result['action'] = self.action.to_dict()
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.target_selector_type is not None:
            result['targetSelectorType'] = self.target_selector_type
        if self.targets is not None:
            result['targets'] = [i.to_dict() for i in self.targets]
        if self.target_selector is not None:
            result['targetSelector'] = self.target_selector.to_dict()
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateActionRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('execution') is not None:
            self.execution = m.get('execution')
        if m.get('action') is not None:
            self.action = Action().from_dict(m.get('action'))
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('targetSelectorType') is not None:
            self.target_selector_type = m.get('targetSelectorType')
        if m.get('targets') is not None:
            self.targets = [Target().from_dict(i) for i in m.get('targets')]
        if m.get('targetSelector') is not None:
            self.target_selector = TargetSelector().from_dict(m.get('targetSelector'))
        return self
