import httpx
class ProductClient:

    BASE_URL = "https://dummyjson.com"

    def get_all_products(self):
        response = httpx.get(
            f"{self.BASE_URL}/products"
        )

        response.raise_for_status()

        return response.json()
    
    def get_a_product(self, id :int) :
        response = httpx.get(
            f"{self.BASE_URL}/products/{id}"
        )
        
        response.raise_for_status()
        
        return response.json()