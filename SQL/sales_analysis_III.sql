with t1 as (
    select
        p.product_id
    from
        Product p
        join Sales s on s.product_id = p.product_id
    where
        s.sale_date not between '2019-01-01'
        and '2019-03-31'
)
select
    p.product_id,
    p.product_name
from
    Product p
where
    p.product_id not in (
        select
            *
        from
            t1
    )