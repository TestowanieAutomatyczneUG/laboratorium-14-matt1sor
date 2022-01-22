from behave import *
from password import password

@given("Password validator")
def step_impl(context):
    context.password=password()

@when('check password {password}')
def step_impl(context, password):
    context.result = context.passowrd.validation(password)
@then('result is {result}')
def step_impl(context,result):
    if int(result) == 1:
        assert context.result
    else:
        assert not context.result