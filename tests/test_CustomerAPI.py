# test_with_pytest.py
from _pytest.fixtures import fixture

from model.Customer import Customer
from model.Shop import Shop


@fixture
def exampleCustomer1():
    c1 = Customer("Markus Muelle", "markus.mueller@email.test", "1101 Vienna", "10.09.2001")
    return c1

@fixture
def exampleCustomer2():
    c2 = Customer("Yves Saint Lauren", "thegoatoffragrance@gmail.test", "1234 Paris","01.08.1936")
    return c2

def test_customer_add(exampleCustomer1):
    shop = Shop()
    shop.addCustomer(exampleCustomer1)
    assert exampleCustomer1 in shop.customers
    # try adding again
    shop.addCustomer(exampleCustomer1)
    assert len(shop.customers) == 1 # should be added only once


def test_customer_add2(exampleCustomer2):
    shop = Shop()
    shop.addCustomer(exampleCustomer2)
    assert exampleCustomer2 in shop.customers
    # try adding again
    shop.addCustomer(exampleCustomer2)
    assert len(shop.customers) == 1 # should be added only once


def test_customer_remove(exampleCustomer1):
    shop = Shop()
    shop.addCustomer(exampleCustomer1)
    assert exampleCustomer1 in shop.customers
    shop.removeCustomer(exampleCustomer1)
    assert exampleCustomer1 not in shop.customers


def test_customer_remove2(exampleCustomer2):
    shop = Shop()
    shop.addCustomer(exampleCustomer2)
    assert exampleCustomer2 in shop.customers
    shop.removeCustomer(exampleCustomer2)
    assert exampleCustomer2 not in shop.customers


def test_customer_get(exampleCustomer1):
    shop = Shop()
    shop.addCustomer(exampleCustomer1)
    assert exampleCustomer1 in shop.customers
    c = shop.getCustomer(exampleCustomer1.customer_id)
    assert c == exampleCustomer1




