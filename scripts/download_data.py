import requests
from bs4 import BeautifulSoup
import os
import argparse

def dl_data(radar_names: list = ['hok'], years: list = [2017]):
    fitacf_local_url = 'https://ergsc.isee.nagoya-u.ac.jp/data/ergsc/ground/radar/sd/fitacf_local/'
    fitacf_url = 'https://ergsc.isee.nagoya-u.ac.jp/data/ergsc/ground/radar/sd/fitacf/'

    for name in radar_names:
        for year in years:
            radar_name_and_year = name + '/' + str(year) + '/'
            dl(fitacf_local_url, radar_name_and_year)
            dl(fitacf_url, radar_name_and_year)

def dl(url, radar_name_and_year):
    home_dir = os.getcwd()
    temp_url = url + radar_name_and_year
    save_dir = home_dir+'/data/' + url.split('/')[-2] + '/' + radar_name_and_year

    os.makedirs(save_dir, exist_ok=True)
    file_requests= requests.get(temp_url)
    soup = BeautifulSoup(file_requests.content, "html.parser")
    for s in soup.find_all("a")[1:]:
        filename = s.get('href')
        file_path = save_dir + filename
        if os.path.exists(file_path):
            print(f'{filename} already exists')
        else:
            data_url = temp_url + filename
            urlData = requests.get(data_url).content
            with open(file_path ,mode='xb') as f: # wb でバイト型を書き込める
                f.write(urlData)
            print(f'{filename} was saved')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n','--names', default=['hok'], nargs='*')
    parser.add_argument('-y', '--years', default=[2017], nargs='*')
    args = parser.parse_args()

    dl_data(args.names, args.years)

if __name__ == '__main__':
    main()
