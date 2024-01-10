CREATE OR REPLACE FUNCTION <UDTF name> (<arguments>)
  returns TABLE (<field_1_name> <field_1_data_type> , <field_2_name> <field_2_data_type>, ... )
  language python
  runtime_version = '3.8'
  << optional: packages=(<list of additional packages>) >>
  << optional: imports=(<list of files and directories to import from defined stages>) >>
  handler = '<name of main Python class>'
as
$$

# Optional Python code to execute logic
# before breaking out into partitions

'''
Define main Python class which is
leveraged to process partitions.
Executes in the following order:
- __init__ | Executes once per partition
- process | Executes once per input row within the partition
- end_partition | Executes once per partition
'''
class <name of main Python class> :
  
  '''
  Optional __init__ method to
  execute logic for a partition
  before breaking out into rows
  '''
  def __init__(self) :
    # Python code at the partition level
  
  '''
  Method to process each input row
  within a partition, returning a 
  tabular value as tuples.
  '''
  def process(self, <arguments>) :
    '''
    Enter Python code here that 
    executes for each input row.
    This likely ends with a set of yield
    clauses that output tuples, 
    for example:
    '''
    yield (<field_1_value_1>, <field_2_value_1>, ...)
    yield (<field_1_value_2>, <field_2_value_2>, ...)
    '''
    Alternatively, this may end with
    a single return clause containing
    an iterable of tuples, for example:
    '''
    return [
        (<field_1_value_1>, <field_2_value_1>, ...)
      , (<field_1_value_2>, <field_2_value_2>, ...)
    ]
  
  '''
  Optional end_partition method to 
  execute logic for a partition
  after processing all input rows
  '''
  def end_partition(self) :
    # Python code at the partition level
    '''
    This ends with a set of yield
    clauses that output tuples, 
    for example:
    '''
    yield (<field_1_value_1>, <field_2_value_1>, ...)
    yield (<field_1_value_2>, <field_2_value_2>, ...)
    '''
    Alternatively, this ends with
    a single return clause containing
    an iterable of tuples, for example:
    '''
    return [
        (<field_1_value_1>, <field_2_value_1>, ...)
      , (<field_1_value_2>, <field_2_value_2>, ...)
    ]
    
$$
;