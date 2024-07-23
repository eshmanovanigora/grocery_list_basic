

# Define function to retrieve prices colum in to a list
def get_prices(data):
    """
    Retrieves prices column in to a list

    Args:
        data (str): CSV format data

    Returns:
        list: list of prices
    """
    prices = []
    for row in data.split('\n')[1:]:
        price = row.split(',')[2]
        prices.append(float(price[1:]))
    return prices

def get_products(data):
    """
    Retrieves products column in to a list

    Args:
        data (str): CSV format data

    Returns:
        list: list of products
    """
    data = data.split('\n')[1:]
    products = []
    for row in data:
        product = row.split(',')[0]
        products.append(product)
    return products
   
def get_expensive(prices):
    """
    Finds the most expensive product of index

    Args:
        prices (list): list of prices

    Returns:
        int: index of most expensive product
    """
    max = prices[0]
    a = 0
    sw = True
    for i in range(len(prices)):
        if prices[i] > max:
            max = prices[i]
            a = i
    return a

# Read data from file
f = open("data.csv")
data = f.read()

# get list of products
products = get_products(data)

# get list of prices
prices = get_prices(data)

# get the index of the most expensive
idx = get_expensive(prices)


print(f'Cost of the most expensive product: {prices[idx]}')
print(f'Most expensive product: {products[idx]}')