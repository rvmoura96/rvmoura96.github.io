from behave import when


@when(u'clico no botão para a próxima página')
def step_impl(context):
    next_button = context.driver.find_elements_by_class_name("next-page")[-1]
    next_button.click()


@when(u'clico no botão "{button}"')
def step_impl(context, button):
    buttons_positions = {"Lorem": 0, "Ipsum": 1, "Dolor": -1}
    button_elements = list(
        context.driver.find_elements_by_class_name("card-montadoras")
    )
    expected_button = button_elements[buttons_positions[button]]
    expected_button.click()
