CREATE OR REPLACE PROCEDURE SPROC_SUBSET_TABLE()
  returns string not null
  language python
  runtime_version = '3.8'
  packages = ('snowflake-snowpark-python')
  handler = 'subset_table'
as
$$
def subset_table(snowpark_session):
  df =  snowpark_session.table('SAMPLE_EMPLOYEE_DATA').select("NAME","AGE")
  return df.collect()
$$
;

CALL SPROC_SUBSET_TABLE()