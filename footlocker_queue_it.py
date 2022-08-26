
# -------------------------------------------------------------------------------------------------------------------- #

import hashlib
import base64
import json

# -------------------------------------------------------------------------------------------------------------------- #

class Footlocker_POW:

    def __init__(self, prod):

        self.prod = prod

    @staticmethod
    def solve_pow(zero_count: int, input: str, complexity: int):

        solutions = []

        postfix = 0

        while True:

            if len(solutions) != zero_count:

                hash = hashlib.sha256(
                    f"{input}{str(postfix)}".encode('utf-8')
                ).hexdigest()

                if hash[0:complexity] == '0' * complexity:
                    solutions.append(
                        {
                            'hash': hash,
                            'postfix': postfix
                        }
                    )

                postfix += 1

            else:
                return solutions

    def generate_session_id_payload(self, solutions: list, meta: str, queue_it_cookie: str, session_id: str, parameters: dict):

        payload = {
            "userId": queue_it_cookie,
            "meta": meta,
            "sessionId": session_id,
            "solution":{
            "hash": solutions,
            "type": "HashChallenge"
        },
            "tags": [
                "powTag-CustomerId:footlocker",
                "X-Queueit-Challange-CustomerId:footlocker",
                f"powTag-EventId:{self.prod}",
                f"X-Queueit-Challange-EventId:{self.prod}",
                f"powTag-UserId:{queue_it_cookie}",
                f"X-Queueit-Challange-UserId:{queue_it_cookie}"
            ],
            "stats": {
                "duration": 1974,
                "tries": 1,
                "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
                "screen": "3116 x 1305",
                "browser": "Chrome",
                "browserVersion": "104.0.0.0",
                "isMobile": False,
                "os": "Windows",
                "osVersion": "10",
                "cookiesEnabled": True
            },
            "parameters": parameters
        }

        payload_encoded = base64.b64encode(bytes(json.dumps(payload).replace("'", '"').replace(": ", ':').replace(', ', ',').replace('KHTML,like Gecko', 'KHTML, like Gecko'), encoding='utf-8'))

        return payload_encoded

    def generate_payload(self):

        # meta = https://footlocker.queue-it.net/challengeapi/pow/challenge/{queue_it_cookie}.json()['meta']

        # session_id = https://footlocker.queue-it.net/challengeapi/pow/challenge/{queue_it_cookie}.json()['sessionId']

        # parameters = https://footlocker.queue-it.net/challengeapi/pow/challenge/{queue_it_cookie}.json()['parameters']

        # input = parameters['input']

        # complexity = parameters['complexity']

        # zero_count = parameters['zeroCount']

        solution = self.solve_pow(
            input="",
            complexity=3,
            zero_count=25
        )

        payload = self.generate_session_id_payload(
            solutions=solution,
            meta="",
            queue_it_cookie='',
            session_id='',
            parameters={}
        )

        print(solution)

        print(payload)

# -------------------------------------------------------------------------------------------------------------------- #

if __name__ == '__main__':
    Footlocker_POW(
        prod='prod8259flpl'
    ).generate_payload()

# -------------------------------------------------------------------------------------------------------------------- #
