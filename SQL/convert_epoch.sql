/******* This assumes SQL Server T-SQL syntax ********/
SELECT id
, CAST(DATEADD(ss, epoch_timestamp, '1970-01-01') AS DATE) AS subdate
FROM my_table
