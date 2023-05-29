from behave import given, when, then
from expects import equal, expect
from main import FizzBuzz


@given('the number "{number}"')
def number(context, number):
    context.number = int(number)


@when("calculates the result")
def calculates(context):
    context.result = FizzBuzz.calculates(num=context.number)


@then('the result should be "{result}"')
def validates(context, result):
    expect(context.result).to(equal(result))
