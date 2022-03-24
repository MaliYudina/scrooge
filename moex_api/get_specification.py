import requests
import logging
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger('get_specification')


def get_secid_specification(secid) -> dict:
    """
    Get SECID specification from MOEX
    :param secid: string name of ticker
    :return: string name of instrument type
    """
    request_url = "https://iss.moex.com/iss/securities/{}.json?lang=en&" \
                  "iss.meta=off&iss.only=description".format(secid)
    print(request_url)
    response = requests.get(request_url)
    specification = response.json()
    specification = specification['description']['data']
    spec_dict = {}
    for s in specification:
        spec_dict[s[0]] = s[2]
    print(spec_dict)
    return spec_dict


# example_list = ['MOEX', 'SBER', 'YNDX', 'ROSN', 'VTBX']
# for i in example_list:
#     spec = get_secid_specification(secid=i)
#     print(spec)
