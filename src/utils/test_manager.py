from pathlib import Path
from pydantic import ValidationError
from py_selenium_auto_core.logging.logger import Logger
from py_selenium_auto_core.utilities.file_reader import FileReader
from py_selenium_auto_core.utilities.root_path_helper import RootPathHelper

from src.models.test_data_model import TestDataModel


class TestDataProvider:
    __test__ = False

    _instance = None
    _file_name = "test_data.json"

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            tests_root = Path(RootPathHelper.calling_root_path(), "tests")

            if not FileReader.is_resource_file_exist(cls._file_name, tests_root):
                Logger.fatal(
                    f"Файл с тестовыми данными '{cls._file_name}' не был найден по пути '{tests_root}'", 
                    FileNotFoundError
                )
            
            try:
                raw_json = FileReader.get_resource_file(cls._file_name, tests_root)
                cls._instance = TestDataModel.model_validate_json(raw_json)
                
            except ValidationError as e:
                Logger.fatal(
                    f"Неверная структура файла с тестовыми данными: {e}", ValueError
                )

        return cls._instance