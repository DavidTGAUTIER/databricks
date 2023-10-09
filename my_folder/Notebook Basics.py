# Databricks notebook source
print("Hello World!")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT("Hello world from SQL !")

# COMMAND ----------

# MAGIC %md
# MAGIC # Title

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Title 1
# MAGIC ## Title 2
# MAGIC ### Title 3
# MAGIC
# MAGIC text with a **bold** and *italicized* in it.
# MAGIC
# MAGIC Ordered list
# MAGIC 1. once
# MAGIC 2. two
# MAGIC 3. three
# MAGIC
# MAGIC Unordered list
# MAGIC * apples
# MAGIC * peaches
# MAGIC * bananas
# MAGIC
# MAGIC Images:
# MAGIC ![Associate-badge](https://www.databricks.com/en-website-assets/static/b89c6b6bd8f101fd86cf9f7afbed759d/93c40/data-engineer-associate.webp)
# MAGIC
# MAGIC And of course, tables : 
# MAGIC
# MAGIC | user_id | user_name |
# MAGIC |---------|-----------|
# MAGIC |    1    |   Adam    |
# MAGIC |    2    |   Sarah   |
# MAGIC |    3    |   John    |
# MAGIC
# MAGIC Links (or Embedded HTML): <a href="https://docs.databricks.com/notebooks/notebooks-manage.html" target="_blank"> Managing Notebooks documentation</a>

# COMMAND ----------

# MAGIC %md
# MAGIC on va utiliser la `Magic Command` **`%run`** qui est utiliser pour executer un autre notebook au sein de notre projet Databricks depuis un notebook actuel. Cela permet de réutiliser et de partager du code entre plusieurs notebooks ou d'executer un flux de travail découpé en plusieurs étapes dans différents notebooks
# MAGIC
# MAGIC `%run /path/to/my_notebook`
# MAGIC
# MAGIC On va prendre un exemple : 
# MAGIC
# MAGIC ```
# MAGIC /part 1 - Intro
# MAGIC      |__ Notebook Basics.dbc
# MAGIC      |__ /Includes
# MAGIC           |_ Setup.dbc
# MAGIC ```
# MAGIC
# MAGIC Comme ca, les variables et les autres déclarations provenant du notebook `Setup.dbc` seront disponibles dans notre notebook actuel `Notebook Basics`

# COMMAND ----------

# MAGIC %run ./Includes/Setup

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
print(files)

# COMMAND ----------

display(files)
