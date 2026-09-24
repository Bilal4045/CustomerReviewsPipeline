select * from reviews;
CREATE SCHEMA IF NOT EXISTS marts;


CREATE MATERIALIZED VIEW marts.score_distribution AS
SELECT score, COUNT(*) AS review_count
FROM reviews
GROUP BY score
ORDER BY score;
SELECT schema_name FROM information_schema.schemata;




CREATE MATERIALIZED VIEW marts.daily_review_volume AS
SELECT DATE_TRUNC('day', TO_TIMESTAMP(time))::DATE AS review_date,
       COUNT(*) AS review_count
FROM Reviews
GROUP BY review_date
ORDER BY review_date;


CREATE MATERIALIZED VIEW marts.monthly_review_volume AS
SELECT DATE_TRUNC('month', TO_TIMESTAMP(time))::DATE AS review_month,
       COUNT(*) AS review_count,
       ROUND(AVG(score), 2) AS avg_score
FROM Reviews
GROUP BY review_month
ORDER BY review_month;




CREATE MATERIALIZED VIEW marts.top_products AS
SELECT product_id,
       COUNT(*) AS review_count,
       ROUND(AVG(score), 2) AS avg_score
FROM reviews
GROUP BY product_id
HAVING COUNT(*) >= 10
ORDER BY avg_score DESC, review_count DESC
LIMIT 50;

CREATE MATERIALIZED VIEW marts.worst_products AS
SELECT product_id,
       COUNT(*) AS review_count,
       ROUND(AVG(score), 2) AS avg_score
FROM reviews
GROUP BY product_id
HAVING COUNT(*) >= 10
ORDER BY avg_score ASC, review_count DESC
LIMIT 50;

CREATE MATERIALIZED VIEW marts.most_reviewed_products AS
SELECT product_id,
       COUNT(*) AS review_count,
       ROUND(AVG(score), 2) AS avg_score
FROM reviews
GROUP BY product_id
ORDER BY review_count DESC
LIMIT 50;





CREATE MATERIALIZED VIEW marts.top_reviewers AS
SELECT user_id,
       MAX(profile_name) AS profile_name,
       COUNT(*) AS review_count,
       ROUND(AVG(score), 2) AS avg_score_given
FROM reviews
GROUP BY user_id
ORDER BY review_count DESC
LIMIT 50;



CREATE MATERIALIZED VIEW marts.most_helpful_reviews AS
SELECT id, product_id, user_id, profile_name, score,
       helpfulness_numerator, helpfulness_denominator,
       ROUND(helpfulness_numerator::NUMERIC / NULLIF(helpfulness_denominator, 0), 2) AS helpfulness_ratio,
       summary
FROM reviews
WHERE helpfulness_denominator >= 5
ORDER BY helpfulness_ratio DESC, helpfulness_denominator DESC
LIMIT 50;















CREATE MATERIALIZED VIEW marts.summary_stats AS
SELECT COUNT(*) AS total_reviews,
       COUNT(DISTINCT product_id) AS total_products,
       COUNT(DISTINCT user_id) AS total_users,
       ROUND(AVG(score), 2) AS overall_avg_score,
       MIN(TO_TIMESTAMP(time))::DATE AS earliest_review,
       MAX(TO_TIMESTAMP(time))::DATE AS latest_review
FROM reviews;




SELECT schemaname, matviewname FROM pg_matviews WHERE schemaname = 'marts';

select * from marts.top_products