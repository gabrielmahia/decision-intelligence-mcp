"""
classical-strategy-mcp — 5,000 Years of Military Strategy and Philosophy
as AI-Accessible Tools

Public domain knowledge, structured for AI agents.

Commanders:
  Napoleon Bonaparte   (1769-1821) — 115 maxims, campaign analysis
  Sun Tzu             (~500 BC)   — 13 chapters, 36 stratagems
  Carl von Clausewitz  (1780-1831) — On War, fog of war, center of gravity
  Alexander the Great  (356-323 BC) — Combined arms, oblique approach
  Hannibal Barca       (247-183 BC) — Cannae, double envelopment
  Genghis Khan         (1162-1227)  — Psychological warfare, Mongol doctrine
  Shaka Zulu           (1787-1828)  — Iklwa, bull-horn formation, total warfare
  Julius Caesar        (100-44 BC)  — Commentarii, Gallic campaigns
  Machiavelli          (1469-1527)  — The Prince, Art of War
  Clausewitz           (1780-1831)  — Friction, culminating point, center of gravity
  Thucydides           (460-400 BC) — History of the Peloponnesian War
  Vegetius             (~4th C AD)  — Epitome Rei Militaris
  Frederick the Great  (1712-1786)  — Instructions for His Generals

All source material is in the public domain.
"""
from __future__ import annotations

import json
import pathlib
from typing import Annotated

from fastmcp import FastMCP

mcp = FastMCP(
    name="classical-strategy-mcp",
    instructions=(
        "Access 5,000 years of military strategy, philosophy, and decision science. "
        "Sources include Napoleon\'s Maxims, Sun Tzu\'s Art of War, Clausewitz\'s On War, "
        "Caesar\'s Commentarii, and accounts of Alexander, Hannibal, Genghis Khan, and Shaka Zulu. "
        "All content is public domain. Use for strategic analysis, decision frameworks, "
        "historical research, and cross-cultural leadership study."
    ),
)

_DATA = pathlib.Path(__file__).parent / "data"


def _load(filename: str) -> dict:
    path = _DATA / filename
    if path.exists():
        return json.loads(path.read_text())
    return {}


@mcp.tool(
    description=(
        "Get Napoleon Bonaparte\'s Military Maxims — 115 principles distilled from "
        "20+ years of campaign experience. The most concentrated body of military wisdom "
        "from any commander in the modern era. Use for strategic planning, logistics, "
        "speed of decision, and concentration of force."
    )
)
def napoleon_maxims(
    category: Annotated[str, "Filter by category: 'strategy'|'tactics'|'logistics'|'leadership'|'intelligence'|'all'"] = "all",
    maxim_number: Annotated[int, "Get a specific maxim by number (1-115). 0 = return all."] = 0,
) -> dict:
    data = _load("napoleon_maxims.json")
    maxims = data.get("maxims", [])
    if maxim_number > 0:
        return next((m for m in maxims if m.get("number") == maxim_number), {"error": f"Maxim {maxim_number} not found"})
    if category != "all":
        maxims = [m for m in maxims if m.get("category","").lower() == category.lower()]
    return {"commander": "Napoleon Bonaparte", "source": "Maximes de Guerre (1831, public domain)",
            "count": len(maxims), "maxims": maxims}


@mcp.tool(
    description=(
        "Get Sun Tzu\'s Art of War — 13 chapters on strategy, intelligence, deception, "
        "and the nature of conflict. The oldest continuously studied strategic text. "
        "Applies to competitive analysis, negotiation, organizational strategy, "
        "and any domain of structured competition."
    )
)
def sun_tzu(
    chapter: Annotated[int, "Chapter number 1-13. 0 = all chapters."] = 0,
    concept: Annotated[str, "Search for a specific concept (e.g. 'deception', 'intelligence', 'terrain')"] = "",
) -> dict:
    data = _load("sun_tzu.json")
    chapters = data.get("chapters", [])
    if chapter > 0:
        return next((c for c in chapters if c.get("number") == chapter), {"error": "Chapter not found"})
    if concept:
        results = []
        for ch in chapters:
            for verse in ch.get("verses", []):
                if concept.lower() in verse.get("text", "").lower():
                    results.append({"chapter": ch.get("title"), "verse": verse.get("number"), "text": verse.get("text")})
        return {"concept": concept, "results": results}
    return {"work": "The Art of War", "author": "Sun Tzu", "date": "~500 BC",
            "source": "Public domain translation", "chapters": chapters}


@mcp.tool(
    description=(
        "Analyze a commander\'s signature tactical innovation — the battle doctrine that "
        "made them historically decisive. Covers: Napoleon (corps system, central position), "
        "Alexander (hammer and anvil), Hannibal (Cannae encirclement), "
        "Genghis Khan (feigned retreat + Mongol doctrine), Shaka Zulu (bull-horn formation), "
        "Caesar (fortification + speed), Frederick the Great (oblique order)."
    )
)
def commander_doctrine(
    commander: Annotated[str, "Commander name: napoleon|alexander|hannibal|genghis|shaka|caesar|sun_tzu|clausewitz|frederick"] = "napoleon",
) -> dict:
    DOCTRINES = {
        "napoleon": {
            "commander": "Napoleon Bonaparte", "dates": "1769-1821", "nationality": "French/Corsican",
            "signature_innovation": "Corps system + central position strategy",
            "doctrine": {
                "corps_system": "Divided army into self-sufficient corps (15,000-30,000 men), each able to operate independently for 24-48 hours. Enabled strategic dispersal and rapid concentration — live off the land, unite for battle.",
                "central_position": "When outnumbered by multiple enemy forces, maneuver between them. Defeat each in detail before they can unite. Speed and interior lines compensate for numbers.",
                "decisive_battle": "War decided by single overwhelming engagement (bataille decisive). Economy of force elsewhere, maximum force at the schwerpunkt (point of decision).",
                "logistics_doctrine": "Army lives off the land. Speed replaces supply lines. An army marches on its stomach — but faster than an army that carries its stomach.",
                "intelligence": "Cavalry screen, civilian informants, newspaper reading. Always know where the enemy is. Never let the enemy know where you are.",
            },
            "decisive_campaigns": ["Italian Campaign 1796-97", "Austerlitz 1805", "Jena-Auerstedt 1806"],
            "maxims_on_doctrine": ["Maxim 25: Never fight against concentrated enemy forces when dispersed", "Maxim 78: The transition from defence to attack is the moment of greatest danger"],
            "modern_applications": ["Startup strategy: small fast teams vs. large slow competitors", "Supply chain: lean inventory + fast response", "Management: decentralized execution, centralized intent"],
            "source": "Napoleon's Maxims (1831, PD); Jomini's Summary of the Art of War (1838, PD)"
        },
        "hannibal": {
            "commander": "Hannibal Barca", "dates": "247-183 BC", "nationality": "Carthaginian",
            "signature_innovation": "Double envelopment — Battle of Cannae (216 BC)",
            "doctrine": {
                "cannae_principle": "Intentional center weakness draws enemy in. Strong flanks envelop. Enemy is surrounded on all sides — unable to maneuver, cannot use numerical superiority. 70,000 Romans killed in 6 hours by 50,000 Carthaginians.",
                "combined_arms": "Iberian and Gallic infantry (center), African veteran infantry (wings), Numidian and Spanish cavalry. Each element had a defined role. Integration not substitution.",
                "psychological_warfare": "Crossed Alps in 15 days — deemed impossible. Psychological shock preceded every battle. The impossible move creates irreversible advantage.",
                "intelligence": "Knew Roman terrain, Roman political vulnerabilities, Italian ally resentments. Exploited the seam between Roman citizens and Italian allies.",
                "strategic_patience": "Operated in Italy 15 years without supply from Carthage. Self-sustaining army through foraging and allied support.",
            },
            "decisive_campaigns": ["Trebia 218 BC", "Lake Trasimene 217 BC", "Cannae 216 BC"],
            "modern_applications": ["Competitive strategy: appear weak in one area to draw competitor, overwhelm on flanks", "Negotiations: apparent concession that creates strategic encirclement", "Product: entry market looks weak (center), builds from flanks (ecosystem)"],
            "source": "Polybius, Histories (PD); Livy, History of Rome (PD)"
        },
        "genghis": {
            "commander": "Temujin / Genghis Khan", "dates": "1162-1227", "nationality": "Mongol",
            "signature_innovation": "Total operational system: intelligence + speed + psychological warfare + feigned retreat",
            "doctrine": {
                "intelligence_network": "Yam (horse relay) system: intelligence traveled 200+ miles/day. Knew enemy positions, politics, terrain before engaging. Never fought blind.",
                "feigned_retreat": "Mongol cavalry retreats convincingly, drawing enemy cavalry in pursuit. Enemy formation breaks. Mongols reform. Heavy cavalry destroys disordered pursuit. Used at Mohi, Legnica, Kalka River.",
                "psychological_warfare": "Surrender = mercy. Resist = total destruction (and its announcement). Reputation for absolute consequence made many cities open gates without siege.",
                "speed_of_advance": "Mongol army moved 60-80 miles/day (vs. European 15-20). Multiple columns operating simultaneously. Enemy could not concentrate before being destroyed in detail.",
                "decimal_organization": "Arban (10), Zuun (100), Myanghan (1,000), Tumen (10,000). Meritocratic. No tribal loyalty — loyalty to the organization. Revolutionary for 1206.",
                "logistics": "Each warrior had 3-5 horses. Lived on dried meat, blood. No supply lines needed. Army was self-contained.",
            },
            "decisive_campaigns": ["Unification of Mongolia 1206", "Jin Dynasty 1211-1234", "Khwarezm 1219-1221"],
            "modern_applications": ["Information warfare: intelligence as primary weapon", "Organizational design: decimal, meritocratic, no clan loyalty", "Competitive speed: 3-5x pace creates structural advantage"],
            "source": "The Secret History of the Mongols (13th C, PD); Juvaini, History of the World-Conqueror (PD)"
        },
        "shaka": {
            "commander": "Shaka kaSenzangakhona (Shaka Zulu)", "dates": "1787-1828", "nationality": "Zulu, Southern Africa",
            "signature_innovation": "Iklwa + bull-horn formation + total warrior system",
            "doctrine": {
                "iklwa": "Replaced the long throwing assegai with the short stabbing iklwa (50cm blade) plus large cowhide shield. Forces close combat. Negates enemy ranged advantage. Complete tactical paradigm shift.",
                "bull_horn_formation": "Chest (isifuba): engages the enemy frontally, fixes their position. Horns (izimpondo): two flanking columns encircle. Loins (umuva): reserve, prevents enemy retreat and reinforcement. Three-dimensional battle management with messengers, signal systems.",
                "age_regiment_system": "Age-based regiments (amabutho). Warriors trained together from youth, compete against other regiments. Intense unit cohesion. Regiments had distinct identities, colors, praise songs.",
                "total_transformation": "Transformed the Zulu from one of many small Nguni chiefdoms into the dominant military power of southern Africa within 12 years. Comparable transformation in scale to Napoleon's reorganization of French armies.",
                "psychological_system": "Regiments permitted to marry only after distinguished battle service. Creates warrior culture where combat prowess has direct social reward.",
            },
            "decisive_campaigns": ["Consolidation of Zulu kingdom 1816-1828", "Defeat of Ndwandwe 1819", "Mfecane campaigns expanding Zulu territory"],
            "modern_applications": ["Organizational transformation: total system change, not incremental", "Team building: cohort-based development, peer competition drives excellence", "Product design: simplify the tool, increase lethality (iklwa principle)"],
            "source": "Henry Francis Fynn, The Diary of Henry Francis Fynn (PD); Nathaniel Isaacs, Travels and Adventures in Eastern Africa (1836, PD)"
        },
        "alexander": {
            "commander": "Alexander III of Macedon", "dates": "356-323 BC", "nationality": "Macedonian",
            "signature_innovation": "Combined arms: Companion cavalry hammer + Macedonian phalanx anvil + oblique approach",
            "doctrine": {
                "hammer_and_anvil": "Phalanx (sarissa-armed, 18-foot pike) pins and fixes enemy infantry — the anvil. Companion cavalry (1,000-2,000 heavy horse) delivers the decisive blow against weakened enemy flank or command element — the hammer. Requires coordination between two arms operating independently.",
                "oblique_approach": "Attack at angle, not direct. Advance right-inclined, drawing enemy leftward, creating gap. Exploit gap with cavalry. Never attack where enemy is strongest.",
                "personal_command": "Alexander led from the front, with Companion cavalry. Creates irreplaceable psychological effect — king risks death alongside men. Also allows real-time tactical adjustment at the decisive point.",
                "engineering": "Sophisticated siege train (Tyre, 332 BC — built causeway to island fortress). Combined arms at strategic level: infantry, cavalry, navy, engineers, logistics.",
                "speed_of_pursuit": "After victory, immediate cavalry pursuit prevents enemy reconstitution. Gaugamela: Darius escaped; Alexander pursued but Persian army was never reconstituted anyway.",
            },
            "decisive_campaigns": ["Granicus 334 BC", "Issus 333 BC", "Gaugamela 331 BC"],
            "modern_applications": ["Competitive: fix competitor with one team, win elsewhere with another", "Leadership: visible risk-taking creates disproportionate follower commitment", "Engineering as strategy: technical capability as decisive advantage"],
            "source": "Arrian, Anabasis of Alexander (PD); Plutarch, Life of Alexander (PD)"
        },
        "clausewitz": {
            "commander": "Carl von Clausewitz", "dates": "1780-1831", "nationality": "Prussian",
            "signature_innovation": "Theory of war: friction, fog, center of gravity, culminating point",
            "doctrine": {
                "war_as_politics": "War is the continuation of policy by other means. Every military action must serve a political objective. War without political aim is purposeless violence.",
                "fog_of_war": "In war, three-quarters of the factors on which action is based are wrapped in a fog of greater or lesser uncertainty. Decisions made on incomplete information are the norm, not the exception.",
                "friction": "In war, everything is simple, but the simplest thing is difficult. Plans degrade on contact with reality. The gap between plan and execution is friction. Plan for friction.",
                "center_of_gravity": "Every force has a center of gravity — the hub of its power and movement. Attack the center of gravity, not the periphery. For an army: its military force. For a nation: its capital, its alliances, its public opinion.",
                "culminating_point": "Every offensive has a culminating point — beyond which the attacker becomes weaker than the defender. Know your culminating point. Do not cross it.",
                "surprise": "Surprise is the most powerful means in war. Even the strategically weaker side can win through superior surprise at the operational or tactical level.",
            },
            "decisive_campaigns": ["Served in Jena 1806 (Prussian defeat), informed On War's theory of decisive battle"],
            "modern_applications": ["Startup: center of gravity = network effects, not product features", "Negotiation: fog and friction — plan for information asymmetry", "Project management: culminating point = scope creep"],
            "source": "Clausewitz, On War (Vom Kriege, 1832, PD)"
        },
        "caesar": {
            "commander": "Gaius Julius Caesar", "dates": "100-44 BC", "nationality": "Roman",
            "signature_innovation": "Speed + fortification + political intelligence as operational weapons",
            "doctrine": {
                "speed": "Caesar's legions marched 30+ miles per day, frequently. Speed achieved strategic surprise. Enemies could not concentrate against a force that arrived before expected.",
                "fortification": "When facing superior forces, entrench. Alesia (52 BC): besieged Vercingetorix with inner circumvallation, then built outer fortification against relief army. Defeated both simultaneously.",
                "psychological_initiative": "Caesar always chose when and where to fight. Never waited. Initiative as strategic weapon.",
                "clemency_as_strategy": "Clemency toward defeated enemies (especially Romans) reduced resistance and converted enemies to allies. Political weapon as powerful as military one.",
                "firsthand_intelligence": "Caesar personally observed terrain, enemy disposition, weather. Did not rely solely on reports. Reduced information distortion.",
            },
            "decisive_campaigns": ["Gallic Wars 58-50 BC (10 years, 800 towns, 1M killed)", "Civil War 49-45 BC", "Alesia 52 BC"],
            "modern_applications": ["Operations: speed as a strategic weapon, not just efficiency gain", "Crisis management: simultaneous multi-front operation", "Leadership: clemency toward defeated competitors builds long-term coalition"],
            "source": "Caesar, De Bello Gallico (The Gallic Wars, 58-50 BC, PD)"
        },
        "sun_tzu": {
            "commander": "Sun Tzu (Sunzi)", "dates": "~544-496 BC", "nationality": "Chinese (State of Qi/Wu)",
            "signature_innovation": "Systematic theory of warfare and strategic competition",
            "doctrine": {
                "supreme_excellence": "Supreme excellence consists in breaking the enemy\'s resistance without fighting. Win before the battle begins through superior position and intelligence.",
                "know_yourself": "If you know the enemy and know yourself, you need not fear the result of a hundred battles.",
                "deception": "All warfare is based on deception. When able to attack, feign inability. When using forces, appear inactive.",
                "formlessness": "The highest art of war is to have no fixed form. Like water — take the shape of the vessel, flow where resistance is least.",
                "intelligence": "Knowledge of the enemy\'s dispositions — and one\'s own — is the first principle. Spies are the most important element of war.",
                "speed": "Quickness is the essence of war. Exploit the enemy\'s lack of preparedness, take unexpected routes, attack unguarded spots.",
            },
            "decisive_campaigns": ["Battle of Boju 506 BC (attributed)"],
            "modern_applications": ["Competitive strategy: win without direct confrontation", "Intelligence: information advantage precedes all other advantage", "Positioning: formlessness makes you impossible to target"],
            "source": "Sun Tzu, The Art of War (Sunzi Bingfa, ~500 BC, PD)"
        },
        "frederick": {
            "commander": "Frederick II (Frederick the Great)", "dates": "1712-1786", "nationality": "Prussian",
            "signature_innovation": "Oblique order + interior lines + aggressive offense from defensive position",
            "doctrine": {
                "oblique_order": "Attack enemy\'s flank with concentrated force while refusing (holding back) the opposite wing. Maximizes local superiority at the decisive point. Used at Leuthen (1757): 33,000 Prussians defeated 65,000 Austrians.",
                "speed_of_maneuver": "Prussian infantry trained to march and deploy in formation at unprecedented speed. Tactical advantage through superior drill and speed.",
                "interior_lines": "When outnumbered and surrounded, strike one enemy before others can arrive. Repeated throughout Seven Years War — Prussia defeated individually superior opponents by interior line maneuver.",
                "combined_arms_coordination": "Artillery used aggressively, not just defensively. Mobile horse artillery. Tight coordination between infantry, cavalry, artillery.",
            },
            "decisive_campaigns": ["Rossbach 1757", "Leuthen 1757", "Seven Years War (Prussia vs. France, Austria, Russia, Sweden, Saxony)"],
            "modern_applications": ["Operating against larger competitors: interior lines strategy", "Organizational: outmaneuver through speed of decision, not size", "Resource allocation: concentrate at decisive point, not spread thin"],
            "source": "Frederick the Great, Instructions for His Generals (1747, PD); Instructions for His Officers (1782, PD)"
        },
    }
    key = commander.lower().strip()
    if key in DOCTRINES:
        return DOCTRINES[key]
    available = list(DOCTRINES.keys())
    return {"error": f"Commander not found. Available: {available}", "available": available}


@mcp.tool(
    description=(
        "Apply classical military principles to a modern strategic problem. "
        "Translates ancient military wisdom into business, technology, organizational, "
        "or geopolitical analysis. Specify the problem domain and the analytical lens."
    )
)
def apply_strategy(
    problem: Annotated[str, "Describe the strategic problem or challenge"],
    lens: Annotated[str, "Strategic lens: 'competition'|'leadership'|'intelligence'|'resources'|'operations'|'psychology'"] = "competition",
    commanders: Annotated[str, "Comma-separated commanders to draw from (or 'all')"] = "all",
) -> dict:
    LENSES = {
        "competition": {
            "key_questions": [
                "Where is the enemy\'s center of gravity? (Clausewitz)",
                "Can you win without fighting? (Sun Tzu)",
                "Where is your competitor\'s flank? (Hannibal)",
                "Can you move faster than they can respond? (Napoleon/Caesar)",
                "What does the enemy not expect? (Genghis Khan)",
            ],
            "relevant_maxims": [
                "Sun Tzu: Supreme excellence is breaking resistance without fighting",
                "Napoleon Maxim 1: War is not an art, it is a science — but science applied under conditions of uncertainty",
                "Clausewitz: Know your enemy\'s center of gravity before committing",
                "Hannibal: Appear weak where you plan to be strong",
                "Caesar: Speed as strategic weapon — arrive before expected",
            ],
        },
        "leadership": {
            "key_questions": [
                "Are you leading from the front? (Alexander)",
                "Is authority decentralized to the point of action? (Napoleon\'s corps system)",
                "Do your people understand intent, not just orders? (Auftragstaktik — Prussian doctrine)",
                "Is your organizational culture creating warriors or bureaucrats? (Shaka\'s amabutho system)",
            ],
            "relevant_maxims": [
                "Napoleon Maxim 75: An army\'s effectiveness depends on its size, training, experience, and morale",
                "Sun Tzu: The general who advances without coveting fame and retreats without fearing disgrace — is the jewel of the kingdom",
                "Shaka: The regiment that fights is the regiment that marries (merit tied to performance)",
            ],
        },
        "intelligence": {
            "key_questions": [
                "Do you know the enemy better than the enemy knows themselves? (Sun Tzu)",
                "How quickly does intelligence reach the decision-maker? (Genghis Khan\'s Yam system)",
                "What does the enemy believe about your intentions? (Deception as art)",
            ],
            "relevant_maxims": [
                "Sun Tzu Chapter 13: He who has foreknowledge must be sought from men who know the enemy situation",
                "Genghis Khan: Intelligence arrived 48-72 hours before his army — enemies were already surprised before he arrived",
                "Napoleon Maxim 15: When an army is inferior in cavalry, seek mountains and forests as terrain compensators",
            ],
        },
        "resources": {
            "key_questions": [
                "Are you at your culminating point? (Clausewitz)",
                "Can your force sustain itself without supply lines? (Genghis Khan)",
                "Are you concentrating resources at the point of decision? (Napoleon)",
            ],
            "relevant_maxims": [
                "Napoleon Maxim 2: In mountain warfare, the advantage is with the defender. In flat warfare, offensive power dominates",
                "Clausewitz: The culminating point of victory — know it before you exceed it",
                "Caesar: Fortify when inferior; advance when superior — never fight on equal terms",
            ],
        },
    }
    result = {
        "problem": problem,
        "lens": lens,
        "framework": LENSES.get(lens, LENSES["competition"]),
        "source": "Synthesized from public domain military literature",
        "note": "These are analytical frameworks, not operational recommendations. Historical strategy requires contextual adaptation.",
    }
    return result


@mcp.tool(
    description=(
        "Get major works of military and strategic philosophy available in the public domain. "
        "Returns title, author, date, themes, and key insights for each work."
    )
)
def public_domain_library(
    domain: Annotated[str, "Domain: 'military'|'philosophy'|'leadership'|'history'|'all'"] = "all",
) -> dict:
    LIBRARY = {
        "military": [
            {"title": "The Art of War", "author": "Sun Tzu", "date": "~500 BC", "themes": ["deception", "intelligence", "formlessness", "economy of force"], "key_insight": "Win before the battle"},
            {"title": "On War (Vom Kriege)", "author": "Carl von Clausewitz", "date": "1832", "themes": ["friction", "fog", "center of gravity", "war as politics"], "key_insight": "War is policy by other means"},
            {"title": "The Gallic Wars (De Bello Gallico)", "author": "Julius Caesar", "date": "58-50 BC", "themes": ["speed", "engineering", "fortification", "intelligence"], "key_insight": "Firsthand observation is irreplaceable"},
            {"title": "Anabasis of Alexander", "author": "Arrian", "date": "~130 AD", "themes": ["combined arms", "oblique attack", "personal command"], "key_insight": "Hammer and anvil — pin and strike"},
            {"title": "Napoleon\'s Maxims of War", "author": "Napoleon Bonaparte", "date": "1831", "themes": ["corps system", "central position", "decisive battle", "logistics"], "key_insight": "Speed and concentration beat numbers"},
            {"title": "Instructions for His Generals", "author": "Frederick the Great", "date": "1747", "themes": ["oblique order", "interior lines", "discipline", "surprise"], "key_insight": "Concentration at the decisive point"},
            {"title": "Epitome Rei Militaris", "author": "Vegetius", "date": "~390 AD", "themes": ["training", "organization", "discipline", "fortification"], "key_insight": "Si vis pacem, para bellum"},
            {"title": "The Peloponnesian War", "author": "Thucydides", "date": "~400 BC", "themes": ["power politics", "alliance dynamics", "decision under pressure"], "key_insight": "The strong do what they can; the weak suffer what they must"},
        ],
        "philosophy": [
            {"title": "Meditations", "author": "Marcus Aurelius", "date": "~170-180 AD", "themes": ["stoicism", "duty", "leadership", "impermanence"], "key_insight": "You have power over your mind, not outside events"},
            {"title": "The Prince (Il Principe)", "author": "Niccolò Machiavelli", "date": "1532", "themes": ["power", "pragmatism", "statecraft", "military"], "key_insight": "It is better to be feared than loved, if you cannot be both"},
            {"title": "Art of War (Dell\'arte della guerra)", "author": "Niccolò Machiavelli", "date": "1521", "themes": ["military organization", "infantry", "discipline"], "key_insight": "An unarmed man has no voice in council"},
            {"title": "Letters from a Stoic (Epistulae Morales)", "author": "Seneca", "date": "~65 AD", "themes": ["time", "virtue", "equanimity", "decision"], "key_insight": "Omnia aliena sunt, tempus tantum nostrum est — Time alone is ours"},
            {"title": "Enchiridion", "author": "Epictetus", "date": "~135 AD", "themes": ["control", "response", "freedom", "duty"], "key_insight": "Some things are in our power; some are not"},
            {"title": "The Republic", "author": "Plato", "date": "~380 BC", "themes": ["justice", "governance", "education", "ideals"], "key_insight": "Until philosophers rule, or rulers philosophize — there will be no end to suffering"},
            {"title": "Nicomachean Ethics", "author": "Aristotle", "date": "~350 BC", "themes": ["virtue", "excellence", "flourishing", "practical wisdom"], "key_insight": "Excellence is not an act but a habit"},
            {"title": "The Art of War (Machiavelli)", "author": "Machiavelli", "date": "1521", "themes": ["military organization", "strategy", "political-military relations"], "key_insight": "Wars are begun when one wills, but not ended when one wills"},
        ],
        "history": [
            {"title": "Histories", "author": "Polybius", "date": "~150 BC", "themes": ["Hannibal", "Roman expansion", "political cycles"], "key_insight": "Primary source for Punic Wars — Cannae described in detail"},
            {"title": "Lives (Parallel Lives)", "author": "Plutarch", "date": "~100 AD", "themes": ["Alexander", "Caesar", "Hannibal", "character"], "key_insight": "Character is destiny"},
            {"title": "Travels and Adventures in Eastern Africa", "author": "Nathaniel Isaacs", "date": "1836", "themes": ["Shaka Zulu", "Zulu military system", "bull-horn formation"], "key_insight": "Primary eyewitness to Shaka\'s military innovations"},
            {"title": "The Diary of Henry Francis Fynn", "author": "Henry Francis Fynn", "date": "1830s/published 1950", "themes": ["Shaka Zulu", "Zulu kingdom", "military culture"], "key_insight": "Eyewitness account of Zulu military organization"},
            {"title": "The Secret History of the Mongols", "author": "Anonymous", "date": "~1240", "themes": ["Genghis Khan", "Mongol organization", "psychological warfare"], "key_insight": "Primary Mongol account of Genghis Khan"},
            {"title": "History of the World-Conqueror", "author": "Ata-Malik Juvaini", "date": "1260", "themes": ["Mongol empire", "conquest strategy", "Khwarezm campaign"], "key_insight": "Persian account of Mongol strategic system"},
        ],
    }
    if domain == "all":
        return {"library": LIBRARY, "total_works": sum(len(v) for v in LIBRARY.values()), "note": "All works are in the public domain"}
    return {"domain": domain, "works": LIBRARY.get(domain, []), "note": "All works are in the public domain"}


def main():
    mcp.run()


if __name__ == "__main__":
    main()
