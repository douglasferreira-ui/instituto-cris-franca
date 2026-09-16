import base64
from pathlib import Path
from urllib.parse import quote

import streamlit as st

# ============================================================
# CONFIGURAÇÕES DO SITE
# ============================================================
BASE_DIR = Path(__file__).parent
ASSETS = BASE_DIR / "assets"

WHATSAPP_NUMBER = "5511945714554"
INSTAGRAM_URL = "https://www.instagram.com/crisfrancah/"
CRP = ""  # Ex.: "CRP 06/000000". Deixe vazio se ainda não quiser exibir.

st.set_page_config(
    page_title="Instituto Cris França | Psicologia & Terapias Integrativas",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def file_to_data_uri(path: Path) -> str:
    suffix = path.suffix.lower().replace(".", "")
    mime = "jpeg" if suffix in {"jpg", "jpeg"} else suffix
    data = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:image/{mime};base64,{data}"


def wa_link(message: str) -> str:
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"


def section_anchor(anchor: str):
    st.markdown(f'<div id="{anchor}" class="anchor"></div>', unsafe_allow_html=True)


logo_full = file_to_data_uri(ASSETS / "logo_full.png")
logo_icon = file_to_data_uri(ASSETS / "logo_icon.png")
avatar = file_to_data_uri(ASSETS / "cris_avatar.jpg")
instagram_screen = file_to_data_uri(ASSETS / "instagram_profile.png")
cris_post = file_to_data_uri(ASSETS / "cris_post.jpg")

# ============================================================
# IDENTIDADE VISUAL
# ============================================================
st.markdown(
    """
<style>
:root {
    --bg: #fbf9f5;
    --paper: #ffffff;
    --paper-2: #f4f1ea;
    --ink: #40382f;
    --muted: #746c63;
    --olive: #75806a;
    --olive-dark: #59644f;
    --gold: #c8a15f;
    --gold-soft: #ead9b9;
    --brown: #4a2d1c;
    --line: rgba(74,45,28,.12);
    --shadow: 0 18px 55px rgba(63, 53, 43, .10);
}

html { scroll-behavior: smooth; }
body, [class*="css"] { color: var(--ink); }
.stApp {
    background:
      radial-gradient(circle at 6% 8%, rgba(200,161,95,.10), transparent 24%),
      radial-gradient(circle at 92% 25%, rgba(117,128,106,.10), transparent 26%),
      var(--bg);
}
.block-container {
    max-width: 1180px;
    padding-top: 1.1rem;
    padding-bottom: 3rem;
}
header[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }
[data-testid="stToolbar"] { display: none; }
[data-testid="collapsedControl"] { display: none; }
.anchor { position: relative; top: -95px; visibility: hidden; }

/* NAV */
.topnav {
    position: sticky;
    top: .65rem;
    z-index: 999;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 22px;
    padding: 12px 18px;
    margin-bottom: 24px;
    border: 1px solid rgba(74,45,28,.09);
    background: rgba(251,249,245,.91);
    backdrop-filter: blur(18px);
    border-radius: 22px;
    box-shadow: 0 10px 35px rgba(63,53,43,.07);
}
.brand-nav { display:flex; align-items:center; gap:10px; min-width:210px; }
.brand-nav img { width: 162px; height:auto; display:block; }
.navlinks { display:flex; align-items:center; gap:18px; flex-wrap:wrap; justify-content:flex-end; }
.navlinks a { color:var(--ink); text-decoration:none; font:600 14px/1.2 Arial, sans-serif; }
.navlinks a:hover { color:var(--olive-dark); }
.nav-cta {
    background:var(--olive-dark);
    color:#fff !important;
    padding:10px 15px;
    border-radius:999px;
}

/* HERO */
.hero {
    position: relative;
    overflow: hidden;
    display:grid;
    grid-template-columns: 1.38fr .72fr;
    gap: 28px;
    align-items:center;
    min-height: 590px;
    padding: clamp(30px,5vw,70px);
    border-radius: 34px;
    border: 1px solid rgba(74,45,28,.08);
    background: linear-gradient(135deg, #fffdf9 0%, #f4f0e6 62%, #eef1e9 100%);
    box-shadow: var(--shadow);
}
.hero::after {
    content:"";
    position:absolute;
    width:440px;
    height:440px;
    right:-125px;
    bottom:-160px;
    background: radial-gradient(circle, rgba(200,161,95,.28), rgba(200,161,95,0) 68%);
}
.eyebrow {
    display:inline-flex;
    align-items:center;
    gap:8px;
    padding:8px 13px;
    border-radius:999px;
    background:rgba(117,128,106,.10);
    color:var(--olive-dark);
    font:700 12px/1 Arial,sans-serif;
    letter-spacing:.08em;
    text-transform:uppercase;
    margin-bottom:18px;
}
.hero h1 {
    margin:0;
    max-width: 760px;
    color:var(--brown);
    font-size: clamp(44px, 6vw, 78px);
    line-height: .98;
    letter-spacing:-.035em;
    font-weight:500;
}
.hero h1 em { color:var(--olive-dark); font-style:italic; }
.hero p {
    max-width:720px;
    margin:22px 0 0;
    color:var(--muted);
    font: 400 clamp(17px,1.8vw,21px)/1.65 Arial,sans-serif;
}
.hero-buttons { display:flex; gap:12px; flex-wrap:wrap; margin-top:30px; }
.btn {
    display:inline-flex;
    align-items:center;
    justify-content:center;
    gap:9px;
    padding:14px 19px;
    border-radius:999px;
    text-decoration:none !important;
    font:700 14px/1 Arial,sans-serif;
    transition:.2s ease;
}
.btn-primary { background:var(--olive-dark); color:white !important; box-shadow:0 10px 22px rgba(89,100,79,.20); }
.btn-primary:hover { transform:translateY(-2px); }
.btn-secondary { background:#fff; color:var(--ink) !important; border:1px solid var(--line); }
.btn-gold { background:var(--gold); color:#2e241d !important; }
.microcopy { margin-top:15px; font:500 12px/1.5 Arial,sans-serif; color:#857c72; }
.hero-person {
    position:relative;
    z-index:2;
    display:flex;
    justify-content:center;
    align-items:center;
}
.portrait-wrap {
    position:relative;
    width:min(360px, 78vw);
    aspect-ratio:1/1;
    padding:14px;
    border-radius:50%;
    background:linear-gradient(145deg,#fff,#e8e2d6);
    box-shadow:0 25px 70px rgba(63,53,43,.18);
}
.portrait-wrap::before {
    content:"";
    position:absolute;
    inset:-14px;
    border:1px solid rgba(200,161,95,.50);
    border-radius:50%;
}
.portrait-wrap img { width:100%;height:100%;object-fit:cover;border-radius:50%;display:block; }
.float-card {
    position:absolute;
    left:-26px;
    bottom:22px;
    width:215px;
    padding:14px 15px;
    border-radius:18px;
    background:rgba(255,255,255,.94);
    border:1px solid var(--line);
    box-shadow:0 14px 35px rgba(63,53,43,.12);
    font:600 13px/1.45 Arial,sans-serif;
    color:var(--ink);
}
.float-card span { color:var(--olive-dark); font-weight:800; }

/* SEÇÕES */
.section { padding: 88px 4px 22px; }
.section-kicker { color:var(--gold); font:800 12px/1 Arial,sans-serif; text-transform:uppercase; letter-spacing:.14em; margin-bottom:12px; }
.section-title { color:var(--brown); font-size:clamp(34px,4.5vw,54px); line-height:1.06; letter-spacing:-.025em; margin:0 0 14px; font-weight:500; }
.section-sub { color:var(--muted); font:400 17px/1.7 Arial,sans-serif; max-width:820px; margin:0 0 30px; }

.trust-grid { display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-top:24px; }
.trust-item { background:#fff;border:1px solid var(--line);border-radius:18px;padding:17px;box-shadow:0 9px 28px rgba(63,53,43,.05); }
.trust-item strong { display:block;color:var(--brown);font:800 14px/1.3 Arial,sans-serif;margin-bottom:5px; }
.trust-item span { color:var(--muted);font:400 13px/1.55 Arial,sans-serif; }

.cards-grid { display:grid;grid-template-columns:repeat(3,1fr);gap:16px; }
.service-card {
    min-height:215px;
    padding:24px;
    border-radius:24px;
    background:#fff;
    border:1px solid var(--line);
    box-shadow:0 12px 35px rgba(63,53,43,.055);
    transition:.25s ease;
}
.service-card:hover { transform:translateY(-3px); box-shadow:0 18px 45px rgba(63,53,43,.09); }
.service-icon { width:46px;height:46px;border-radius:15px;background:#eef0e9;display:flex;align-items:center;justify-content:center;font-size:24px;margin-bottom:22px; }
.service-card h3 { margin:0 0 10px;color:var(--brown);font-size:22px;line-height:1.15; }
.service-card p { margin:0;color:var(--muted);font:400 14px/1.7 Arial,sans-serif; }

.highlight {
    margin-top: 30px;
    display:grid;
    grid-template-columns: .82fr 1.18fr;
    overflow:hidden;
    border-radius:30px;
    background:var(--olive-dark);
    color:#fff;
}
.highlight .photo { min-height:420px;background-size:cover;background-position:center; }
.highlight .text { padding:46px;display:flex;flex-direction:column;justify-content:center; }
.highlight .text h3 { font-size:clamp(32px,4vw,50px);line-height:1.02;margin:0 0 16px;font-weight:500; }
.highlight .text p { color:rgba(255,255,255,.82);font:400 16px/1.75 Arial,sans-serif; }
.highlight .mini { color:#ecd6ad;font:800 12px/1 Arial,sans-serif;letter-spacing:.12em;text-transform:uppercase;margin-bottom:13px; }

/* FLORAIS */
.catalog-note {
    margin:16px 0 28px;
    border-left:4px solid var(--gold);
    padding:14px 16px;
    background:#fffaf0;
    border-radius:0 14px 14px 0;
    color:#6e604d;
    font:500 13px/1.65 Arial,sans-serif;
}
.floral-card {
    height:100%;
    min-height:220px;
    padding:22px;
    border-radius:22px;
    background:#fff;
    border:1px solid var(--line);
    box-shadow:0 9px 26px rgba(63,53,43,.05);
}
.floral-tag { display:inline-block;padding:6px 9px;border-radius:999px;background:#eef0e9;color:var(--olive-dark);font:800 10px/1 Arial,sans-serif;text-transform:uppercase;letter-spacing:.06em;margin-bottom:13px; }
.floral-card h4 { margin:0 0 9px;color:var(--brown);font-size:20px;line-height:1.2; }
.floral-card p { margin:0 0 18px;color:var(--muted);font:400 13.5px/1.65 Arial,sans-serif; }
.floral-card a { color:var(--olive-dark);font:800 12px/1 Arial,sans-serif;text-decoration:none; }

/* PROCESSO */
.steps { display:grid;grid-template-columns:repeat(3,1fr);gap:16px; }
.step { padding:25px;border-radius:22px;background:#f0eee8;border:1px solid var(--line); }
.step-num { color:var(--gold);font:500 42px/1 Georgia,serif; }
.step h4 { margin:12px 0 9px;font-size:20px;color:var(--brown); }
.step p { margin:0;color:var(--muted);font:400 14px/1.65 Arial,sans-serif; }

/* INSTAGRAM */
.instagram-box { display:grid;grid-template-columns:1fr .82fr;gap:24px;align-items:center;background:#fff;border:1px solid var(--line);border-radius:28px;padding:24px;box-shadow:var(--shadow); }
.instagram-box img { width:100%;display:block;border-radius:20px;border:1px solid var(--line); }

/* CONTATO */
.contact-panel { padding:42px;border-radius:30px;background:linear-gradient(135deg,#46301f,#5d4a36 58%,#66705c);color:#fff;box-shadow:var(--shadow); }
.contact-panel h3 { font-size:clamp(34px,4vw,52px);line-height:1.03;font-weight:500;margin:0 0 12px; }
.contact-panel p { color:rgba(255,255,255,.78);font:400 15px/1.7 Arial,sans-serif;max-width:720px; }

.footer { text-align:center;padding:50px 12px 25px;color:#837b72;font:400 12px/1.7 Arial,sans-serif; }
.footer img { width:190px;max-width:70%;height:auto;opacity:.92;margin-bottom:12px; }

/* STREAMLIT COMPONENTS */
.stTextInput input, .stTextArea textarea, .stSelectbox [data-baseweb="select"] > div {
    border-radius:14px !important;
    border-color:rgba(74,45,28,.14) !important;
    background:#fff !important;
}
.stButton button, .stLinkButton a { border-radius:999px !important; font-weight:700 !important; }

@media (max-width: 980px) {
    .navlinks a:not(.nav-cta) { display:none; }
    .hero { grid-template-columns:1fr;min-height:auto;padding:34px 24px; }
    .hero-person { order:-1;margin-top:10px; }
    .portrait-wrap { width:min(300px,74vw); }
    .float-card { left:0;bottom:-12px;width:190px; }
    .trust-grid, .cards-grid { grid-template-columns:repeat(2,1fr); }
    .highlight, .instagram-box { grid-template-columns:1fr; }
    .highlight .photo { min-height:360px; }
    .steps { grid-template-columns:1fr; }
}
@media (max-width: 620px) {
    .block-container { padding-left:14px;padding-right:14px; }
    .topnav { border-radius:18px;padding:10px 12px; }
    .brand-nav img { width:145px; }
    .nav-cta { font-size:12px !important;padding:9px 11px; }
    .hero h1 { font-size:44px; }
    .hero { border-radius:25px; }
    .trust-grid, .cards-grid { grid-template-columns:1fr; }
    .section { padding-top:68px; }
    .highlight .text, .contact-panel { padding:28px 22px; }
    .instagram-box { padding:14px; }
}
</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# NAVEGAÇÃO
# ============================================================
main_wa = wa_link("Olá, Cris! Vim pelo seu site e gostaria de saber mais sobre os atendimentos.")

st.markdown(
    f"""
<nav class="topnav">
  <div class="brand-nav"><img src="{logo_full}" alt="Instituto Cris França"></div>
  <div class="navlinks">
    <a href="#sobre">Sobre</a>
    <a href="#atuacao">Atuação</a>
    <a href="#florais">Florais</a>
    <a href="#instagram">Instagram</a>
    <a class="nav-cta" href="{main_wa}" target="_blank">Agendar consulta</a>
  </div>
</nav>
""",
    unsafe_allow_html=True,
)

# ============================================================
# HERO
# ============================================================
section_anchor("inicio")
crp_line = f" • {CRP}" if CRP else ""
st.markdown(
    f"""
<section class="hero">
  <div>
    <div class="eyebrow">Psicologia & Terapias Integrativas</div>
    <h1>Um espaço para <em>acolher</em>, compreender e transformar.</h1>
    <p>
      Atendimento psicológico com foco em dependência emocional, fortalecimento da autoestima
      e relações mais saudáveis, integrado a recursos complementares como Florais de Saint Germain
      e Medicina Tradicional Chinesa.
    </p>
    <div class="hero-buttons">
      <a class="btn btn-primary" href="{main_wa}" target="_blank">💬 Agendar pelo WhatsApp</a>
      <a class="btn btn-secondary" href="{INSTAGRAM_URL}" target="_blank">◎ Conhecer o Instagram</a>
    </div>
    <div class="microcopy">Atendimento online e presencial{crp_line} • Consulte horários pelo WhatsApp</div>
  </div>
  <div class="hero-person">
    <div class="portrait-wrap"><img src="{avatar}" alt="Cris França"></div>
    <div class="float-card"><span>Atendimento individual</span><br>com escuta cuidadosa, ética e acolhimento.</div>
  </div>
</section>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="trust-grid">
  <div class="trust-item"><strong>🧠 Psicologia</strong><span>Escuta clínica e acompanhamento individual.</span></div>
  <div class="trust-item"><strong>💔 Dependência emocional</strong><span>Foco em limites, autoestima e vínculos mais saudáveis.</span></div>
  <div class="trust-item"><strong>🌿 Terapias integrativas</strong><span>Recursos complementares dentro de uma abordagem de cuidado.</span></div>
  <div class="trust-item"><strong>🎤 Palestras</strong><span>Conteúdos para grupos, empresas e eventos.</span></div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================
# SOBRE
# ============================================================
section_anchor("sobre")
st.markdown(
    """
<div class="section">
  <div class="section-kicker">Sobre a profissional</div>
  <h2 class="section-title">Cuidado emocional com presença, técnica e humanidade.</h2>
  <p class="section-sub">
    O Instituto Cris França nasce para oferecer um espaço de escuta e desenvolvimento emocional,
    unindo Psicologia a práticas integrativas de forma complementar e responsável. O trabalho é
    direcionado a pessoas que desejam compreender seus padrões, fortalecer o próprio valor e construir
    relações mais conscientes.
  </p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    f"""
<div class="highlight">
  <div class="photo" style="background-image:url('{cris_post}');background-position:63% 28%;"></div>
  <div class="text">
    <div class="mini">Cris França • Psicóloga</div>
    <h3>Seu processo não precisa ser vivido sozinho.</h3>
    <p>
      Cada acompanhamento é construído de forma individual, respeitando história, contexto, ritmo
      e objetivos. A proposta é criar um ambiente seguro para ampliar consciência, reconhecer padrões
      e desenvolver recursos emocionais para a vida cotidiana.
    </p>
    <p><strong>Especialidade comunicada:</strong> dependência emocional, com atuação também em psicologia,
    florais, Medicina Tradicional Chinesa e palestras.</p>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================
# ÁREAS DE ATUAÇÃO
# ============================================================
section_anchor("atuacao")
st.markdown(
    """
<div class="section">
  <div class="section-kicker">Como posso ajudar</div>
  <h2 class="section-title">Áreas de atuação</h2>
  <p class="section-sub">Uma apresentação clara dos serviços, sem linguagem de “floricultura” e sem transformar o cuidado emocional em produto.</p>
  <div class="cards-grid">
    <div class="service-card"><div class="service-icon">🧠</div><h3>Psicoterapia</h3><p>Acompanhamento psicológico individual para autoconhecimento, organização emocional e desenvolvimento de recursos para lidar com desafios.</p></div>
    <div class="service-card"><div class="service-icon">💔</div><h3>Dependência emocional</h3><p>Trabalho voltado à compreensão de vínculos, limites, medo de abandono, autoestima e padrões relacionais repetitivos.</p></div>
    <div class="service-card"><div class="service-icon">🌿</div><h3>Florais de Saint Germain</h3><p>Uso complementar dentro de uma proposta integrativa de bem-estar, sempre com orientação e sem substituir tratamentos de saúde indicados.</p></div>
    <div class="service-card"><div class="service-icon">☯️</div><h3>Medicina Tradicional Chinesa</h3><p>Recursos integrativos voltados ao equilíbrio e cuidado global, utilizados de forma complementar ao acompanhamento profissional.</p></div>
    <div class="service-card"><div class="service-icon">🎤</div><h3>Palestras & encontros</h3><p>Conteúdos sobre saúde emocional, relações, autoestima, dependência emocional, autocuidado e desenvolvimento humano.</p></div>
    <div class="service-card"><div class="service-icon">💻</div><h3>Online e presencial</h3><p>Formatos de atendimento para facilitar o acesso ao acompanhamento, conforme disponibilidade e necessidade de cada pessoa.</p></div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================
# COMO FUNCIONA
# ============================================================
st.markdown(
    """
<div class="section" style="padding-top:64px">
  <div class="section-kicker">Primeiro contato</div>
  <h2 class="section-title">Simples, acolhedor e sem burocracia.</h2>
  <div class="steps">
    <div class="step"><div class="step-num">01</div><h4>Fale pelo WhatsApp</h4><p>Envie uma mensagem contando, de forma breve, o que você está buscando.</p></div>
    <div class="step"><div class="step-num">02</div><h4>Escolha o formato</h4><p>Verifique disponibilidade para atendimento online ou presencial.</p></div>
    <div class="step"><div class="step-num">03</div><h4>Inicie seu processo</h4><p>No primeiro encontro, objetivos e necessidades são compreendidos com cuidado e individualidade.</p></div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================
# CATÁLOGO FLORAIS
# ============================================================
section_anchor("florais")
st.markdown(
    """
<div class="section">
  <div class="section-kicker">Florais & recursos integrativos</div>
  <h2 class="section-title">Essências e fórmulas</h2>
  <p class="section-sub">Um catálogo informativo e elegante, com contato direto pelo WhatsApp para orientação, disponibilidade e compra.</p>
  <div class="catalog-note"><strong>Importante:</strong> florais e práticas integrativas são recursos complementares. As descrições abaixo apresentam associações tradicionais da linha e não substituem avaliação psicológica, médica, diagnóstico ou tratamento profissional.</div>
</div>
""",
    unsafe_allow_html=True,
)

ESSENCES = [
    ("Abies de Lourdes", "Força interior e coragem diante de grandes responsabilidades e sensação de sobrecarga."),
    ("Abricó", "Associado a presença, atenção e maior conexão com atividades de estudo e trabalho."),
    ("Abundância", "Associado a prosperidade, fé e percepção de possibilidades."),
    ("Alcachofra", "Apoio simbólico em momentos de perda de direção, desolação ou necessidade de reorganização interna."),
    ("Algodão", "Associado a clareza de percepção, limpeza emocional e sensação de maior centramento."),
    ("Allium", "Associado a proteção, fé, determinação e tranquilidade."),
    ("Aloe", "Apoio em momentos de baixa autoestima, desânimo e necessidade de recuperar vitalidade emocional."),
    ("Ameixa", "Associado a organização mental, clareza e redução da sensação de confusão interna."),
    ("Amygdalus", "Associado a autocontrole, consciência de desejos e escolhas mais alinhadas."),
    ("Anis", "Apoio simbólico para coragem, maturidade e maior liberdade para viver novas experiências."),
    ("Arnica Silvestre", "Associado a recomposição subjetiva após períodos emocionalmente intensos."),
    ("Aveia Selvagem", "Associado a discernimento e tomada de decisão em momentos de indecisão."),
    ("Bambusa", "Apoio para foco, continuidade e compromisso com o que precisa ser realizado."),
    ("Begônia", "Associado a autoconhecimento, clareza e sensação de desbloqueio emocional."),
    ("Boa Deusa", "Apoio em momentos de forte abalo, ajudando a reconectar com entusiasmo e continuidade."),
    ("Boa Sorte", "Associado a abertura de caminhos, confiança e perseverança diante de dificuldades."),
    ("Bom dia", "Associado a disposição e mobilização em períodos de desânimo pela manhã."),
    ("Canela", "Apoio para ampliar perspectivas, flexibilidade mental e lidar com excesso de preocupação."),
    ("Capim Luz", "Associado a expressão, comunicação e sensação de desbloqueio."),
    ("Chapéu de Sol", "Associado a proteção emocional e fortalecimento de limites."),
    ("Cidreira", "Associado a desaceleração mental, serenidade e preparação para repouso."),
    ("Cocos", "Apoio simbólico para força interior e saída de padrões de imobilidade."),
    ("Coronarium", "Associado a lucidez, discernimento e organização de pensamentos repetitivos."),
    ("Curculigum", "Associado a fortalecimento do 'eu', limites e capacidade de dizer não quando necessário."),
    ("Dulcis", "Associado a serenidade, sensação de saciedade emocional e elevação."),
    ("Embaúba", "Apoio simbólico para trabalhar ressentimentos e reconexão afetiva."),
    ("Erbum", "Associado à elaboração de ressentimentos profundos e recuperação de leveza emocional."),
    ("Erianthum", "Apoio para quem se sente estagnado, favorecendo aprofundamento, reflexão e movimento interno."),
    ("Flor Branca", "Associado a limpeza de hábitos, simplicidade, propósito e reconexão com valores pessoais."),
    ("Focum", "Associado a acolhimento após experiências intensas e fortalecimento da sensação de segurança."),
    ("Gerânio", "Apoio para presença, estabilidade emocional e adaptação a desafios cotidianos."),
    ("Gloxinia", "Associado a organização, priorização e manejo de sobrecarga de tarefas."),
    ("Goiaba", "Associado a coragem, segurança e tranquilidade em situações de pressão."),
    ("Gracilis", "Associado a centramento, reintegração e sensação de alinhamento interno."),
    ("Grandiflora", "Apoio complementar após vivências de humilhação, opressão ou forte impacto emocional."),
    ("Grevilia", "Associado à transformação de irritação e raiva em maior equilíbrio interno."),
    ("Helicônia", "Trabalho simbólico sobre padrões centrados excessivamente na imagem e validação externa."),
    ("Incensum", "Associado a recolhimento, meditação, limpeza simbólica e sensação de elevação."),
    ("Indica", "Associado a intuição, percepção interna e escuta de si."),
    ("Ipê Roxo", "Apoio em momentos de trauma, estresse intenso e sensação de não encontrar saída."),
    ("Jasmim Madagascar", "Associado a comunicação, posicionamento e maior clareza para se expressar."),
    ("Laurus Nobilis", "Associado a libertação de condicionamentos antigos e revisão de vínculos com o passado."),
    ("Lavanda de Saint Germain", "Associado a harmonia mental, tranquilidade e fortalecimento interior."),
    ("Leucantha", "Associado a segurança emocional e reconexão com vínculos afetivos."),
    ("Limão", "Associado à elaboração de amargura, rigidez e pensamentos hostis."),
    ("Lisiandra", "Apoio para organização, pontualidade e estruturação da rotina."),
    ("Lírio da Paz", "Associado à pacificação de conflitos internos e busca de serenidade."),
    ("Lírio Real", "Associado a liberdade interior, autonomia e sensação de expansão."),
    ("Lótus Azul", "Associado a confiança, conquista, fé e motivação para seguir objetivos."),
    ("Lótus do Egito", "Associado a clareza, elevação de consciência e práticas contemplativas."),
    ("Lótus Magnolia", "Associado a proteção emocional e filtragem de influências externas."),
    ("Madressilva SG", "Associado a liberdade emocional em relação a vínculos e padrões que aprisionam."),
    ("Mangífera", "Apoio para momentos de perda de fé, esperança e perspectiva."),
    ("Margarida de Saint Germain", "Associado a compaixão, compreensão e apoio em processos de aprendizagem."),
]

FORMULAS = [
    ("Fórmula Emergencial", "Apoio complementar em situações de impacto emocional, tensão e períodos de grande exigência."),
    ("Fórmula do Estudante", "Concentração, memória, organização, perseverança e força de vontade para a rotina de estudos."),
    ("Bom Sono", "Associado a relaxamento, desaceleração dos pensamentos e preparação para o sono."),
    ("Sensação de Ansiedade", "Associado a calma, flexibilidade, paciência e maior estabilidade diante das preocupações da rotina."),
    ("Ânimo e Equilíbrio", "Apoio complementar em períodos de desânimo e sensação de desesperança."),
    ("Autoestima e Vitalidade", "Associado a amor-próprio, confiança, força de vontade e energia para a vida cotidiana."),
    ("Anti-Estresse", "Associado a redução da sensação de sobrecarga, cansaço emocional e desânimo."),
    ("Calma e Tranquilidade", "Apoio complementar para nervosismo, agitação interna e dificuldade de desacelerar."),
    ("Meia Idade", "Associado a equilíbrio emocional em fases de transição e mudanças do ciclo de vida."),
    ("Fórmula do Panicum", "Apoio complementar em momentos de medo intenso, pânico e sensação de perda de controle."),
    ("Prosperidade", "Associado a abundância, propósito, confiança e abertura para possibilidades."),
    ("Fórmula de Proteção", "Associado a fortalecimento emocional, limites e sensação de proteção."),
    ("Fórmula Leucantha", "Trabalho complementar relacionado a vínculos, separação precoce e sensação de desconexão afetiva."),
    ("Espiritualidade e Meditação", "Associado a foco, intuição, presença e conexão com a vida interior."),
    ("Integração Familiar", "Associado a harmonia, perdão, diálogo e integração nos vínculos familiares."),
    ("Apoio Emocional", "Fórmula voltada a acolhimento e conforto em períodos de grande abalo emocional."),
    ("DETOX", "Proposta simbólica de limpeza de hábitos e relações percebidos como tóxicos, incentivando uma rotina de autocuidado."),
    ("Ho'oponopono — Fórmulas e Kit", "Linha concentrada apresentada para práticas pessoais de autocuidado e reflexão."),
]

search_col, type_col = st.columns([2.2, 1])
with search_col:
    query = st.text_input("Pesquisar essência ou fórmula", placeholder="Ex.: Lavanda, ansiedade, autoestima...", label_visibility="collapsed")
with type_col:
    selected_type = st.selectbox("Tipo", ["Todos", "Essências", "Fórmulas"], label_visibility="collapsed")

items = []
if selected_type in {"Todos", "Essências"}:
    items.extend([("Essência", n, d) for n, d in ESSENCES])
if selected_type in {"Todos", "Fórmulas"}:
    items.extend([("Fórmula", n, d) for n, d in FORMULAS])

if query.strip():
    q = query.casefold().strip()
    items = [item for item in items if q in item[1].casefold() or q in item[2].casefold()]

st.caption(f"{len(items)} item(ns) encontrado(s)")

for row_start in range(0, len(items), 3):
    cols = st.columns(3)
    for col, item in zip(cols, items[row_start:row_start + 3]):
        kind, name, desc = item
        link = wa_link(f"Olá, Cris! Vi no seu site o item '{name}' e gostaria de saber mais sobre orientação, disponibilidade e compra.")
        with col:
            st.markdown(
                f"""
<div class="floral-card">
  <div class="floral-tag">{kind}</div>
  <h4>{name}</h4>
  <p>{desc}</p>
  <a href="{link}" target="_blank">Consultar pelo WhatsApp →</a>
</div>
""",
                unsafe_allow_html=True,
            )

# ============================================================
# INSTAGRAM
# ============================================================
section_anchor("instagram")
st.markdown(
    """
<div class="section">
  <div class="section-kicker">Conteúdo & presença digital</div>
  <h2 class="section-title">Acompanhe a Cris no Instagram</h2>
  <p class="section-sub">Conteúdos sobre psicologia, dependência emocional, autocuidado, relações e terapias integrativas.</p>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    f"""
<div class="instagram-box">
  <div><img src="{instagram_screen}" alt="Instagram Cris França"></div>
  <div>
    <div class="section-kicker">@crisfrancah</div>
    <h3 style="font-size:38px;line-height:1.06;color:var(--brown);margin:0 0 14px;font-weight:500;">Conteúdo que continua o cuidado para além da sessão.</h3>
    <p style="color:var(--muted);font:400 15px/1.7 Arial,sans-serif;">Acompanhe publicações e reflexões sobre saúde emocional, vínculos, autoestima e práticas integrativas.</p>
    <a class="btn btn-secondary" href="{INSTAGRAM_URL}" target="_blank">Abrir Instagram</a>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================
# CONTATO INTELIGENTE
# ============================================================
section_anchor("contato")
st.markdown(
    """
<div class="section">
  <div class="contact-panel">
    <h3>Vamos conversar?</h3>
    <p>Escolha abaixo o motivo do contato e o site prepara uma mensagem para o WhatsApp. Nenhuma informação fica armazenada aqui.</p>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

c1, c2 = st.columns(2)
with c1:
    contact_name = st.text_input("Seu nome", placeholder="Como você gostaria de ser chamado(a)?")
with c2:
    contact_reason = st.selectbox(
        "Assunto",
        [
            "Agendar consulta de psicologia",
            "Dependência emocional",
            "Florais de Saint Germain",
            "Medicina Tradicional Chinesa",
            "Palestras e eventos",
            "Comprar/consultar um floral",
            "Outro assunto",
        ],
    )
contact_message = st.text_area("Mensagem", placeholder="Se quiser, conte brevemente o que está buscando.", height=110)

name_part = f" Meu nome é {contact_name.strip()}." if contact_name.strip() else ""
extra = f" {contact_message.strip()}" if contact_message.strip() else ""
prepared = f"Olá, Cris! Vim pelo site.{name_part} Meu contato é sobre: {contact_reason}.{extra}"
st.link_button("💬 Enviar mensagem pelo WhatsApp", wa_link(prepared), use_container_width=True)

# ============================================================
# RODAPÉ
# ============================================================
st.markdown(
    f"""
<div class="footer">
  <img src="{logo_full}" alt="Instituto Cris França"><br>
  Psicologia & Terapias Integrativas • Atendimento online e presencial<br>
  WhatsApp: (11) 94571-4554 • Instagram: @crisfrancah<br><br>
  <strong>Nota de cuidado:</strong> informações sobre florais e práticas integrativas têm caráter informativo e complementar e não substituem acompanhamento psicológico, médico ou tratamentos prescritos.
</div>
""",
    unsafe_allow_html=True,
)
