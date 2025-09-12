import inspect
from product import Product  # Assuming your class is in product.py



def test_add_product_query():
    db = ProductDB()
    expected_query = "insert into products (product_id, name, category_id, price, stock_quantity) values (%s, %s, %s, %s, %s)"
    actual_query = inspect.getsource(db.add_product)
    assert expected_query.replace(" ", "") in actual_query
def test_list_products_query():
    db = ProductDB()
    expected_query = "select * from products"
    actual_query = inspect.getsource(db.list_products)
    assert expected_query.replace(" ", "") in actual_query

def test_update_product_query():
    db = ProductDB()
    expected_query = "update products set price=%s, stock_quantity=%s where product_id=%s"
    actual_query = inspect.getsource(db.update_product)
    assert expected_query.replace(" ", "") in actual_query

def test_delete_product_query():
    db = ProductDB()
    expected_query = "delete from products where product_id=%s"
    actual_query = inspect.getsource(db.delete_product)
    assert expected_query.replace(" ", "") in actual_query

# --- Method Signature Tests ---

def test_add_product_signature():
    sig = inspect.signature(ProductDB.add_product)
    assert list(sig.parameters.keys()) == ["self", "product_id", "name", "category_id", "price", "stock_quantity"]

def test_list_products_signature():
    sig = inspect.signature(ProductDB.list_products)
    assert list(sig.parameters.keys()) == ["self"]

def test_update_product_signature():
    sig = inspect.signature(ProductDB.update_product)
    assert list(sig.parameters.keys()) == ["self", "product_id", "price", "stock_quantity"]

def test_delete_product_signature():
    sig = inspect.signature(ProductDB.delete_product)
    assert list(sig.parameters.keys()) == ["self", "product_id"]


