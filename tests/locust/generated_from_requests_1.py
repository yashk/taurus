# This script was generated by Taurus

from gevent import sleep
from re import findall, compile
from locust import HttpLocust, TaskSet, task

class UserBehaviour(TaskSet):
    @task(1)
    def generated_task(self):
        with self.client.get(headers={"Connection": "close", "Keep-Alive": "timeout=15, max=100", "var2": "val2"}, timeout=30.0, url="/", catch_response=True) as response:
            if not all(str(val) in response.content for val in ['text1', 'text2']):
                response.failure("['text1', 'text2'] not found in body")
            elif not all(findall(compile(str(val)), response.content) for val in ['enigma for body']):
                response.failure("['enigma for body'] not found in body")
            elif any(findall(compile(str(val)), str(response.status_code)) for val in ['200']):
                response.failure("['200'] found in http-code")
            else:
                response.success()
        sleep(5.0)
        
        with self.client.post(data={"var1": "val1"}, headers={"Connection": "close", "Keep-Alive": "timeout=15, max=100"}, timeout=1.5, url="/page", catch_response=True) as response:
            if not all(findall(compile(str(val)), response.content) for val in ['\\w+l1e']):
                response.failure("['\\w+l1e'] not found in body")
            else:
                response.success()
        sleep(1.0)
        

class GeneratedSwarm(HttpLocust):
    task_set = UserBehaviour
    host = "http://blazedemo.com"
    min_wait = 0
    max_wait = 0

