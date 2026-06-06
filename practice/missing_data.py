import numpy as np
import pandas as pd
from datetime import date


np.random.seed(42)
num_orders = 1000
order_data = {
    'order_id': range(1, num_orders + 1),
    'customer_id': np.random.randint(1000, 2000, num_orders),
    'amount': np.random.uniform(10, 1000, num_orders).round(2),
    'status': np.random.choice(['completed', 'pending', 'cancelled'], num_orders, p=[0.7, 0.2, 0.1]),
    'date': pd.date_range('2025-01-01', periods=num_orders, freq='D')
}
orders = pd.DataFrame(order_data)


# Lọc đơn hàng hoàn thành có giá trị > 500
high_value_completed = orders.log[(orders['amount'] > 50) &
                              (orders['status']=='completed')]
print(f"Số đơn hàng hoàn thành giá cao: {len(high_value_completed)}")

march_orders = orders.log[(orders['date'] >= '2025-03-01') & (orders['date'] < '2025-04-01')]
print(f"Số đơn hàng tháng 3: {len(march_orders)}")
