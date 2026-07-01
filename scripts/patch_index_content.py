#!/usr/bin/env python3
"""Apply content/SEO patches to index.html (em-dash removal, CV sync)."""
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
INDEX = REPO / "index.html"
text = INDEX.read_text(encoding="utf-8")

replacements = [
    # IMC Olympiad
    (
        '          <li><div class="honor-date">2019</div><div class="honor-body"><strong>IMC Olympiad · 7th globally</strong> · International Mathematics Competition.</div></li>\n',
        "",
    ),
    # Weber email footer
    (
        '        <a href="mailto:esmaeilmousavi@weber.edu">esmaeilmousavi@weber.edu</a>\n',
        "",
    ),
    # Resume link
    (
        '          <a href="https://acrobat.adobe.com/id/urn:aaid:sc:VA6C2:121393a0-345c-4c7c-abf2-e50a534956fd">Résumé / CV · Adobe Acrobat</a>\n',
        '          <a href="/documents/Esmaeil-Mousavi-CV.pdf">Curriculum vitae (PDF)</a>\n',
    ),
    # Addresses: replace Layton block with San Jose + Provo
    (
        """        <div class="address-block">
          <strong>Ogden · Research HQ</strong>
          <div><a href="https://maps.app.goo.gl/Sj19cZZqcoe2wRrF8">Room 337, School of Computing Faculty Research Lab, Noorda Applied Science &amp; Technology Building, 1465 Edvalson St, Ogden, UT 84403</a></div>
        </div>
        <div class="address-block" style="margin-top:24px;">
          <strong>Layton · Autonomous Lab</strong>
          <div><a href="https://maps.app.goo.gl/XqVj9oGZS1FFcDan8">Room 128 · Autonomous Vehicles &amp; Electronics Lab · Computer &amp; Automotive Engineering Building, 2750 University Park Blvd, Layton, UT 84041</a></div>
        </div>""",
        """        <div class="address-block">
          <strong>San Jose · navNote AI HQ</strong>
          <div><a href="https://maps.google.com/?q=San+Jose+CA">San Jose, Silicon Valley, CA</a></div>
        </div>
        <div class="address-block" style="margin-top:24px;">
          <strong>Ogden · Weber State research</strong>
          <div><a href="https://maps.app.goo.gl/Sj19cZZqcoe2wRrF8">Room 337, School of Computing Faculty Research Lab, Noorda Applied Science &amp; Technology Building, 1465 Edvalson St, Ogden, UT 84403</a></div>
        </div>
        <div class="address-block" style="margin-top:24px;">
          <strong>Provo · Utah Innovation Hub (iHub)</strong>
          <div><a href="https://maps.google.com/?q=1555+N+Freedom+Blvd+Provo+UT+84604">1555 N Freedom Blvd, Suite 200, Provo, UT 84604</a></div>
        </div>""",
    ),
    # About: remove IMC-adjacent math honors line
    (
        "      <p>He came to the United States from Iran in 2022 to further his studies in computer science. At 17 he received an international patent through WIPO for an internal combustion engine he designed — the Two-Stroke X-Shaped Engine. The same period included strong international honors in mathematics and talent programs.</p>",
        "      <p>He came to the United States from Iran in 2022 to further his studies in computer science. At 17 he designed an internal-combustion engine — the Two-Stroke X-Shaped Engine — and filed it as an international patent application under the Patent Cooperation Treaty (PCT), published by WIPO in 2020. He was top-ranked in Iran’s NODET national talent entrance examination.</p>",
    ),
    # Graduation date
    (
        "          <div class=\"cv-meta\">Weber State · 2022–present (expected December 2025)</div>",
        "          <div class=\"cv-meta\">Weber State · 2022–present (expected December 2026)</div>",
    ),
    # Colophon
    (
        "      <span>© Esmaeil Mousavi · Manhattan · Ogden</span>",
        "      <span>© Esmaeil Mousavi · San Jose, Silicon Valley · Silicon Slopes</span>",
    ),
    # Profiles intro (no em dash left but fix wording)
    (
        "          Every verified profile mirrors the canonical data on esmaeil.org · research IDs, collaborations, archival teaching pages, calendars, patents, institutional references.",
        "          Verified profiles and canonical links for research IDs, navNote AI, patents, and institutional references.",
    ),
    # SEO email
    ('<meta name="reply-to" content="esmaeilmousavi@weber.edu" />', '<meta name="reply-to" content="esmaeil@navnote.ai" />'),
    ('"email": "esmaeilmousavi@weber.edu"', '"email": "esmaeil@navnote.ai"'),
    (
        '"email": "esmaeilmousavi@weber.edu"\n        },\n        {\n          "@type": "ContactPoint",\n          "contactType": "social media"',
        '"email": "esmaeil@navnote.ai"\n        },\n        {\n          "@type": "ContactPoint",\n          "contactType": "social media"',
    ),
    # Schema addresses Layton -> San Jose + Provo
    (
        """        {
          "@type": "PostalAddress",
          "name": "Layton Office",
          "streetAddress": "Room 128, Autonomous Vehicles and Electronics Lab, Computer & Automotive Engineering Building, 2750 University Park Blvd",
          "addressLocality": "Layton",
          "addressRegion": "UT",
          "postalCode": "84041",
          "addressCountry": "USA"
        }""",
        """        {
          "@type": "PostalAddress",
          "name": "San Jose Headquarters",
          "addressLocality": "San Jose",
          "addressRegion": "CA",
          "addressCountry": "USA"
        },
        {
          "@type": "PostalAddress",
          "name": "Provo · Utah Innovation Hub",
          "streetAddress": "1555 N Freedom Blvd, Suite 200",
          "addressLocality": "Provo",
          "addressRegion": "UT",
          "postalCode": "84604",
          "addressCountry": "USA"
        }""",
    ),
    ('"foundingDate": "2020"', '"foundingDate": "2025"'),
    ('"dateModified": "2026-02-06"', '"dateModified": "2026-05-21"'),
]

# Add profile links before Calendly if not present
profile_insert = """          <a href="https://www.navnote.ai/">navNote AI</a>
          <a href="https://www.navnote.ai/contact">navNote · contact</a>
          <a href="https://itubelabs.com">iTubeLabs</a>
          <a href="https://ncwqr.org/">National Center for Water Quality Research</a>
          <a href="https://www.ibm.com/z">IBM Z Systems</a>
          <a href="https://www.acm.org/">ACM</a>
          <a href="https://www.perplexity.ai/">Perplexity</a>
          <a href="https://www.mimik.com/">mimik Technologies</a>
"""
if "https://www.navnote.ai/contact" not in text:
    text = text.replace(
        '          <a href="https://calendly.com/esmaeilmousavi-weber">Calendly</a>\n',
        profile_insert + '          <a href="https://calendly.com/esmaeilmousavi-weber">Calendly</a>\n',
    )

# Add navNote researcher role at top of career
career_navnote = """        <article class="cv-role">
          <h5>Researcher · AI/ML &amp; Backend Systems</h5>
          <div class="cv-meta">Weber State University · May 2025–present</div>
          <ul>
            <li>Faculty-mentored applied research through the navNote platform for enterprise field operations.</li>
            <li>Large-scale image understanding, predictive analytics, autonomous task orchestration, and scalable backend architectures.</li>
          </ul>
        </article>
"""
if "Researcher · AI/ML" not in text:
    text = text.replace(
        '      <div class="section-label"><span class="num">/ 06</span>Experience<br>&amp; Education</div>\n      <div>\n        <article class="cv-role">\n          <h5>Graduate Teaching Assistant',
        '      <div class="section-label"><span class="num">/ 06</span>Experience<br>&amp; Education</div>\n      <div>\n' + career_navnote + '        <article class="cv-role">\n          <h5>Graduate Teaching Assistant',
    )

# Update assistant researcher end dates
text = text.replace(
    '<div class="cv-meta">Weber State · Oct 2022–present</div>',
    '<div class="cv-meta">Weber State · Oct 2022–May 2025</div>',
)
text = text.replace(
    '<div class="cv-meta">Weber State · Jan 2023–present</div>',
    '<div class="cv-meta">Weber State · Jan 2023–May 2025</div>',
)

# NODET honor wording from CV
text = text.replace(
    '<strong>NODET cohort (Iran)</strong> · top quintile scholarly performance grades 7–12.',
    '<strong>NODET (Iran)</strong> · top-ranked national talent entrance examination.',
)

# Title and meta block
head_updates = {
    '<title>Esmaeil Mousavi - AI/ML Researcher, Founder of navNote AI | Weber State University</title>':
    '<title>Esmaeil Mousavi · AI Researcher &amp; navNote AI Founder | Official Site</title>',
    '<meta property="og:title" content="Esmaeil Mousavi - AI/ML Researcher, Founder of navNote AI | Weber State University" />':
    '<meta property="og:title" content="Esmaeil Mousavi · Founder of navNote AI · AI/ML Researcher" />',
    '<meta name="twitter:title" content="Esmaeil Mousavi - AI/ML Researcher, Founder of navNote AI | Weber State University" />':
    '<meta name="twitter:title" content="Esmaeil Mousavi · Founder of navNote AI · AI/ML Researcher" />',
}
for old, new in head_updates.items():
    text = text.replace(old, new)

desc = (
    "Esmaeil Mousavi is Founder &amp; CEO of navNote AI (navnote.ai), building agentic AI for retail operations, "
    "and an AI/ML researcher at Weber State University. Inventor of the Two-Stroke X-Shaped Engine, a WIPO-published (PCT) patent application. "
    "Based in San Jose, Silicon Valley, with research in Silicon Slopes (Utah)."
)
text = text.replace(
    'content="Esmaeil Mousavi: AI/ML Researcher at Weber State University, Founder & CEO of navNote AI, Patent Holder of Two-Stroke X-Shaped Engine. Expert in artificial intelligence, machine learning, autonomous vehicles, and innovative automotive technologies. Graduate Teaching Assistant and Tech Entrepreneur."',
    f'content="{desc}"',
)
text = text.replace(
    'content="AI/ML Researcher at Weber State University, Founder & CEO of navNote AI, Patent Holder of Two-Stroke X-Shaped Engine. Expert in artificial intelligence, machine learning, autonomous vehicles, and innovative automotive technologies."',
    f'content="{desc}"',
)

text = text.replace('<meta name="geo.placename" content="Ogden, Utah" />', '<meta name="geo.placename" content="San Jose, California; Provo, Utah; Ogden, Utah" />')
text = text.replace('<meta name="location" content="Ogden, Utah, USA" />', '<meta name="location" content="San Jose, California; Provo, Utah; Ogden, Utah, USA" />')

# sameAs additions
if '"https://www.navnote.ai/"' not in text:
    text = text.replace(
        '"https://g.co/kgs/7GbuQHr"\n      ],',
        '"https://g.co/kgs/7GbuQHr",\n        "https://www.navnote.ai/",\n        "https://itubelabs.com",\n        "https://ncwqr.org/",\n        "https://www.acm.org/",\n        "https://www.ibm.com/z"\n      ],',
    )

# FAQ navNote answer
text = text.replace(
    '"text": "navNote AI is an AI technology company founded by Esmaeil Mousavi in 2020, specializing in innovative artificial intelligence solutions for autonomous systems and intelligent navigation."',
    '"text": "navNote AI (navnote.ai) builds agentic AI for retail operations, founded in 2025 by Esmaeil Mousavi. Agents help run store operations including audits, planograms, pricing, and field teams. Headquarters: San Jose, Silicon Valley."',
)

# Person description in JSON-LD
text = text.replace(
    '"description": "Esmaeil Mousavi is an AI/ML Researcher at Weber State University, Graduate Teaching Assistant, and Founder & CEO of navNote AI. Expert in artificial intelligence, machine learning, autonomous vehicles, and innovative automotive technologies. Patent holder for Two-Stroke X-Shaped Engine technology."',
    '"description": "Esmaeil Mousavi is Founder and CEO of navNote AI, building agentic AI for retail operations (navnote.ai), and an AI/ML researcher at Weber State University. Inventor of the Two-Stroke X-Shaped Engine, a WIPO-published (PCT) patent application. Works across San Jose (Silicon Valley) and Silicon Slopes (Utah)."',
)

# navNote org description
text = text.replace(
    '"description": "AI technology company specializing in innovative artificial intelligence solutions for autonomous systems and intelligent navigation"',
    '"description": "Agentic AI for retail operations. AI agents for audits, planograms, pricing, promotions, and field operations."',
    1,
)

for old, new in replacements:
    if old not in text:
        print("WARN missing:", old[:60], "...")
    else:
        text = text.replace(old, new)

# Remove remaining em dashes (U+2014)
text = text.replace("\u2014", " · ")

INDEX.write_text(text, encoding="utf-8")
print("Patched", INDEX)
