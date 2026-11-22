import os

T = "Sell AI-written Etsy/Shopify listing rewrites at $15 each. Day 1: $0 spend; find 40 stores with thin descriptions, email each a free rewritten sample + Stripe link. Send 40/day, deliver in 1h by LLM API (~$0.02). Reinvest profit in outreach."
assert 1 <= len(T) <= 280, len(T)
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(T)
