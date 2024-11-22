from abc import ABC, abstractmethod

class GameRepository(ABC):
    # abstractmethod는 ABC클래스 내에 인터페이스를 선언 할 경우 사용
    @abstractmethod
    def Play(self):
    # 아무것도 하지 않음(pass)
        pass