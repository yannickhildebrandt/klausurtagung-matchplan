"""
Matchplan 2026 – G.U.T. BIRK Kempten
Klausurtagung Themensteckbriefe & Trainer-Handreichung
"""
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Matchplan 2026 – G.U.T. BIRK Kempten",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ASSETS = Path(__file__).parent / "assets"

# ─── CI Colors ───────────────────────────────────────────────
CI = {
    "blue":      "#00518e",
    "bright":    "#0094f0",
    "mid":       "#007ecc",
    "deep":      "#083c69",
    "dark":      "#122331",
    "dark2":     "#1f3241",
    "red":       "#DC052B",
    "gold":      "#EBBC4E",
    "gold_light":"#fbf2dc",
    "green":     "#5a8a1e",
    "green_lt":  "#96C11F",
    "bronze":    "#BF8C4A",
    "light":     "#E5EDF3",
    "light2":    "#f8fbfd",
}

# ─── Theme Data ──────────────────────────────────────────────
THEMES = [
    {
        "id": "db",
        "num": "01",
        "title": "DB – Starkes Verkaufen",
        "trainer": "André Kleefeld (VKL Kempten)",
        "color1": CI["blue"],
        "color2": CI["deep"],
        "accent": CI["blue"],
        "accent_bg": CI["light"],
        "goal": "DB-Steigerung um +1 Prozentpunkt",
        "sidebar": [
            "Konditionssystem optimieren",
            "Weniger manuelle Preisveränderungen",
            "DB-Kennzahl konsequent steigern",
        ],
        "kpis": None,
        "taktik": [
            ("Kosten & Vertriebszüge", "Aktiv die GUT-Börse nutzen, Einkaufsvorteile gezielt weitergeben"),
            ("Sortimente (Marke/Exklusiv)", "Mehr aktive Beratung und Empfehlung von margenstarken Produkten"),
            ("Konditionen prüfen", "Angebote konsequent nachfassen, DB-Sätze kennen und verhandeln"),
            ("Mehrwert/Leistung verkaufen", "Beratung, Service und Dienstleistungen für Endkunden in den Vordergrund stellen"),
            ("DLVH forcieren", "Schulungen aktiv mitanbieten, Logistik optimieren"),
        ],
        "training": [
            ("DB-Taskforce gründen: Austausch & Redaktion", "VKL + VKL-Ebene, ZVK-Teamleitung, GL, Fr. Nicole", "Auftakt 15.04.26"),
        ],
        "review": [("Alle 4 Wochen", "DB-Turnier / Taskforce-Review")],
        "foto": "foto-DB-Starkes-VK.jpeg",
    },
    {
        "id": "digital",
        "num": "02",
        "title": "Digital Sales",
        "trainer": "Linda Rehle (Digital Coach)",
        "color1": CI["bright"],
        "color2": CI["mid"],
        "accent": CI["mid"],
        "accent_bg": "#e8f4fd",
        "goal": "Online-Quote um 3% erhöhen",
        "sidebar": [
            "CRM-Quote steigern",
            "Zentrale Kampagnen aufsetzen",
            "Exklusiv-Marken = DB erhöhen",
        ],
        "kpis": ["Kunden spezifisch erreichen", "Erreichbarkeit Newsletter", "Zustellrate Newsletter",
                 "Umsatz durch Verkaufsförderung", "Klickrate", "Online-Quote", "Exklusiv-Marken-Anteil"],
        "taktik": [
            ("1x/Monat Newsletter", "versenden (Aktion + Information)"),
            ("8 zentrale Kampagnen", "pro Jahr umsetzen"),
            ("1x/Monat OP-Schulung", "durchführen (2x2 Stunden)"),
            ("5 CRM-Leads pro Woche", "qualifizieren und bearbeiten"),
            ("Neukunden über Homepage", "gewinnen, Homepageberater einsetzen"),
            ("CRM-Daten pflegen", "Anwesenheit abgleichen, Productfeed aktuell halten"),
            ("3 Online-Kunden je VIM/VAM", "gezielt ansprechen, die kürzlich online bestellt haben"),
            ("Top 40 Kunden", "gezielt mit digitalen Angeboten versorgen"),
        ],
        "training": [
            ("OP-Schulung (Online-Plattform)", "Linda", "30. April"),
            ("VTB-Schulung Kasching", "VIM / VAM", "Ende Juli"),
            ("Newsletter & Markt verbessern", "Linda", "Bis Jahresende"),
            ("CRM abgleichen & pflegen", "Linda / VKL / Phil", "Monatsende (lfd.)"),
            ("Gesamtkonzept erstellen", "Linda", "Dez. 2026"),
        ],
        "review": [("1x / Monat", "VKL / OG / PMS Review"), ("1x / Quartal", "Teilnahme ZVK-Teamgespräch"), ("Regelmäßig", "Teilnahme VAM-Jour fixe")],
        "foto": "foto-Digital-Sales.jpeg",
    },
    {
        "id": "elements",
        "num": "03",
        "title": "ELEMENTS Vertriebskonzept",
        "trainer": "Christian Zens (Elements VKL) / Florian Schropp",
        "color1": CI["green"],
        "color2": "#3d6612",
        "accent": CI["green"],
        "accent_bg": "#eef5e4",
        "goal": "ELEMENTS-Umsatz um 10% steigern",
        "sidebar": [
            "ELEMENTS VKL als Treiber",
            "Sanitär VAM einbinden",
            "Neue MA mit Kundendaten versorgen",
        ],
        "kpis": ["Neukundengewinnung", "Begehungen Handwerker", "Terminkalender-Auslastung",
                 "Exklusiv-/Listenprodukte", "Auftrags-Quote 95–98%", "Umsatz pro Kopf"],
        "taktik": [
            ("2 Termine pro Kunde/Monat", "Regelmäßiger Kundenkontakt sicherstellen"),
            ("7 Kunden pro Bedarf/Sale", "Gezielte Kundenansprache je Verkaufsanlass"),
            ("Handwerker-Begehungen", "Auf-/Abrechnung je Filiale & Standort transparent machen"),
            ("Aktives Selling", "Halbjahres-Schwerpunkt auf aktiven Verkauf legen"),
            ("Verbindlichkeit schaffen", "Klare Kommunikation und Nachverfolgung"),
            ("20 Angebote aktiv", "Leads in der Ausstellung konsequent bedienen"),
        ],
        "training": [
            ("Kundentermine aufbauen & Begehungsplan starten", "BVK", "30. April"),
            ("Handwerker-Abrechnung je Filiale aufsetzen", "EVK", "30. Juni"),
            ("Aktiv-Selling Halbjahresziel auswerten", "BVK", "31. Oktober"),
            ("Verbindlichkeit & Kommunikation etablieren", "BVK / EVK", "30. Juni"),
        ],
        "review": [("Quartalsweise", "ELEMENTS-Vertriebsreview"), ("Halbjährlich", "Selling-Auswertung & Ziel-Check")],
        "foto": "foto-ELEMENTS.jpeg",
    },
    {
        "id": "vam",
        "num": "04",
        "title": "Neue VAM-Gebiete",
        "trainer": "Cengiz Yilmaz (VKL Lindau)",
        "color1": CI["bronze"],
        "color2": "#8a6230",
        "accent": CI["bronze"],
        "accent_bg": "#fdf5e8",
        "goal": "Erhöhung Marktanteil um 2 Mio. €",
        "sidebar": [
            "Neues Personal aufbauen",
            "Zusätze ABEX-Standort",
            "Gebietserschließung Ravensburg & Ostallgäu",
        ],
        "kpis": ["30 Neukunden", "15 Abholer / ABEX-Quote", "3 neue Kollegen", "2+ neue Partnerschaften"],
        "taktik": [
            ("VAM wöchentlich ansprechen", "Direkte, wöchentliche Kommunikation mit dem Außendienst"),
            ("5 Kunden/Woche aufrufen", "Systematische Neukundenansprache per Telefon"),
            ("Kunden-Feedback einholen", "Aktiv Rückmeldungen sammeln und auswerten"),
            ("Standort präsentieren", "Unternehmen und Standortvorteile bei Kunden vorstellen"),
            ("Anwerben", "2+ MA und Werkband-Kontakte gezielt ansprechen"),
            ("Kommunikation zum Markt", "Hohe Frequenz zu Außendienst und Markt sicherstellen"),
        ],
        "training": [
            ("Marktanalyse: Adressen selektieren", "VKL / VAM", "zeitnah"),
            ("Ansprechpartner identifizieren & Telefonliste", "VKL / VAM", "zeitnah"),
            ("Kontakt herstellen (pLG-Ebene)", "pLG / VKL", "laufend"),
        ],
        "review": [("Wöchentlich", "VKL / VAM Abstimmung"), ("Wöchentlich", "VKL / VIM / VAM Update"), ("Monatlich", "pLG / VKL Gesamtreview")],
        "foto": "foto-Neue-VAM-Gebiete.jpeg",
    },
    {
        "id": "waerme",
        "num": "05",
        "title": "Vermarktung Wärmeerzeuger",
        "trainer": "Stefan Krautz (Ltg. Lüftung) / Felix Berghofer (Ltg. Heizung)",
        "color1": CI["red"],
        "color2": "#9a041e",
        "accent": CI["red"],
        "accent_bg": "#fde8ec",
        "goal": "Gesamtumsatz Wärmeerzeuger um 10% steigern",
        "sidebar": [
            "ETA als Schwerpunktmarke",
            "Spezialberatung mit Herstellern",
        ],
        "kpis": None,
        "taktik": [
            ("Frühlings-Klassik-Aktion", "Saisonale Verkaufsaktion starten"),
            ("ETA-Umsatz generieren", "Fokus auf ETA-Produkte im Vertrieb"),
            ("Wärmepumpenkunden nutzen", "Chancen bei bestehenden Kunden identifizieren"),
            ("10% mehr Kunden aktiv beraten", "Beratungsquote systematisch steigern"),
            ("TVK-Personal verdoppeln", "Kapazitäten im Technischen Vertrieb aufbauen"),
            ("Service verbessern", "Annahme, Fertigung und Auslieferung optimieren"),
            ("Markenfokus & MK-Steuerung", "Nachhaltigkeit und Bestellprozesse optimieren"),
            ("Sourcing VAM-Ranking", "VAM-Angebote bei jedem Termin systematisch einsetzen"),
            ("Ersatzteile in ABEX", "Verfügbarkeit und Bestellprozess sicherstellen"),
            ("VP / Sonderlösungen", "30 Sonderleistungen im VP verbessern"),
        ],
        "training": [
            ("Ersatzteile in ABEX einpflegen", "Felix", "KW 13"),
            ("TVK-Maßnahmen umsetzen", "TVK", "31.03.2026"),
            ("Sourcing & VAM-Ranking etablieren", "Felix", "laufend"),
            ("Quartalsweise Review", "Felix / Stefan", "quartalsweise"),
            ("VK-Besuche beim Kunden starten", "Felix", "ab 06/2026"),
        ],
        "review": [("1x / Monat", "Firmen-Meeting (TVK + VKLs)"), ("2x / Monat", "Zahlen-Sharing Felix / ETA (je 30 Min.)")],
        "foto": "foto-Waermeerzeuger.jpeg",
    },
    {
        "id": "zvk",
        "num": "06",
        "title": "Erfolgreicher Vertrieb im ZVK",
        "trainer": "Florian Schropp (IDL Lindau) / Matthias Trunzer (IDL Kempten)",
        "color1": CI["dark2"],
        "color2": CI["dark"],
        "accent": "#273D51",
        "accent_bg": "#e9ecee",
        "goal": "Vom Abwickler zum aktiven Verkäufer",
        "sidebar": [
            "Maßnahmen im ZVK verankern",
            "Produktiver Abverkauf steigern",
            "Merken & Maßnahmen etablieren",
        ],
        "kpis": ["Online-Quote steigern", "Umschlagshäufigkeit", "Neue Warengruppe (Oberkante)"],
        "taktik": [
            ("2 Kunden/Tag digital kontaktieren", "pro Standort – konsequent umsetzen"),
            ("2 Kundenanalysen/Monat pro Standort", "Abwickler vs. aktive Kunden identifizieren"),
            ("Kunden für Digitales gewinnen", "Online-Bestellwege aktiv empfehlen und begleiten"),
        ],
        "training": [
            ("VK-Aktion starten (D-VK)", "Termin mit Digi-Coach → je 9 Kunden", "zeitnah"),
            ("D/H-Kundenanalyse durchführen", "Haupt-Besuchspläne → je 9 Kunden", "zeitnah"),
            ("Teamleitung ZVK einbinden", "Teamleitung ZVK", "laufend"),
        ],
        "review": [("2 Wo. nach Aktion", "Oliva-Kontrolle"), ("4 Wo. nach Gespräch", "Umsatz-/VKE-Auswertung"), ("Regelmäßig", "Teamleiter + VIM/VKL Abstimmung")],
        "foto": "foto-ZVK.jpeg",
    },
]


# ─── Global CSS ──────────────────────────────────────────────
def inject_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:wght@700;900&display=swap');
    * { font-family: 'Inter', sans-serif; }

    /* Hide default streamlit chrome */
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding-top: 0 !important; padding-bottom: 2rem !important; max-width: 1100px !important;}
    [data-testid="stSidebar"] {display: none;}

    /* ── Hero ── */
    .hero-banner {
        background: linear-gradient(135deg, %(dark)s 0%%, %(deep)s 50%%, %(blue)s 100%%);
        padding: 2.5rem 2rem 3.5rem;
        text-align: center;
        border-radius: 0 0 20px 20px;
        margin: -1rem -1rem 0 -1rem;
        position: relative;
        overflow: hidden;
    }
    .hero-banner::before {
        content: '';
        position: absolute;
        top: -30%%; right: -10%%;
        width: 400px; height: 400px;
        background: radial-gradient(circle, rgba(0,148,240,.12) 0%%, transparent 70%%);
        border-radius: 50%%;
    }
    .hero-badge {
        display: inline-block;
        background: %(gold)s;
        color: %(dark)s;
        padding: .3rem 1rem;
        border-radius: 50px;
        font-weight: 700;
        font-size: .7rem;
        letter-spacing: 2px;
        text-transform: uppercase;
        margin-bottom: .75rem;
    }
    .hero-banner h1 {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        font-weight: 900;
        color: white;
        line-height: 1.1;
        margin: 0;
    }
    .hero-banner h1 span { color: %(gold)s; }
    .hero-sub {
        color: rgba(255,255,255,.5);
        font-size: 1rem;
        font-weight: 300;
        margin-top: .3rem;
    }
    .hero-meta {
        color: rgba(255,255,255,.4);
        font-size: .8rem;
        margin-top: 1.25rem;
    }
    .hero-meta strong { color: rgba(255,255,255,.7); }

    /* ── Dashboard Cards ── */
    .card-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.2rem;
        margin-top: -2rem;
        position: relative;
        z-index: 2;
    }
    .dash-card {
        background: white;
        border-radius: 14px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0,0,0,.08);
        border: 1px solid rgba(0,81,142,.08);
        transition: all .3s ease;
        cursor: pointer;
        text-decoration: none;
        color: inherit;
        display: flex;
        flex-direction: column;
    }
    .dash-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 24px rgba(0,0,0,.12);
    }
    .dash-card-head {
        padding: 1.3rem 1.3rem 1rem;
        color: white;
        position: relative;
    }
    .dash-card-num {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 26px; height: 26px;
        border-radius: 7px;
        background: rgba(255,255,255,.15);
        font-size: .7rem;
        font-weight: 800;
        margin-bottom: .5rem;
    }
    .dash-card-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.2rem;
        font-weight: 900;
        line-height: 1.2;
    }
    .dash-card-trainer {
        font-size: .75rem;
        color: rgba(255,255,255,.6);
        margin-top: .2rem;
    }
    .dash-card-body {
        padding: 1rem 1.3rem;
        flex: 1;
    }
    .dash-card-goal {
        font-size: .9rem;
        font-weight: 800;
        color: %(dark)s;
        margin-bottom: .6rem;
    }
    .dash-card-goal-label {
        font-size: .6rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #94a3b8;
    }
    .tag-row { display: flex; flex-wrap: wrap; gap: .3rem; }
    .dash-card-foot {
        padding: .7rem 1.3rem;
        border-top: 1px solid #f1f5f9;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: .7rem;
        color: #94a3b8;
    }

    /* ── Detail page ── */
    .detail-header {
        padding: 1.75rem 2rem;
        border-radius: 12px 12px 0 0;
        color: white;
        position: relative;
    }
    .detail-number {
        display: inline-block;
        background: rgba(255,255,255,.2);
        padding: .25rem .65rem;
        border-radius: 5px;
        font-size: .7rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        margin-bottom: .6rem;
    }
    .detail-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.7rem;
        font-weight: 900;
        margin: 0;
    }
    .detail-trainer {
        font-size: .85rem;
        color: rgba(255,255,255,.7);
        margin-top: .2rem;
    }
    .goal-box {
        display: flex;
        gap: 1rem;
        align-items: center;
        padding: 1.25rem 1.5rem;
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        margin: 1rem 0;
    }
    .goal-icon-box {
        width: 44px; height: 44px;
        border-radius: 11px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.3rem;
        flex-shrink: 0;
    }
    .goal-label {
        font-size: .65rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #94a3b8;
    }
    .goal-val {
        font-size: 1.2rem;
        font-weight: 800;
        color: %(dark)s;
    }
    .taktik-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: .75rem .9rem;
        display: flex;
        gap: .65rem;
        align-items: flex-start;
        margin-bottom: .5rem;
    }
    .taktik-num {
        width: 22px; height: 22px;
        border-radius: 5px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: .65rem;
        font-weight: 800;
        flex-shrink: 0;
        color: white;
    }
    .taktik-label { font-weight: 600; color: #0f172a; font-size: .85rem; }
    .taktik-desc { color: #475569; font-size: .83rem; }
    .review-card {
        border-radius: 8px;
        padding: .75rem;
        text-align: center;
    }
    .review-freq { font-size: 1rem; font-weight: 800; }
    .review-what { font-size: .78rem; color: #475569; margin-top: .15rem; }
    .section-head {
        font-size: .9rem;
        font-weight: 700;
        color: %(dark)s;
        margin-bottom: .6rem;
        display: flex;
        align-items: center;
        gap: .5rem;
    }
    .section-icon {
        width: 28px; height: 28px;
        border-radius: 7px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: .85rem;
    }
    .kpi-pill {
        display: inline-block;
        background: #f1f5f9;
        border: 1px solid #e2e8f0;
        padding: .2rem .6rem;
        border-radius: 20px;
        font-size: .75rem;
        color: #475569;
        margin: .15rem .15rem;
    }
    .foto-section {
        background: white;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        overflow: hidden;
        margin-top: 1.5rem;
    }
    .foto-head {
        padding: 1rem 1.5rem;
        border-bottom: 1px solid #f1f5f9;
        font-weight: 700;
        font-size: .9rem;
        color: %(dark)s;
    }
    .sidebar-item {
        padding: .15rem 0 .15rem .8rem;
        position: relative;
        font-size: .83rem;
        color: #475569;
    }
    .sidebar-item::before {
        content: '›';
        position: absolute;
        left: 0;
        color: #94a3b8;
        font-weight: 700;
    }
    .back-btn {
        display: inline-flex;
        align-items: center;
        gap: .4rem;
        color: %(blue)s;
        font-weight: 600;
        font-size: .85rem;
        text-decoration: none;
        margin-bottom: 1rem;
        padding: .4rem .8rem;
        border-radius: 6px;
        border: 1px solid %(light)s;
        transition: all .2s;
    }
    .back-btn:hover {
        background: %(light)s;
    }
    .footer-text {
        text-align: center;
        color: #94a3b8;
        font-size: .78rem;
        padding: 2rem 0 1rem;
    }
    @media (max-width: 768px) {
        .card-grid { grid-template-columns: 1fr !important; }
        .hero-banner h1 { font-size: 2rem; }
    }
    </style>
    """ % CI, unsafe_allow_html=True)


# ─── Dashboard View ──────────────────────────────────────────
def show_dashboard():
    inject_css()

    # Hero
    st.markdown(f"""
    <div class="hero-banner">
        <div class="hero-badge">Klausurtagung 2026</div>
        <h1>Matchplan <span>2026</span></h1>
        <div class="hero-sub">Themensteckbriefe &amp; Trainer-Handreichung</div>
        <div class="hero-meta">
            <strong>G.U.T. BIRK Kempten</strong> &nbsp;·&nbsp;
            Kempten, <strong>05.–06. März 2026</strong> &nbsp;·&nbsp;
            Moderation: <strong>Yannick Hildebrandt</strong> (Eggers und Partner)
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<p style="text-align:center;color:#94a3b8;font-size:.72rem;font-weight:600;letter-spacing:2px;text-transform:uppercase;margin:2rem 0 .5rem;">Wähle ein Themenfeld</p>', unsafe_allow_html=True)

    # Cards as Streamlit columns with buttons
    rows = [THEMES[:3], THEMES[3:]]
    for row in rows:
        cols = st.columns(3, gap="medium")
        for col, t in zip(cols, row):
            with col:
                tags = "".join(
                    f'<span style="display:inline-block;padding:.18rem .5rem;border-radius:5px;font-size:.65rem;font-weight:600;background:{t["accent_bg"]};color:{t["accent"]};border:1px solid {t["accent"]}22;margin:.15rem .1rem;">{label}</span>'
                    for label, _ in t["taktik"][:4]
                )
                st.markdown(f"""
                <div style="background:white;border-radius:14px;overflow:hidden;box-shadow:0 4px 12px rgba(0,0,0,.08);border:1px solid {t['accent']}15;border-bottom:3px solid {t['color1']};margin-bottom:.5rem;">
                    <div style="background:linear-gradient(135deg,{t['color1']},{t['color2']});padding:1.2rem 1.3rem 1rem;color:white;">
                        <div class="dash-card-num">{t['num']}</div>
                        <div class="dash-card-title">{t['title']}</div>
                        <div class="dash-card-trainer">Trainer: <strong>{t['trainer'].split('(')[0].strip()}</strong></div>
                    </div>
                    <div style="padding:1rem 1.3rem;">
                        <div class="dash-card-goal-label">Ergebnisziel</div>
                        <div class="dash-card-goal">{t['goal']}</div>
                        <div class="tag-row">{tags}</div>
                    </div>
                    <div class="dash-card-foot">
                        <span><strong>{len(t['taktik'])}</strong> Taktik-Maßnahmen · <strong>{len(t['training'])}</strong> Trainingsschritte</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"Öffnen →", key=f"btn_{t['id']}", use_container_width=True):
                    st.session_state.page = t["id"]
                    st.rerun()

    st.markdown('<div class="footer-text"><strong>Matchplan 2026</strong> – Klausurtagung G.U.T. BIRK Kempten<br>Kempten, 05.–06. März 2026 · Moderation: Yannick Hildebrandt (Eggers und Partner)</div>', unsafe_allow_html=True)


# ─── Detail View ─────────────────────────────────────────────
def show_detail(theme_id: str):
    inject_css()
    t = next(th for th in THEMES if th["id"] == theme_id)

    # Back button
    if st.button("← Zurück zur Übersicht", key="back"):
        st.session_state.page = "dashboard"
        st.rerun()

    # Header
    st.markdown(f"""
    <div class="detail-header" style="background:linear-gradient(135deg,{t['color1']},{t['color2']});">
        <div class="detail-number">Thema {t['num']}</div>
        <div class="detail-title">{t['title']}</div>
        <div class="detail-trainer">Trainer: <strong>{t['trainer']}</strong></div>
    </div>
    """, unsafe_allow_html=True)

    # Goal + Sidebar
    col_goal, col_side = st.columns([3, 2])
    with col_goal:
        st.markdown(f"""
        <div class="goal-box">
            <div class="goal-icon-box" style="background:{t['accent_bg']};color:{t['accent']};">🎯</div>
            <div>
                <div class="goal-label">Ergebnisziel 2026</div>
                <div class="goal-val">{t['goal']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col_side:
        sidebar_items = "".join(f'<div class="sidebar-item">{s}</div>' for s in t["sidebar"])
        st.markdown(f"""
        <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:1rem 1.25rem;margin:1rem 0;">
            <div class="goal-label" style="margin-bottom:.4rem;">Rahmenbedingungen</div>
            {sidebar_items}
        </div>
        """, unsafe_allow_html=True)

    # KPIs
    if t["kpis"]:
        pills = "".join(f'<span class="kpi-pill">{k}</span>' for k in t["kpis"])
        st.markdown(f"""
        <div class="section-head"><div class="section-icon" style="background:{t['accent_bg']};color:{t['accent']};">📊</div> Kennzahlen im Blick</div>
        <div style="margin-bottom:1rem;">{pills}</div>
        """, unsafe_allow_html=True)

    # Taktiktafel
    st.markdown(f"""<div class="section-head"><div class="section-icon" style="background:{t['accent_bg']};color:{t['accent']};">⚽</div> Taktiktafel</div>""", unsafe_allow_html=True)
    col_l, col_r = st.columns(2)
    for i, (label, desc) in enumerate(t["taktik"]):
        target = col_l if i % 2 == 0 else col_r
        with target:
            st.markdown(f"""
            <div class="taktik-card">
                <div class="taktik-num" style="background:{t['accent']};">{i+1}</div>
                <div><span class="taktik-label">{label}:</span> <span class="taktik-desc">{desc}</span></div>
            </div>
            """, unsafe_allow_html=True)

    # Trainingsplan
    st.markdown(f"""<div class="section-head" style="margin-top:1.2rem;"><div class="section-icon" style="background:{t['accent_bg']};color:{t['accent']};">📋</div> Trainingsplan</div>""", unsafe_allow_html=True)
    header_cols = st.columns([4, 3, 2])
    header_cols[0].markdown("**Was?**")
    header_cols[1].markdown("**Wer?**")
    header_cols[2].markdown("**Bis Wann?**")
    for was, wer, wann in t["training"]:
        r = st.columns([4, 3, 2])
        r[0].markdown(f"**{was}**")
        r[1].markdown(wer)
        r[2].markdown(f'`📅 {wann}`')

    # Spielstandsanzeige
    st.markdown(f"""<div class="section-head" style="margin-top:1.2rem;"><div class="section-icon" style="background:{t['accent_bg']};color:{t['accent']};">📈</div> Spielstandsanzeige</div>""", unsafe_allow_html=True)
    review_cols = st.columns(len(t["review"]))
    for col, (freq, what) in zip(review_cols, t["review"]):
        with col:
            st.markdown(f"""
            <div class="review-card" style="background:{t['accent_bg']};border:1px solid {t['accent']}25;">
                <div class="review-freq" style="color:{t['accent']};">{freq}</div>
                <div class="review-what">{what}</div>
            </div>
            """, unsafe_allow_html=True)

    # Fotodokumentation
    foto_path = ASSETS / t["foto"]
    if foto_path.exists():
        st.markdown(f"""
        <div class="foto-section">
            <div class="foto-head">📷 Fotodokumentation</div>
        </div>
        """, unsafe_allow_html=True)
        st.image(str(foto_path), caption=f'Ergebnis-Poster „{t["title"]}" – Klausurtagung Matchplan 2026, G.U.T. BIRK Kempten', use_container_width=True)

    # Footer
    st.markdown('<div class="footer-text"><strong>Matchplan 2026</strong> – Klausurtagung G.U.T. BIRK Kempten<br>Kempten, 05.–06. März 2026 · Moderation: Yannick Hildebrandt (Eggers und Partner)</div>', unsafe_allow_html=True)


# ─── Router ──────────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "dashboard"

if st.session_state.page == "dashboard":
    show_dashboard()
else:
    show_detail(st.session_state.page)
