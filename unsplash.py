
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 09:16:43 2021

@author: csponkoj
"""

import os
import requests
import time

#terms_to_find = ["balcony","garage", "terrace", "fireplace"]
feature = input("Enter Feature: ")

def find_pages_limit(terms):
    r = requests.get(f'https://api.unsplash.com/search/photos?query={terms}&per_page=30&client_id=2rDzsV__-QjH2NO6QEJ1NI6Qx5RdYgaGCdifhuDJjxk')
    data = r.json()
    page_limit=data['total_pages']
    total_number_of_image = data['total']
    r.close()
    return page_limit,total_number_of_image

    
    
download_dir = "D:/unsplash/" + feature #put your directory file name here
if not os.path.exists(download_dir):
    os.mkdir(download_dir) 

page_number,image_numbers = find_pages_limit(feature)


for page in range(0,page_number): 

    try:
        r = requests.get(f'https://api.unsplash.com/s/photos?query={feature}&page={page}&per_page=30&client_id=2rDzsV__-QjH2NO6QEJ1NI6Qx5RdYgaGCdifhuDJjxk')
        r.close()
    except requests.exceptions.RequestException as e:
        print(e)
        print('failure')
        pass
    
    data = r.json()
    for f,i in enumerate(data['results']):
        name = data['results'][f]['id']
        url = data['results'][f]['urls']['raw']
        filepath = f"{os.path.join(os.path.realpath(os.getcwd()),download_dir,name)}.jpg"
        if not os.path.exists(filepath):
            with open(filepath,"wb") as f:
                f.write(requests.request("GET",url).content)
                print(f)
    time.sleep(10)
    print("Taking Nap")
        