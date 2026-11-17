/*
1757. Recyclable and Low Fat Products  (Easy)
https://leetcode.com/problems/recyclable-and-low-fat-products/

Approach
--------
- WHERE filters rows one by one before they are returned.
- AND keeps a row only if BOTH conditions are true.
- SELECT then picks just the product_id column.

Time:  O(n) - every row is checked once
Space: O(1) - no extra structures
*/

-- Write your PostgreSQL query statement below
SELECT product_id
FROM Products
WHERE low_fats = 'Y'
  AND recyclable = 'Y';

/*
Solved example
--------------
Products:
| product_id | low_fats | recyclable |
|     0      |    Y     |     N      |  -> recyclable fails, skip
|     1      |    Y     |     Y      |  -> both pass, keep
|     2      |    N     |     Y      |  -> low_fats fails, skip
|     3      |    Y     |     Y      |  -> both pass, keep
|     4      |    N     |     N      |  -> both fail, skip

Output: product_id = 1, 3
*/
