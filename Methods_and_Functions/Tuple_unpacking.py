
stock_prices = [('AAPL', 200), ('GOOG', 400), ('MSFT', 100)]
for item in stock_prices:
    print (item)
('AAPL', 200)
('GOOG', 400)
('MSFT', 100)
#-----
for ticker, price in stock_prices:
    print (price+(0.1*price)) 
220.0
440.0
110.0
#-----

