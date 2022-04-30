import threading
import time

def work():
    print("[sub] start")
    keyword = input("[sub] 검색어를 입력하세요 >>>")
    print(f"[sub] {keyword}로 검색을 시작합니다.")
    print("[sub] end")

print("[main]")

worker = threading.Thread(target=work)
worker.daemon = True
worker.start()

print("[main] 메인 스레드는 자기할일을 합니다..")
print("[main] end")


