/*
1378. Replace Employee ID With The Unique Identifier  (Easy)
https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

Approach
--------
- Employees is the "main" table: every employee must appear in the output.
- EmployeeUNI may not have a row for some employees.
- LEFT JOIN keeps every row from Employees and fills unique_id with NULL
  when there is no match in EmployeeUNI.
- INNER JOIN would drop employees without a unique id, which is wrong here.

Time:  O(n + m) - with a hash join; O(n * m) worst case without one
Space: O(1) - no extra structures beyond the join itself
*/

SELECT
    eu.unique_id,
    e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu
    ON e.id = eu.id;

/*
Solved example
--------------
Employees:               EmployeeUNI:
| id | name     |        | id | unique_id |
| 1  | Alice    |        | 3  |    1      |
| 7  | Bob      |        | 11 |    2      |
| 11 | Meir     |        | 90 |    3      |
| 90 | Winston  |
| 3  | Jonathan |

Join on id:
Alice    (id 1)  -> no match   -> unique_id = NULL
Bob      (id 7)  -> no match   -> unique_id = NULL
Meir     (id 11) -> match      -> unique_id = 2
Winston  (id 90) -> match      -> unique_id = 3
Jonathan (id 3)  -> match      -> unique_id = 1

Output: (NULL, Alice), (NULL, Bob), (2, Meir), (3, Winston), (1, Jonathan)
*/
