create or replace function column_adder(x string, y string)
returns string
language python
runtime_version = 3.8
packages = ('pandas')
handler = 'column_adder'
as $$
import pandas
from _snowflake import vectorized

@vectorized(input=pandas.DataFrame)
def column_adder(df):
  return df[0] + "," + df[1]
$$;


select col1 as CITY,col2 as COUNTRY,column_adder(col1,col2) as CITY_COUNTRY
from (
  select City as col1,Country as col2 from SAMPLE_EMPLOYEE_DATA
);
