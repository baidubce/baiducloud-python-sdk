"""
CsnRtAssociation information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class CsnRtAssociation(AbstractModel):
    """
    CsnRtAssociation
    """

    def __init__(
        self,
        attach_id=None,
        description=None,
        instance_id=None,
        instance_name=None,
        instance_region=None,
        instance_type=None,
        status=None,
    ):
        """
        Initialize CsnRtAssociation instance.

        :param attach_id: 网络实例在云智能网中的身份ID
        :type attach_id: str (optional)

        :param description: 关联关系的描述信息
        :type description: str (optional)

        :param instance_id: 网络实例的ID
        :type instance_id: str (optional)

        :param instance_name: 网络实例的名称
        :type instance_name: str (optional)

        :param instance_region: 网络实例所属region
        :type instance_region: str (optional)

        :param instance_type: 网络实例类型，取值 [ vpc \\| channel \\| bec_vpc ]
        :type instance_type: str (optional)

        :param status: 关联关系的状态
        :type status: str (optional)
        """
        super().__init__()
        self.attach_id = attach_id
        self.description = description
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_region = instance_region
        self.instance_type = instance_type
        self.status = status

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
        if self.attach_id is not None:
            result['attachId'] = self.attach_id
        if self.description is not None:
            result['description'] = self.description
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.instance_name is not None:
            result['instanceName'] = self.instance_name
        if self.instance_region is not None:
            result['instanceRegion'] = self.instance_region
        if self.instance_type is not None:
            result['instanceType'] = self.instance_type
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: CsnRtAssociation

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('attachId') is not None:
            self.attach_id = m.get('attachId')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')
        if m.get('instanceRegion') is not None:
            self.instance_region = m.get('instanceRegion')
        if m.get('instanceType') is not None:
            self.instance_type = m.get('instanceType')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self
