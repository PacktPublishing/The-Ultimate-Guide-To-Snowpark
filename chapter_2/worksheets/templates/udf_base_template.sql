CREATE OR REPLACE FUNCTION <UDF name> (<arguments>)
  returns <data type> << optional: not null >>
  language python
  runtime_version = '3.8'
  << optional: packages=(<list of additional packages>) >>
  << optional: imports=(<list of files and directories to import from defined stages>) >>
  handler = '<name of main Python function>'
as
$$
def <name of main Python function>(<arguments>):
  # Python code to determine the main 
  # functionality of the UDF. 
  # This ends with a return clause:
  return <function output>
$$
;