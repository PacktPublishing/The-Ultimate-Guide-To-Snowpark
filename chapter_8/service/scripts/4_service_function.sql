CREATE FUNCTION filter_doc_udf (InputText varchar)
  RETURNS varchar
  SERVICE=filter_service
  ENDPOINT=filterendpoint
  AS '/filter';