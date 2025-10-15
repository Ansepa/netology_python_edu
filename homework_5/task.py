import csv
import json

purchase_dict = {}
with open("purchase_log.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            data = json.loads(line)
            user_id = data["user_id"]
            category = data["category"]
            purchase_dict[user_id] = category
with open("./visit_log.csv", "r", encoding="utf-8") as visits_file, \
     open("./funnel.csv", "w", encoding="utf-8", newline="") as funnel_file:

    reader = csv.reader(visits_file)
    writer = csv.writer(funnel_file)

    writer.writerow(["user_id", "source", "category"])

    next(reader)

    for row in reader:
        user_id = row[0]
        source = row[1]
        if user_id in purchase_dict:
            category = purchase_dict[user_id]
            writer.writerow([user_id, source, category])
