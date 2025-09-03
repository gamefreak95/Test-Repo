SELECT
	pair,
	ROUND(AVG(received_time - event_time),4) AS average_r_e,
	ROUND(PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY received_time - event_time),4) AS "50th_percentile",
	ROUND(PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY received_time - event_time),4) AS "75th_percentile",
	ROUND(PERCENTILE_CONT(0.90) WITHIN GROUP (ORDER BY received_time - event_time),4) AS "90th_percentile",
	ROUND(PERCENTILE_CONT(0.95) WITHIN GROUP (ORDER BY received_time - event_time),4) AS "95th_percentile",
	ROUND(PERCENTILE_CONT(0.99) WITHIN GROUP (ORDER BY received_time - event_time),4) AS "99th_percentile"
FROM trades_logs
WHERE event_time IS NOT NULL
GROUP BY pair,
ORDER BY pair;