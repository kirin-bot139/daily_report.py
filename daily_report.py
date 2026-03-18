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
- Supermarket / bakery / chain store expansion trends
- Sustainability and packaging demand in Europe
- Energy efficiency regulations affecting refrigeration equipment

==================================================
3. Trade Risk & Policy Reminder
==================================================
Please monitor:
- EU / US product compliance changes
- CE / UL / food-contact / energy-efficiency related updates
- Freight / port congestion / customs delays
- Tariff changes and trade barriers
- Geopolitical risks affecting shipment or payment

Action principle:
- Turn every policy change into a business impact note
- Turn every business impact note into a customer communication option

==================================================
4. Follow-up Topics for Customers
==================================================
Topic A: Market trend update
Use for: silent customers / quoted customers
Purpose: re-open conversation naturally

Topic B: Industry demand shift
Use for: traders / wholesalers / brand customers
Purpose: build professionalism and create relevance

Topic C: Compliance / delivery / risk reminder
Use for: project customers / chain customers / factories
Purpose: show responsibility and reduce uncertainty

==================================================
5. English Outreach Sample
==================================================
Subject: A quick market update that may be relevant to your planning

Hi [Name],

I wanted to share a quick update from the market that may be relevant to your current planning.

We have seen some recent changes in [industry / logistics / pricing / compliance], which could have an impact on purchasing decisions, delivery expectations, or cost planning in the coming weeks.

If useful, I’d be happy to share a brief update from our side and see whether there is anything we can support for your current projects or sourcing plans.

Best regards,
[Your Name]

==================================================
6. Today’s Priority Actions
==================================================
1. Follow up with silent quoted customers using a market-update angle
2. Review Europe-focused products for compliance / energy-efficiency messaging
3. Prioritize prospects in retail, chain-store, hospitality, and foodservice sectors
Watch for opportunities to connect product news with customer-specific needs
==================================================7. Holiday / Human-touch Reminder
Check whether today or this week contains any important holidays in Europe or North America
If yes, adjust outreach timing
Add short human-touch messages where appropriate
Regards,
Your Foreign Trade Intelligence Assistant
"""
return report.strip()

if name == "main":
print(build_report())
