import json
import os
import threading

try:
    from colorama import Fore
    import requests
except ModuleNotFoundError:
    os.system('pip3 install colorama requests && title tiktok view bot, please restart && pause >NUL && exit')


class Main:
    def __init__(self, tiktok_video_url: str, views_max: int, threads_max: int):
        self.tiktok_video_url = tiktok_video_url
        self.views_max = views_max
        self.threads_max = threads_max
        self.views_sent = 0
        self.retries = 0

    def _botter(self, item_id: str) -> None:
        while True:
            try:
                response_view = requests.post(
                    url='https://api16-core-c-alisg.tiktokv.com/aweme/v1/aweme/stats/?ac=WIFI&op_region=SA', headers={
                        'Host': 'api16-core-c-alisg.tiktokv.com',
                        'Connection': 'close',
                        'Content-Length': '117',
                        'sdk-version': '2',
                        'passport-sdk-version': '5.12.1',
                        'x-Tt-Token': '010bcdc98424c32ae89cc3107afa55e05404d93afdc646ffe52f00765027281ea4a3925f965d979fe4b42352d9a67cc85784f67e0ce51639a7c82f272f89b7d2f0cdd2cb576f155abf94ba09a6dbaaae2923f-1.0.0',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'User-Agent': 'TikTok 17.4.0 rv:174014 (iPhone; iOS 14.2; ar_SA@calendar=gregorian) Cronet',
                        'X-SS-STUB': '88216088E2878AC941E829BCB0744C2D',
                        'x-tt-store-idc': 'alisg',
                        'x-tt-store-region': 'sa',
                        'X-SS-DP': '1233',
                        'x-tt-trace-id': '00-c9a77c9e1060b2d9bb9c828606df04d1-c9a77c9e1060b2d9-01',
                        'Accept-Encoding': 'gzip, deflate',
                        'Cookie': 'passport_csrf_token=1f52305413453c9f064fdbb44c45ce8f; passport_csrf_token_default=1f52305413453c9f064fdbb44c45ce8f; d_ticket=c506701932849ea607835bc4ba2a6de8ec830; cmpl_token=AgQQAPO_F-RPsI4vzNb-op0_-tNAiDMdv4Q0YP89_g; multi_sids=6778236784885122054%3A0bcdc98424c32ae89cc3107afa55e054%7C6958702576372352001%3A19297903fa3cd1033c702c984a5960da%7C6961103230660166661%3A35637e321e7e4a81db24c69b17b4a60b; odin_tt=85b7f8bbfec7c8b0ed0702ded3901861b7a3f7672b30a8e981e05892a8ec91d063f79a8b66626ffa0ee77da8dd8ab78758407ebe1b9b153b79bd8e7801b8d154; sessionid=0bcdc98424c32ae89cc3107afa55e054; sessionid_ss=0bcdc98424c32ae89cc3107afa55e054; sid_guard=0bcdc98424c32ae89cc3107afa55e054%7C1622584971%7C5184000%7CSat%2C+31-Jul-2021+22%3A02%3A51+GMT; sid_tt=0bcdc98424c32ae89cc3107afa55e054; uid_tt=9da77c7397d3a1b2fcb09b2c308caf13bccd0e8f661fcfa42ae4b28e59eeb375; uid_tt_ss=9da77c7397d3a1b2fcb09b2c308caf13bccd0e8f661fcfa42ae4b28e59eeb375; store-country-code=sa; store-idc=alisg; install_id=6968950756058875649; ttreq=1$8931d94e61cc87fb7605bef76f9095961bf9ed9c',
                        'X-Khronos': '1622585867',
                        'X-Gorgon': '8402e0ae600039b3627aaa59cff051f5627a0c1b6c31a11ca101',
                        'x-common-params-v2': 'pass-region=1&pass-route=1&language=ar&version_code=17.4.0&app_name=musical_ly&vid=ECA76874-2CC7-47AB-8FF1-203212A0FA4C&app_version=17.4.0&carrier_region=SA&channel=App%20Store&mcc_mnc=42001&device_id=6967870973303490054&tz_offset=10800&account_region=&sys_region=SA&aid=1233&residence=SA&screen_width=1125&uoo=1&openudid=c8bc81b8a71df3dd85c09f6ef7c54f7f4d95fe5d&os_api=18&os_version=14.2&app_language=ar&tz_name=Asia/Riyadh&current_region=SA&device_platform=iphone&build_number=174014&device_type=iPhone10,6&iid=6968950756058875649&idfa=00000000-0000-0000-0000-000000000000&locale=ar&cdid=A834593D-2AB1-4D73-9C58-E29AC50FA194&content_language='
                    }, data=f'action_time=1622585868&aweme_type=0&first_install_time=1622333917&item_id={item_id}&play_delta=1&tab_type=4'
                )
            except Exception:
                self.retries += 1
            else:
                try:
                    status_code = response_view.json()['status_code']
                except json.decoder.JSONDecodeError:
                    self.retries += 1
                else:
                    if status_code == 0:
                        self.views_sent += 1
                        break
                    else:
                        self.retries += 1

    def _title_updater(self) -> None:
        while True:
            if self.views_sent >= self.views_max:
                os.system(f'title tiktok viewbot | sent: {self.views_sent} ({round(((self.views_sent / self.views_max) * 100), 2)}%) ^| retries: {self.retries}')
                break
            os.system(f'title title tiktok viewbot | sent: {self.views_sent} ({round(((self.views_sent / self.views_max) * 100), 2)}%) ^| retries: {self.retries}')

        print(f'{Fore.WHITE}[{Fore.GREEN}>{Fore.WHITE}] completed{Fore.GREEN}.{Fore.WHITE}')
        os.system('pause >NUL')

    def setup(self) -> None:
        try:
            video_data = requests.get(
                url=self.tiktok_video_url, headers={
                    'Connection': 'close',
                    'Pragma': 'no-cache',
                    'Cache-Control': 'no-cache',
                    'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'Sec-Fetch-Site': 'none',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-User': '?1',
                    'Sec-Fetch-Dest': 'document',
                    'Accept-Encoding': 'gzip, deflate',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Cookie': 'tt_webid_v2=6940688826462406145; tt_webid=6940688826462406145; ttwid=1%7Cbza8rvLOfNRPRwC43Zn3utwgngykYIkkhCtiFchZVMA%7C1616005073%7C1dd5efed4a61e4b1654f08f10a6ff7b85e3d57622a4d6011f6642b1bbf785fcb; passport_csrf_token=bb82884d8da300de0ce4f8508694e635; passport_csrf_token_default=bb82884d8da300de0ce4f8508694e635; store-country-code=sa; tta_attr_id=0.1616499265.6942811476331593729; store-idc=alisg; sid_guard=5c3ba51706c6f27ef59bb4fcaf0d282b%7C1617813999%7C5184000%7CSun%2C+06-Jun-2021+16%3A46%3A39+GMT; uid_tt=9896d319adfbb4f4f7a56b2122e84ef36354da5b7a766c3d93f08771723b2e3f; uid_tt_ss=9896d319adfbb4f4f7a56b2122e84ef36354da5b7a766c3d93f08771723b2e3f; sid_tt=5c3ba51706c6f27ef59bb4fcaf0d282b; sessionid=5c3ba51706c6f27ef59bb4fcaf0d282b; sessionid_ss=5c3ba51706c6f27ef59bb4fcaf0d282b; odin_tt=530994ec29b8076689f2e696e07f7968d74abe62dc6990364400b7b666b98e83afe2d12f34a5c717c851ce41d2368908d1f4c45a8c3974fb4230088b6d230969a128029a783f0ae00352b0d06fa62e0a; R6kq3TV7=AMgpub14AQAASGoycNrCjOkGEeZn3OSfPJcGlZpRyawc4vVW0_K5JN1ScBmQ|1|0|427184ccd78b46f2f1443048844aba7bf6064745; cmpl_token=AgQQAPO_F-RMpY4vzNb-op0_-jPehXJPv4M0YPgasw; tt_csrf_token=Ev5Kwld907oqGN2T1k0HrHWF; ak_bmsc=ED95FE19720A8F91CACBCE8408BFC78E56335E9519250000BF887260FE32B047~pl7zsPkhgfEfP2YwW3Ph6y02EtVXax7QH9oUN1eMfTdDnvOlFJcDXESyLLkFAXRIaueH2qItg4EdfKBI5loXsbdYeZAAy2oCOz7PNDhyQvstusWjR1M6xBMzpFKRcIXuEXMwtrfBx4nQLynJxNr7CJOOKb02W/y1LENhAnX2p+eHB4S6HL5PRUVaJXx6xqRPtjaFzenP3I/+Wx44jRsDjDNlxmlM7krZQs+TzdJApyqZ4=; bm_sz=F1634B2D883BE7F7F8E55AF4D48798F6~YAAQlV4zViahf3R4AQAAIitmvwtx/krEk+BEEQt4CoGeEB0X2JTHtZKLSBFVXxGgh8oLe8VcsrGqbUWhtO2eK/fhU6tdNs4C36OkPBJt7HlGRC07i6coxuZO1bcf0pxWJoJppYUoC9vPHQYh1++jflOXTPVSS0hw/W++SqiceRZkS+Q5SWGwWgWnx6hP4VB1; bm_sv=5AF097FF6E9C14E8BF077EE5BD7D126D~LBiUQfj1jYvhXvESNmEdfPzQcX6s8MGsQ79mJvSVV/OclkEWqotEPinlq8GADZ+tDMWTfCrS+nQ/dH0mG7bwj0L/5a8LC5sn4KJC+CEzqxHnt2JcMCSmRrYV5vO6sJDXY01ZEpWWSdJTGeCbBD7l2DPIFidy9J5ujWVeVBBbY6I=; _abck=494D5CEEE963A444A9BFED1397AE4A1A~-1~YAAQl14zVjHK03V4AQAAfJRovwV3ujEp8mNTnNKx5q6XhLXbDZgBUZwYi8ZS6N3zYCWz6lpsDgFzXfDQT7dKaxDyijowI/MIW0aLuDCIUFU5bw1xBMaKFv4tvXv8QfiThLmgZh3ihOCUJ9xBvVcf9Aw3OQ0YIpDK7oCidJ7WeQkT5jGIhm9yXvB6zUde3/xrOzZyDyxLO6qbSuunOwTmgGN/+qoNcrE82ZJDp3faWXgLMEtgi22ui9gENAV5rnlzEZll3e8AZMn9xZbq+9Aa7SAtgmih3i4WTgyPxwR7DXjPNZ+pnnAb/qJ+JCI+TFIiRW31KVuqy0A6142qz3Whm+XM++sQIWOuThkmXtEh25NeYtyKV3LwWDHMPg7sICqWEjOtgCLPh4lUxLpZaroVbcn0hnVZQ/ab~0~-1~-'
                }
            )
            video_id = video_data.text.split('"video":{"id":"')[1].split('"')[0]
        except Exception:
            print(f'{Fore.WHITE}[{Fore.RED}!{Fore.WHITE}] Failed to parse Video ID{Fore.RED}.{Fore.WHITE}')
            os.system('title title tiktok viewbot | Restart expected && pause >NUL')
        else:
            threading.Thread(target=self._title_updater).start()
            for _ in range(self.views_max):
                while True:
                    if threading.active_count() <= self.threads_max:
                        threading.Thread(target=self._botter, args=(video_id,)).start()
                        break


if __name__ == '__main__':
    os.system('clear && title tiktok viewbot | Main Menu')
    main = Main(
        input(f'{Fore.WHITE}[{Fore.YELLOW}>>{Fore.WHITE}] TikTok Video URL{Fore.YELLOW}: {Fore.WHITE}'),
        int(input(f'{Fore.WHITE}[{Fore.YELLOW}>>{Fore.WHITE}] Views{Fore.YELLOW}: {Fore.WHITE}')),
        int(input(f'{Fore.WHITE}[{Fore.YELLOW}>>{Fore.WHITE}] Threads{Fore.YELLOW}: {Fore.WHITE}'))
    )
    main.setup()
