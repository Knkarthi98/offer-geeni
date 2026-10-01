import os, json, requests, feedparser

FEED = "https://www.reddit.com/r/deals/.rss"
TOKEN, CHAT = os.environ["BOT_TOKEN"], os.environ["CHAT_ID"]
SEEN_FILE = "seen.json"

seen = set(json.load(open(SEEN_FILE))) if os.path.exists(SEEN_FILE) else set()
new = [e for e in feedparser.parse(FEED).entries[:10] if e.link not in seen]

for e in new:
    requests.post(
        f"https://api.telegram.org/bot{TOKEN}/sendMessage",
        data={"chat_id": CHAT, "text": f"🔥 {e.title}\n{e.link}"},
    )
    seen.add(e.link)

json.dump(list(seen)[-200:], open(SEEN_FILE, "w"))
