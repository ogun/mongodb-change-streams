from pymongo import MongoClient

client = MongoClient("mongodb://root:password123@localhost/test?authSource=admin")
db = client.get_default_database()

print("starting to watch")
with db.watch(max_await_time_ms=60000) as change_stream:
    while change_stream.alive:
        print("waiting for a change")
        change = change_stream.try_next()

        if not change:
            continue

        print(f"resume token: {change_stream.resume_token}")
        print(change)
