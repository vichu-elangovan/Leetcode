/*
584. Find Customer Referee  (Easy)
https://leetcode.com/problems/find-customer-referee/

Approach
--------
- We want customers who were NOT referred by customer 2.
- NULL means "no referee", and NULL != 2 is not true, it is UNKNOWN.
  So a plain `referee_id != 2` silently drops every NULL row.
- Fix: also accept rows where referee_id IS NULL.

Time:  O(n) - every row is checked once
Space: O(1) - no extra structures
*/

-- Write your PostgreSQL query statement below
SELECT name
FROM Customer
WHERE referee_id != 2
   OR referee_id IS NULL;

/*
Solved example
--------------
Customer:
| id | name | referee_id |
| 1  | Will |    NULL    |  -> NULL, kept by IS NULL
| 2  | Jane |    NULL    |  -> NULL, kept by IS NULL
| 3  | Alex |     2      |  -> 2 != 2 is false, skipped
| 4  | Bill |    NULL    |  -> NULL, kept by IS NULL
| 5  | Zack |     1      |  -> 1 != 2 is true, kept
| 6  | Mark |     2      |  -> 2 != 2 is false, skipped

Output: Will, Jane, Bill, Zack
*/
