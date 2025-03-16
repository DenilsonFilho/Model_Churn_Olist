select t1.*,
        t2.avg_review_score as flag_avg_next_score

from tb_book_sellers as t1

left join (

    select seller_id,
            dt_ref,
            avg_review_score
    
    from tb_book_sellers
) as t2
    on t1.seller_id = t2.seller_id
    and t2.dt_ref = date(t1.dt_ref, '+1 months')

where t2.avg_review_score is not null

order by t1.seller_id