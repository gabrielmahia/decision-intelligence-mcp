# classical-strategy-mcp

**5,000 years of military strategy, philosophy, and decision science — as AI-accessible tools.**



---
**Compatible with `claude-sonnet-5`** (released 2026-06-30)
---

An MCP (Model Context Protocol) server exposing structured public domain knowledge from history's greatest strategic thinkers. Connect to Claude, GPT, or any MCP-compatible AI assistant and access the complete strategic literature of human civilization.

## Commanders and Thinkers

| Commander | Dates | Signature Doctrine | Source |
|-----------|-------|-------------------|--------|
| Sun Tzu | ~500 BC | Supreme excellence: win without fighting | Art of War (PD) |
| Julius Caesar | 100-44 BC | Speed + fortification + political intelligence | Gallic Wars (PD) |
| Hannibal Barca | 247-183 BC | Cannae double envelopment | Polybius, Livy (PD) |
| Alexander the Great | 356-323 BC | Hammer and anvil, oblique approach | Arrian, Plutarch (PD) |
| Julius Caesar | 100-44 BC | Speed, engineering, clemency as weapons | De Bello Gallico (PD) |
| Napoleon Bonaparte | 1769-1821 | Corps system, central position, decisive battle | 115 Maxims (PD) |
| Carl von Clausewitz | 1780-1831 | Fog, friction, center of gravity, culminating point | On War (PD) |
| Frederick the Great | 1712-1786 | Oblique order, interior lines | Instructions for His Generals (PD) |
| Shaka Zulu | 1787-1828 | Iklwa, bull-horn formation, amabutho system | Isaacs, Fynn (PD) |
| Genghis Khan | 1162-1227 | Yam intelligence, feigned retreat, total warfare | Secret History (PD) |

## Tools

```python
napoleon_maxims(category="strategy")         # 115 maxims, filterable
sun_tzu(chapter=3)                            # Art of War by chapter
commander_doctrine(commander="hannibal")      # Doctrine deep-dive
apply_strategy(problem="...", lens="competition")  # Apply to modern problem
public_domain_library(domain="military")      # Full bibliography
```

## Quick Start

```bash
pip install classical-strategy-mcp

# Claude Code
claude mcp add strategy -- classical-strategy-mcp

# Or run directly
classical-strategy-mcp
```

## What This Is Not

This is a research and analytical tool. Public domain military history for:
- Strategic analysis and decision frameworks
- Historical research and education
- Leadership and organizational thinking
- Competitive strategy and planning

Not for operational military planning.

## The Public Domain Opportunity

Every work cited here is in the public domain. The content is free. The value is in:
- Structured access (not raw text scanning)
- AI-native interfaces (not PDFs)
- Synthesis across traditions (not single-source)
- Modern application frameworks (not historical trivia)

This is the model for the next wave of knowledge infrastructure.

## All Sources — Public Domain

- Napoleon's Maxims (1831)
- Clausewitz, On War / Vom Kriege (1832)
- Caesar, De Bello Gallico (58-50 BC)
- Arrian, Anabasis of Alexander (~130 AD)
- Polybius, Histories (~150 BC)
- Livy, History of Rome (27 BC-17 AD)
- Sun Tzu, The Art of War (~500 BC)
- Frederick the Great, Instructions for His Generals (1747)
- Vegetius, Epitome Rei Militaris (~390 AD)
- Thucydides, History of the Peloponnesian War (~400 BC)
- Nathaniel Isaacs, Travels in Eastern Africa (1836) — Shaka Zulu
- Henry Francis Fynn, Diary (1830s)
- Anonymous, The Secret History of the Mongols (~1240)
- Juvaini, History of the World-Conqueror (1260)
- Marcus Aurelius, Meditations (~170-180 AD)
- Machiavelli, The Prince (1532) and Art of War (1521)
- Seneca, Letters from a Stoic (~65 AD)
- Epictetus, Enchiridion (~135 AD)

---

**Part of the [East Africa AI coordination infrastructure](https://github.com/gabrielmahia)**
*Public domain as raw material. AI as the refinery. Knowledge as the product.*

## Part of the East Africa Coordination Stack

This MCP server is one of 32 tools in the Kenya coordination infrastructure.
Connect it to [`africa-coord-bus`](https://github.com/gabrielmahia/africa-coord-bus) —
the coordination event bus that routes signals between domains automatically.

```bash
pip install africa-coord-bus
```

All 32 servers: [pypi.org/user/gmahia](https://pypi.org/user/gmahia/)
Live demo: [coord-cascade-demo](https://github.com/gabrielmahia/coord-cascade-demo)