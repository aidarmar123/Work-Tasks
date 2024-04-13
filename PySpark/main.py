from pyspark.sql import SparkSession
from pyspark.sql.functions import when

spark = (SparkSession.builder
        .master('local[*]')
        .appName('RecruitmentTask')
        .getOrCreate())
products = spark.createDataFrame([
    {"id":1,"name_product":"apple", "price":50, "quantity":1},
    {"id":2,"name_product":"cheese", "price":80, "quantity":1},
    {"id":3,"name_product":"apple pie", "price":130, "quantity":1},
    {"id":4,"name_product":"yogurt", "price":120, "quantity":1},
    {"id":5,"name_product":"ball", "price":250, "quantity":1}
])
categories = spark.createDataFrame([
    {"id":1,"name_category":"fruit"},
    {"id":2,"name_category":"dairy"},#Молочные продукты
    {"id":3,"name_category":"bakery"},
    {"id":4,"name_category":"dessert"},
    {"id":5,"name_category":"snacks"},
    {"id":6,"name_category":"tools"}
])
categoriesProduct = spark.createDataFrame([
    {'id':1,'product_id':4, "category_id":2},
    {'id':2,'product_id':3, "category_id":4},
    {'id':3,'product_id':3, "category_id":3},
    {'id':4,'product_id':2, "category_id":5},
    {'id':5,'product_id':1, "category_id":1},
    {'id':6,'product_id':4, "category_id":4},
    {'id':6,'product_id':5, "category_id":7},
])
have_category = categoriesProduct.join(products, products.id == categoriesProduct.product_id).join(categories, categories.id == categoriesProduct.category_id)
have_category.select(have_category.name_product,have_category.name_category).show()

no_category=categoriesProduct.join(products, products.id == categoriesProduct.product_id)
result_table = no_category.join(have_category,"name_product","left_anti")
result_table.select('name_product').show()


