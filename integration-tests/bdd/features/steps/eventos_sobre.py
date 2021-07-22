
from behave import when
from faker import Faker
from selenium import webdriver

@when(u'preencho o campo "{field}"')
def step_impl(context, field):
    faker = Faker("pt_br")
    dummy_data = {
        "nome": faker.name(),
        "email": faker.email(),
        "telefone": faker.phone_number(),
    }
    field_element = context.driver.find_element_by_id(field)

    if field == "aceito":
        field_element.click()
    else:
        field_element.send_keys(dummy_data[field])

    context.driver.find_element_by_id("historia").click()

@when(u'clico no botão submit')
def step_impl(context):
    button = context.driver.find_element_by_tag_name("button")
    button.click()
