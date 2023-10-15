num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1)
print("数字11.345宽度限制7，小数精度2，结果是：%7.2f" % num2)
print("数字11.345宽度不限制，小数精度2，结果是：%.2f" % num2)

# 快速格式化方式： f"{占位}"
name = "mate60 pro"
price = 6499.00
year = 2023
print(f"我是{name}, 发布于：{year}，价格是：{price}")

# 表达式格式化
print("1*1的结果是：%d" % (1 * 1))
print(f"1*2的结果是：{1*2}")
print("字符串在Python中的类型名是：%s" % type('字符串'))

name = 'jerico'
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days

print(f"公司：{name}，股票代码：{stock_code}, 当前股价：{stock_price}，每日增长系数为：{stock_price_daily_growth_factor}，经过{growth_days}天增长，最终价格为：{finally_stock_price}")
print("公司：%s，股票代码：%s，当前股价：%.2f，每日增长系数为：%.1f，经过%d天增长，最终价格为：%f" % (name, stock_code, stock_price, stock_price_daily_growth_factor, growth_days, finally_stock_price))