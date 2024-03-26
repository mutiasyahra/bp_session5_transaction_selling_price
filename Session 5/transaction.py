class CosmeticItem:
    def __init__(self, name, variants, prices, stocks):
        self.name = name
        self.variants = variants
        self.prices = prices
        self.stocks = stocks

    def calculate_selling_price(self, variant_index):
        return self.prices[variant_index] + (self.prices[variant_index] * 0.10)

    def make_transaction(self, variant_index):
        if self.stocks[variant_index] > 0:
            self.stocks[variant_index] -= 1
            return True
        return False

def display_items(cosmetic_items):
    for item in cosmetic_items:
        print(f"Item: {item.name}")
        print("Variants: {}\nOriginal Prices: {}\nAvailable Stocks: {}".format(item.variants, item.prices, item.stocks))
        print("Selling Prices: {}\n".format(item.calculate_selling_price(0) if len(item.prices) == 1 else [item.calculate_selling_price(i) for i in range(len(item.prices))]))

def display_transactions(cosmetic_items):
    total_transactions = 0
    total_profit = 0
    for item in cosmetic_items:
        total_transactions += sum(item.stocks)
        total_profit += sum([(item.calculate_selling_price(i) - item.prices[i]) * item.stocks[i] for i in range(len(item.prices))])
    print(f"Total number of transactions: {total_transactions}")
    print(f"Total profit: {total_profit}")

if __name__ == "__main__":
    cosmetic_items = [
        CosmeticItem("Eye Shadow", ["Matte", "Powder"], [10000, 15000], [100, 100]),
        CosmeticItem("Lipstick", ["Matte", "Glossy"], [55000, 70000], [100, 100]),
        CosmeticItem("Powder", ["Compact", "Loose"], [75000, 85000], [100, 100]),
    ]

    # Making transactions
    cosmetic_items[0].make_transaction(0)
    cosmetic_items[1].make_transaction(1)

    display_items(cosmetic_items)
    display_transactions(cosmetic_items)