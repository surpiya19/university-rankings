-- ============================================================
-- PROOF OF CRUD OPERATIONS ON university_rankings DATABASE
-- ============================================================

-- 1. SELECT — Retrieve the top 5 universities in 2015
SELECT institution, country, world_rank, score
FROM university_rankings
WHERE year = 2015
ORDER BY score DESC
LIMIT 5;


-- 2. SELECT (COUNT) — Count Japanese universities ranked in the top 200 in 2013
SELECT COUNT(*) AS japan_top200
FROM university_rankings
WHERE country = 'Japan'
  AND year = 2013
  AND world_rank <= 200;


-- 3. INSERT — Add a new record for "Duke Tech" (2014)
INSERT INTO university_rankings (institution, country, world_rank, score, year)
VALUES ('Duke Tech', 'USA', 350, 60.5, 2014);

-- 🔍 Proof of INSERT
SELECT *
FROM university_rankings
WHERE institution = 'Duke Tech' AND year = 2014;


-- 4. UPDATE — Increase University of Oxford’s 2014 score by 1.2
UPDATE university_rankings
SET score = score + 1.2
WHERE institution = 'University of Oxford'
  AND year = 2014;

-- 🔍 Proof of UPDATE
SELECT institution, year, score
FROM university_rankings
WHERE institution = 'University of Oxford'
  AND year = 2014;


-- 5. DELETE — Make it visible by temporarily adding a low-score 2015 university
INSERT INTO university_rankings (institution, country, world_rank, score, year)
VALUES ('Test University', 'USA', 999, 40, 2015);

-- Before deletion: count low-score 2015 universities
SELECT COUNT(*) AS before_delete_count
FROM university_rankings
WHERE year = 2015 AND score < 45;

-- Perform the deletion
DELETE FROM university_rankings
WHERE year = 2015 AND score < 45;

-- After deletion: confirm rows removed
SELECT COUNT(*) AS after_delete_count
FROM university_rankings
WHERE year = 2015 AND score < 45;

-- 🔍 Proof: show that "Test University" is gone
SELECT *
FROM university_rankings
WHERE institution = 'Test University' AND year = 2015;

-- ============================================================
-- END OF CRUD PROOF
-- ============================================================
