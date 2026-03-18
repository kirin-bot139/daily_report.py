from datetime import datetime

def build_report():
today = datetime.utcnow().strftime("%Y-%m-%d")

report = f"""
Subject: Daily Foreign Trade Brief | {today}

Good morning, Chen,

Here is your daily foreign trade brief.

==================================================
1. Exchange Rate & Pricing Watch
==================================================
- USD / EUR / GBP: Please update with real-time exchange rate data
- Suggested action:
- Review whether quotation validity should be shortened
- Monitor exchange fluctuation impact on margin
- Re-check conversion sensitivity for Europe/US orders

==================================================
2. Industry Opportunity Signals
==================================================
Product focus:
- Delivery robots
- Reception robots
- Non-woven bags
- Commercial refrigerators / freezers
- Cake display cabinets
- Ice makers

Suggested daily tracking directions:
- Robotics adoption in retail / hospitality / healthcare / logistics
- Foodservice equipment replacement demand
