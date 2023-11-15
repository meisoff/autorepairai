import requests
from config import regions, RSA_API

def get_price(report_date: str,
               catalog_number: str,
               rf_subject: int):
    # берем название субъекта из нашего справочника
    rf_subject = regions[f"{rf_subject}"]

    # получаем справочник субъектов РФ
    get_rf_subject_ids_result = requests.get(RSA_API['get_rf_subject_ids'].format(report_date))
    subjects = {row['subjectName']: row['subjectRF'] for row in get_rf_subject_ids_result.json()}

    # получаем cписок марок автомобилей
    get_oem_ids_result = requests.get(RSA_API['get_oem_ids'].format(report_date))
    brands = {row['name']: row['id'] for row in get_oem_ids_result.json()}
    car_brand = "ВАЗ.LADA"

    # получаем цены на запчасть
    request_data = {
        'oemId': brands[car_brand],
        'subjectRF': subjects[rf_subject],
        'versionDate': report_date,
        'partNumber1': catalog_number
    }
    get_price_url_result = requests.post(RSA_API['get_price_url'], json=request_data)
    spare_info = get_price_url_result.json()['repairPartDtoList'][0]

    if spare_info['found']:
        return {
            'spare_name': spare_info['spareName'],
            'reg_coef': spare_info['regCoef'],
            'spare_price': spare_info['sparePrice'],
            'base_cost': spare_info['baseCost']
        }
