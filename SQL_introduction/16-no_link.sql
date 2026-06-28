-- Lists all records with a non-empty name from second_table.
-- Displays the score and name ordered by descending score.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
AND name != ""
ORDER BY score DESC;
