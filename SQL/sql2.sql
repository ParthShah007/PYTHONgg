select * from products;
Select name, price,
Case when (price > 1000) then 'Expensive'
	when price between 500 and 1000 then 'moderate'
	else 'cheap'
End as price_tag from products;

alter table products
add column price_tag text;

update products
set price_tag =
Case when (price > 1000) then 'Expensive'
	when price between 500 and 1000 then 'moderate'
	else 'cheap'
end;



