---create schema 
create schema gold;

-----------------------------------
--create view calendar
---------------------------------
create view gold.calendar
as 
select * from 
OPENROWSET(
    BULK 'https://firoztwogen2.blob.core.windows.net/silver/calendar/calendar.parquet/',
    FORMAT = 'PARQUET'
)as query1

--create view returns
create view gold.returns
as 
select * from 
OPENROWSET(
    BULK 'https://firoztwogen2.blob.core.windows.net/silver/Returns/Returns.parquet/',
    FORMAT = 'PARQUET'
)as query1

--create view Territory
create view gold.Territory
as 
select * from 
OPENROWSET(
    BULK 'https://firoztwogen2.blob.core.windows.net/silver/Territory/Territory.parquet/',
    FORMAT = 'PARQUET'
)as query1

--create view customer
create view gold.customer
as 
select * from 
OPENROWSET(
    BULK 'https://firoztwogen2.blob.core.windows.net/silver/customer/customer.parquet/',
    FORMAT = 'PARQUET'
)as query1

--create view product_subcategories
create view gold.product_subcategories
as 
select * from 
OPENROWSET(
    BULK 'https://firoztwogen2.blob.core.windows.net/silver/product_subcategories/product_subcategories.parquet/',
    FORMAT = 'PARQUET'
)as query1

---create view products
create view gold.products
as 
select * from 
OPENROWSET(
    BULK 'https://firoztwogen2.blob.core.windows.net/silver/products/products.parquet/',
    FORMAT = 'PARQUET'
)as query1


---create view sales
create view gold.sales
as 
select * from 
OPENROWSET(
    BULK 'https://firoztwogen2.blob.core.windows.net/silver/sales/sales.parquet/',
    FORMAT = 'PARQUET'
)as query1


--create master key
CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'Fir0z@2002#Secure!';

----create credential
create database scoped credential cred_firoz
with 
IDENTITY = 'managed identity'

---create external data source source_silver
create external data source source_silver
with 
(
    location = 'https://firoztwogen2.blob.core.windows.net/silver',
    credential = cred_firoz
)
---create external data source_gold
create external data source source_gold
with 
(
    location = 'https://firoztwogen2.blob.core.windows.net/gold',
    credential = cred_firoz
)

---create external file format 
create EXTERNAL file FORMAT FORMAT_parquet
WITH(
    FORMAT_TYPE= parquet,
    DATA_COMPRESSION = 'org.apache.hadoop.io.compress.SnappyCodec'
)

-----------------------------------
--create external table extsales
------------------------------------

---external table gold.extsales
create EXTERNAL table gold.extsales
WITH
(
    location ='extsales',
    data_source =source_gold,
    file_format = format_parquet
)as 
select * from gold.sales

select * from gold.extsales

