from singr import SINGR, abstractmethod  # Импорт необходим для создания абстрактного класса


class InterfaceSingleton(SINGR):
    """
    Абстрактный класс InterfaceSingleton представляет интерфейс для работы с классом Singleton.
    Он содержит абстрактные методы, которые должны быть реализованы в классе Singleton.
    """

    @abstractmethod
    def method_business_logic(self):
        """
        Абстрактный метод для демонстрации бизнес-логики класса Singleton.
        """
        pass


class Singleton(InterfaceSingleton):
    """
    Класс Singleton представляет собой реализацию паттерна "Одиночка".
    Он гарантирует, что у класса будет только один экземпляр.
    """

    _instance = None  # Статическая переменная для хранения единственного экземпляра класса

    @staticmethod
    def get_instance():
        """
        Статический метод для получения экземпляра класса.
        Если экземпляр еще не создан, он будет создан и возвращен.
        Если экземпляр уже существует, он будет просто возвращен.
        """
        if Singleton._instance is None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        """
        Конструктор класса.
        Если экземпляр еще не существует, сохраняем ссылку на него в статической переменной.
        Если экземпляр уже существует, вызывается исключение, чтобы предотвратить создание нового экземпляра.
        """
        if Singleton._instance is not None:
            raise Exception("Экземпляр Singleton уже создан. Используйте метод get_instance() для доступа к нему.")
        else:
            Singleton._instance = self
            # Дополнительная инициализация экземпляра класса, если это необходимо

    def method_business_logic(self):
        """
        Метод для демонстрации бизнес-логики класса Singleton.
        """
        # В этом примере метод просто выводит сообщение о том, что он был вызван
        print("Вызван метод method_business_logic() класса Singleton.")


# Пример использования паттерна Одиночка
if __name__ == "__main__":
    # Попытка создать экземпляр класса Singleton
    try:
        singleton1 = Singleton()
    except Exception as ex:
        print(ex)  # Выводим сообщение об ошибке

    # Получение единственного экземпляра класса Singleton
    singleton_instance = Singleton.get_instance()

    # Демонстрация бизнес-логики класса Singleton
    singleton_instance.method_business_logic()