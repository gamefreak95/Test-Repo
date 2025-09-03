WITH

LastFillTimes AS (
SELECT
CONVERT(date, fil1.FillTime) AS TradeDate,
fil1.InstrumentId,
MAX(fil1.FillTime) AS LastFillTime
FROM dbo.Fills as fil1
WHERE CONVERT(date, fil1.FillTime) = CONVERT(date, GETDATE())
GROUP BY
	CONVERT(date, fil1.FillTime),
	fil1.InstrumentId
),

ClosingPrices AS (
SELECT
lft.TradeDate,
lft.InstrumentId,
fil2.Price AS ClosingPrice
FROM LastFillTimes AS lft
INNER JOIN dbo.Fills AS fil2 ON fil2.InstrumentId = lft.InstrumentId
AND CONVERT(date, fil2.FillTime) = lft.TradeDate
AND fil2.FillTime = lft.LastFillTime),

NetPositions AS (
SELECT CONVERT(date, fil.FillTime) AS TradeDate,
fil.InstrumentId,
fil.AccountId,
SUM(CASE
		WHEN fil.Side = 'B' THEN  fil.Quantity
		WHEN fil.Side = 'S' THEN -fil.Quantity
		ELSE 0
	END) AS NetQty
FROM dbo.Fills AS fil
WHERE CONVERT(date, fil.FillTime) = CONVERT(date, GETDATE())
GROUP BY
	CONVERT(date, fil.FillTime),
	fil.InstrumentId,
	fil.AccountId)

SELECT
	NetPos.TradeDate,
	NetPos.InstrumentId,
	NetPos.AccountId,
	NetPos.NetQty AS Quantity,
	(NetPos.NetQty * ClPr.ClosingPrice) AS EodPositionMark
FROM NetPositions AS NetPos
INNER JOIN
ClosingPrices AS ClPr
ON ClPr.TradeDate = NetPos.TradeDate
AND ClPr.InstrumentId = NetPos.InstrumentId
WHERE NetPos.NetQty != 0
ORDER BY
	NetPos.TradeDate,
	NetPos.InstrumentId,
	NetPos.AccountId