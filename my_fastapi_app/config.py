RSA_API = {
    'get_rf_subject_ids':
        'https://prices.autoins.ru/priceAutoPublicCheck/api/rf_subject/date?versionDate={}',
    'get_oem_ids':
        'https://prices.autoins.ru/priceAutoPublicCheck/api/oem/date?versionDate={}',
    'get_price_url':
        'https://prices.autoins.ru/priceAutoPublicCheck/api/spareprice'
}

regions = {'0': 'Москва', '1': 'Московская область', '2': 'Санкт-Петербург', '3': 'Ленинградская область',
           '4': 'Республика Адыгея', '5': 'Республика Алтай', '6': 'Алтайский край', '7': 'Амурская область',
           '8': 'Архангельская область', '9': 'Астраханская область', '10': 'Белгородская область',
           '11': 'Брянская область', '12': 'Владимирская область', '13': 'Волгоградская область',
           '14': 'Вологодская область', '15': 'Воронежская область', '16': 'Еврейская автономная область',
           '17': 'Ивановская область', '18': 'Иркутская область', '19': 'Кабардино-Балкарская Республика',
           '20': 'Калининградская область', '21': 'Калужская область', '22': 'Камчатский край',
           '23': 'Карачаево-Черкесская Республика', '24': 'Кемеровская область', '25': 'Кировская область',
           '26': 'Костромская область', '27': 'Краснодарский край', '28': 'Красноярский край',
           '29': 'Курганская область', '30': 'Курская область', '31': 'Липецкая область', '32': 'Магаданская область',
           '33': 'Мурманская область', '34': 'Ненецкий автономный округ', '35': 'Нижегородская область',
           '36': 'Новгородская область', '37': 'Новосибирская область', '38': 'Омская область',
           '39': 'Оренбургская область', '40': 'Орловская область', '41': 'Пензенская область', '42': 'Пермский край',
           '43': 'Приморский край', '44': 'Псковская область', '45': 'Республика Башкортостан',
           '46': 'Республика Бурятия', '47': 'Республика Ингушетия', '48': 'Республика Дагестан',
           '49': 'Республика Калмыкия', '50': 'Республика Карелия', '51': 'Республика Коми',
           '52': 'Республика Марий Эл', '53': 'Республика Мордовия', '54': 'Республика Саха (Якутия)',
           '55': 'Республика Северная Осетия-Алания', '56': 'Республика Татарстан', '57': 'Республика Тыва',
           '58': 'Республика Хакасия', '59': 'Ростовская область', '60': 'Рязанская область', '61': 'Самарская область',
           '62': 'Саратов', '63': 'Саратовская область', '64': 'Сахалинская область', '65': 'Свердловская область',
           '66': 'Смоленская область', '67': 'Ставропольский край', '68': 'Тамбовская область',
           '69': 'Тверская область', '70': 'Томская область', '71': 'Тульская область', '72': 'Тюменская область',
           '73': 'Удмуртская Республика', '74': 'Хабаровский край', '75': 'Ханты-Мансийский автономный округ-Югра',
           '76': 'Челябинская область', '77': 'Забайкальский край', '78': 'Чувашская Республика',
           '79': 'Чукотский автономный округ', '80': 'Ямало-Ненецкий автономный округ', '81': 'Ярославская область',
           '82': 'Чеченская Республика', '83': 'Ульяновская область', '84': 'Севастополь', '85': 'Республика Крым'}

for_parsing = {
   "granta":{
      "damaged door":{
         "Дверь передняя правая":"11180-8212324-00",
         "Дверь передняя левая":"11180-8212325-00",
         "Дверь задняя правая":"11180-8212326-00",
         "Дверь задняя левая":"11180-8212327-00"
      },
      "damaged window":{
         "Стекло переднее правое":"11180-6103200-25",
         "Стекло переднее левое":"11180-6103201-25",
         "Стекло заднее правое":"11180-6203200-15",
         "Стекло заднее левое":"11180-6203201-15"
      },
      "damaged headlight":{
         "Фара правая":"21910-2803196-00",
         "Фара левая":"21910-2803197-00"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"21902-6102010-00"
      },
      "damaged hood":{
         "Капот":"21070-8402108-00"
      },
      "damaged bumper":{
         "Бампер":"21900-2804038-00"
      },
      "damaged wind shield":{
         "Стекло ветровое":"21900-5206012-05"
      }
   },
   "largus":{
      "damaged door":{
         "Дверь передняя правая":"801002133R",
         "Дверь передняя левая":"801013696R",
         "Дверь задняя правая":"821001782R",
         "Дверь задняя левая":"821010234R"
      },
      "damaged window":{
         "Стекло переднее правое":"6001547002",
         "Стекло переднее левое":"6001547003",
         "Стекло заднее правое":"8200396108",
         "Стекло заднее левое":"8200396082"
      },
      "damaged headlight":{
         "Фара правая":"8450000252",
         "Фара левая":"8450000253"
      },
      "damaged mirror":{
         "Левое зеркало":"8200815704",
         "Правое зеркало":"8200815703"
      },
      "damaged hood":{
         "Капот":"6001546685"
      },
      "damaged bumper":{
         "Бампер":"8450000244"
      },
      "damaged wind shield":{
         "Стекло ветровое":"8200211045"
      }
   },
   "priora":{
      "damaged door":{
         "Дверь передняя правая":"21100-6100014-20",
         "Дверь передняя левая":"21100-6100015-20",
         "Дверь задняя правая":"21100-6200014-00",
         "Дверь задняя левая":"21100-6200015-00"
      },
      "damaged window":{
         "Стекло переднее правое":"None",
         "Стекло переднее левое":"None",
         "Стекло заднее правое":"21710-6204010-00",
         "Стекло заднее левое":"None"
      },
      "damaged headlight":{
         "Фара правая":"21720-8404412-00",
         "Фара левая":"21720-8404413-00"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"21700-8402010-00"
      },
      "damaged bumper":{
         "Бампер":"21704-2803056-10"
      },
      "damaged wind shield":{
         "Стекло ветровое":"21700-5206010-15"
      }
   },
   "kalina":{
      "damaged door":{
         "Дверь передняя правая":"11180-8212324-00",
         "Дверь передняя левая":"11180-8212325-00",
         "Дверь задняя правая":"11180-8212326-00",
         "Дверь задняя левая":"11180-8212327-00"
      },
      "damaged window":{
         "Стекло переднее правое":"11180-6103200-15",
         "Стекло переднее левое":"11180-6103201-15",
         "Стекло заднее правое":"11170-6203292-01",
         "Стекло заднее левое":"11170-6203293-01"
      },
      "damaged headlight":{
         "Фара правая":"21900-8403512-00",
         "Фара левая":"21900-8403513-00"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"11180-8407128-00"
      },
      "damaged bumper":{
         "Бампер":"21940-2804039-00"
      },
      "damaged wind shield":{
         "Стекло ветровое":"21900-5206012-05"
      }
   },
   "lada 4x4":{
      "damaged door":{
         "Дверь передняя правая":"21310-6100015-10",
         "Дверь передняя левая":"21214-6100031-20",
         "Дверь задняя правая":"21310-6200014-00",
         "Дверь задняя левая":"21310-6200015-00"
      },
      "damaged window":{
         "Стекло переднее правое":"None",
         "Стекло переднее левое":"None",
         "Стекло заднее правое":"None",
         "Стекло заднее левое":"21310-6204021-00"
      },
      "damaged headlight":{
         "Фара правая":"21210-8404314-00",
         "Фара левая":"21210-8404315-00"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"21213-8402012-00"
      },
      "damaged bumper":{
         "Бампер":"21210-2804037-10"
      },
      "damaged wind shield":{
         "Стекло ветровое":"21210-5206010-20"
      }
   },
   "ваз-21213-214i (niva)":{
      "damaged door":{
         "Дверь передняя правая":"None",
         "Дверь передняя левая":"None",
         "Дверь задняя правая":"None",
         "Дверь задняя левая":"None"
      },
      "damaged window":{
         "Стекло переднее правое":"None",
         "Стекло переднее левое":"None",
         "Стекло заднее правое":"None",
         "Стекло заднее левое":"None"
      },
      "damaged headlight":{
         "Фара правая":"None",
         "Фара левая":"None"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"None"
      },
      "damaged bumper":{
         "Бампер":"None"
      },
      "damaged wind shield":{
         "Стекло ветровое":"None"
      }
   },
   "ваз-21213 (niva)":{
      "damaged door":{
         "Дверь передняя правая":"None",
         "Дверь передняя левая":"None",
         "Дверь задняя правая":"None",
         "Дверь задняя левая":"None"
      },
      "damaged window":{
         "Стекло переднее правое":"None",
         "Стекло переднее левое":"None",
         "Стекло заднее правое":"None",
         "Стекло заднее левое":"None"
      },
      "damaged headlight":{
         "Фара правая":"None",
         "Фара левая":"None"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"None"
      },
      "damaged bumper":{
         "Бампер":"None"
      },
      "damaged wind shield":{
         "Стекло ветровое":"None"
      }
   },
   "ваз-2131 (niva)":{
      "damaged door":{
         "Дверь передняя правая":"None",
         "Дверь передняя левая":"None",
         "Дверь задняя правая":"None",
         "Дверь задняя левая":"None"
      },
      "damaged window":{
         "Стекло переднее правое":"None",
         "Стекло переднее левое":"None",
         "Стекло заднее правое":"None",
         "Стекло заднее левое":"None"
      },
      "damaged headlight":{
         "Фара правая":"None",
         "Фара левая":"None"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"None"
      },
      "damaged bumper":{
         "Бампер":"None"
      },
      "damaged wind shield":{
         "Стекло ветровое":"None"
      }
   },
   "ваз-2121 (niva)":{
      "damaged door":{
         "Дверь передняя правая":"None",
         "Дверь передняя левая":"None",
         "Дверь задняя правая":"None",
         "Дверь задняя левая":"None"
      },
      "damaged window":{
         "Стекло переднее правое":"None",
         "Стекло переднее левое":"None",
         "Стекло заднее правое":"None",
         "Стекло заднее левое":"None"
      },
      "damaged headlight":{
         "Фара правая":"None",
         "Фара левая":"None"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"None"
      },
      "damaged bumper":{
         "Бампер":"None"
      },
      "damaged wind shield":{
         "Стекло ветровое":"None"
      }
   },
   "ваз-2120 (надежда)":{
      "damaged door":{
         "Дверь передняя правая":"None",
         "Дверь передняя левая":"None",
         "Дверь задняя правая":"None",
         "Дверь задняя левая":"None"
      },
      "damaged window":{
         "Стекло переднее правое":"None",
         "Стекло переднее левое":"None",
         "Стекло заднее правое":"None",
         "Стекло заднее левое":"None"
      },
      "damaged headlight":{
         "Фара правая":"None",
         "Фара левая":"None"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"None"
      },
      "damaged bumper":{
         "Бампер":"None"
      },
      "damaged wind shield":{
         "Стекло ветровое":"None"
      }
   },
   "vesta":{
      "damaged door":{
         "Дверь передняя правая":"8450039385",
         "Дверь передняя левая":"8450039379",
         "Дверь задняя правая":"8450008081",
         "Дверь задняя левая":"8450008082"
      },
      "damaged window":{
         "Стекло переднее правое":"8450007730",
         "Стекло переднее левое":"8450007731",
         "Стекло заднее правое":"8450039391",
         "Стекло заднее левое":"8450039390"
      },
      "damaged headlight":{
         "Фара правая":"8450008252",
         "Фара левая":"8450008253"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"8450039378"
      },
      "damaged bumper":{
         "Бампер":"8450006704"
      },
      "damaged wind shield":{
         "Стекло ветровое":"8450007323"
      }
   },
   "ваз-1111 \"ока\"":{
      "damaged door":{
         "Дверь передняя правая":"1111-6100014",
         "Дверь передняя левая":"1111-6100015",
         "Дверь задняя правая":"None",
         "Дверь задняя левая":"None"
      },
      "damaged window":{
         "Стекло переднее правое":"None",
         "Стекло переднее левое":"None",
         "Стекло заднее правое":"None",
         "Стекло заднее левое":"None"
      },
      "damaged headlight":{
         "Фара правая":"1111-8401426",
         "Фара левая":"1111-8401427"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"1111-8407016"
      },
      "damaged bumper":{
         "Бампер":"1111-2803018"
      },
      "damaged wind shield":{
         "Стекло ветровое":"1111-5206016"
      }
   },
   "niva":{
      "damaged door":{
         "Дверь передняя правая":"21230-6100014-00-0",
         "Дверь передняя левая":"21230-6100015-00-0",
         "Дверь задняя правая":"21230-6200014-00-0",
         "Дверь задняя левая":"21230-6200015-00-0"
      },
      "damaged window":{
         "Стекло переднее правое":"21230-6104010-00",
         "Стекло переднее левое":"21230-6104011-00",
         "Стекло заднее правое":"21230-6204010-00-0",
         "Стекло заднее левое":"21230-6204011-00-0"
      },
      "damaged headlight":{
         "Фара правая":"21230-8401112-01-0",
         "Фара левая":"21230-8401113-01-0"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"21230-8406070-00-0"
      },
      "damaged bumper":{
         "Бампер":"21230-2803134-00-0"
      },
      "damaged wind shield":{
         "Стекло ветровое":"21230-5206016-00-0"
      }
   },
   "2123":{
      "damaged door":{
         "Дверь передняя правая":"21230-6100020-75",
         "Дверь передняя левая":"21230-6100021-75",
         "Дверь задняя правая":"21230-6200020-75",
         "Дверь задняя левая":"21230-6200021-75"
      },
      "damaged window":{
         "Стекло переднее правое":"21230-6104010-00",
         "Стекло переднее левое":"21230-6104011-00",
         "Стекло заднее правое":"21230-6204010-00",
         "Стекло заднее левое":"21230-6204011-00"
      },
      "damaged headlight":{
         "Фара правая":"2123-8401112",
         "Фара левая":"2123-8401113"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"21230-8402010-70"
      },
      "damaged bumper":{
         "Бампер":"21230-2803134-00"
      },
      "damaged wind shield":{
         "Стекло ветровое":"21230-5206016-11"
      }
   },
   "vis":{
      "damaged door":{
         "Дверь передняя правая":"None",
         "Дверь передняя левая":"None",
         "Дверь задняя правая":"None",
         "Дверь задняя левая":"None"
      },
      "damaged window":{
         "Стекло переднее правое":"None",
         "Стекло переднее левое":"None",
         "Стекло заднее правое":"None",
         "Стекло заднее левое":"None"
      },
      "damaged headlight":{
         "Фара правая":"None",
         "Фара левая":"None"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"None"
      },
      "damaged bumper":{
         "Бампер":"None"
      },
      "damaged wind shield":{
         "Стекло ветровое":"None"
      }
   },
   "21214":{
      "damaged door":{
         "Дверь передняя правая":"21214-6100030-42",
         "Дверь передняя левая":"21214-6100031-44",
         "Дверь задняя правая":"21213-5601108-10",
         "Дверь задняя левая":"21317-6200015-12"
      },
      "damaged window":{
         "Стекло переднее правое":"21214-6103214-00",
         "Стекло переднее левое":"21214-6103215-00",
         "Стекло заднее правое":"None",
         "Стекло заднее левое":"21310-6204021-00"
      },
      "damaged headlight":{
         "Фара правая":"8450107440",
         "Фара левая":"8450107441"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"8450107440"
      },
      "damaged bumper":{
         "Бампер":"8450107432"
      },
      "damaged wind shield":{
         "Стекло ветровое":"21217-5206008-01"
      }
   },
   "21310":{
      "damaged door":{
         "Дверь передняя правая":"21214-6100030-42",
         "Дверь передняя левая":"21214-6100031-44",
         "Дверь задняя правая":"21213-5601108-10",
         "Дверь задняя левая":"21317-6200015-12"
      },
      "damaged window":{
         "Стекло переднее правое":"21214-6103214-00",
         "Стекло переднее левое":"21214-6103215-00",
         "Стекло заднее правое":"None",
         "Стекло заднее левое":"21310-6204021-00"
      },
      "damaged headlight":{
         "Фара правая":"8450107440",
         "Фара левая":"8450107441"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"8450107440"
      },
      "damaged bumper":{
         "Бампер":"8450107432"
      },
      "damaged wind shield":{
         "Стекло ветровое":"21217-5206008-01"
      }
   },
   "21314":{
      "damaged door":{
         "Дверь передняя правая":"21214-6100030-42",
         "Дверь передняя левая":"21214-6100031-44",
         "Дверь задняя правая":"21213-5601108-10",
         "Дверь задняя левая":"21317-6200015-12"
      },
      "damaged window":{
         "Стекло переднее правое":"21214-6103214-00",
         "Стекло переднее левое":"21214-6103215-00",
         "Стекло заднее правое":"None",
         "Стекло заднее левое":"21310-6204021-00"
      },
      "damaged headlight":{
         "Фара правая":"8450107440",
         "Фара левая":"8450107441"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"8450107440"
      },
      "damaged bumper":{
         "Бампер":"8450107432"
      },
      "damaged wind shield":{
         "Стекло ветровое":"21217-5206008-01"
      }
   },
   "urban":{
      "damaged door":{
         "Дверь передняя правая":"21214-6100030-42",
         "Дверь передняя левая":"21214-6100031-44",
         "Дверь задняя правая":"21213-5601108-10",
         "Дверь задняя левая":"21317-6200015-12"
      },
      "damaged window":{
         "Стекло переднее правое":"21214-6103214-00",
         "Стекло переднее левое":"21214-6103215-00",
         "Стекло заднее правое":"None",
         "Стекло заднее левое":"21310-6204021-00"
      },
      "damaged headlight":{
         "Фара правая":"8450107440",
         "Фара левая":"8450107441"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"8450107440"
      },
      "damaged bumper":{
         "Бампер":"8450107432"
      },
      "damaged wind shield":{
         "Стекло ветровое":"21217-5206008-01"
      }
   },
   "bronto":{
      "damaged door":{
         "Дверь передняя правая":"21214-6100030-42",
         "Дверь передняя левая":"21214-6100031-44",
         "Дверь задняя правая":"21213-5601108-10",
         "Дверь задняя левая":"21317-6200015-12"
      },
      "damaged window":{
         "Стекло переднее правое":"21214-6103214-00",
         "Стекло переднее левое":"21214-6103215-00",
         "Стекло заднее правое":"None",
         "Стекло заднее левое":"21310-6204021-00"
      },
      "damaged headlight":{
         "Фара правая":"8450107440",
         "Фара левая":"8450107441"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"8450107440"
      },
      "damaged bumper":{
         "Бампер":"8450107432"
      },
      "damaged wind shield":{
         "Стекло ветровое":"21217-5206008-01"
      }
   },
   "xray":{
      "damaged door":{
         "Дверь передняя правая":"801005064R",
         "Дверь передняя левая":"801015140R",
         "Дверь задняя правая":"821002780R",
         "Дверь задняя левая":"821019191R"
      },
      "damaged window":{
         "Стекло переднее правое":"807201362R",
         "Стекло переднее левое":"807213463R",
         "Стекло заднее правое":"827209924R",
         "Стекло заднее левое":"827214500R"
      },
      "damaged headlight":{
         "Фара правая":"8450021103",
         "Фара левая":"8450021104"
      },
      "damaged mirror":{
         "Левое зеркало":"963669241R",
         "Правое зеркало":"802923054R"
      },
      "damaged hood":{
         "Капот":"651007207R"
      },
      "damaged bumper":{
         "Бампер":"620228136R"
      },
      "damaged wind shield":{
         "Стекло ветровое":"727129727R"
      }
   },
   "ваз-2170":{
      "damaged door":{
         "Дверь передняя правая":"21100-6100014-20",
         "Дверь передняя левая":"21100-6100015-20",
         "Дверь задняя правая":"21100-6200014-00",
         "Дверь задняя левая":"21100-6200015-00"
      },
      "damaged window":{
         "Стекло переднее правое":"None",
         "Стекло переднее левое":"None",
         "Стекло заднее правое":"21710-6204010-00",
         "Стекло заднее левое":"None"
      },
      "damaged headlight":{
         "Фара правая":"21720-8404412-00",
         "Фара левая":"21720-8404413-00"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"21700-8402010-00"
      },
      "damaged bumper":{
         "Бампер":"21704-2803056-10"
      },
      "damaged wind shield":{
         "Стекло ветровое":"21700-5206010-15"
      }
   },
   "ваз-1118":{
      "damaged door":{
         "Дверь передняя правая":"1118-6100014",
         "Дверь передняя левая":"1118-6100015",
         "Дверь задняя правая":"1118-6200014",
         "Дверь задняя левая":"1118-6200015"
      },
      "damaged window":{
         "Стекло переднее правое":"None",
         "Стекло переднее левое":"None",
         "Стекло заднее правое":"1118-6204010",
         "Стекло заднее левое":"1118-6204011"
      },
      "damaged headlight":{
         "Фара правая":"1118-8403512",
         "Фара левая":"1118-8403513"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"1118-5007402"
      },
      "damaged bumper":{
         "Бампер":"None"
      },
      "damaged wind shield":{
         "Стекло ветровое":"1118-5206012"
      }
   },
   "ваз-1111 (ока)":{
      "damaged door":{
         "Дверь передняя правая":"None",
         "Дверь передняя левая":"None",
         "Дверь задняя правая":"None",
         "Дверь задняя левая":"None"
      },
      "damaged window":{
         "Стекло переднее правое":"None",
         "Стекло переднее левое":"None",
         "Стекло заднее правое":"None",
         "Стекло заднее левое":"None"
      },
      "damaged headlight":{
         "Фара правая":"None",
         "Фара левая":"None"
      },
      "damaged mirror":{
         "Левое зеркало":"None",
         "Правое зеркало":"None"
      },
      "damaged hood":{
         "Капот":"None"
      },
      "damaged bumper":{
         "Бампер":"None"
      },
      "damaged wind shield":{
         "Стекло ветровое":"None"
      }
   }
}
