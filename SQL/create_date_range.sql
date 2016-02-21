DECLARE @Date1 DATE, @Date2 DATE
SET @Date1 = '20130501'
SET @Date2 = '20130831'

SELECT DATEADD(DAY,number+1,@Date1) [Date]
FROM master..spt_values
WHERE type = 'P'
AND DATEADD(DAY,number+1,@Date1) < @Date2
