--https://leetcode.com/problems/exchange-seats/

# Write your MySQL query statement below
SELECT S.id, case WHEN S.id%2=0 THEN (
                                        SELECT SS.student
                                        FROM seat SS
                                        WHERE SS.id=(S.id-1))   
                    WHEN S.id=(SELECT count(*) FROM seat SSS) and S.id%2=1 THEN S.student
                    WHEN S.id%2=1 THEN(
                                        SELECT SS.student
                                        FROM seat SS
                                        WHERE SS.id=(S.id+1)) 
                    
             END as student
FROM seat S
