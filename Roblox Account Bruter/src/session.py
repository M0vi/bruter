from primp import Client
from random import choice
from typing import Union, List
from util import Util

class Session:
    @staticmethod
    def session() -> List[Union[Client, str, str, str]]:
        proxy = Util.get_random_proxy()

        browsers = [
            ("chrome_131", '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"', "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"),
            ("chrome_131", '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"', "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36")
        ]

        impersonate, sec_ch_ua, user_agent = choice(browsers)

        session = Client(impersonate=impersonate, proxy=proxy, verify=False)

        return (session, sec_ch_ua, user_agent, proxy)