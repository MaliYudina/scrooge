import requests
import logging
logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger('get_specification')


def get_secid_specification(secid) -> dict:
    """
    Get SECID specification from MOEX
    :param secid: string name of ticker
    :return: string name of instrument type
    Does not have figi (use Tinkoff api)
    """
    request_url = "https://iss.moex.com/iss/securities/{}.json?lang=en&" \
                  "iss.meta=off&iss.only=description".format(secid)
    # LOG.info('request_url')
    print(request_url)
    response = requests.get(request_url)
    specification = response.json()
    specification = specification['description']['data']
    spec_dict = {}
    for s in specification:
        spec_dict[s[0]] = s[2]
    # print(spec_dict)
    return spec_dict
