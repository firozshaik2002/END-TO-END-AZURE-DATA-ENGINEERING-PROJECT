# Databricks notebook source
# MAGIC %md
# MAGIC ### silver layer script
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data loading

# COMMAND ----------

from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import *


# COMMAND ----------


df_returns = spark.read.option("header", True).csv("abfss://bronze@firoztwogen2.dfs.core.windows.net/Returns/returns.csv")
df_calendar = spark.read.option("header", True).csv("abfss://bronze@firoztwogen2.dfs.core.windows.net/calendar_lookup/calendar_lookup.csv")
df_customer = spark.read.option("header", True).csv("abfss://bronze@firoztwogen2.dfs.core.windows.net/customer_lookup/customer_lookup.csv")
df_product_categories = spark.read.option("header", True).csv("abfss://bronze@firoztwogen2.dfs.core.windows.net/product_categories_lookup/product_categories_lookup.csv")
df_product = spark.read.option("header", True).csv("abfss://bronze@firoztwogen2.dfs.core.windows.net/product_lookup/product_lookup.csv")
df_product_subcategories = spark.read.option("header", True).csv("abfss://bronze@firoztwogen2.dfs.core.windows.net/product_subcategories_lookup/product_subcategories_lookup.csv")
df_Territory = spark.read.option("header", True).csv("abfss://bronze@firoztwogen2.dfs.core.windows.net/Territory/Territory.csv")
df_sales_data = spark.read.option("header", True).csv("abfss://bronze@firoztwogen2.dfs.core.windows.net/sales_data_2020/sales_data_2020.csv")
df_sales_2021 = spark.read.option("header", True).csv("abfss://bronze@firoztwogen2.dfs.core.windows.net/sales_2021/sales_2021.csv")
df_sales_2022 = spark.read.option("header", True).csv("abfss://bronze@firoztwogen2.dfs.core.windows.net/sales_2022/sales_2022.csv")


# COMMAND ----------

df_calendar.display()
df_customer.display()
df_product.display()
df_product_categories.display()
df_product_subcategories.display()
df_returns.display()
df_Territory.display()
df_sales_data.display()
df_sales_2022.display()
df_sales_2021.display()

# COMMAND ----------

df_calendar.display(
)

# COMMAND ----------

df_calendar_withColumn = df_calendar.withColumn('Month',month(col('Date')))\
                                    .withColumn('Year',year(col("Date")))
                                    
df_calendar_withColumn.display()


# COMMAND ----------

df_calendar_withColumn.write.format('parquet')\
                      .mode('append')\
                     .option("path","abfss://silver@firoztwogen2.dfs.core.windows.net/calendar/calendar.parquet")\
                     .save()

# COMMAND ----------

df_customer.display()

# COMMAND ----------

df_customer_withColumn = df_customer.withColumn("FullName",concat(col('Prefix'),lit(' '),col('FirstName'),lit(' '),col('LastName')))
df_customer_withColumn.display()
 ##(or)
df_customer_wColumn = df_customer.withColumn("FullName",concat_ws(' ',col('Prefix'),col('FirstName'),col('LastName')))
df_customer_wColumn.display()


# COMMAND ----------

df_customer_wColumn.write.format('parquet')\
                      .mode('append')\
                     .option("path","abfss://silver@firoztwogen2.dfs.core.windows.net/customer/customer.parquet")\
                     .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### sub Categories
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

df_product_subcategories.display()

# COMMAND ----------

df_product_subcategories.write.format('parquet')\
                        .mode('append')\
                        .option("path","abfss://silver@firoztwogen2.dfs.core.windows.net/product_subcategories/product_subcategories.parquet")\
                        .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### products

# COMMAND ----------

df_product.display()

# COMMAND ----------

df_peoduct_withColumn = df_product.withColumn('ProductSKU',split(col('ProductSKU'),'-')[0])\
                        .withColumn('ProductName',split(col('ProductName'),' ')[0])
               

# COMMAND ----------

df_peoduct_withColumn.display()


# COMMAND ----------

df_peoduct_withColumn.write.format('parquet')\
                      .mode('append')\
                     .option("path","abfss://silver@firoztwogen2.dfs.core.windows.net/products/products.parquet")\
                     .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Returns

# COMMAND ----------

df_returns.display()

# COMMAND ----------

df_returns.write.format('parquet')\
                      .mode('append')\
                     .option("path","abfss://silver@firoztwogen2.dfs.core.windows.net/Returns/Returns.parquet")\
                     .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Territory

# COMMAND ----------

df_Territory.display()

# COMMAND ----------

df_Territory.write.format('parquet')\
                      .mode('append')\
                     .option("path","abfss://silver@firoztwogen2.dfs.core.windows.net/Territory/Territory.parquet")\
                     .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Sales

# COMMAND ----------

df_sales = df_sales_data.withColumn('StockDate',to_timestamp('StockDate'))

# COMMAND ----------

df_sales = df_sales.withColumn('OrderNumber',regexp_replace(col('OrderNumber'),'S','T'))

# COMMAND ----------

df_sales = df_sales.withColumn('multiply',col('OrderLineItem')*col('OrderQuantity'))

# COMMAND ----------

df_sales_data = df_sales_data.withColumn('OrderLineItem', col('OrderLineItem').cast('int')) \
                   .withColumn('OrderQuantity', col('OrderQuantity').cast('int')) 
                  

# COMMAND ----------

df_sales.display()

# COMMAND ----------

df_sales.write.format('parquet')\
                      .mode('append')\
                     .option("path","abfss://silver@firoztwogen2.dfs.core.windows.net/sales/sales.parquet")\
                     .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Sales Analysis

# COMMAND ----------

df_sales.groupBy("OrderDate").agg(count('OrderNumber').alias('total_order')).display()

# COMMAND ----------

df_product_categories.display()

# COMMAND ----------

df_Territory.display()