from util import Util
from time import sleep
from curl_cffi import requests

config = Util.get_config()

SOLVER_KEY = config["solverKey"]

def get_token(roblox_session: requests.Session, blob, proxy, cookie):
    session = requests.Session()

    challengeInfo = {
        "publicKey": "476068BF-9607-4799-B53D-966BE98E2B81",
        "site": "https://www.roblox.com/",
        "surl": "https://arkoselabs.roblox.com",
        "capiMode": "inline",
        "styleTheme": "default",
        "languageEnabled": False,
        "jsfEnabled": False,
        "extraData": {
            "blob": blob
        },
        "ancestorOrigins": ["https://www.roblox.com", "https://www.roblox.com"],
        "treeIndex": [1, 0],
        "treeStructure": "[[],[[]]]",
        "locationHref":  "https://www.roblox.com/arkose/iframe"
    }

    browserInfo = {
        'Cookie': cookie,
        'Sec-Ch-Ua': roblox_session.headers["sec-ch-ua"],
        'User-Agent': roblox_session.headers["user-agent"]
    }

    payload = {
        "key": SOLVER_KEY,
        "challengeInfo": challengeInfo,
        "browserInfo": browserInfo,
        "proxy": proxy
    }

    response = session.post("https://rosolve.pro/createTask", json=payload, timeout=120).json()

    task_id = response.get("taskId")

    if task_id == None:
        raise ValueError(f"Failed to get taskId, reason: {response["error"]}")
    
    counter = 0

    while counter < 60:
        sleep(1)

        solution = session.get(f"https://rosolve.pro/taskResult/{task_id}").json()

        print(solution)

        if solution["status"] == "completed":
            return solution["result"]["solution"]
        
        elif solution["status"] == "failed":
            return None
        
        counter += 1

    return None