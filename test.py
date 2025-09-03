import json
from collections import defaultdict

def parse_the_lines(line):
    try:
        parts = line.strip().split('|')

        recieved_time = float(parts[0])
        log_from_json = json.loads(parts[4])

        event_time = log_from_json.get('event_time')
        pair = log_from_json.get('pair')
        exchange = log_from_json.get('exchange')

        if event_time is None or pair is None or exchange is None:
            return None

        delay_milliseconds = (recieved_time - event_time) * 1000
        return pair, exchange, delay_milliseconds

    except:
       return None

#Store the R-E values by (symbol, exchange)
stored_data = defaultdict(list)

with open('D:\\trades.log\\trades.log') as f:
    for line in f:
        parsed = parse_the_lines(line)
        if parsed:
            pair, exchange, delay_milliseconds = parsed
            stored_data[(pair,exchange)].append(delay_milliseconds)

#Calculate the percentiles
def get_percentiles(values,percent):
    values = sorted(values)
    calculations = int(len(values) * (percent/100))
    return values[min(calculations, len(values)-1)]

#Output
for(pair,exchange),delay_milliseconds in stored_data.items():
    average = sum(delay_milliseconds) / len(delay_milliseconds)
    print(f"\nPair&Exchange: {pair}:{exchange}")
    print(f"Average R-E: {average} milliseconds")
    print("Percentiles:")
    for percents in [50,75,90,95,99]:
        values = get_percentiles(delay_milliseconds, percents)
        print(f"{percents}th {values}ms")