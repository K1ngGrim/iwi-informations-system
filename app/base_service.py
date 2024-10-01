import json
import os
import re
from datetime import datetime
from pathlib import Path
from typing import TypeVar, Generic

from file import File

T = TypeVar('T')


class BaseFactory(Generic[T]):
    _instance = None

    @classmethod
    def get_instance(cls) -> T:
        if cls._instance is None:
            cls._instance = cls.create_instance()

        return cls._instance

    @classmethod
    def create_instance(cls) -> T:
        raise NotImplementedError("Die Methode create_instance() muss in der Unterklasse implementiert werden.")


class BaseService:

    def __init__(self):
        pass

class ConfigService:
    pattern = re.compile(r'appconfig.*\.json')

    _config = None

    def __init__(self):
        self._logger = LogServiceFactory.get_instance()
        self._config = self.load_config()
        if self._config is not None:
            found = self._search_configs()
            self._init_files_config(found)

    @staticmethod
    def load_config(path="./appconfig.json"):
        with open(path, 'r') as file:
            return json.load(file)

    @staticmethod
    def save_config(config, path="./appconfig.json"):
        with open(path, 'w') as file:
            json.dump(config, file, indent=4)

    def get_value(self, key: str, config=None):
        if config is None:
            config = self._config

        if '.' in key:
            keys = key.split('.')
            if not config.get(keys[0], None):
                return None
            val = config[keys[0]]
            keys.pop(0)
            for key in keys:
                if not config.get(key, None):
                    return None
                val = val[key]
            return val

        if not config.get(key, None):
            return None

        return config[key]

    def set_value(self, key: str, value: any):
        self._config[key] = value
        return self._config[key]

    def get_dict(self):
        return self._config

    def update_files(self):
        found = self._search_configs()
        self._init_files_config(found)

    def _init_files_config(self, config_name):
        self._logger.Info("Started file updating procedure")
        new = 0
        try:
            folder = self.get_value("folder")

            if config_name is None:
                config_name = f"appconfig.{str(folder).split('/')[-1]}.json"
                with open(f"{folder}/{config_name}", "x") as c_file:
                    c_file.write("{\n}")
                    c_file.close()

            _file_config = self.load_config(f"{folder}/{config_name}")
            files = []
            if _file_config.get("files", None) is not None:
                files = _file_config["files"]
            for file in os.listdir(self.get_value("folder")):
                if file.lower().endswith(tuple(self.get_value("allowed-files"))):
                    json_files = self.get_value("files", _file_config)
                    if json_files is None: json_files = []
                    if not any(item['name'] == file for item in json_files):
                        files.append(
                            File(file, 30, datetime.now().date().strftime("%Y-%m-%d")).dict()
                        )

                        self._logger.Info(f"    Found file {file}")

                        new = new + 1

            _file_config["files"] = files
            self.save_config(_file_config, f"{folder}/{config_name}")

            self._config["files"] = files

            self._logger.Info(f"Finished file updating procedure. Found {new} new files")

        except Exception:
            self._logger.Error("Exception initializing files")


    def _search_configs(self):
        directory = Path(self.get_value("folder"))
        for file_path in directory.iterdir():
            if file_path.is_file() and self.pattern.match(file_path.name):
                return file_path.name


"""Factory for Singleton-Pattern of ConfigService"""


class ConfigServiceFactory(BaseFactory[ConfigService]):

    @classmethod
    def get_instance(cls):
        return super().get_instance()

    @classmethod
    def create_instance(cls) -> ConfigService:
        return ConfigService()

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