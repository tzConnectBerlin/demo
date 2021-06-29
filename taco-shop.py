import smartpy as sp

TACO_SHOP_STORAGE = {
    1: {
        "current_stock": 100,
        "max_price": 10
    }
}

class TacoShop(sp.Contract):
    def __init__(self, storage = TACO_SHOP_STORAGE):
        self.init(storage=storage)

    @sp.entry_point
    def buy_taco(self, taco_type):
        taco = self.data.storage[taco_type]
        current_price = taco["max_price"] / taco["current_stock"]
        sp.verify(sp.amount == current_price, "Sorry, the taco you are trying to purchase has a different price")
        sp.verify(taco["current_stock"] > 0, "Sorry, no more tacos")
        self.data.storage[taco_type]["current_stock"] = taco["current_stock"] - 1
