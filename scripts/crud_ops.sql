-- ===========================================
-- University Rankings - CRUD Operations
-- ===========================================
-- Author: Supriya
-- Description: SQL version of the operations performed in query.py
-- ===========================================

-- 1. READ: Top 5 universities in 2015
SELECT institution, country, world_rank, score
FROM university_rankings
WHERE year = 2015
ORDER BY score DESC
LIMIT 5;

-- -------------------------------------------

-- 2. READ: Count of Japanese universities in top 200 (2013)
SELECT COUNT(*) AS japan_top200
FROM university_rankings
WHERE country = 'Japan'
  AND year = 2013
  AND world_rank <= 200;

-- -------------------------------------------

-- 3. INSERT: Add Duke Tech (2014)
INSERT INTO university_rankings (institution, country, world_rank, score, year)
VALUES ('Duke Tech', 'USA', 350, 60.5, 2014);

-- -------------------------------------------

-- 4. UPDATE: Increase University of Oxford's 2014 score by +1.2
UPDATE university_rankings
SET score = score + 1.2
WHERE institution = 'University of Oxford'
  AND year = 2014;

-- -------------------------------------------

-- 5. DELETE: Remove universities with score < 45 in 2015
DELETE FROM university_rankings
WHERE year = 2015
  AND score < 45;

-- -------------------------------------------

-- 6. READ (Optional): View updated top 5 universities in 2015
SELECT institution, country, world_rank, score
FROM university_rankings
WHERE year = 2015
ORDER BY score DESC
LIMIT 5;
