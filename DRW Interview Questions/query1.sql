Select
acc.AccountName,
ins.DisplaySymbol,
SUM(CASE WHEN fil.Side = 'B' THEN fil.Quantity ELSE 0 END) AS BuyQuantity,
CASE
	WHEN SUM(CASE WHEN fil.Side = 'B' THEN fil.Quantity ELSE 0 END) = 0
	THEN 0
	ELSE SUM(CASE WHEN fil.Side = 'B' THEN fil.Price * fil.Quantity ELSE 0 END)/
	SUM(CASE WHEN fil.Side = 'B' THEN fil.Quantity ELSE 0 END) END AS BuyAveragePrice,
SUM(CASE WHEN fil.Side = 'S' THEN fil.Quantity ELSE 0 END) AS SellQuantity,
CASE
	WHEN SUM(CASE WHEN fil.Side = 'S' THEN fil.Quantity ELSE 0 END) = 0
	THEN 0
	ELSE SUM(CASE WHEN fil.Side = 'S' THEN fil.Price * fil.Quantity ELSE 0 END)/
	SUM(CASE WHEN fil.Side = 'S'THEN fil.Quantity ELSE 0 END) END AS SellAveragePrice,
te.Team
from dbo.Fills as fil
INNER JOIN dbo.Accounts as acc on fil.AccountId = acc.AccountId
INNER JOIN dbo.Instruments as ins ON fil.InstrumentId = ins.InstrumentId
INNER JOIN dbo.Traders as te ON fil.TraderId = te.TraderId
GROUP BY
    acc.AccountName,
	ins.DisplaySymbol,
    te.Team
ORDER BY
    te.Team,
    ins.DisplaySymbol DESC;
