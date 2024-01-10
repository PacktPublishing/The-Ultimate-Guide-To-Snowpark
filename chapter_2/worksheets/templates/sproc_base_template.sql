CREATE OR REPLACE PROCEDURE <stored procedure name> (<arguments>)
  returns <data type> << optional: not null >>
  language python
  runtime_version = '3.8'
  packages=('snowflake-snowpark-python', <optional list of additional packages>)
  << optional: imports=(<list of files and directories to import from defined stages>) >>
  handler = '<name of main Python function>'
as
$$
def <name of main Python function>(snowpark_session, <arguments>):
  # Python code to determine the main 
  # functionality of the stored procedure. 
  # This ends with a return clause:
  return <function output>
$$
;