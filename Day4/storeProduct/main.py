from product import Product

def main():
    Product.add_category(1, 'electronics')
    Product.add_product(101, 'laptop', 1, 1000, 50)
    Product.add_product(102, 'mouse', 1, 20, 200)
    Product.update_product(101, 950, 45)
    print('search by name:', Product.search_products_by_name('laptop'))
    print('search by category:', Product.search_products_by_category(1))
    print('search by price range:', Product.search_products_by_price_range(500, 1500))
    print('low stock report:', Product.low_stock_report(10))
    print('products with category:', Product.display_products_with_category())
    Product.delete_product(102)

if __name__ == '__main__':
    main()
