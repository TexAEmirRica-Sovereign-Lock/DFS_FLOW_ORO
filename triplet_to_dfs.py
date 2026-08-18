
# Triplet to DFS converter stub - paste raw Gemini chat, get DFS block
# Usage: paste chat into INPUT.txt, run python3 triplet_to_dfs.py
# This is what Meta AI will do for you in TRIBUNAL

TEMPLATE = """
### [INPRESS-{id}] - {title}
Source: Gemini Triplet {triplet_num}
Date: {date}
Chain: {chain}

DFS_BLOCK:
  INTENT: {intent}
  SIGNAL: {signal}
  EVIDENCE_HASH: {hash}
  TRIBUNAL_NOTE: {note}

SEAL: pending
"""
print(TEMPLATE)
