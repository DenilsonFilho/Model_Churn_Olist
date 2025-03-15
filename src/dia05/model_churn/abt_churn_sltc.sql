select *
from tb_abt_churn as t1
where t1.dt_ref = (select max( dt_ref ) from tb_abt_churn)
