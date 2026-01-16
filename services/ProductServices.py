class ProductService:

    def get_available_products(self, data: dict):
        available_products = []

        for product in data["products"]:
            if product["stock"] > 0:
                available_products.append(product)

        data["products"] = available_products

        return data
    
    def get_a_product(self, data : dict) :
        
        if data["stock"] > 0 :
            return data
    