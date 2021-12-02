import os
import requests
import sys
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv

load_dotenv()

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('url1', nargs='+')
    parser.add_argument('url2', nargs='+')
 
    return parser

def parse_url(user_link):
   parsed_url = urlparse(user_link)
   parse_url = f'{parsed_url.netloc}{parsed_url.path}'
   return parse_url


def is_bitlink(bitlink_url):
    response = requests.get(
        f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_url}',
        headers={'Authorization': f'Bearer {token_bitly}'})
    status = response.ok
    return status


def shorten_link(token_bitly, user_link):
    url_bitly = 'https://api-ssl.bitly.com/v4/bitlinks'
    payload = {'long_url': user_link, 'domain': 'bit.ly'}

    response = requests.post(
        url_bitly,
        json=payload,
        headers={'Authorization': f'Bearer {token_bitly}'})
    response.raise_for_status()
    bitly_short_link = response.json()['id']
    return bitly_short_link


def count_clicks(token_bitly, bitlink_url):
    url_stat = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink_url}/clicks/summary'
    response = requests.get(url_stat,
                            headers={'Authorization': f'Bearer {token_bitly}'})
    response.raise_for_status()

    result = response.json()['total_clicks']
    return result


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    token_bitly = os.environ['BITLY_TOKEN']
    for name in namespace.name:
        print('name', name)
        if name:
            user_link = name
        else:
            user_link = input('Введите ссылку: ')
    url_parse = parse_url(user_link)
    is_bitlinks_url = is_bitlink(url_parse)
    if is_bitlinks_url:
        click_stat = count_clicks(token_bitly, url_parse)
        print(click_stat)
    else:
        short_link = shorten_link(token_bitly, user_link)
        print(short_link)
