WITH proc AS PROCEDURE(table_name TEXT,country TEXT)
RETURNS TEXT
LANGUAGE PYTHON
RUNTIME_VERSION = '3.8'
PACKAGES = ('snowf""lake-snowpark-python')
HANDLER = 'main'
AS
$$

from snowflake.snowpark.functions import col
def main(session, table_name,country):
  return session.table(table_name).filter(col("country") == country).count()
$$

CALL proc('SAMPLE_EMPLOYEE_DATA','USA');