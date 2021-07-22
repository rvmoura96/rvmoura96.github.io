from time import sleep

from behave import given, then, when

from bdd.modules.auxiliar import cast_table_to_dict


@given(u'que acesse a home')
def access_index_given(context):
    context.driver.get(context.url)
    sleep(3)


@when(u'acesso a home')
def access_index(context):
    context.driver.get(context.url)
    sleep(3)


@when(u'clico no botão de "{button_name}"')
def step_impl(context, button_name):
    classes = {
        "download": "menu-lista-download",
        "contato": "menu-lista-contato"
    }
    download_button = context.driver.find_elements_by_class_name(
        classes[button_name]
    )[-1]
    download_button.click()


@then(u'deverá ser enviado o seguinte evento')
def step_impl(context):
    sleep(3)
    requests = context.driver.requests
    expected = cast_table_to_dict(context.table)
    filtred_request = [
        request for request in requests
        if "google-analytics" in request.url
        and request.method == "GET"
    ]
    event_querystring = [
        request for request in filtred_request
        if "event" in request.querystring
    ][-1].querystring.split("&")

    el = [key.split("=")[-1] for key in event_querystring if "el=" in key][-1]
    ea = [key.split("=")[-1] for key in event_querystring if "ea=" in key][-1]
    ec = [key.split("=")[-1] for key in event_querystring if "ec=" in key][-1]

    result = {"el": el, "ea": ea, "ec": ec}

    assert expected == result

@then(u'deverá ser enviado um evento de Pageview')
def step_impl(context):
    sleep(3)
    expected = cast_table_to_dict(context.table)
    requests = context.driver.requests
    filtred_request = [
        request for request in requests
        if "analytics" in request.url
        and request.method == "POST"
    ][-1]
    result = {"t":filtred_request.params["t"]}

    assert expected == result
