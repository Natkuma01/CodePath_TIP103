from collections import defaultdict
# ================ Problem 1 ====================
def track_screen_time(logs):
    res = {}

    for item in logs:
        if item[0] not in res:
            res[item[0]] = item[1]
        else:
            res[item[0]] += item[1]
    return res

# time complexity - O(n)
# space complexity - O(n)

print("================ Problem 1 ====================")
logs_1 = [("Instagram", 30), ("YouTube", 20), ("Instagram", 25), ("Snapchat", 15), ("YouTube", 10)]
logs_2 = [("Twitter", 10), ("Reddit", 20), ("Twitter", 15), ("Instagram", 35)]
logs_3 = [("TikTok", 40), ("TikTok", 50), ("YouTube", 60), ("Snapchat", 25)]

print(track_screen_time(logs_1))
print(track_screen_time(logs_2))
print(track_screen_time(logs_3))



# ================ Problem 2 ====================
def most_used_app(screen_time):
    return max(screen_time, key=lambda item: screen_time[item])

# time complexity - O(n)
# space complexity - O(1)

print("================ Problem 2 ====================")
screen_time_1 = {"Instagram": 55, "YouTube": 30, "Snapchat": 15}
screen_time_2 = {"Twitter": 25, "Reddit": 20, "Instagram": 35}
screen_time_3 = {"TikTok": 90, "YouTube": 90, "Snapchat": 25}

print(most_used_app(screen_time_1))
print(most_used_app(screen_time_2))
print(most_used_app(screen_time_3))


# ================ Problem 3 ====================
def most_varied_app(app_usage):
    record = {}
    for app, lst in app_usage.items():
        smallest = min(lst)
        largest = max(lst)
        record[app] = largest - smallest

    return max(record, key=lambda item: record[item])

# time complexity - O(n * m)
# space complexity - O(n)

print("================ Problem 3 ====================")
app_usage = {
    "Instagram": [60, 55, 65, 60, 70, 55, 60],
    "YouTube": [100, 120, 110, 100, 115, 105, 120],
    "Snapchat": [30, 35, 25, 30, 40, 35, 30]
}

app_usage_2 = {
    "Twitter": [15, 15, 15, 15, 15, 15, 15],
    "Reddit": [45, 50, 55, 50, 45, 50, 55],
    "Facebook": [80, 85, 80, 85, 80, 85, 80]
}

app_usage_3 = {
    "TikTok": [80, 100, 90, 85, 95, 105, 90],
    "Spotify": [40, 45, 50, 45, 40, 45, 50],
    "WhatsApp": [60, 60, 60, 60, 60, 60, 60]
}

print(most_varied_app(app_usage))
print(most_varied_app(app_usage_2))
print(most_varied_app(app_usage_3))



# ================ Problem 4 ====================
def peak_usage_hours(screen_time):
    prev, curr, nxt = 0, 1, 2
    largest = 0
    start = 0

    while nxt < len(screen_time):
        total = screen_time[prev] + screen_time[curr] + screen_time[nxt]
        if total > largest:
            largest = total
            start = prev
        prev += 1
        curr += 1
        nxt += 1

    return (start, largest)

# time complexity - O(n)
# space complexity - O(1)

print("================ Problem 4 ====================")
screen_time = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240]
screen_time_2 = [5, 15, 10, 20, 30, 25, 50, 40, 35, 45, 60, 55, 65, 75, 70, 85, 95, 90, 100, 110, 105, 115, 120, 125]
screen_time_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(peak_usage_hours(screen_time))
print(peak_usage_hours(screen_time_2))    
print(peak_usage_hours(screen_time_3)) 



# ================ Problem 5 ====================
def find_longest_repeating_pattern(app_logs):
    n = len(app_logs)
    max_count = 0
    max_pattern = []

    for i in range (n):
        for j in range (i+1, n):
            pattern = app_logs[i:j] 
            pattern_length = len(pattern)
            count = 1
        
            for k in range (j, n, pattern_length):
                if app_logs[k:k + pattern_length] == pattern:
                    count += 1
                else:
                    break
        
            if count > 1 and pattern_length * count <= n:
                if count * pattern_length > len(max_pattern) * max_count:
                    max_pattern = pattern
                    max_count = count

    return (max_pattern, max_count)

# time complexity - O(n^3)
# space complexity - O(n)

print("================ Problem 5 ====================")
app_logs = ["Instagram", "YouTube", "Snapchat", "Instagram", "YouTube", "Snapchat", "Instagram", "YouTube", "Snapchat", "Facebook", "Twitter", "Instagram"]
app_logs_2 = ["Facebook", "Instagram", "Facebook", "Instagram", "Facebook", "Instagram", "Snapchat", "Snapchat", "Snapchat", "Instagram"]
app_logs_3 = ["WhatsApp", "TikTok", "Instagram", "YouTube", "Snapchat", "Twitter", "Facebook", "WhatsApp", "TikTok", "Instagram", "YouTube", "Snapchat", "Twitter", "Facebook"]

print(find_longest_repeating_pattern(app_logs))
print(find_longest_repeating_pattern(app_logs_2))
print(find_longest_repeating_pattern(app_logs_3))




# ================ Problem 6 ====================
def manage_screen_time_sessions(actions):
    stack = []
    for item in actions:
        parts = item.split(" ")
        if parts[0] == "OPEN":
            stack.append([parts[0], parts[1]])
        else:
            if stack and parts[1] == stack[-1][1]:
                stack.pop()
            else:
                return False
    return True

# time complexity - O(n)
# space complexity - O(n)

print("================ Problem 6 ====================")
actions = ["OPEN Instagram", "OPEN Facebook", "CLOSE Facebook", "CLOSE Instagram"]
actions_2 = ["OPEN Instagram", "CLOSE Instagram", "CLOSE Facebook"]
actions_3 = ["OPEN Instagram", "OPEN Facebook", "CLOSE Instagram", "CLOSE Facebook"]

print(manage_screen_time_sessions(actions))  
print(manage_screen_time_sessions(actions_2))  
print(manage_screen_time_sessions(actions_3))



# ================ Problem 7 ====================
def analyze_weekly_usage(weekly_usage):

    total = {"Social Media": 0, "Entertainment": 0, "Productivity": 0}
    for item in weekly_usage.values():
        total["Social Media"] += item["Social Media"]
        total["Entertainment"] += item["Entertainment"]
        total["Productivity"] += item["Productivity"]
    
    total_category_usage = total
    highest_category = max(total, key=lambda item: total["Social Media"])

    busiest = ""
    max_total = 0

    for day, item in weekly_usage.items():
        total = sum(item.values())
        if total > max_total:
            max_total = total
            busiest = day
    return {"total_category_usage": total_category_usage, "busiest_day": busiest, "most_used_category": highest_category[0]}
    
# time complexity - O(n)
# space complexity - O(n)

print("================ Problem 7 ====================")
weekly_usage = {
    "Monday": {"Social Media": 120, "Entertainment": 60, "Productivity": 90},
    "Tuesday": {"Social Media": 100, "Entertainment": 80, "Productivity": 70},
    "Wednesday": {"Social Media": 130, "Entertainment": 70, "Productivity": 60},
    "Thursday": {"Social Media": 90, "Entertainment": 60, "Productivity": 80},
    "Friday": {"Social Media": 110, "Entertainment": 100, "Productivity": 50},
    "Saturday": {"Social Media": 180, "Entertainment": 120, "Productivity": 40},
    "Sunday": {"Social Media": 160, "Entertainment": 140, "Productivity": 30}
}
print(analyze_weekly_usage(weekly_usage))



# ================ Problem 8 ====================
def find_best_break_pair(break_times, target):

    i, j = 0, len(break_times)-1

    potential_break = []

    while i < j:
        if break_times[i] + break_times[j] == target:
            potential_break.append((break_times[i], break_times[j]))
            i += 1
            j -= 1
        elif break_times[i] + break_times[j] > target:
            j -= 1
        else:
            i += 1
    
    
    if len(potential_break) > 1:
        less_duration = abs(potential_break[0][1] - potential_break[0][0])
        start = 0
        end = 0
        for item in potential_break:
            if abs(item[0] - item[1]) < less_duration:
                less_duration = abs(item[0] - item[1])
                start = item[0]
                end = item[1]
        return ((start, end))
    elif not potential_break:
        return ()
    else:
        return potential_break[0]
    
# time complexity - O(n)
# space complexity - O(n)

print("================ Problem 8 ====================")
break_times = [10, 20, 35, 40, 50]
break_times_2 = [5, 10, 25, 30, 45]
break_times_3 = [15, 25, 35, 45]
break_times_4 = [30]

print(find_best_break_pair(break_times, 60))  
print(find_best_break_pair(break_times_2, 50))  
print(find_best_break_pair(break_times_3, 70))  
print(find_best_break_pair(break_times_4, 60))  