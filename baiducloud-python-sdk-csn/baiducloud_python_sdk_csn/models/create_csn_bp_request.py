"""
Request entity for CreateCsnBpRequest information.
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel
from baiducloud_python_sdk_csn.models.billing import Billing
from baiducloud_python_sdk_csn.models.tag_model import TagModel


class CreateCsnBpRequest(AbstractModel):
    """
    Request entity for CreateCsnBpRequest operation.

    This class encapsulates all parameters for the API request.
    """

    def __init__(
        self, name, bandwidth, geographic_a, geographic_b, billing, client_token=None, interwork_type=None, tags=None
    ):
        """
        Initialize CreateCsnBpRequest request entity.

        :param client_token: client_token parameter
        :type client_token: str (optional)

        :param name: 带宽包的名称，不能为空
        :type name: str (required)

        :param interwork_type: interwork_type parameter
        :type interwork_type: str (optional)

        :param bandwidth: 带宽包的带宽值，最大值为10000
        :type bandwidth: int (required)

        :param geographic_a: 网络实例所属的区域。取值 [ China \\| Asia-Pacific ]，分别表示中国大陆、亚太区域
        :type geographic_a: str (required)

        :param geographic_b: 另一个网络实例所属的区域。取值 [ China \\| Asia-Pacific ]，分别表示中国大陆、亚太区域
        :type geographic_b: str (required)

        :param billing: billing parameter
        :type billing: Billing (required)

        :param tags: 待创建的标签键值对列表
        :type tags: List[TagModel] (optional)
        """
        super().__init__()
        self.client_token = client_token
        self.name = name
        self.interwork_type = interwork_type
        self.bandwidth = bandwidth
        self.geographic_a = geographic_a
        self.geographic_b = geographic_b
        self.billing = billing
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
        if self.name is not None:
            result['name'] = self.name
        if self.interwork_type is not None:
            result['interworkType'] = self.interwork_type
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        if self.geographic_a is not None:
            result['geographicA'] = self.geographic_a
        if self.geographic_b is not None:
            result['geographicB'] = self.geographic_b
        if self.billing is not None:
            result['billing'] = self.billing.to_dict()
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
        :rtype: CreateCsnBpRequest

        :raises TypeError: If input is not a dictionary or field type mismatch
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('interworkType') is not None:
            self.interwork_type = m.get('interworkType')
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        if m.get('geographicA') is not None:
            self.geographic_a = m.get('geographicA')
        if m.get('geographicB') is not None:
            self.geographic_b = m.get('geographicB')
        if m.get('billing') is not None:
            self.billing = Billing().from_dict(m.get('billing'))
        if m.get('tags') is not None:
            self.tags = [TagModel().from_dict(i) for i in m.get('tags')]
        return self
