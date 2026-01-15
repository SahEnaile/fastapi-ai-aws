class ProductService:

    def get_available_products(self, data: dict):
        available_products = []

        for product in data["products"]:
            if product["stock"] > 0:
                available_products.append(product)

        data["products"] = available_products

        return data