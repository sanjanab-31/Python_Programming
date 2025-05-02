# retrieve the marks of specific student    #SASIKIRAN 24CS216
a={'Ali': 90, 'Sara': 85, 'Tariq': 78, 'Aisha': 92}
b=input("Enter the name of the student:")
print(a[b])

# Count the occurence of each word using string    #SASIKIRAN 24CS216
a='apple banana apple orange banana apple'
b=a.split()
c={}
for i in b:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print(c)

# merge two dictionaries if they have same key sum    #SASIKIRAN 24CS216
a={'a':1,'b':2,'c':3}
b={'a':4,'b':5}
c={}
for i in a:
    if i in b:
        c[i]=a[i]+b[i]
    else:
        c[i]=a[i]
for i in b:
    if i not in c:
        c[i]=b[i]
print(c)


# find the character that appears the most in a string print the maximum occurs   #SASIKIRAN 24CS216
a="banana"
b={}
for i in a:
    if i in b: 
        b[i]+=1
    else:
        b[i]=1
print(max(b,key=b.get))
print(max(b.values()))

# find the key that are present in both dictionaries    #SASIKIRAN 24CS216
a={'a':1,'b':2,'c':3}
b={'a':4,'b':5}
c={}
for i in a:
    if i in b:
        c[i]=a[i]
print(c)

#Given a list of words, return the k most frequent words, sorted by frequency and
# lexicographical order.    #SASIKIRAN 24CS216
a=['i','love','leetcode','i','love','coding']
b=2
c={}
for i in a:
    if i in c:
        c[i]+=1
    else:
        c[i]=1 
sorted_words = sorted(c.keys(), key=lambda x: (-c[x], x))
print(sorted_words[:b])

# 7. Given a list of words, group anagrams together.    #SASIKIRAN 24CS216
a=["eat","tea","tan","ate","nat","bat"]
b={}
for i in a:
    c=''.join(sorted(i))
    if c in b:
        b[c].append(i)
    else:
        b[c]=[i]
print(list(b.values()))

# Real-Time Weather Data Analysis System    #SASIKIRAN 24CS216
weather_data = {
    "New York": {"Temperature": 25, "Humidity": 60, "AQI": 80},
    "London": {"Temperature": 18, "Humidity": 70, "AQI": 75},
    "Tokyo": {"Temperature": 30, "Humidity": 55, "AQI": 90}
}
best_city = min(weather_data, key=lambda city: weather_data[city]["AQI"])
print("Best Air Quality:", best_city)
max_temp_city = max(weather_data, key=lambda city: weather_data[city]["Temperature"])
min_temp_city = min(weather_data, key=lambda city: weather_data[city]["Temperature"])
print("Hottest City:", max_temp_city)
print("Coldest City:", min_temp_city)
for city, info in weather_data.items():
    if info["AQI"] > 100:
        print(f"{city}: Poor Air Quality Alert!")
    elif info["Temperature"] > 35:
        print(f"{city}: Heatwave Alert!")
    elif info["Humidity"] > 80:
        print(f"{city}: High Humidity Alert!")
    else:
        print(f"{city}: Weather is Normal")

# IoT-Based Smart Home Energy Optimization System# IoT Smart Home Energy Optimize -#SASIKIRAN 24CS216
e = {
    "LR": {"L": 50, "AC": 500, "TV": 100},"BR": {"L": 30, "AC": 600, "F": 50},"K": {"Fz": 300, "O": 200, "L": 40}
}
m = {}
for r, a in e.items():
    for n, u in a.items():
        if n in m:
            m[n] += u
        else:
            m[n] = u
mx = max(m, key=m.get)
print("Max Energy App:", mx)
print("Usage:", m[mx])
rec = {
    "L": "Use LED","AC": "Set 24°C","TV": "Turn Off Unused","F": "Use Efficient Fan","Fz": "Keep Optimal Temp","O": "Use Microwave"
}
for n in m:
    if n in rec:
        print(f"Tip for {n}: {rec[n]}")
    else:
        print(f"No Tip for {n}")
u = {
    "LR": {"TV": 100}, "BR": {"F": 50}, "K": {"O": 200}
}
for r, a in u.items():
    for n, v in a.items():
        if v < 100:
            print(f"Auto-OFF {n} in {r}")
        else:
            print(f"{n} in {r} used often")


#Automated Resume Shortlisting for Job Applications   #SASIKIRAN 24CS216
r = {
    "C1": {"S": ["Py", "AI", "ML"], "E": 5},
    "C2": {"S": ["Jv", "Cl", "DO"], "E": 3},
    "C3": {"S": ["Py", "DS", "SQL"], "E": 4}
}
print("Exp 5+ :")
for n, d in r.items():
    if d["E"] >= 5:
        print(n)
print("\nDS Role :")
for n, d in r.items():
    if "DS" in d["S"]:
        print(n)
req = ["Py", "DS", "SQL"]
print("\nSkill Rank :")
rk = {}
for n, d in r.items():
    m = len(set(d["S"]) & set(req))
    p = (m / len(req)) * 100
    rk[n] = p
for n, s in sorted(rk.items(), key=lambda x: x[1], reverse=True):
    print(f"{n} - {s}%")

# 11. Multi-Store Inventory and Auto-Restock System  #SASIKIRAN 24CS216
s= {
    "S1": {"L": {"stk": 5, "pr": 700}, "P": {"stk": 10, "pr": 500}},
    "S2": {"L": {"stk": 2, "pr": 750}, "P": {"stk": 5, "pr": 550}}
}
p = "L"
mp = 9999
sn = ""
for k, v in s.items():
    if p in v and v[p]["pr"] < mp:
        mp = v[p]["pr"]
        sn = k
print("Low Price:", sn, mp)
for k, v in s.items():
    for i, d in v.items():
        if d["stk"] < 3:
            print("Restock:", i, "at", k)


# 12. Decentralized Cryptocurrency Wallet System    #SASIKIRAN 24CS216
w = {
    "A": {"B": 0.5, "E": 2, "D": 5000},
    "B": {"B": 1, "E": 5, "D": 10000},
    "C": {"B": 0.2, "E": 1, "D": 3000}
}
r = {"B": 30000, "E": 2000, "D": 0.1}
w["A"]["B"] -= 0.1
w["B"]["B"] += 0.1
t = {}
for u, c in w.items():
    t[u] = sum(q * r[cc] for cc, q in c.items())
top = sorted(t.items(), key=lambda x: x[1], reverse=True)[:2]
print("Top:", top)

# 13. Fake News Detection Using Word Frequency Analysis #SASIKIRAN 24CS216
word_frequencies = {
    "article1": {"COVID": 10, "Vaccine": 8, "Cure": 12},
    "article2": {"Election": 15, "Fraud": 20, "Democracy": 5},
    "article3": {"Investment": 18, "Scam": 22, "Profit": 7}
}
suspicious = []
for article, words in word_frequencies.items():
    if "Fraud" in words or "Scam" in words:
        suspicious.append(article)
print("Suspicious Articles:", suspicious)

# 14. Airline Ticket Pricing and Availability System   #SASIKIRAN 24CS216
f = {
    "A1": {"E": {"s": 50, "p": 500}, "B": {"s": 10, "p": 1500}},
    "B2": {"E": {"s": 20, "p": 700}, "B": {"s": 5, "p": 2000}}
}
f["A1"]["E"]["s"] -= 1
print("Booked")
for k, v in f.items():
    for c, d in v.items():
        if d["s"] < 10:
            d["p"] *= 1.2
print(f)


# 15. Advanced Student Performance Analyticss  #SASIKIRAN 24CS216
s = {
    "A": {"M": 85, "P": 78, "C": 92},
    "B": {"M": 90, "P": 88, "C": 79},
    "C": {"M": 76, "P": 85, "C": 85}
}
for n, m in s.items():
    a = sum(m.values()) / len(m)
    print(n, "Avg:", a)
sub = ["M", "P", "C"]
for sb in sub:
    t = max(s, key=lambda x: s[x][sb])
    print("Top in", sb, ":", t)
for n, m in s.items():
    a = sum(m.values()) / len(m)
    if a < 80:
        print(n, "Improve")
