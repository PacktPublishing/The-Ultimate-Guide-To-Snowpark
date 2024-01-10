create or replace aggregate function python_sum(a int)
returns int
language python
runtime_version=3.8
handler='PythonSum'
as $$
class PythonSum:
  def __init__(self):
    # This aggregate state is a primitive Python data type.
    self._partial_sum = 0

  @property
  def aggregate_state(self):
    return self._partial_sum

  def accumulate(self, input_value):
    self._partial_sum += input_value

  def merge(self, other_partial_sum):
    self._partial_sum += other_partial_sum

  def finish(self):
    return self._partial_sum
$$;


select python_sum(price) from sales;