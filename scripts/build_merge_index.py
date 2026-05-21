# Assembles portfolio body + scraped head fragment.
# Run after: tmp/newhead.html + tmp/gallery_frag.html exist
#   python3 scripts/build_merge_index.py

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
HEAD = Path("/tmp/newhead.html").read_text(encoding="utf-8")
GALLERY = Path("/tmp/gallery_frag.html").read_text(encoding="utf-8")

BODY = r"""<body>

<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MPNLQ3X"
  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>

<a class="skip-link" href="#about">Skip to content</a>

<div class="container" id="main">

  <header class="top">
    <div class="top-row">
      <div>Esmaeil Mousavi <span style="color: var(--accent); margin: 0 12px;">·</span> Portfolio</div>
      <nav>
        <a href="#about">About</a>
        <a href="#identity">Focus</a>
        <a href="#work">Work</a>
        <a href="#research">Research</a>
        <a href="#career">Experience</a>
        <a href="#honors">Honors</a>
        <a href="#profiles">Profiles</a>
        <a href="#gallery">Photos</a>
        <a href="#contact">Contact</a>
      </nav>
    </div>

    <div class="masthead">
      <div class="kicker">Researcher · Entrepreneur · Builder</div>
      <h1 class="name">Esmaeil<br><em>Mousavi</em></h1>
      <p class="subhead">Building artificial intelligence that sees, reasons, and acts in the physical world · from autonomous vehicles to the operating system of retail.</p>
    </div>
  </header>

  <div class="hero-grid">
    <div class="photo-card">
      <img src="images/esmaeil_mousavi.jpg" alt="Esmaeil Mousavi · researcher" loading="lazy" decoding="async" />
      <div class="photo-caption">Weber State University · Research &amp; Teaching</div>
    </div>
    <div class="photo-card">
      <img src="images/gallery-collab-night.png" alt="Esmaeil Mousavi with collaborator" loading="lazy" decoding="async" />
      <div class="photo-caption">navNote AI · Collaboration</div>
    </div>
  </div>

  <section class="about" id="about">
    <div class="section-label">
      <span class="num">/ 01</span>
      About
    </div>
    <div class="about-body">
      <p class="lead">Esmaeil is a researcher and entrepreneur working at the intersection of artificial intelligence, autonomous systems, and the physical world.</p>
      <p>He is the cofounder of <em>navNote AI</em>, headquartered in Manhattan, building an AI-native operating system for retail’s physical operations. His research spans computer vision, reinforcement learning, 3D LiDAR perception, swarm learning, and ML-based cybersecurity · with presented work across autonomous vehicles, environmental forecasting, and acoustic systems security.</p>
      <p><em>Education:</em> Pursuing a Bachelor of Science in Computer Science at Weber State University (Ogden, UT), with coursework and lab work spanning computing, robotics, autonomous systems, and data science. More than $100,000 in combined university scholarships and external research grants has supported his degree and laboratory work.</p>
      <p>He came to the United States from Iran in 2022 to further his studies in computer science. At 17 he received an international patent through WIPO for an internal combustion engine he designed: the Two-Stroke X-Shaped Engine. He was top-ranked in Iran’s NODET national talent entrance examination.</p>
    </div>
  </section>

  <section class="identity" id="identity">
    <div class="section-label">
      <span class="num">/ 02</span>
      Two Disciplines
    </div>
    <div class="identity-grid">
      <div class="identity-col">
        <h3><span class="arrow">→</span>Research Scientist</h3>
        <p>Esmaeil’s research focuses on applied artificial intelligence in real-world, real-time environments · reinforcement learning for autonomous perception, decentralized SWARM learning for collaborative obstacle recognition, ML defenses against acoustic denial-of-service attacks, and predictive modeling on long-horizon environmental sensor data.</p>
        <p>As a graduate teaching assistant he co-developed and led a graduate-level course in route planning and navigation for autonomous systems. He presents at undergraduate research forums and participates in interdisciplinary groups including Harvard SEAS Computer Science Colloquium. Cumulative internal scholarships and external research grants for his education and labs exceed $100,000.</p>
      </div>
      <div class="identity-col">
        <h3><span class="arrow">→</span>Tech Entrepreneur</h3>
        <p>As cofounder of navNote AI, he is building intelligent systems that observe, reason, and act across in-store workflows at scale · bridging agentic AI with brick-and-mortar operations. He has raised hundreds of thousands of dollars in investment for the company alongside state innovation awards and strategic partnerships.</p>
        <p>He also develops independent initiatives such as iTubeLabs, an AI growth platform for creators, and engages across industry partners and innovation hubs (Utah iHub, enterprise pilots, frontier AI collaborators).</p>
      </div>
    </div>
  </section>

  <section class="work" id="work">
    <div class="section-label" style="margin-bottom: 24px;">
      <span class="num">/ 03</span>
      Selected Work
    </div>
    <h2 class="section-title">Things I have built.</h2>
    <div class="work-list">
      <div class="work-item">
        <div class="work-num">001</div>
        <div class="work-main">
          <h4><a href="https://www.navnote.ai/" target="_blank" rel="noopener noreferrer">navNote AI</a></h4>
          <p>Cofounder. AI-native operating systems for retail’s physical workflows. Hundreds of thousands of dollars raised in investment and innovation funding.</p>
        </div>
        <div class="work-meta">
          <span>2025 · Present</span>
          <span class="tag">Manhattan</span>
        </div>
      </div>
      <div class="work-item">
        <div class="work-num">002</div>
        <div class="work-main">
          <h4><a href="https://itubelabs.com" target="_blank" rel="noopener noreferrer">iTubeLabs</a></h4>
          <p>Solo project · AI-assisted YouTube creator growth workflows.</p>
        </div>
        <div class="work-meta">
          <span>2024 · Present</span>
          <span class="tag">Indie</span>
        </div>
      </div>
      <div class="work-item">
        <div class="work-num">003</div>
        <div class="work-main">
          <h4><a href="https://patents.google.com/patent/WO2020026037A1/en" target="_blank" rel="noopener noreferrer">Two-Stroke X-Shaped Engine</a></h4>
          <p>WIPO WO/2020/026037 · patented internal combustion architecture.</p>
          <div class="pub-inline-links">
            <a href="https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2020026037" target="_blank" rel="noopener noreferrer">WIPO dossier</a>
            <a href="https://open.mit.edu/c/lemelsoneducators/4bg/twostroke-xshaped-engine-the-future-of-automotive" target="_blank" rel="noopener noreferrer">MIT Open · Lemelson</a>
          </div>
        </div>
        <div class="work-meta">
          <span>2020 · Patent</span>
          <span class="tag">WIPO</span>
        </div>
      </div>
      <div class="work-item">
        <div class="work-num">004</div>
        <div class="work-main">
          <h4>Autonomous Vehicle Perception</h4>
          <p>TurtleBot · InDro · F1-Tenth · deep learning &amp; collaborative perception at Weber State.</p>
        </div>
        <div class="work-meta">
          <span>2022 · 2025</span>
          <span class="tag">Labs</span>
        </div>
      </div>
      <div class="work-item">
        <div class="work-num">005</div>
        <div class="work-main">
          <h4>Acoustic DoS mitigation (HDD)</h4>
          <p>ML-driven defenses against acoustic attacks on disks · simulations &amp; NCUR trajectory.</p>
        </div>
        <div class="work-meta">
          <span>2023 · 2025</span>
          <span class="tag">Security</span>
        </div>
      </div>
      <div class="work-item">
        <div class="work-num">006</div>
        <div class="work-main">
          <h4>Water Quality Forecasting (NCWQR)</h4>
          <p>ARIMA + supervised ML forecasting on phosphorus &amp; suspended sediment telemetry.</p>
        </div>
        <div class="work-meta">
          <span>2021 · 2022</span>
          <span class="tag">Applied ML</span>
        </div>
      </div>
    </div>
  </section>

  <section class="research" id="research">
    <div class="section-label">
      <span class="num">/ 04</span>
      Publications<br>&amp; Patents
    </div>
    <div>
      <ul class="pub-list">
        <li>
          <div class="pub-title">Two-Stroke X-Shaped Engine · WIPO #WO/2020/026037</div>
          <div class="pub-meta"><span class="date">June 2020</span><span>International patent dossier</span></div>
          <div class="pub-inline-links">
            <a href="https://patents.google.com/patent/WO2020026037A1/en" target="_blank" rel="noopener noreferrer">Google Patents</a>
            <a href="https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2020026037" target="_blank" rel="noopener noreferrer">Patentscope</a>
          </div>
        </li>
        <li>
          <div class="pub-title">Machine intelligence defenses for acoustic DoS on HDDs</div>
          <div class="pub-meta"><span class="date">In progress · WSU</span><span>With Kyle Feuz</span></div>
        </li>
        <li>
          <div class="pub-title">Forecasting Sandusky River particulate phosphorus ratios</div>
          <div class="pub-meta"><span class="date">April 2022 poster · NCWQR</span><span>Environmental ML</span></div>
          <div class="pub-inline-links">
            <a href="https://acrobat.adobe.com/link/track?uri=urn%3Aaaid%3Ascds%3AUS%3A160a31d0-0adc-3960-a272-1618d89d8739&amp;viewer%21megaVerb=group-discover" target="_blank" rel="noopener noreferrer">Poster preview (Adobe)</a>
          </div>
        </li>
      </ul>
    </div>
  </section>

  <section class="honors extra-section">
    <div class="honors-grid">
      <div class="section-label" id="honors">
        <span class="num">/ 05</span>
        Honors<br>&amp; Highlights
      </div>
      <div>
        <ul class="honors-list">
          <li><div class="honor-date">2025</div><div class="honor-body"><strong>navNote AI · investment</strong> · Hundreds of thousands of dollars raised in investment and innovation capital for the company.</div></li>
          <li><div class="honor-date">2022–2026</div><div class="honor-body"><strong>Scholarships &amp; research grants</strong> · More than $100,000 in combined internal and external awards supporting education and laboratory research.</div></li>
          <li><div class="honor-date">2014–2020</div><div class="honor-body"><strong>NODET (Iran)</strong> · top-ranked national talent entrance examination.</div></li>
          <li><div class="honor-date">2021 · Present</div><div class="honor-body"><strong>Harvard SEAS Computer Science Colloquium</strong> member.</div></li>
          <li><div class="honor-date">2021 · Present</div><div class="honor-body"><strong>IBM Z ambassador · workshop lead</strong>.</div></li>
          <li><div class="honor-date">2022 · Present</div><div class="honor-body"><strong>ACM professional member</strong>.</div></li>
          <li><div class="honor-date">2019 · 2021</div><div class="honor-body"><strong>Iran’s National Elites Foundation</strong> pipeline.</div></li>
          <li><div class="honor-date">July 2023</div><div class="honor-body"><strong>SWARM advising</strong> · NVIDIA &amp; HPE swarm learning rollout.</div></li>
          <li><div class="honor-date">2023 · 2024</div><div class="honor-body"><strong>Student senator · College of EAST</strong> · Weber State.</div></li>
          <li><div class="honor-date">Oct–Dec 2023</div><div class="honor-body"><strong>Faculty Senate &amp; Academic Resource committees</strong> · Weber State.</div></li>
          <li><div class="honor-date">Jan 2024 · Present</div><div class="honor-body"><strong>IT Advisory committee</strong> · Weber State.</div></li>
          <li><div class="honor-date">Jan 2024</div><div class="honor-body"><strong>Undergraduate Research grant (OUR)</strong> · Weber State.</div></li>
          <li><div class="honor-date">April 2022</div><div class="honor-body"><strong>Heidelberg immersion certificates</strong> · ambassador &amp; emerging leader laurels.</div></li>
          <li><div class="honor-date">2025</div><div class="honor-body"><strong>Utah innovation recognition</strong> · navNote AI early-stage citation.</div></li>
          <li><div class="honor-date">2026</div><div class="honor-body"><strong>Perplexity Business Fellow</strong> · Comet-style frontier AI cohort.</div></li>
        </ul>
      </div>
    </div>
  </section>

  <section class="extra-section" id="career">
    <div class="extra-inner">
      <div class="section-label"><span class="num">/ 06</span>Experience<br>&amp; Education</div>
      <div>
        <article class="cv-role">
          <h5>Researcher · AI/ML &amp; Backend Systems</h5>
          <div class="cv-meta">Weber State University · May 2025–present</div>
          <ul>
            <li>Faculty-mentored applied research through the navNote platform for enterprise field operations.</li>
            <li>Large-scale image understanding, predictive analytics, autonomous task orchestration, and scalable backend architectures.</li>
            <li>Raised hundreds of thousands of dollars in investment and innovation awards as navNote cofounder.</li>
          </ul>
        </article>
        <article class="cv-role">
          <h5>Graduate Teaching Assistant · CS 6300 Route Planning &amp; Navigation</h5>
          <div class="cv-meta">Weber State University · March 2023–Dec 2023</div>
          <ul>
            <li>Graduate studio bridging CS &amp; automotive engineering for cohort of seven scholars.</li>
            <li>Hands-on labs with TurtleBots, InDro hardware, F1-Tenth racing stacks.</li>
          </ul>
        </article>
        <article class="cv-role">
          <h5>Assistant Researcher · Autonomous Vehicles &amp; Robotics</h5>
          <div class="cv-meta">Weber State · Oct 2022–May 2025</div>
          <ul>
            <li>OpenCV / Torch pipelines, multi-LiDAR perception stacks, swarm learning pilots.</li>
            <li>Hosted lab tours / symposia to grow autonomy community on campus (+30% interest uplift).</li>
          </ul>
        </article>
        <article class="cv-role">
          <h5>Assistant Researcher · Acoustic denial &amp; cybersecurity</h5>
          <div class="cv-meta">Weber State · Jan 2023–May 2025</div>
          <ul>
            <li>Executed 100+ acoustic attack simulations paired with adaptive cancellation defenses.</li>
            <li>Secured $5k OUR grant earmarked toward NCUR presentation cycle.</li>
          </ul>
        </article>
        <article class="cv-role">
          <h5>Research collaborator · Environmental ML · NCWQR</h5>
          <div class="cv-meta">Nov 2021–Sep 2022</div>
          <ul>
            <li>Predictive models on phosphorus + suspended sediment interplay with collaborator institutions.</li>
            <li>Visualization dashboards for watershed stakeholders.</li>
          </ul>
        </article>
        <article class="cv-role">
          <h5>Bachelor of Science · Computer Science</h5>
          <div class="cv-meta">Weber State · 2022–present (expected December 2026)</div>
          <ul>
            <li>More than $100,000 in combined university scholarships and external research grants across the program.</li>
          </ul>
        </article>
      </div>
    </div>
  </section>

  <section class="extra-section" id="profiles">
    <div class="extra-inner">
      <div class="section-label"><span class="num">/ 07</span>Professional<br>profiles</div>
      <div>
        <p style="font-size:16px;color:var(--ink-soft);margin-bottom:8px;line-height:1.6;">
          Verified profiles and canonical links for navNote AI, research IDs, patents, and institutional references.
        </p>
        <div class="link-grid">
          <a href="https://www.linkedin.com/in/mousavi-ai/">LinkedIn</a>
          <a href="https://twitter.com/thisisEsmaeil">X / Twitter (@thisisEsmaeil)</a>
          <a href="https://github.com/esmaeilmousavi">GitHub · esmaeilmousavi</a>
          <a href="https://github.com/mousaviasl">GitHub · mousaviasl</a>
          <a href="https://scholar.google.com/citations?hl=en&amp;user=lZQif9oAAAAJ">Google Scholar</a>
          <a href="https://orcid.org/0000-0002-2483-4275">ORCID</a>
          <a href="https://www.wikidata.org/wiki/Q131101184">Wikidata</a>
          <a href="https://open.mit.edu/profile/01G7XMK3A48PDBDGVNMSTJWQTN/">MIT Open profile</a>
          <a href="https://g.co/kgs/7GbuQHr">Google Knowledge shortcut</a>
          <a href="https://www.crunchbase.com/person/esmaeil-mousavi">Crunchbase · person</a>
          <a href="https://www.crunchbase.com/organization/navnote">Crunchbase · navNote</a>
          <a href="https://www.linkedin.com/company/navnote">LinkedIn · navNote</a>
          <a href="https://www.ihubutah.org/directory/people/details/esmaeil+mousavi/r/recHYS1kzup6X3Eyx">Utah Innovation Hub portrait</a>
          <a href="/documents/Esmaeil-Mousavi-CV.pdf">Curriculum vitae (PDF)</a>
          <a href="https://www.navnote.ai/">navNote AI</a>
          <a href="https://www.navnote.ai/contact">navNote · contact</a>
          <a href="https://itubelabs.com">iTubeLabs</a>
          <a href="https://ncwqr.org/">National Center for Water Quality Research</a>
          <a href="https://www.ibm.com/z">IBM Z Systems</a>
          <a href="https://open.mit.edu/">MIT Open Learning</a>
          <a href="https://www.acm.org/">ACM</a>
          <a href="https://www.perplexity.ai/">Perplexity</a>
          <a href="https://www.mimik.com/">mimik Technologies</a>
          <a href="https://calendly.com/esmaeilmousavi-weber">Calendly</a>
          <a href="https://sites.google.com/mail.weber.edu/esmaeil/contact-esmaeil/contact-info">Weber dossier · contact archive</a>
          <a href="https://sites.google.com/mail.weber.edu/esmaeil/pictures">Weber dossier · photos</a>
          <a href="https://sites.google.com/mail.weber.edu/esmaeil/">Weber dossier · legacy site root</a>
          <a href="https://www.weber.edu/computing">Weber · School of Computing</a>
        </div>
      </div>
    </div>
  </section>

  <section class="extra-section">
    <div class="extra-inner">
      <div class="section-label"><span class="num">/ 08</span>Partners</div>
      <div class="collabs-wrap">
        <p style="margin-bottom:12px;color:var(--ink-soft);font-size:17px;">Institutions &amp; sponsors.</p>
        <img alt="Collaborators collage" src="images/Collabs.png" loading="lazy" decoding="async" />
      </div>
    </div>
  </section>

  <section class="extra-section">
    <div class="extra-inner">
      <div class="section-label"><span class="num">/ 09</span>Addresses</div>
      <div>
        <div class="address-block">
          <strong>Manhattan · navNote AI HQ</strong>
          <div><a href="https://maps.google.com/?q=60+Madison+Avenue+New+York+NY+10010">60 Madison Avenue, 9th Floor, New York, NY 10010</a></div>
        </div>
        <div class="address-block" style="margin-top:24px;">
          <strong>Ogden · Weber State research</strong>
          <div><a href="https://maps.app.goo.gl/Sj19cZZqcoe2wRrF8">Room 337, School of Computing Faculty Research Lab, Noorda Applied Science &amp; Technology Building, 1465 Edvalson St, Ogden, UT 84403</a></div>
        </div>
        <div class="address-block" style="margin-top:24px;">
          <strong>Provo · Utah Innovation Hub (iHub)</strong>
          <div><a href="https://maps.google.com/?q=1555+N+Freedom+Blvd+Provo+UT+84604">1555 N Freedom Blvd, Suite 200, Provo, UT 84604</a></div>
        </div>
      </div>
    </div>
  </section>

  <section class="extra-section" id="speaking">
    <div class="extra-inner">
      <div class="section-label"><span class="num">/ 10</span>Speaking &amp;<br>Programs</div>
      <div>
        <div class="speaking-row"><div class="speak-date">November 2023</div><div class="speak-body">Organizer &amp; panelist · Weber State AI &amp; Autonomous Vehicles Symposium.</div></div>
        <div class="speaking-row"><div class="speak-date">October 2023</div><div class="speak-body">VIP delegate · Utah AI leadership summit hosted at Pluralsight Navigate / Grand America Hotel.</div></div>
        <div class="speaking-row"><div class="speak-date">July 2023</div><div class="speak-body">Participant · NASA JPL uncertainty quantification colloquium (Caltech Pasadena).</div></div>
        <div class="speaking-row"><div class="speak-date">March 2023</div><div class="speak-body">Participant · Terasaki Institute innovation summit · UCLA campus.</div></div>
        <div class="speaking-row"><div class="speak-date">November 2023</div><div class="speak-body">Leadership to Legacy programming · Weber State.</div></div>
        <div class="speaking-row"><div class="speak-date">April 2022</div><div class="speak-body">Poster presenter · Heidelberg University research symposium · Tiffin, OH.</div></div>
      </div>
    </div>
  </section>

  <section class="extra-section" id="gallery">
    <div class="extra-inner">
      <div class="section-label"><span class="num">/ 11</span>Photo gallery</div>
      <div>
        <p style="color:var(--ink-soft);font-size:17px;">Documenting research travel, prototyping sprints, and collaborations.</p>
        <div class="gallery-grid-port">
{gallery}
        </div>
      </div>
    </div>
  </section>

  <footer class="bottom" id="contact">
    <div class="footer-grid">
      <div class="footer-pull">
        Most doors that seem locked aren’t · they haven’t been <em>pushed.</em>
      </div>
      <div class="contact-block">
        <div class="label">Say hello</div>
        <a href="mailto:esmaeil@navnote.ai">esmaeil@navnote.ai</a>
        <a href="/documents/Esmaeil-Mousavi-CV.pdf">Curriculum vitae (PDF)</a>
        <a href="https://www.navnote.ai/">navnote.ai</a>
        <a href="https://www.linkedin.com/in/mousavi-ai/">LinkedIn · in/mousavi-ai</a>
        <a href="https://github.com/esmaeilmousavi">GitHub</a>
      </div>
    </div>
    <div class="colophon">
      <span>© Esmaeil Mousavi · Manhattan · Provo · Ogden</span>
      <span>New studio skin · Feb 2026</span>
    </div>
  </footer>

</div>

</body>
</html>
"""


def main() -> None:
    spaced = "\n".join(("      " + ln if ln.strip() else "") for ln in GALLERY.splitlines())
    assembled = BODY.replace("{gallery}", spaced)
    html = HEAD + assembled
    (REPO / "index.html").write_text(html, encoding="utf-8")
    print("Wrote index.html,", len(html), "chars")


if __name__ == "__main__":
    main()
