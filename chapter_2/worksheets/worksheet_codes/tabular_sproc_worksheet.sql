CREATE OR REPLACE PROCEDURE filterByCountry(tableName VARCHAR, country VARCHAR)
RETURNS TABLE(id INT,name VARCHAR, age INT, email VARCHAR, city VARCHAR,country VARCHAR)
LANGUAGE PYTHON
RUNTIME_VERSION = '3.8'
PACKAGES = ('snowflake-snowpark-python')
HANDLER = 'filter_by_country'
AS
$$
from snowflake.snowpark.functions import col
def filter_by_country(session, table_name, country):
  df = session.table(table_name)
  return df.filter(col("country") == country)
$$;


CALL filterByCountry('SAMPLE_EMPLOYEE_DATA', 'USA');