from multiprocessing import Process
import time

class Subprocess(Process):
    def __init__(self, name):
        Process.__init__(self)
        self.name = name
    
    def run(self):
        print(f"[sub] {self.name} start")
        time.sleep(5)
        print(f"[sub] {self.name} end")

if __name__ == "__main__":
    print("[main] start")
    p = Subprocess(name='startcoding')
    p.start()
    #p.join()

    time.sleep(1)

    print(p.is_alive())

    #if p.is_alive:
    #    p.terminate()

    p.join()

    print("[main] end")

## 추가 학습
## 스레드간 데이터 처리(lock)
## 프로세스간 데이터 전송(Queue, pipe)
