<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Muhammed Rashid — GitHub Profile README</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Syne:wght@400;600;700;800&display=swap" rel="stylesheet"/>
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --bg:        #0d1117;
    --bg2:       #161b22;
    --bg3:       #1c2128;
    --border:    #30363d;
    --text:      #c9d1d9;
    --muted:     #8b949e;
    --accent:    #ff6d00;
    --green:     #2ea043;
    --blue:      #58a6ff;
    --code-bg:   #161b22;
  }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Syne', sans-serif;
    font-size: 15px;
    line-height: 1.7;
    padding: 0;
    min-height: 100vh;
  }

  .wrapper {
    max-width: 900px;
    margin: 0 auto;
    padding: 48px 32px 80px;
  }

  /* ── ASCII HERO ─────────────────────────────────── */
  .hero {
    text-align: center;
    padding: 40px 0 32px;
    position: relative;
  }
  .ascii {
    font-family: 'JetBrains Mono', monospace;
    font-size: clamp(6px, 1.2vw, 11px);
    color: var(--accent);
    line-height: 1.2;
    letter-spacing: 0.05em;
    display: inline-block;
    text-shadow: 0 0 20px rgba(255,109,0,0.4);
    animation: glow 3s ease-in-out infinite alternate;
  }
  @keyframes glow {
    from { text-shadow: 0 0 10px rgba(255,109,0,0.3); }
    to   { text-shadow: 0 0 30px rgba(255,109,0,0.7), 0 0 60px rgba(255,109,0,0.2); }
  }
  .subtitle {
    margin-top: 20px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: var(--muted);
    letter-spacing: 0.08em;
  }
  .subtitle span { color: var(--green); }
  .subtitle .dot { color: var(--border); margin: 0 8px; }

  /* ── BADGES ─────────────────────────────────────── */
  .badges {
    display: flex;
    justify-content: center;
    gap: 10px;
    flex-wrap: wrap;
    margin-top: 20px;
  }
  .badge {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    padding: 7px 16px;
    border-radius: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 600;
    text-decoration: none;
    letter-spacing: 0.05em;
    border: 1px solid var(--border);
    transition: all 0.2s;
  }
  .badge:hover { transform: translateY(-2px); border-color: var(--accent); }
  .badge-dark  { background: #000; color: #fff; }
  .badge-blue  { background: #0A66C2; color: #fff; }
  .badge-red   { background: #EA4335; color: #fff; }

  /* ── DIVIDER ─────────────────────────────────────── */
  hr {
    border: none;
    height: 1px;
    background: linear-gradient(to right, transparent, var(--border), transparent);
    margin: 40px 0;
  }

  /* ── INTRO GRID ──────────────────────────────────── */
  .intro-grid {
    display: grid;
    grid-template-columns: 1fr 340px;
    gap: 32px;
    align-items: start;
  }
  .intro-text h3 {
    font-size: 18px;
    font-weight: 700;
    color: #fff;
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .intro-text p {
    color: var(--text);
    margin-bottom: 12px;
    font-size: 14px;
  }
  .intro-text strong { color: var(--accent); }
  .stats-card {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
  }
  .stats-card img { width: 100%; display: block; }

  /* ── CODE BLOCK ──────────────────────────────────── */
  pre {
    background: var(--code-bg);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 18px 22px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12.5px;
    line-height: 1.8;
    overflow-x: auto;
    margin: 16px 0;
    position: relative;
  }
  pre::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(to right, var(--accent), var(--green));
    border-radius: 10px 10px 0 0;
  }
  code {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    background: var(--code-bg);
    padding: 2px 6px;
    border-radius: 4px;
    color: var(--green);
    border: 1px solid var(--border);
  }
  pre code {
    background: none;
    padding: 0;
    border: none;
    font-size: 12.5px;
    color: var(--text);
  }
  .kw  { color: #ff7b72; }  /* keywords */
  .str { color: #a5d6ff; }  /* strings */
  .cls { color: #ffa657; }  /* classes */
  .cmt { color: #8b949e; }  /* comments */
  .grn { color: #7ee787; }  /* values */

  /* ── SECTION HEADERS ─────────────────────────────── */
  h2 {
    font-size: 20px;
    font-weight: 800;
    color: #fff;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    gap: 10px;
    letter-spacing: -0.02em;
  }
  h2::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(to right, var(--border), transparent);
  }

  /* ── TECH STACK TABLE ────────────────────────────── */
  .tech-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }
  .tech-card {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 20px;
    transition: border-color 0.2s;
  }
  .tech-card:hover { border-color: var(--accent); }
  .tech-card h4 {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    font-weight: 600;
    color: var(--accent);
    margin-bottom: 12px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }
  .tech-card pre {
    margin: 0;
    background: transparent;
    border: none;
    padding: 0;
    font-size: 12px;
    line-height: 1.9;
    color: var(--text);
  }
  .tech-card pre::before { display: none; }

  /* ── PROJECT GRID ────────────────────────────────── */
  .projects-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
  }
  .project-card {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 22px;
    transition: all 0.25s;
    position: relative;
    overflow: hidden;
  }
  .project-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(to right, var(--accent), var(--green));
    transform: scaleX(0);
    transform-origin: left;
    transition: transform 0.3s;
  }
  .project-card:hover { border-color: var(--accent); transform: translateY(-3px); box-shadow: 0 8px 30px rgba(255,109,0,0.1); }
  .project-card:hover::before { transform: scaleX(1); }
  .project-card h3 {
    font-size: 15px;
    font-weight: 700;
    color: #fff;
    margin-bottom: 6px;
  }
  .project-card .meta {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: var(--muted);
    margin-bottom: 12px;
    letter-spacing: 0.04em;
  }
  .project-card p {
    font-size: 13px;
    color: var(--text);
    margin-bottom: 14px;
    line-height: 1.6;
  }
  .project-card ul {
    list-style: none;
    font-size: 12.5px;
    color: var(--muted);
    margin-bottom: 16px;
  }
  .project-card ul li {
    padding: 3px 0;
    display: flex;
    align-items: flex-start;
    gap: 8px;
  }
  .project-card ul li::before { content: '▸'; color: var(--green); flex-shrink: 0; margin-top: 1px; }
  .project-card ul li strong { color: var(--text); }
  .pill-row { display: flex; gap: 6px; flex-wrap: wrap; }
  .pill {
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    padding: 3px 9px;
    border-radius: 20px;
    background: var(--bg3);
    border: 1px solid var(--border);
    color: var(--muted);
    text-decoration: none;
    transition: all 0.2s;
  }
  .pill:hover { border-color: var(--accent); color: var(--accent); }
  .pill.live { background: rgba(46,160,67,0.1); border-color: var(--green); color: var(--green); }

  /* ── ANALYTICS ───────────────────────────────────── */
  .analytics-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 16px;
  }
  .analytics-grid img, .activity-graph img {
    width: 100%;
    border-radius: 10px;
    border: 1px solid var(--border);
    display: block;
  }

  /* ── PROGRESS BARS ───────────────────────────────── */
  .progress-list { display: flex; flex-direction: column; gap: 14px; }
  .progress-item { }
  .progress-header {
    display: flex;
    justify-content: space-between;
    margin-bottom: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
  }
  .progress-header .name { color: var(--text); }
  .progress-header .tech { color: var(--muted); font-size: 11px; }
  .progress-header .pct  { color: var(--accent); font-weight: 600; }
  .progress-track {
    height: 6px;
    background: var(--bg3);
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--border);
  }
  .progress-fill {
    height: 100%;
    border-radius: 10px;
    background: linear-gradient(to right, var(--accent), var(--green));
    position: relative;
    animation: fillBar 1.5s ease-out forwards;
    transform-origin: left;
  }
  @keyframes fillBar { from { transform: scaleX(0); } to { transform: scaleX(1); } }

  /* ── FOOTER ──────────────────────────────────────── */
  .footer {
    text-align: center;
    padding: 32px 0 0;
    color: var(--muted);
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
  }
  .footer span { color: var(--accent); }
  .views-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 11px;
    margin-top: 12px;
    color: var(--muted);
  }
  .views-badge .dot { width: 7px; height: 7px; background: var(--accent); border-radius: 50%; animation: pulse 2s infinite; }
  @keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:0.5;transform:scale(0.8)} }

  @media (max-width: 680px) {
    .intro-grid, .tech-grid, .projects-grid, .analytics-grid { grid-template-columns: 1fr; }
    .ascii { font-size: 5px; }
  }
</style>
</head>
<body>
<div class="wrapper">

  <!-- HERO -->
  <div class="hero">
    <pre class="ascii">
██████╗  █████╗ ███████╗██╗  ██╗██╗██████╗ 
██╔══██╗██╔══██╗██╔════╝██║  ██║██║██╔══██╗
██████╔╝███████║███████╗███████║██║██║  ██║
██╔══██╗██╔══██║╚════██║██╔══██║██║██║  ██║
██║  ██║██║  ██║███████║██║  ██║██║██████╔╝
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═════╝</pre>
    <div class="subtitle">
      <code>&lt; Full Stack Developer /&gt;</code>
      <span class="dot">·</span>
      <span>.NET</span>
      <span class="dot">·</span>
      <span>React</span>
      <span class="dot">·</span>
      <span>Next.js</span>
      <span class="dot">·</span>
      <span>TypeScript</span>
    </div>
    <div class="badges">
      <a class="badge badge-dark" href="https://rashid-mp.vercel.app/">⬡ Portfolio</a>
      <a class="badge badge-blue" href="https://www.linkedin.com/in/muhammed-rashid-full-stack-developer">⬡ LinkedIn</a>
      <a class="badge badge-red"  href="mailto:muhammedrashidr222@gmail.com">⬡ Email</a>
    </div>
  </div>

  <hr/>

  <!-- INTRO -->
  <div class="intro-grid">
    <div class="intro-text">
      <h3>👋 Hello, World</h3>
      <p>I'm <strong>Muhammed Rashid</strong> — a Full Stack Developer from <strong>Malappuram, Kerala</strong>, building things with <code>.NET</code> on the backend and <code>React / Next.js</code> on the frontend.</p>
      <p>Currently interning at <strong>Bridgeon Solutions LLP</strong>, shipping production features daily — RESTful APIs, clean architecture backends, and responsive TypeScript UIs.</p>
      <pre><code><span class="kw">var</span> rashid <span class="kw">=</span> <span class="kw">new</span> <span class="cls">Developer</span> {
  Role     <span class="kw">=</span> <span class="str">"Full Stack Developer"</span>,
  Location <span class="kw">=</span> <span class="str">"Malappuram, Kerala 🇮🇳"</span>,
  Backend  <span class="kw">=</span> [<span class="str">"C#"</span>, <span class="str">"ASP.NET Core"</span>, <span class="str">"EF Core"</span>, <span class="str">"SQL Server"</span>],
  Frontend <span class="kw">=</span> [<span class="str">"Next.js"</span>, <span class="str">"React"</span>, <span class="str">"TypeScript"</span>, <span class="str">"Tailwind"</span>],
  Focus    <span class="kw">=</span> <span class="str">"Clean code · Scalable APIs · Great UX"</span>
};</code></pre>
    </div>
    <div class="stats-card">
      <img src="https://github-readme-stats.vercel.app/api?username=Rashi003mp&show_icons=true&count_private=true&theme=dark&hide_border=true&border_radius=0&title_color=ff6d00&icon_color=2ea043&text_color=c9d1d9&bg_color=161b22" alt="GitHub Stats"/>
    </div>
  </div>

  <hr/>

  <!-- TECH STACK -->
  <h2>⚡ Tech Stack</h2>
  <div class="tech-grid">
    <div class="tech-card">
      <h4>🔷 Backend</h4>
      <pre>C# · ASP.NET Core · .NET 8
Entity Framework Core · Dapper · LINQ
ADO.NET · RESTful APIs
Dependency Injection · Clean Architecture
JWT Auth · RBAC · Middleware</pre>
    </div>
    <div class="tech-card">
      <h4>🔶 Frontend</h4>
      <pre>Next.js · React.js · TypeScript
Redux Toolkit · Context API
Tailwind CSS · Bootstrap · GSAP
SSR · SSG · Lazy Loading
Lighthouse Optimization</pre>
    </div>
    <div class="tech-card">
      <h4>🗄️ Database</h4>
      <pre>MS SQL Server · Stored Procedures
Query Optimization · Schema Design
Normalization (3NF) · Soft Delete
Indexing · SSMS</pre>
    </div>
    <div class="tech-card">
      <h4>☁️ Cloud &amp; DevOps</h4>
      <pre>Microsoft Azure · Azure SQL Database
Docker · CI/CD · GitHub Actions
Git · GitHub · Visual Studio
VS Code · Postman · Figma · npm</pre>
    </div>
  </div>

  <hr/>

  <!-- PROJECTS -->
  <h2>🚀 Featured Projects</h2>
  <div class="projects-grid">

    <div class="project-card">
      <h3>🏗️ ConstructPro ERP</h3>
      <div class="meta">Full-Stack · ASP.NET Core · Next.js · TypeScript</div>
      <p>An ERP-style construction management system supporting <strong>4 user roles</strong> with granular, role-based access control.</p>
      <ul>
        <li><strong>25+ RESTful APIs</strong> — projects, tasks, progress, reporting</li>
        <li>Clean Architecture — API / Application / Domain / Infrastructure</li>
        <li>Normalized SQL Server schema with soft-delete & audit</li>
        <li>Next.js + TypeScript role-based dashboards</li>
      </ul>
      <div class="pill-row">
        <a class="pill" href="https://github.com/Rashi003mp">GitHub ↗</a>
      </div>
    </div>

    <div class="project-card">
      <h3>🛍️ JEANOGRAM E-commerce</h3>
      <div class="meta">Full-Stack · ASP.NET Core · React · Redux</div>
      <p>Complete e-commerce platform with User and Admin modules, secured end-to-end.</p>
      <ul>
        <li><strong>JWT auth</strong> with refresh token flow + RBAC</li>
        <li>Redux Toolkit for type-safe state management</li>
        <li>SQL Server schema normalized to <strong>3NF</strong></li>
        <li>Mobile-first responsive UI with Tailwind CSS</li>
      </ul>
      <div class="pill-row">
        <a class="pill" href="https://github.com/Rashi003mp">GitHub ↗</a>
      </div>
    </div>

    <div class="project-card">
      <h3>🌐 Personal Portfolio</h3>
      <div class="meta">Next.js · GSAP · TypeScript · Tailwind</div>
      <p>Animated portfolio with scroll-triggered GSAP animations and high Lighthouse performance scores.</p>
      <ul>
        <li>Smooth <strong>GSAP</strong> page transitions & scroll animations</li>
        <li>Optimized with SSG, lazy loading & image optimization</li>
        <li>Fully responsive across all screen sizes</li>
      </ul>
      <div class="pill-row">
        <a class="pill live" href="https://rashid-mp.vercel.app/">Live ↗</a>
        <a class="pill" href="https://github.com/Rashi003mp">GitHub ↗</a>
      </div>
    </div>

    <div class="project-card">
      <h3>🛒 E-commerce Frontend</h3>
      <div class="meta">React · TypeScript · Redux Toolkit · Tailwind</div>
      <p>Standalone frontend with separate User &amp; Admin modules and complete shopping flows.</p>
      <ul>
        <li><strong>User &amp; Admin</strong> module separation</li>
        <li>Full cart / wishlist / checkout flow in Redux</li>
        <li>Type-safe components with strict TypeScript</li>
        <li>Mobile-first responsive design</li>
      </ul>
      <div class="pill-row">
        <a class="pill" href="https://github.com/Rashi003mp">GitHub ↗</a>
      </div>
    </div>

  </div>

  <hr/>

  <!-- ANALYTICS -->
  <h2>📊 GitHub Analytics</h2>
  <div class="analytics-grid">
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=Rashi003mp&layout=compact&theme=dark&hide_border=true&border_radius=10&title_color=ff6d00&text_color=c9d1d9&bg_color=0d1117&langs_count=8" alt="Top Languages"/>
    <img src="https://github-readme-streak-stats.herokuapp.com?user=Rashi003mp&theme=dark&hide_border=true&border_radius=10&background=0d1117&stroke=2ea043&ring=ff6d00&fire=ff6d00&currStreakLabel=ffffff&sideLabels=2ea043&currStreakNum=ff6d00&sideNums=c9d1d9" alt="Streak"/>
  </div>
  <div class="activity-graph">
    <img src="https://github-readme-activity-graph.vercel.app/graph?username=Rashi003mp&custom_title=Contribution%20Graph&bg_color=0d1117&color=2ea043&line=ff6d00&point=ffffff&area=true&hide_border=true&radius=8&area_color=0d3320" alt="Contribution Graph"/>
  </div>

  <hr/>

  <!-- CURRENTLY WORKING ON -->
  <h2>🎯 Currently Working On</h2>
  <div class="progress-list">
    <div class="progress-item">
      <div class="progress-header">
        <span class="name">▶ &nbsp;ConstructPro ERP</span>
        <span class="tech">ASP.NET Core + Next.js</span>
        <span class="pct">75%</span>
      </div>
      <div class="progress-track"><div class="progress-fill" style="width:75%"></div></div>
    </div>
    <div class="progress-item">
      <div class="progress-header">
        <span class="name">▶ &nbsp;.NET Deep Dive</span>
        <span class="tech">Advanced Patterns &amp; Testing</span>
        <span class="pct">60%</span>
      </div>
      <div class="progress-track"><div class="progress-fill" style="width:60%"></div></div>
    </div>
    <div class="progress-item">
      <div class="progress-header">
        <span class="name">▶ &nbsp;TypeScript Mastery</span>
        <span class="tech">Strict Mode + Generics</span>
        <span class="pct">80%</span>
      </div>
      <div class="progress-track"><div class="progress-fill" style="width:80%"></div></div>
    </div>
    <div class="progress-item">
      <div class="progress-header">
        <span class="name">▶ &nbsp;Azure Deployment</span>
        <span class="tech">App Service + SQL + Pipelines</span>
        <span class="pct">50%</span>
      </div>
      <div class="progress-track"><div class="progress-fill" style="width:50%"></div></div>
    </div>
  </div>

  <hr/>

  <!-- FOOTER -->
  <div class="footer">
    <p>Building one clean API at a time. &nbsp;·&nbsp; <span>Open to opportunities 🚀</span></p>
    <div class="views-badge">
      <span class="dot"></span>
      Profile Views · Rashi003mp
    </div>
  </div>

</div>
</body>
</html>
