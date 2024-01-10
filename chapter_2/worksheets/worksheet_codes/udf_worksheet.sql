CREATE
OR REPLACE FUNCTION LAST_NAME_FINDER (input_name string) 
returns string not null 
language python runtime_version = '3.8' 
handler = 'last_name_finder' 
as 
$$
def last_name_finder(input_name:str):
  last_name = input_name.split()[1]
  return last_name
$$;


SELECT
    NAME
  , LAST_NAME_FINDER(NAME) AS LAST_NAME
FROM SAMPLE_EMPLOYEE_DATA;

