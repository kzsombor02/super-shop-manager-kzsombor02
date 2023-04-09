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

def test_customer_get2(exampleCustomer2):
    shop = Shop()
    shop.addCustomer(exampleCustomer2)
    assert exampleCustomer2 in shop.customers
    c = shop.getCustomer(exampleCustomer2.customer_id)
    assert c == exampleCustomer2



def test_customer_generate_temporary_password():
    customer = Customer("John Doe", "johndoe@test.com", "123 Main St", "01/01/2000")
    password = customer.generate_temporary_password()
    assert isinstance(password, str)
    assert len(password) == 5

def test_customer_generate_temporary_password2():
    customer = Customer("Jake Len", "jake.len@test.com", "1234 Main St", "01/01/2001")
    password = customer.generate_temporary_password()
    assert isinstance(password, str)
    assert len(password) == 5


def test_customer_reset_password(exampleCustomer1):
    shop = Shop()
    shop.addCustomer(exampleCustomer1)
    assert exampleCustomer1 in shop.customers
    new_password = "new_password"
    exampleCustomer1.reset_password(exampleCustomer1.generate_temporary_password(), new_password)
    assert exampleCustomer1.password == new_password

def test_customer_reset_password2(exampleCustomer2):
    shop = Shop()
    shop.addCustomer(exampleCustomer2)
    assert exampleCustomer2 in shop.customers
    new_password = "newer_password"
    exampleCustomer2.reset_password(exampleCustomer2.generate_temporary_password(), new_password)
    assert exampleCustomer2.password == new_password


def test_return_Bonus_points(exampleCustomer1):
    shop = Shop()
    shop.addCustomer(exampleCustomer1)
    assert exampleCustomer1 in shop.customers
    assert exampleCustomer1.returnBonusPoints() == 0

def test_return_Bonus_points2(exampleCustomer2):
    shop = Shop()
    shop.addCustomer(exampleCustomer2)
    assert exampleCustomer2 in shop.customers
    assert exampleCustomer2.returnBonusPoints() == 0



def test_add_Bonus_points(exampleCustomer1):
    shop = Shop()
    shop.addCustomer(exampleCustomer1)
    assert exampleCustomer1 in shop.customers
    exampleCustomer1.addBonusPoints(10)
    assert exampleCustomer1.returnBonusPoints() == 10

def test_add_Bonus_points2(exampleCustomer2):
    shop = Shop()
    shop.addCustomer(exampleCustomer2)
    assert exampleCustomer2 in shop.customers
    exampleCustomer2.addBonusPoints(10)
    assert exampleCustomer2.returnBonusPoints() == 10


