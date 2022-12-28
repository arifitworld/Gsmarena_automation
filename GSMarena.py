from requests import get, post
from base64 import b64encode
from pprint import pp
from GSMarenaFunctions import featureimg, paragraph, heading2, urlify, wptable
import json


api_url = 'https://mobile-phone-server.vercel.app/phones'
response = get(api_url)
if response.status_code == 200:
    data = response.json()
    items = data.get('RECORDS')
    # print(data)
    # pp(items)

for item in items:
    phone_name = item.get('name').title()
    released_date = item.get('released_at').replace('Released ', '')
    os = item.get('os')
    camera = item.get('camera_pixels')
    battery = item.get('battery_size')
    src_img = item.get('picture')
    body = item.get('body')
    storage = item.get('storage')
    display_size = item.get('display_size')
    display_resolution = item.get('display_resolution')
    video_pixels = item.get('video_pixels')
    ram = item.get('ram')
    chipset = item.get('chipset')
    battery_size = item.get('battery_size')
    battery_type = item.get('battery_type')


    #this is overview section:
    overview = {
        'name': phone_name,
        'released_at': released_date,
        'body': body,
        'os': os,
        'storage': storage,
        'display_size': display_size,
        'display_resolution': display_resolution,
        'camera_pixels': camera,
        'video_pixels': video_pixels,
        'ram': ram,
        'chipset': chipset,
        'battery_size': battery_size,
        'battery_type': battery_type
    }

    #Specification convert to json section:
    spec_str = item.get('specifications')
    specifications = json.loads(spec_str)
    # print(specifications)

    peragraph1 = f'The {phone_name} is one of the best phone in time. This phone was released on {released_date}. It comes with OS android 10 and it has 8 MP front camera. The best news is {phone_name} phone has a {battery}battery. So what are you lokking for?'
    peragraph_1 = paragraph(peragraph1)
    first_image = featureimg(src_img, phone_name)
    heading_1 = heading2(f'{phone_name} Overview')
    table_1 = wptable(overview)
    heading_2 = heading2(f'{phone_name} Specification')
    table_2 = wptable(specifications)
    url = urlify(phone_name)

    content = f'{peragraph_1} {first_image} {heading_1} {table_1} {heading_2} {table_2}'

    wp_api = 'https://wordpress-880942-3117404.cloudwaysapps.com/wp-json/wp/v2/posts'
    user = 'arifitdev@gmail.com'
    password = 'PHP7 hETy zsow 6hpu gnDJ N7gJ'
    crediential = f'{user}:{password}'
    token = b64encode(crediential.encode())
    header = {'Authorization': f'Basic {token.decode("utf-8")}'}

    def wppost(title, content, url, featured_media, status='publish'):
        api_url = 'https://wordpress-880942-3117404.cloudwaysapps.com/wp-json/wp/v2/posts'
        data = {
            'title': title,
            'content': content,
            'url': url,
            'featured_media': featured_media,
            'status': status,
        }
        response = post(api_url, headers=header, json=data)
        print(f'{title} is posted successfully')

    final_post = wppost(phone_name, content, url,)

