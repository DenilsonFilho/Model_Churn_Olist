select *,
        case when order_delivered_customer_date > order_estimated_delivery_date then 1 else 0 end as atraso
from tb_orders
