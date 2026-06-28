-- Lists the number of records with the same score in second_table.
-- Displays the score and the number of records for each score.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
