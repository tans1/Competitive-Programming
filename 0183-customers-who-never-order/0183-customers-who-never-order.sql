
# select name as 'Customers'
# from Customers
# left join Orders 
# on Customers.id = Orders.customerId
# where Orders.customerId is null

# or 

select name as 'Customers'
from Customers
where id not in 
(
    select customerId
    from Orders
)