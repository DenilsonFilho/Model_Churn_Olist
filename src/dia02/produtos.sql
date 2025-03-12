select distinct t2.product_category_name,
        count(1)

from tb_order_items as t1

left join tb_products as t2
    on t1.product_id = t2.product_id

where t2.product_category_name is not null

group by t2.product_category_name

order by count(1) desc

limit 50


sum(case when product_category_name = 'cama_mesa_banho' then 1 else 0 end) as prod_cama_mesa_banho,
sum(case when product_category_name = 'beleza_saude' then 1 else 0 end) as prod_beleza_saude,
sum(case when product_category_name = 'esporte_lazer' then 1 else 0 end) as prod_esporte_lazer,
sum(case when product_category_name = 'moveis_decoracao' then 1 else 0 end) as prod_moveis_decoracao,
sum(case when product_category_name = 'informatica_acessorios' then 1 else 0 end) as prod_informatica_acessorios,
sum(case when product_category_name = 'utilidades_domesticas' then 1 else 0 end) as prod_utilidades_domesticas,
sum(case when product_category_name = 'relogios_presentes' then 1 else 0 end) as prod_relogios_presentes,
sum(case when product_category_name = 'telefonia' then 1 else 0 end) as prod_telefonia,
sum(case when product_category_name = 'ferramentas_jardim' then 1 else 0 end) as prod_ferramentas_jardim,
sum(case when product_category_name = 'automotivo' then 1 else 0 end) as prod_automotivo,
sum(case when product_category_name = 'brinquedos' then 1 else 0 end) as prod_brinquedos,
sum(case when product_category_name = 'cool_stuff' then 1 else 0 end) as prod_cool_stuff,
sum(case when product_category_name = 'perfumaria' then 1 else 0 end) as prod_perfumaria,
sum(case when product_category_name = 'bebes' then 1 else 0 end) as prod_bebes,
sum(case when product_category_name = 'eletronicos' then 1 else 0 end) as prod_eletronicos,
sum(case when product_category_name = 'papelaria' then 1 else 0 end) as prod_papelaria,
sum(case when product_category_name = 'fashion_bolsas_e_acessorios' then 1 else 0 end) as prod_fashion_bolsas_e_acessorios,
sum(case when product_category_name = 'pet_shop' then 1 else 0 end) as prod_pet_shop,
sum(case when product_category_name = 'moveis_escritorio' then 1 else 0 end) as prod_moveis_escritorio,
sum(case when product_category_name = 'consoles_games' then 1 else 0 end) as prod_consoles_games,
sum(case when product_category_name = 'malas_acessorios' then 1 else 0 end) as prod_malas_acessorios,
sum(case when product_category_name = 'construcao_ferramentas_construcao' then 1 else 0 end) as prod_construcao_ferramentas_construcao,
sum(case when product_category_name = 'eletrodomesticos' then 1 else 0 end) as prod_eletrodomesticos,
sum(case when product_category_name = 'instrumentos_musicais' then 1 else 0 end) as prod_instrumentos_musicais,
sum(case when product_category_name = 'eletroportateis' then 1 else 0 end) as prod_eletroportateis,
sum(case when product_category_name = 'casa_construcao' then 1 else 0 end) as prod_casa_construcao,
sum(case when product_category_name = 'livros_interesse_geral' then 1 else 0 end) as prod_livros_interesse_geral,
sum(case when product_category_name = 'alimentos' then 1 else 0 end) as prod_alimentos,
sum(case when product_category_name = 'moveis_sala' then 1 else 0 end) as prod_moveis_sala,
sum(case when product_category_name = 'casa_conforto' then 1 else 0 end) as prod_casa_conforto,
sum(case when product_category_name = 'bebidas' then 1 else 0 end) as prod_bebidas,
sum(case when product_category_name = 'audio' then 1 else 0 end) as prod_audio,
sum(case when product_category_name = 'market_place' then 1 else 0 end) as prod_market_place,
sum(case when product_category_name = 'construcao_ferramentas_iluminacao' then 1 else 0 end) as prod_construcao_ferramentas_iluminacao,
sum(case when product_category_name = 'climatizacao' then 1 else 0 end) as prod_climatizacao,
sum(case when product_category_name = 'moveis_cozinha_area_de_servico_jantar_e_jardim' then 1 else 0 end) as prod_moveis_cozinha_area_de_servico_jantar_e_jardim,
sum(case when product_category_name = 'alimentos_bebidas' then 1 else 0 end) as prod_alimentos_bebidas,
sum(case when product_category_name = 'industria_comercio_e_negocios' then 1 else 0 end) as prod_industria_comercio_e_negocios,
sum(case when product_category_name = 'livros_tecnicos' then 1 else 0 end) as prod_livros_tecnicos,
sum(case when product_category_name = 'telefonia_fixa' then 1 else 0 end) as prod_telefonia_fixa,
sum(case when product_category_name = 'fashion_calcados' then 1 else 0 end) as prod_fashion_calcados,
sum(case when product_category_name = 'construcao_ferramentas_jardim' then 1 else 0 end) as prod_construcao_ferramentas_jardim,
sum(case when product_category_name = 'eletrodomesticos_2' then 1 else 0 end) as prod_eletrodomesticos_2,
sum(case when product_category_name = 'agro_industria_e_comercio' then 1 else 0 end) as prod_agro_industria_e_comercio,
sum(case when product_category_name = 'artes' then 1 else 0 end) as prod_artes,
sum(case when product_category_name = 'pcs' then 1 else 0 end) as prod_pcs,
sum(case when product_category_name = 'sinalizacao_e_seguranca' then 1 else 0 end) as prod_sinalizacao_e_seguranca,
sum(case when product_category_name = 'construcao_ferramentas_seguranca' then 1 else 0 end) as prod_construcao_ferramentas_seguranca,
sum(case when product_category_name = 'artigos_de_natal' then 1 else 0 end) as prod_artigos_de_natal,
sum(case when product_category_name = 'fashion_roupa_masculina' then 1 else 0 end) as prod_fashion_roupa_masculina,