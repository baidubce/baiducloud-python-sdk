"""
Request entity for UpdateRelatedCloudProductsRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class UpdateRelatedCloudProductsRequest(AbstractModel):
    """
    Request entity for UpdateRelatedCloudProductsRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(self, instance_id, scopes):
        """
        Initialize UpdateRelatedCloudProductsRequest request entity.

        :param instance_id: instance_id parameter
        :type instance_id: str (required)

        :param scopes: 需要关联的云产品列表。取值可通过接口【获取可关联的 BCM 云产品列表】查询，传空数组或不传则表示清空云产品关联。
        :type scopes: List[str] (required)
        """
        super().__init__()
        self.instance_id = instance_id
        self.scopes = scopes

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
        if self.scopes is not None:
            result['scopes'] = self.scopes
        return result

    def from_dict(self, m):
        """
        Populate the request entity from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing request data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: UpdateRelatedCloudProductsRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('scopes') is not None:
            self.scopes = m.get('scopes')
        return self
