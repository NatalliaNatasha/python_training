from model.group import Group
import shutil
import json
import pytest
from fixture.application import Application
import jsonpickle
import os.path
import importlib
from fixture.db import Dbfixture
from fixture.orm import ORMFixture


fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target=json.load(f)
    return target


@pytest.fixture
def app(request):
    print(shutil.which("geckodriver.exe"))
    global fixture
    browser = request.config.getoption("--browser")
    web_config=load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture=Application(browser=browser,baseUrl=web_config["baseUrl"])
    fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
    return fixture

@pytest.fixture(scope="session", autouse = True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")



#pytest_addoption(parser):
#special hook that pytest will look for when it starts up. It takes a parser argument, which is used to add options to the pytest command line

def pytest_addoption(parser):
    parser.addoption("--browser", action="store",default="chrome")
    parser.addoption("--target", action="store", default="target.json")
    parser.addoption("--check_ui", action="store_true")


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            testdata=load_from_module(fixture[5:])
            metafunc.parametrize(fixture,testdata,ids=[str(x) for x in testdata])
        elif fixture.startswith("json_"):
            testdata = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, testdata, ids=[str(x) for x in testdata])

def load_from_module(module):
    return importlib.import_module("data.%s" % module).testdata


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())

#фикстура для подключения БД
@pytest.fixture(scope="session")# создание подключения для всей сессии
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture=ORMFixture(host=db_config['host'],name=db_config['name'],user=db_config['user'],password=db_config['password'])# создание объекта класса Dbfixture
    def fin():# вызов в конце сессии для закрытия соединения
        dbfixture.destroy()
    request.addfinalizer(fin)# после завершения тестов (или при аварийном завершении) будет вызвана автоматически для корректного закрытия бд
    return dbfixture






