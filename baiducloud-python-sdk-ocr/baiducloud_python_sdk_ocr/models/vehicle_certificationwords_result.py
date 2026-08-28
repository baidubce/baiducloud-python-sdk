"""
VehicleCertificationwordsResult information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class VehicleCertificationwordsResult(AbstractModel):
    """
    VehicleCertificationwordsResult
    """

    def __init__(
        self,
        certification_no=None,
        certificate_date=None,
        manufacturer=None,
        car_brand=None,
        car_name=None,
        car_model=None,
        vin_no=None,
        car_color=None,
        engine_type=None,
        engine_no=None,
        fuel_type=None,
        displacement=None,
        power=None,
        emission_standard=None,
        tyre_num=None,
        wheelbase=None,
        axle_num=None,
        steering_type=None,
        total_weight=None,
        saddle_mass=None,
        limit_passenger=None,
        speed_limit=None,
        manufacture_date=None,
        chassis_id=None,
        chassis_model=None,
        seating_capacity=None,
        qualify_seal=None,
        cgs_seal=None,
    ):
        """
        Initialize VehicleCertificationwordsResult instance.

        :param certification_no: 合格证编号
        :type certification_no: str (optional)

        :param certificate_date: 发证日期
        :type certificate_date: str (optional)

        :param manufacturer: 车辆制造企业名
        :type manufacturer: str (optional)

        :param car_brand: 车辆品牌
        :type car_brand: str (optional)

        :param car_name: 车辆名称
        :type car_name: str (optional)

        :param car_model: 车辆型号
        :type car_model: str (optional)

        :param vin_no: 车架号
        :type vin_no: str (optional)

        :param car_color: 车身颜色
        :type car_color: str (optional)

        :param engine_type: 发动机型号
        :type engine_type: str (optional)

        :param engine_no: 发动机号
        :type engine_no: str (optional)

        :param fuel_type: 燃料种类
        :type fuel_type: str (optional)

        :param displacement: 排量
        :type displacement: str (optional)

        :param power: 功率
        :type power: str (optional)

        :param emission_standard: 排放标准
        :type emission_standard: str (optional)

        :param tyre_num: 轮胎数
        :type tyre_num: str (optional)

        :param wheelbase: 轴距
        :type wheelbase: str (optional)

        :param axle_num: 轴数
        :type axle_num: str (optional)

        :param steering_type: 转向形式
        :type steering_type: str (optional)

        :param total_weight: 总质量
        :type total_weight: str (optional)

        :param saddle_mass: 整备质量
        :type saddle_mass: str (optional)

        :param limit_passenger: 驾驶室准乘人数
        :type limit_passenger: str (optional)

        :param speed_limit: 最高设计车速
        :type speed_limit: str (optional)

        :param manufacture_date: 车辆制造日期
        :type manufacture_date: str (optional)

        :param chassis_id: 底盘ID
        :type chassis_id: str (optional)

        :param chassis_model: 底盘型号
        :type chassis_model: str (optional)

        :param seating_capacity: 额定载客人数
        :type seating_capacity: str (optional)

        :param qualify_seal: 合格印章：1表示有，0表示无
        :type qualify_seal: str (optional)

        :param cgs_seal: CGS印章：1表示有，0表示无
        :type cgs_seal: str (optional)
        """
        super().__init__()
        self.certification_no = certification_no
        self.certificate_date = certificate_date
        self.manufacturer = manufacturer
        self.car_brand = car_brand
        self.car_name = car_name
        self.car_model = car_model
        self.vin_no = vin_no
        self.car_color = car_color
        self.engine_type = engine_type
        self.engine_no = engine_no
        self.fuel_type = fuel_type
        self.displacement = displacement
        self.power = power
        self.emission_standard = emission_standard
        self.tyre_num = tyre_num
        self.wheelbase = wheelbase
        self.axle_num = axle_num
        self.steering_type = steering_type
        self.total_weight = total_weight
        self.saddle_mass = saddle_mass
        self.limit_passenger = limit_passenger
        self.speed_limit = speed_limit
        self.manufacture_date = manufacture_date
        self.chassis_id = chassis_id
        self.chassis_model = chassis_model
        self.seating_capacity = seating_capacity
        self.qualify_seal = qualify_seal
        self.cgs_seal = cgs_seal

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
        if self.certification_no is not None:
            result['CertificationNo'] = self.certification_no
        if self.certificate_date is not None:
            result['CertificateDate'] = self.certificate_date
        if self.manufacturer is not None:
            result['Manufacturer'] = self.manufacturer
        if self.car_brand is not None:
            result['CarBrand'] = self.car_brand
        if self.car_name is not None:
            result['CarName'] = self.car_name
        if self.car_model is not None:
            result['CarModel'] = self.car_model
        if self.vin_no is not None:
            result['VinNo'] = self.vin_no
        if self.car_color is not None:
            result['CarColor'] = self.car_color
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type
        if self.engine_no is not None:
            result['EngineNo'] = self.engine_no
        if self.fuel_type is not None:
            result['FuelType'] = self.fuel_type
        if self.displacement is not None:
            result['Displacement'] = self.displacement
        if self.power is not None:
            result['Power'] = self.power
        if self.emission_standard is not None:
            result['EmissionStandard'] = self.emission_standard
        if self.tyre_num is not None:
            result['TyreNum'] = self.tyre_num
        if self.wheelbase is not None:
            result['Wheelbase'] = self.wheelbase
        if self.axle_num is not None:
            result['AxleNum'] = self.axle_num
        if self.steering_type is not None:
            result['SteeringType'] = self.steering_type
        if self.total_weight is not None:
            result['TotalWeight'] = self.total_weight
        if self.saddle_mass is not None:
            result['SaddleMass'] = self.saddle_mass
        if self.limit_passenger is not None:
            result['LimitPassenger'] = self.limit_passenger
        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit
        if self.manufacture_date is not None:
            result['ManufactureDate'] = self.manufacture_date
        if self.chassis_id is not None:
            result['ChassisID'] = self.chassis_id
        if self.chassis_model is not None:
            result['ChassisModel'] = self.chassis_model
        if self.seating_capacity is not None:
            result['SeatingCapacity'] = self.seating_capacity
        if self.qualify_seal is not None:
            result['QualifySeal'] = self.qualify_seal
        if self.cgs_seal is not None:
            result['CGSSeal'] = self.cgs_seal
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: VehicleCertificationwordsResult

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('CertificationNo') is not None:
            self.certification_no = m.get('CertificationNo')
        if m.get('CertificateDate') is not None:
            self.certificate_date = m.get('CertificateDate')
        if m.get('Manufacturer') is not None:
            self.manufacturer = m.get('Manufacturer')
        if m.get('CarBrand') is not None:
            self.car_brand = m.get('CarBrand')
        if m.get('CarName') is not None:
            self.car_name = m.get('CarName')
        if m.get('CarModel') is not None:
            self.car_model = m.get('CarModel')
        if m.get('VinNo') is not None:
            self.vin_no = m.get('VinNo')
        if m.get('CarColor') is not None:
            self.car_color = m.get('CarColor')
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')
        if m.get('EngineNo') is not None:
            self.engine_no = m.get('EngineNo')
        if m.get('FuelType') is not None:
            self.fuel_type = m.get('FuelType')
        if m.get('Displacement') is not None:
            self.displacement = m.get('Displacement')
        if m.get('Power') is not None:
            self.power = m.get('Power')
        if m.get('EmissionStandard') is not None:
            self.emission_standard = m.get('EmissionStandard')
        if m.get('TyreNum') is not None:
            self.tyre_num = m.get('TyreNum')
        if m.get('Wheelbase') is not None:
            self.wheelbase = m.get('Wheelbase')
        if m.get('AxleNum') is not None:
            self.axle_num = m.get('AxleNum')
        if m.get('SteeringType') is not None:
            self.steering_type = m.get('SteeringType')
        if m.get('TotalWeight') is not None:
            self.total_weight = m.get('TotalWeight')
        if m.get('SaddleMass') is not None:
            self.saddle_mass = m.get('SaddleMass')
        if m.get('LimitPassenger') is not None:
            self.limit_passenger = m.get('LimitPassenger')
        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')
        if m.get('ManufactureDate') is not None:
            self.manufacture_date = m.get('ManufactureDate')
        if m.get('ChassisID') is not None:
            self.chassis_id = m.get('ChassisID')
        if m.get('ChassisModel') is not None:
            self.chassis_model = m.get('ChassisModel')
        if m.get('SeatingCapacity') is not None:
            self.seating_capacity = m.get('SeatingCapacity')
        if m.get('QualifySeal') is not None:
            self.qualify_seal = m.get('QualifySeal')
        if m.get('CGSSeal') is not None:
            self.cgs_seal = m.get('CGSSeal')
        return self
