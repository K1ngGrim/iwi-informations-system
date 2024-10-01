from app.services.base_service import BaseFactory, BaseService

class LogService(BaseService):

    @staticmethod
    def Info(info: str):
        print("[INFO] ", info)

    @staticmethod
    def Error(err: str):
        print("[ERROR] ", err)



class LogServiceFactory(BaseFactory[LogService]):

    @classmethod
    def get_instance(cls) -> LogService:
        return super().get_instance()

    @classmethod
    def create_instance(cls) -> LogService:
        return LogService()
