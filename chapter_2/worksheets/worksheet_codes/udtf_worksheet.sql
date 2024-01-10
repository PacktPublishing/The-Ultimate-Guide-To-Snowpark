CREATE OR REPLACE FUNCTION AVERAGE_AGE (input_age INT )
  returns TABLE (AVG_AGE FLOAT)
  language python
  runtime_version = '3.8'
  handler = 'CalculateAverage'
as
$$

class CalculateAverage:
  def __init__(self) :
    self._values = []

  def process(self, input_measure: int) :
    self._values.append(input_measure)

  def end_partition(self) :
    values_list = self._values
    average = sum(values_list) / len(values_list)
    yield(average ,)
$$
;

SELECT
COUNTRY,Avg_Age
FROM SAMPLE_EMPLOYEE_DATA
,table(AVERAGE_AGE(AGE) over (partition by COUNTRY))