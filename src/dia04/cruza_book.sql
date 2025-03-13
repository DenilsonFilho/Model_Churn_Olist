/* select dt_ref,
        seller_id

from tb_book_sellers

where seller_id = '7c67e1448b00f6e969d365cea6b010ab' */

select t1.order_approved_at as dt_venda,
        t2.seller_id,
        max(1) as venda

from tb_orders as t1

left join tb_order_items as t2
    on t1.order_id = t2.order_id

where t1.order_approved_at is not null
    and t2.seller_id
    and t1.order_status = 'delivered'

group by t1.order_approved_at, t2.seller_id

