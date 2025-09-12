from config import get_connection
from mysql.connector import Error

class Product:
    def add_category(category_id, category_name):
        conn = get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("insert into categories (category_id, category_name) values (%s, %s)", (category_id, category_name))
                conn.commit()
            except Exception as e:
                print(f'error adding category: {e}')
            finally:
                conn.close()

    def add_product(product_id, name, category_id, price, stock_quantity):
        conn = get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("insert into products (product_id, name, category_id, price, stock_quantity) values (%s, %s, %s, %s, %s)", (product_id, name, category_id, price, stock_quantity))
                conn.commit()
            except Exception as e:
                print(f'error adding product: {e}')
            finally:
                conn.close()

    def update_product(product_id, price, stock_quantity):
        conn = get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("update products set price=%s, stock_quantity=%s where product_id=%s", (price, stock_quantity, product_id))
                conn.commit()
            except Exception as e:
                print(f'error updating product: {e}')
            finally:
                conn.close()

    def delete_product(product_id):
        conn = get_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("delete from products where product_id=%s", (product_id,))
                conn.commit()
            except Exception as e:
                print(f'error deleting product: {e}')
            finally:
                conn.close()

    def search_products_by_name(name):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("select * from products where name like %s", ('%' + name + '%',))
            results = cursor.fetchall()
            conn.close()
            return results

    def search_products_by_category(category_id):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("select * from products where category_id=%s", (category_id,))
            results = cursor.fetchall()
            conn.close()
            return results

    def search_products_by_price_range(min_price, max_price):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("select * from products where price between %s and %s", (min_price, max_price))
            results = cursor.fetchall()
            conn.close()
            return results

    def low_stock_report(threshold):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("select * from products where stock_quantity<%s", (threshold,))
            results = cursor.fetchall()
            conn.close()
            return results

    def display_products_with_category():
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("""
                select p.product_id, p.name, c.category_name, p.price, p.stock_quantity
                from products p
                join categories c on p.category_id=c.category_id
            """)
            results = cursor.fetchall()
            conn.close()
            return results
