"""Hooks file."""
from behave.tag_matcher import ActiveTagMatcher
from ipdb import post_mortem
from json import load
from os import makedirs
from os.path import isdir
from logging import getLogger, config

from seleniumwire import webdriver

from bdd.helpers import constants

active_tag_value_provider = {
    "config_0": False
}

active_tag_matcher = ActiveTagMatcher(active_tag_value_provider)


def before_all(context):
    context.userdata = context.config.userdata
    context.config_0 = context.userdata.get('config_0', 'False')
    context.logger = setup_logger()


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    browser_name = context.userdata.get('browser', 'firefox')
    local_machine_ip = context.userdata.get('local_machine_ip', '192.168.15.19')
    selenium_port =  context.userdata.get('selenium_hub_port', '4444')
    command_executor = f"{local_machine_ip}:{selenium_port}/wd/hub"
    context.options = {"addr": local_machine_ip}
    context.desired_capabilities = {"browserName": browser_name}
    context.driver = webdriver.Remote(
        command_executor=command_executor,
        desired_capabilities=context.desired_capabilities,
        seleniumwire_options=context.options,
    )
    context.url = context.userdata.get('url', 'http://localhost:5000/case')


def before_tag(context, tag):
    pass


def after_step(context, step):
    if context.config.userdata.get('debug') and step.status == "failed":
        post_mortem(step.exc_traceback)


def after_tag(context, tag):
    pass


def after_scenario(context, scenario):
    context.driver.quit()


def after_feature(context, feature):
    pass


def after_all(context):
    pass


def setup_logger():
    if not isdir(constants.LOG_FILE_DIR):
        makedirs(constants.LOG_FILE_DIR)

    with open(constants.LOGGER_CONFIG, 'rt') as f:
        options = load(f)

    config.dictConfig(options)
    return getLogger(__name__)
