import streamlit as st


st.set_page_config(page_title="Adelantado Arquitectura", page_icon="✦", layout="wide")

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Instrument+Serif:ital@0;1&display=swap');

        :root {
            --paper: #eeeae4;
            --ink: #181817;
            --muted: #716e68;
            --line: rgba(24, 24, 23, .2);
            --accent: #c15e43;
        }

        #MainMenu, header[data-testid="stHeader"], footer,
        div[data-testid="stToolbar"], div[data-testid="stDecoration"] { display: none !important; }
        html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
            background: var(--paper); color: var(--ink); font-family: 'DM Mono', monospace;
        }
        .block-container { max-width: 100%; padding: 0 !important; }
        * { box-sizing: border-box; }
        a { color: inherit; }

        .site { overflow: hidden; }
        .topbar { position: absolute; top: 0; left: 0; right: 0; z-index: 3; display: flex;
            justify-content: space-between; align-items: center; padding: 1.35rem 4vw; font-size: .68rem;
            letter-spacing: .12em; text-transform: uppercase; }
        .topbar a { text-decoration: none; }
        .topmark { display: flex; align-items: center; gap: .65rem; white-space: nowrap; }
        .brand-logo { display: block; width: 30px; height: 22px; flex: 0 0 auto; }
        .brand-logo path { fill: none; stroke: currentColor; stroke-width: 2.4; stroke-linecap: round; stroke-linejoin: round; }
        .brand-logo rect { fill: currentColor; opacity: .14; stroke: none; }
        .nav { display: flex; gap: 2rem; }
        .nav a:hover { color: var(--accent); }

        .hero { min-height: 100vh; display: grid; grid-template-columns: 1.05fr .95fr; padding-top: 4.5rem; }
        .hero-copy { display: flex; flex-direction: column; justify-content: space-between; padding: 11vh 8vw 5rem 8vw; }
        .hero-brand { width: min(100%, 31rem); margin-bottom: 3.2rem; text-align: left; }
        .lockup-mark { display: block; width: min(14rem, 58vw); height: auto; margin: 0 0 1.5rem; }
        .lockup-mark path { fill: none; stroke: var(--ink); stroke-width: 2.2; stroke-linecap: round; stroke-linejoin: round; }
        .lockup-mark polygon { fill: rgba(24, 24, 23, .2); stroke: none; }
        .lockup-name { margin: 0; font-family: 'DM Mono', monospace; font-size: clamp(1.25rem, 2.8vw, 2.35rem); font-weight: 400;
          letter-spacing: .19em; line-height: 1; white-space: nowrap; }
        .lockup-sub { margin: .9rem 0 0; font-family: 'DM Mono', monospace; font-size: clamp(.66rem, 1.25vw, 1rem);
          letter-spacing: .48em; line-height: 1; white-space: nowrap; }
        .eyebrow { font-size: .66rem; letter-spacing: .14em; text-transform: uppercase; color: var(--muted); }
        .hero h1 { font-family: 'Instrument Serif', serif; font-weight: 400; font-size: clamp(5rem, 10vw, 11rem); line-height: .78;
            letter-spacing: -.055em; max-width: 8ch; margin: 0; }
        .hero h1 em { color: var(--accent); font-style: italic; }
        .hero-intro { max-width: 30rem; font-size: .75rem; line-height: 1.8; color: var(--muted); }
        .hero-art { min-height: 90vh; margin: 0 4vw 4vw 0; position: relative; overflow: hidden;
            background: linear-gradient(135deg, rgba(22,30,26,.1), rgba(22,30,26,.02)),
            url('https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?auto=format&fit=crop&w=1400&q=85') center/cover; }
        .hero-art:after { content: '01 / 04'; position: absolute; bottom: 1.2rem; left: 1.3rem; color: white; font-size: .68rem; letter-spacing: .12em; }
        .vertical-note { position: absolute; right: 1rem; top: 1rem; writing-mode: vertical-rl; color: white; font-size: .6rem; letter-spacing: .14em; }

        .section { padding: 9rem 8vw; border-top: 1px solid var(--line); }
        .section-head { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4rem; }
        .section-title { font-family: 'Instrument Serif', serif; font-weight: 400; font-size: clamp(3.3rem, 7vw, 7rem); line-height: .85; letter-spacing: -.045em; margin: 0; }
        .section-number { font-size: .65rem; color: var(--muted); letter-spacing: .12em; }
        .manifesto { display: grid; grid-template-columns: 1fr 1fr; gap: 7vw; }
        .manifesto-lead { font-family: 'Instrument Serif', serif; font-size: clamp(2rem, 3.4vw, 4.2rem); line-height: .95; margin: 0; }
        .manifesto-copy { align-self: end; max-width: 29rem; color: var(--muted); font-size: .74rem; line-height: 1.9; }
        .manifesto-copy strong { color: var(--ink); font-weight: 500; }

        .projects { display: grid; grid-template-columns: 1.25fr .75fr; gap: 2rem; }
        .project { margin: 0; }
        .project:nth-child(2) { margin-top: 9rem; }
        .project-image { aspect-ratio: 1.18 / 1; overflow: hidden; background-size: cover; background-position: center; transition: transform .6s ease; }
        .project:hover .project-image { transform: scale(.985); }
        .project-image.one { background-image: url('https://images.unsplash.com/photo-1600607687920-4e2a09cf159d?auto=format&fit=crop&w=1200&q=85'); }
        .project-image.two { background-image: url('https://images.unsplash.com/photo-1600566753190-17f0baa2a6c3?auto=format&fit=crop&w=1000&q=85'); }
        .project figcaption { display: flex; justify-content: space-between; padding-top: .9rem; font-size: .68rem; text-transform: uppercase; letter-spacing: .09em; }
        .project figcaption span:last-child { color: var(--muted); }

        .services { display: grid; grid-template-columns: .8fr 1.2fr; gap: 8vw; }
        .services-intro { font-family: 'Instrument Serif', serif; font-size: 2rem; line-height: 1; max-width: 15rem; }
        .service-list { border-top: 1px solid var(--line); }
        .service { display: grid; grid-template-columns: 3rem 1fr auto; gap: 1rem; align-items: center; padding: 1.4rem 0; border-bottom: 1px solid var(--line); font-size: .76rem; }
        .service span:first-child, .service span:last-child { color: var(--muted); font-size: .63rem; }

        .contact { min-height: 72vh; display: flex; flex-direction: column; justify-content: space-between; background: var(--ink); color: var(--paper); }
        .contact .section-number, .contact .eyebrow { color: rgba(238,234,228,.55); }
        .contact h2 { font-family: 'Instrument Serif', serif; font-weight: 400; font-size: clamp(4rem, 10vw, 11rem); line-height: .76; letter-spacing: -.06em; max-width: 8ch; margin: 0; }
        .contact h2 em { color: var(--accent); }
        .contact-bottom { display: flex; justify-content: space-between; align-items: end; gap: 2rem; font-size: .7rem; }
        .contact-button { display: inline-flex; padding: 1rem 1.4rem; border: 1px solid rgba(238,234,228,.45); border-radius: 999px; text-decoration: none; text-transform: uppercase; letter-spacing: .1em; }
        .contact-button:hover { background: var(--paper); color: var(--ink); }
        .footer { padding: 1.3rem 8vw; display: flex; justify-content: space-between; border-top: 1px solid rgba(238,234,228,.2); color: rgba(238,234,228,.55); font-size: .62rem; letter-spacing: .08em; text-transform: uppercase; }

        @media (max-width: 760px) {
            .topbar { padding: 1.1rem 1.25rem; }
            .nav { gap: .8rem; font-size: .58rem; }
            .hero { display: flex; flex-direction: column; padding-top: 4rem; }
            .hero-copy { min-height: 62vh; padding: 8vh 1.25rem 3rem; }
            .hero-brand { margin-bottom: 2.5rem; }
            .lockup-mark { width: 9.5rem; margin-bottom: 1.05rem; }
            .lockup-name { font-size: clamp(.95rem, 5vw, 1.35rem); letter-spacing: .14em; }
            .lockup-sub { margin-top: .7rem; font-size: .58rem; letter-spacing: .35em; }
            .hero h1 { font-size: clamp(4.8rem, 23vw, 7rem); }
            .hero-art { min-height: 58vh; margin: 0 1.25rem 1.25rem; }
            .section { padding: 5.5rem 1.25rem; }
            .section-head { margin-bottom: 2.5rem; }
            .manifesto, .services, .projects { grid-template-columns: 1fr; gap: 2.5rem; }
            .project:nth-child(2) { margin-top: 0; }
            .project-image { aspect-ratio: 1.15 / 1; }
            .contact { min-height: 78vh; }
            .contact-bottom { align-items: start; flex-direction: column; }
            .footer { padding: 1.2rem 1.25rem; }
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <main class="site">
      <header class="topbar">
        <a class="topmark" href="#inicio">
          <svg class="brand-logo" viewBox="0 0 80 58" aria-label="Logo Adelantado Arquitectura" role="img">
            <path d="M8 42 40 8l32 34"/><path d="M20 42V24h40v18"/><path d="M20 42h40"/><path d="M30 42V31h20v11"/><rect x="34" y="26" width="12" height="16"/>
          </svg>
          Adelantado / Arquitectura
        </a>
        <nav class="nav" aria-label="Navegación principal">
          <a href="#estudio">Estudio</a><a href="#proyectos">Proyectos</a><a href="#contacto">Contacto</a>
        </nav>
      </header>

      <section class="hero" id="inicio">
        <div class="hero-copy">
          <div class="hero-brand" aria-label="Adelantado Arquitectura">
            <svg class="lockup-mark" viewBox="0 0 190 150" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Isotipo Adelantado">
              <path d="M20 105 150 25v45l38 23v38"/><path d="M20 135 102 91"/><path d="M150 70 188 93"/><polygon points="108,50 140,69 140,119 108,119"/>
            </svg>
            <p class="lockup-name">ADELANTADO</p>
            <p class="lockup-sub">ARQUITECTURA</p>
          </div>
          <p class="eyebrow">Arquitectura · Interiorismo · Territorio</p>
          <h1>Espacios<br>con <em>carácter.</em></h1>
          <p class="hero-intro">Adelantado Arquitectura es un estudio independiente que transforma la forma de habitar en una experiencia serena, precisa y duradera.</p>
        </div>
        <div class="hero-art"><span class="vertical-note">Casa en la sierra · Madrid · 2024</span></div>
      </section>

      <section class="section" id="estudio">
        <div class="section-head"><h2 class="section-title">El estudio</h2><span class="section-number">01 — 04</span></div>
        <div class="manifesto">
          <p class="manifesto-lead">Diseñamos lo esencial para que cada lugar pueda contar su propia historia.</p>
          <p class="manifesto-copy"><strong>Adelantado Arquitectura</strong> nace de una manera de mirar: escuchar el contexto, entender la materia y construir con intención. Trabajamos desde la escala doméstica hasta espacios colectivos, buscando siempre una belleza que no dependa de la tendencia.<br><br>La luz, la proporción y el tiempo son nuestras herramientas.</p>
        </div>
      </section>

      <section class="section" id="proyectos">
        <div class="section-head"><h2 class="section-title">Proyectos<br><em>seleccionados</em></h2><span class="section-number">02 — 04</span></div>
        <div class="projects">
          <figure class="project"><div class="project-image one"></div><figcaption><span>Casa Ladera</span><span>Madrid · 2024</span></figcaption></figure>
          <figure class="project"><div class="project-image two"></div><figcaption><span>Patio Blanco</span><span>Toledo · 2023</span></figcaption></figure>
        </div>
      </section>

      <section class="section" id="servicios">
        <div class="section-head"><h2 class="section-title">Cómo<br>trabajamos</h2><span class="section-number">03 — 04</span></div>
        <div class="services">
          <p class="services-intro">Un proceso cercano, claro y atento a cada decisión.</p>
          <div class="service-list">
            <div class="service"><span>01</span><span>Arquitectura y obra nueva</span><span>→</span></div>
            <div class="service"><span>02</span><span>Rehabilitación y reforma</span><span>→</span></div>
            <div class="service"><span>03</span><span>Interiorismo y detalle</span><span>→</span></div>
            <div class="service"><span>04</span><span>Dirección y acompañamiento</span><span>→</span></div>
          </div>
        </div>
      </section>

      <section class="section contact" id="contacto">
        <div class="section-head"><p class="eyebrow">¿Hablamos?</p><span class="section-number">04 — 04</span></div>
        <h2>Hagamos<br>algo <em>duradero.</em></h2>
        <div class="contact-bottom"><span>Madrid · España<br>hola@adelantadoarquitectura.com</span><a class="contact-button" href="mailto:hola@adelantadoarquitectura.com">Iniciar conversación ↗</a></div>
      </section>
      <footer class="footer"><span>© 2026 Adelantado Arquitectura</span><span>Instagram · LinkedIn</span></footer>
    </main>
    """,
    unsafe_allow_html=True,
)
