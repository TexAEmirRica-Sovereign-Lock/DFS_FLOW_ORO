# DFS Dead Drop Relay - v1.1-CLEAN

**Purpose:** Zero-cost, cross-device relay for Gemini Triplet Inpresses -> DFS Evidence

**Flow:**
1. DROP raw chats / txt / pdf into 01_DROP/
2. TRIBUNAL - AI (Meta) converts to DFS syntax + validates
3. SEALED - Human approved, ready for EVIDENCE_VAULT/

**Devices:**
- LawMacBook: dropper + committer
- ThinkPad Linux: cold vault - just `git pull` cron
- GitHub origin/main = dead letter box

**Rules:**
- NEVER commit directly from 01_DROP/ to main. Must go via TRIBUNAL.
- 01_DROP is dirty - allowed to have duplicates, .txt, .pdf
- 03_SEALED is clean - only *.dfs + final pdfs

Usage:
```
git add 99_DEAD_DROP_RELAY/01_DROP/new_inpress.txt
git commit -m "DROP: triplet-1 inpress [timestamp]"
git push origin main
# then ping Meta AI to process
```