from datetime import datetime
import json

def foo(data):
    events = json.loads(data)
    durations = []
    for event in events:
        start_date = datetime.strptime(event['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(event['end_date'], '%Y-%m-%d')
        duration = (end_date - start_date).days + 1
        durations.append(duration)
    return durations


if __name__ == '__main__':
    data = '''[
        {
            "name": "Event 1",
            "start_date": "2022-01-01",
            "end_date": "2022-01-05"
        },
        {
            "name": "Event 2",
            "start_date": "2022-02-15",
            "end_date": "2022-02-18"
        },
        {
            "name": "Event 3",
            "start_date": "2022-03-10",
            "end_date": "2022-03-20"
        }
    ]'''
print(foo(data))
