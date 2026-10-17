"""Generate the hand-built SVG assets for the het12779-ui profile.

Everything is authored here rather than pulled from a badge service so the
profile has one palette, one type scale and no third-party dependency.

    python tools/make_assets.py
"""
from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "assets"

BG = "#04070c"
PANEL = "#060b12"
INK = "#d6e7f3"
MUTED = "#7f97a9"
DIM = "#465c6e"
GREEN = "#2ee88a"
CYAN = "#34d8ff"
AMBER = "#ffc45c"
RED = "#ff7b72"
VIOLET = "#a78bfa"

MONO = "Consolas, 'SF Mono', 'JetBrains Mono', Menlo, monospace"

# 6x7 pixel glyphs for the monogram.
GLYPHS = {
    "H": ["100001", "100001", "100001", "111111", "100001", "100001", "100001"],
    "E": ["111111", "100000", "100000", "111110", "100000", "100000", "111111"],
    "T": ["111111", "001100", "001100", "001100", "001100", "001100", "001100"],
}


def monogram(x: float, y: float, cell: float = 20, gap_cells: int = 2) -> str:
    cells = []
    col = 0
    index = 0
    for letter in "HET":
        grid = GLYPHS[letter]
        for row, bits in enumerate(grid):
            for c, bit in enumerate(bits):
                if bit == "1":
                    cx = x + (col + c) * cell
                    cy = y + row * cell
                    begin = 0.45 + index * 0.016
                    flicker = ""
                    if index % 9 == 4:
                        flicker = (
                            f'\n          <animate attributeName="opacity" values="1;1;0.38;1" '
                            f'keyTimes="0;0.86;0.9;1" dur="{7 + index % 5}s" '
                            f'begin="{2 + index * 0.05}s" repeatCount="indefinite"/>'
                        )
                    cells.append(
                        f'        <rect x="{cx:g}" y="{cy:g}" width="{cell - 2:g}" height="{cell - 2:g}" rx="3" '
                        f'opacity="0">\n'
                        f'          <animate attributeName="opacity" from="0" to="1" dur="0.22s" '
                        f'begin="{begin:.2f}s" fill="freeze"/>{flicker}\n'
                        f"        </rect>"
                    )
                    index += 1
        col += 6 + gap_cells
    return "\n".join(cells)


def hero() -> str:
    pixels = monogram(64, 132)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 560" width="1200" height="560" role="img" aria-labelledby="t d">
  <title id="t">het patel — computer engineering student</title>
  <desc id="d">A terminal window types a shell session: whoami, three shipped systems, 187 passing tests, and a blinking cursor, beside a pixel-matrix monogram spelling HET.</desc>
  <defs>
    <linearGradient id="frame" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{GREEN}" stop-opacity="0.55"/>
      <stop offset="0.45" stop-color="#1b3a34" stop-opacity="0.35"/>
      <stop offset="1" stop-color="{CYAN}" stop-opacity="0.3"/>
    </linearGradient>
    <linearGradient id="monoFill" gradientUnits="userSpaceOnUse" x1="60" y1="120" x2="520" y2="290">
      <stop offset="0" stop-color="#9dffd2"/>
      <stop offset="0.45" stop-color="{GREEN}"/>
      <stop offset="1" stop-color="{CYAN}"/>
    </linearGradient>
    <linearGradient id="band" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{GREEN}" stop-opacity="0"/>
      <stop offset="0.5" stop-color="{GREEN}" stop-opacity="0.06"/>
      <stop offset="1" stop-color="{GREEN}" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="glowA" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="{GREEN}" stop-opacity="0.34"/>
      <stop offset="1" stop-color="{GREEN}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glowB" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="{CYAN}" stop-opacity="0.26"/>
      <stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
    </radialGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M32 0H0V32" fill="none" stroke="#7fffd4" stroke-opacity="0.045" stroke-width="1"/>
    </pattern>
    <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">
      <rect width="4" height="1" y="2" fill="#ffffff" fill-opacity="0.022"/>
    </pattern>
    <filter id="soft" x="-40%" y="-40%" width="180%" height="180%">
      <feGaussianBlur stdDeviation="46"/>
    </filter>
    <clipPath id="panelClip"><rect x="30" y="24" width="1140" height="512" rx="16"/></clipPath>
    <clipPath id="l1"><rect x="592" y="112" width="0" height="26"><animate attributeName="width" to="70" dur="0.18s" begin="0.55s" fill="freeze"/></rect></clipPath>
    <clipPath id="l2"><rect x="592" y="142" width="0" height="26"><animate attributeName="width" to="420" dur="1.0s" begin="0.85s" fill="freeze"/></rect></clipPath>
    <clipPath id="l3"><rect x="592" y="180" width="0" height="26"><animate attributeName="width" to="132" dur="0.34s" begin="2.15s" fill="freeze"/></rect></clipPath>
    <clipPath id="l4"><rect x="592" y="210" width="0" height="26"><animate attributeName="width" to="340" dur="0.72s" begin="2.65s" fill="freeze"/></rect></clipPath>
    <clipPath id="l5"><rect x="592" y="248" width="0" height="26"><animate attributeName="width" to="162" dur="0.4s" begin="3.65s" fill="freeze"/></rect></clipPath>
    <clipPath id="l6"><rect x="592" y="278" width="0" height="26"><animate attributeName="width" to="330" dur="0.78s" begin="4.2s" fill="freeze"/></rect></clipPath>
    <clipPath id="l7"><rect x="592" y="308" width="0" height="26"><animate attributeName="width" to="304" dur="0.72s" begin="5.1s" fill="freeze"/></rect></clipPath>
    <clipPath id="l8"><rect x="592" y="346" width="0" height="26"><animate attributeName="width" to="154" dur="0.36s" begin="6.0s" fill="freeze"/></rect></clipPath>
    <clipPath id="l9"><rect x="592" y="376" width="0" height="26"><animate attributeName="width" to="302" dur="0.7s" begin="6.45s" fill="freeze"/></rect></clipPath>
    <clipPath id="l10"><rect x="592" y="414" width="0" height="26"><animate attributeName="width" to="26" dur="0.12s" begin="7.25s" fill="freeze"/></rect></clipPath>
  </defs>

  <rect width="1200" height="560" fill="{BG}"/>
  <rect width="1200" height="560" fill="url(#grid)"/>
  <rect x="30" y="24" width="1140" height="512" rx="16" fill="{PANEL}" stroke="url(#frame)" stroke-width="1.4"/>
  <g filter="url(#soft)" clip-path="url(#panelClip)" opacity="0.85">
    <circle cx="240" cy="470" r="300" fill="url(#glowA)">
      <animate attributeName="opacity" values="0.7;1;0.7" dur="13s" repeatCount="indefinite"/>
    </circle>
    <circle cx="990" cy="70" r="260" fill="url(#glowB)">
      <animate attributeName="opacity" values="0.9;0.55;0.9" dur="17s" repeatCount="indefinite"/>
    </circle>
  </g>
  <rect x="30" y="24" width="1140" height="46" rx="16" fill="#08111a"/>
  <rect x="30" y="54" width="1140" height="16" fill="#08111a"/>
  <path d="M30 70H1170" stroke="#ffffff" stroke-opacity="0.07"/>

  <circle cx="58" cy="47" r="5" fill="#ff5f57" fill-opacity="0.85"/>
  <circle cx="78" cy="47" r="5" fill="#ffbd2e" fill-opacity="0.85"/>
  <circle cx="98" cy="47" r="5" fill="#28c840" fill-opacity="0.9">
    <animate attributeName="fill-opacity" values="0.9;0.45;0.9" dur="3.4s" repeatCount="indefinite"/>
  </circle>

  <g font-family="{MONO}" text-anchor="middle">
    <text x="600" y="52" fill="#6d8798" font-size="13">het@localhost — ~/profile</text>
    <text x="1146" y="52" fill="#42586a" font-size="12" text-anchor="end">zsh · 120×40</text>
  </g>

  <text x="64" y="108" fill="{DIM}" font-family="{MONO}" font-size="12" letter-spacing="1.4">// fig.00 — the operator</text>

  <g fill="url(#monoFill)">
    <animate attributeName="opacity" values="1;0.9;1" dur="9s" repeatCount="indefinite"/>
{pixels}
  </g>
  <g fill="none" stroke="{CYAN}" stroke-opacity="0.12">
    <path d="M64 300h452" stroke-dasharray="2 8"/>
  </g>

  <g font-family="{MONO}" font-size="16.5">
    <text x="64" y="330" fill="{GREEN}">&gt; computer engineering student</text>
    <text x="64" y="358" fill="{MUTED}">&gt; building systems that explain themselves</text>
    <text x="64" y="404" fill="#4d6478" font-size="14">python · typescript · sql · vue · c# (learning)</text>
    <text x="64" y="432" fill="#3b5164" font-size="13">gandhinagar, in · utc+5:30</text>
  </g>

  <path d="M560 100V462" stroke="#ffffff" stroke-opacity="0.06"/>
  <circle cx="560" cy="100" r="2.5" fill="{GREEN}" fill-opacity="0.6"/>

  <g font-family="{MONO}" font-size="17" xml:space="preserve">
    <g fill="{GREEN}">
      <text x="592" y="132" clip-path="url(#l1)">$ whoami</text>
      <text x="592" y="200" clip-path="url(#l3)">$ ls ~/systems</text>
      <text x="592" y="268" clip-path="url(#l5)">$ ./status --all</text>
      <text x="592" y="366" clip-path="url(#l8)">$ cat focus.txt</text>
    </g>
    <g fill="{INK}">
      <text x="592" y="162" clip-path="url(#l2)">het patel · computer engineering student</text>
      <text x="592" y="230" clip-path="url(#l4)" fill="#9fd6ff">paceguard  channeltruth  adsentry</text>
      <text x="592" y="298" clip-path="url(#l6)">✓ 187 tests green   ✓ CI passing</text>
      <text x="592" y="328" clip-path="url(#l7)" fill="{MUTED}">9 public repos · 4 CI workflows</text>
      <text x="592" y="396" clip-path="url(#l9)" fill="{AMBER}">"make the data explain itself"</text>
      <text x="592" y="434" clip-path="url(#l10)">$</text>
    </g>
    <rect x="614" y="416" width="10.5" height="21" fill="{GREEN}">
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;0.8;0.84;0.92;0.96;1" dur="1.15s" begin="7.4s" repeatCount="indefinite"/>
    </rect>
  </g>

  <text x="592" y="462" fill="#3b5164" font-family="{MONO}" font-size="12">↓ the receipts are below</text>

  <rect x="30" y="70" width="1140" height="408" fill="url(#scan)" opacity="0.9"/>
  <g opacity="0.55">
    <rect x="30" y="0" width="1140" height="120" fill="url(#band)">
      <animateTransform attributeName="transform" type="translate" from="0 60" to="0 470" dur="8s" repeatCount="indefinite"/>
    </rect>
  </g>

  <path d="M30 484H1170" stroke="#ffffff" stroke-opacity="0.07"/>
  <g font-family="{MONO}" font-size="12.5" fill="#4a6072" xml:space="preserve">
    <text x="52" y="512" fill="{GREEN}">main*</text>
    <text x="118" y="512">✓ 187 tests</text>
    <text x="212" y="512">4 workflows</text>
    <text x="330" y="512">utf-8</text>
    <text x="392" y="512">lf</text>
    <text x="1020" y="512" text-anchor="end">session 0x7f · no build step</text>
  </g>
  <rect x="36" y="506" width="6" height="6" fill="{GREEN}">
    <animate attributeName="opacity" values="1;0.15;1" dur="2.2s" repeatCount="indefinite"/>
  </rect>

  <g stroke="#ffffff" stroke-opacity="0.15" fill="none">
    <path d="M14 44h-6v-6M14 516h-6v6"/>
    <path d="M1186 44h6v-6M1186 516h6v6"/>
  </g>
</svg>
"""


def packet(path_id: str, color: str, dur: float, begin: float) -> str:
    return (
        f'    <circle r="3.4" fill="{color}" filter="url(#dot)">\n'
        f'      <animateMotion dur="{dur}s" begin="{begin}s" repeatCount="indefinite" rotate="auto">\n'
        f'        <mpath href="#{path_id}"/>\n'
        f"      </animateMotion>\n"
        f"    </circle>"
    )


def pipeline() -> str:
    sources = [
        ("spend events", "hourly platform sync", GREEN, 130),
        ("touch points", "journeys · 30 day window", VIOLET, 248),
        ("delivery metrics", "daily restatement", AMBER, 366),
    ]
    services = [
        ("PaceGuard", "pacing · projections · guardrails", GREEN, "72 ms", 118),
        ("ChannelTruth", "5 attribution models · roas", VIOLET, "0.37 s", 238),
        ("AdSentry", "robust z-scores · incidents", AMBER, "246 ms", 358),
    ]

    parts = []
    for i, (title, sub, color, y) in enumerate(sources):
        parts.append(
            f"""  <g>
    <rect x="64" y="{y}" width="196" height="66" rx="10" fill="#081018" stroke="{color}" stroke-opacity="0.34"/>
    <rect x="64" y="{y}" width="3" height="66" rx="1.5" fill="{color}" fill-opacity="0.8"/>
    <text x="82" y="{y + 28}" fill="{INK}" font-family="{MONO}" font-size="15">{title}</text>
    <text x="82" y="{y + 50}" fill="{DIM}" font-family="{MONO}" font-size="11.5">{sub}</text>
  </g>"""
        )

    for i, (name, sub, color, latency, y) in enumerate(services):
        parts.append(
            f"""  <g>
    <rect x="430" y="{y}" width="336" height="86" rx="12" fill="#091420" stroke="{color}" stroke-opacity="0.5"/>
    <rect x="430" y="{y}" width="336" height="86" rx="12" fill="none" stroke="{color}" stroke-opacity="0.18">
      <animate attributeName="stroke-opacity" values="0.1;0.42;0.1" dur="{6 + i * 1.7}s" repeatCount="indefinite"/>
    </rect>
    <text x="452" y="{y + 34}" fill="{INK}" font-family="{MONO}" font-size="17">{name}</text>
    <text x="452" y="{y + 58}" fill="{MUTED}" font-family="{MONO}" font-size="12">{sub}</text>
    <text x="744" y="{y + 34}" fill="{color}" font-family="{MONO}" font-size="13" text-anchor="end">{latency}</text>
  </g>"""
        )

    paths = []
    for i, (_, _, color, sy) in enumerate(sources):
        ty = services[i][4] + 43
        d = f"M260 {sy + 33} C 340 {sy + 33}, 350 {ty}, 430 {ty}"
        paths.append(
            f'  <path id="p{i}" d="{d}" fill="none" stroke="#1d2e3c" stroke-width="1.2"/>\n'
            f'  <path d="{d}" fill="none" stroke="{color}" stroke-opacity="0.45" stroke-width="1.2" '
            f'stroke-dasharray="5 9">\n'
            f'    <animate attributeName="stroke-dashoffset" from="28" to="0" dur="1.8s" repeatCount="indefinite"/>\n'
            f"  </path>"
        )

    decision_y = 268
    targets = [decision_y + 30, decision_y + 60, decision_y + 90]
    out_paths = []
    for i, (_, _, color, _, sy) in enumerate(services):
        ty = targets[i]
        d = f"M766 {sy + 43} C 822 {sy + 43}, 836 {ty}, 878 {ty}"
        out_paths.append(
            f'  <path id="o{i}" d="{d}" fill="none" stroke="#1d2e3c" stroke-width="1.2"/>\n'
            f'  <path d="{d}" fill="none" stroke="{color}" stroke-opacity="0.3" stroke-width="1.2" '
            f'stroke-dasharray="4 10">\n'
            f'    <animate attributeName="stroke-dashoffset" from="28" to="0" dur="2.4s" repeatCount="indefinite"/>\n'
            f"  </path>"
        )

    packets = []
    for i, (_, _, color, _) in enumerate(sources):
        packets.append(packet(f"p{i}", color, 3.0 + i * 0.4, 0.2 + i * 0.5))
        packets.append(packet(f"p{i}", color, 3.0 + i * 0.4, 1.7 + i * 0.5))
    for i, (_, _, color, _, _) in enumerate(services):
        packets.append(packet(f"o{i}", color, 4.2, 0.6 + i * 0.3))

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 540" width="1200" height="540" role="img" aria-labelledby="t d">
  <title id="t">Lifecycle: three ingest sources, three services, one decision</title>
  <desc id="d">Animated data-flow diagram. Spend events feed PaceGuard, touch points feed ChannelTruth, delivery metrics feed AdSentry, and all three converge on a decision node. Packets travel the paths continuously.</desc>
  <defs>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M32 0H0V32" fill="none" stroke="#7fffd4" stroke-opacity="0.045" stroke-width="1"/>
    </pattern>
    <radialGradient id="glowA" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="{GREEN}" stop-opacity="0.26"/>
      <stop offset="1" stop-color="{GREEN}" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glowB" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="{VIOLET}" stop-opacity="0.22"/>
      <stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="hdr" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{GREEN}" stop-opacity="0.5"/>
      <stop offset="1" stop-color="#ffffff" stop-opacity="0.05"/>
    </linearGradient>
    <filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="52"/></filter>
    <clipPath id="panelClip"><rect x="30" y="24" width="1140" height="492" rx="16"/></clipPath>
    <filter id="dot" x="-400%" y="-400%" width="900%" height="900%">
      <feGaussianBlur stdDeviation="4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>

  <rect width="1200" height="540" fill="{BG}"/>
  <rect width="1200" height="540" fill="url(#grid)"/>
  <rect x="30" y="24" width="1140" height="492" rx="16" fill="{PANEL}" stroke="#16303a" stroke-width="1.2"/>
  <g filter="url(#soft)" clip-path="url(#panelClip)" opacity="0.8">
    <circle cx="180" cy="80" r="240" fill="url(#glowA)"/>
    <circle cx="900" cy="480" r="260" fill="url(#glowB)"/>
  </g>
  <text x="56" y="66" fill="{GREEN}" font-family="{MONO}" font-size="15">$ ./topology --explain</text>
  <text x="1146" y="66" fill="{DIM}" font-family="{MONO}" font-size="12" text-anchor="end">fig.01 / one lifecycle</text>
  <rect x="30" y="86" width="1140" height="1" fill="url(#hdr)"/>

  <g font-family="{MONO}" font-size="11" fill="{DIM}" letter-spacing="1.6">
    <text x="64" y="118">SOURCES</text>
    <text x="430" y="100">SERVICES</text>
    <text x="878" y="248">OUTCOME</text>
  </g>

{chr(10).join(parts)}

  <g font-family="{MONO}" font-size="10.5" fill="{DIM}" text-anchor="middle" letter-spacing="0.6">
    <text x="345" y="180">idempotent upsert</text>
    <text x="345" y="298">journey assembly</text>
    <text x="345" y="416">metric restatement</text>
  </g>

{chr(10).join(paths)}
{chr(10).join(out_paths)}

{chr(10).join(packets)}

  <g>
    <rect x="878" y="{decision_y}" width="268" height="120" rx="12" fill="#0c1016" stroke="{AMBER}" stroke-opacity="0.55"/>
    <text x="902" y="{decision_y + 30}" fill="{AMBER}" font-family="{MONO}" font-size="12" letter-spacing="2">DECISION</text>
    <text x="902" y="{decision_y + 56}" fill="{INK}" font-family="{MONO}" font-size="14">shift budget</text>
    <text x="902" y="{decision_y + 78}" fill="{INK}" font-family="{MONO}" font-size="14">pause a line item</text>
    <text x="902" y="{decision_y + 100}" fill="{MUTED}" font-family="{MONO}" font-size="14">or call the client</text>
  </g>

  <text x="64" y="474" fill="{DIM}" font-family="{MONO}" font-size="12">at-least-once in · idempotent out · evaluation never on the read path</text>
  <text x="1146" y="474" fill="{DIM}" font-family="{MONO}" font-size="12" text-anchor="end">same tenant model · same schema rules · same CI shape</text>
</svg>
"""


LANG_BARS = [
    ("python", 31.5, GREEN),
    ("typescript", 29.0, CYAN),
    ("html", 26.2, "#6ea8ff"),
    ("css", 7.2, VIOLET),
    ("javascript", 5.2, AMBER),
]


def system() -> str:
    rows = [
        ("langs", "Python · TypeScript · C# (learning)"),
        ("systems", "PaceGuard · ChannelTruth · AdSentry"),
        ("repos", "9 public · 3 shipped · 1 ML team build"),
        ("tests", "187 passing · no database mocks"),
        ("ci", "4 workflows · py3.11 + py3.12 + smoke"),
        ("ui", "Vue 3 · React · plain ES modules"),
        ("data", "SQL Server DDL · SQLite demo store"),
        ("tools", "git · docker · pytest · playwright · gh"),
    ]
    row_svg = []
    for i, (key, value) in enumerate(rows):
        y = 128 + i * 27
        row_svg.append(
            f'    <text x="520" y="{y}" fill="{DIM}" font-size="13">{key}</text>\n'
            f'    <text x="620" y="{y}" fill="{INK}" font-size="13.5">{value}</text>'
        )

    bars = []
    for i, (name, pct, color) in enumerate(LANG_BARS):
        y = 372 + i * 26
        width = pct / 35 * 640
        bars.append(
            f"""  <g font-family="{MONO}">
    <text x="64" y="{y + 4}" fill="{MUTED}" font-size="12">{name}</text>
    <rect x="176" y="{y - 8}" width="640" height="10" rx="5" fill="#0d1620"/>
    <rect x="176" y="{y - 8}" width="0" height="10" rx="5" fill="{color}" fill-opacity="0.85">
      <animate attributeName="width" to="{width:.0f}" dur="1.1s" begin="{0.6 + i * 0.14:.2f}s" fill="freeze" calcMode="spline" keySplines="0.2 0 0.2 1"/>
    </rect>
    <text x="836" y="{y + 4}" fill="{DIM}" font-size="12">{pct}%</text>
  </g>"""
        )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 560" width="1200" height="560" role="img" aria-labelledby="t d">
  <title id="t">System readout: het patel, computer engineering student</title>
  <desc id="d">A neofetch-style panel listing languages, systems, tests and tooling, with animated bars for language bytes across all public repositories.</desc>
  <defs>
    <linearGradient id="name" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#e6fff4"/>
      <stop offset="0.6" stop-color="{GREEN}"/>
      <stop offset="1" stop-color="{CYAN}"/>
    </linearGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M32 0H0V32" fill="none" stroke="#7fffd4" stroke-opacity="0.04" stroke-width="1"/>
    </pattern>
    <radialGradient id="glowA" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="{GREEN}" stop-opacity="0.22"/>
      <stop offset="1" stop-color="{GREEN}" stop-opacity="0"/>
    </radialGradient>
    <filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="58"/></filter>
    <clipPath id="panelClip"><rect x="30" y="24" width="1140" height="512" rx="16"/></clipPath>
  </defs>

  <rect width="1200" height="560" fill="{BG}"/>
  <rect width="1200" height="560" fill="url(#grid)"/>


  <rect x="30" y="24" width="1140" height="512" rx="16" fill="{PANEL}" stroke="#16303a" stroke-width="1.2"/>
  <circle cx="150" cy="60" r="280" fill="url(#glowA)" filter="url(#soft)" clip-path="url(#panelClip)" opacity="0.8"/>
  <text x="56" y="66" fill="{GREEN}" font-family="{MONO}" font-size="15">$ neofetch --off</text>
  <text x="1146" y="66" fill="{DIM}" font-family="{MONO}" font-size="12" text-anchor="end">fig.02 / machine readable</text>
  <path d="M30 86H1170" stroke="#ffffff" stroke-opacity="0.07"/>

  <text x="64" y="160" fill="url(#name)" font-family="{MONO}" font-size="44" font-weight="600" letter-spacing="-1">het patel</text>
  <text x="64" y="194" fill="{GREEN}" font-family="{MONO}" font-size="16">computer engineering student</text>
  <path d="M64 216H430" stroke="#ffffff" stroke-opacity="0.08" stroke-dasharray="3 5"/>
  <g font-family="{MONO}" font-size="13" fill="{MUTED}">
    <text x="64" y="244">gandhinagar, in · utc+5:30</text>
    <text x="64" y="268">computer engineering · still a student</text>
  </g>

  <g font-family="{MONO}">
    <rect x="64" y="292" width="212" height="30" rx="15" fill="#0a1a14" stroke="{GREEN}" stroke-opacity="0.4"/>
    <circle cx="84" cy="307" r="3.5" fill="{GREEN}">
      <animate attributeName="opacity" values="1;0.2;1" dur="2.4s" repeatCount="indefinite"/>
    </circle>
    <text x="98" y="312" fill="{GREEN}" font-size="12.5">open to internships</text>
  </g>

  <g font-family="{MONO}" letter-spacing="0.2">
{chr(10).join(row_svg)}
  </g>

  <path d="M64 340H1136" stroke="#ffffff" stroke-opacity="0.06"/>
  <text x="64" y="356" fill="{DIM}" font-family="{MONO}" font-size="11.5" letter-spacing="1.4">LANGUAGE BYTES · ALL PUBLIC REPOS</text>

{chr(10).join(bars)}

  <text x="64" y="516" fill="#3b5164" font-family="{MONO}" font-size="11.5">github.com/het12779-ui · measured, not claimed</text>
  <text x="1146" y="516" fill="#3b5164" font-family="{MONO}" font-size="11.5" text-anchor="end">utf-8 · lf · no build step</text>
</svg>
"""


def diff() -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="1200" height="420" role="img" aria-labelledby="t d">
  <title id="t">Attribution diff: the same journeys, two verdicts</title>
  <desc id="d">A git diff of last-touch against first-touch credit for Google, showing 1.57x versus 0.55x on identical journeys, with the five supported models listed on the right.</desc>
  <defs>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M32 0H0V32" fill="none" stroke="#7fffd4" stroke-opacity="0.04" stroke-width="1"/>
    </pattern>
    <radialGradient id="glow" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="{VIOLET}" stop-opacity="0.2"/>
      <stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/>
    </radialGradient>
    <filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="54"/></filter>
    <clipPath id="panelClip"><rect x="30" y="24" width="1140" height="372" rx="16"/></clipPath>
  </defs>

  <rect width="1200" height="420" fill="{BG}"/>
  <rect width="1200" height="420" fill="url(#grid)"/>


  <rect x="30" y="24" width="1140" height="372" rx="16" fill="{PANEL}" stroke="#16303a" stroke-width="1.2"/>
  <circle cx="1050" cy="40" r="240" fill="url(#glow)" filter="url(#soft)" clip-path="url(#panelClip)" opacity="0.8"/>
  <text x="56" y="64" fill="{GREEN}" font-family="{MONO}" font-size="14.5">$ git diff credit/last_touch credit/first_touch</text>
  <text x="1146" y="64" fill="{DIM}" font-family="{MONO}" font-size="12" text-anchor="end">fig.03 / channeltruth</text>
  <path d="M30 84H1170" stroke="#ffffff" stroke-opacity="0.07"/>

  <g font-family="{MONO}" font-size="14.5" xml:space="preserve">
    <text x="56" y="118" fill="{RED}" fill-opacity="0.8">--- a/credit/last_touch</text>
    <text x="56" y="144" fill="{GREEN}" fill-opacity="0.85">+++ b/credit/first_touch</text>
    <text x="56" y="182" fill="{CYAN}">@@ google · same 5,000 journeys @@</text>

    <rect x="40" y="198" width="700" height="30" fill="{RED}" fill-opacity="0.07"/>
    <text x="56" y="219" fill="{RED}">-  credited_roas  1.57x   # closing click</text>

    <rect x="40" y="232" width="700" height="30" fill="{GREEN}" fill-opacity="0.07"/>
    <text x="56" y="253" fill="{GREEN}">+  credited_roas  0.55x   # opening click</text>

    <text x="56" y="298" fill="{MUTED}">   conversions: identical</text>
    <text x="56" y="324" fill="{AMBER}">   verdict: an argument, not a measurement</text>
  </g>

  <g font-family="{MONO}" font-size="12.5">
    <rect x="820" y="100" width="316" height="196" rx="10" fill="#0a1119" stroke="{VIOLET}" stroke-opacity="0.35"/>
    <text x="844" y="128" fill="{VIOLET}" font-size="11.5" letter-spacing="1.8">MODELS IN THE BUILD</text>
    <text x="844" y="158" fill="{INK}">last-touch</text>
    <text x="844" y="182" fill="{INK}">first-touch</text>
    <text x="844" y="206" fill="{INK}">linear</text>
    <text x="844" y="230" fill="{INK}">position-based</text>
    <text x="844" y="254" fill="{INK}">time-decay</text>
    <text x="844" y="280" fill="{DIM}" font-size="11">102 tests · totals reconcile</text>
  </g>

  <path d="M30 352H1170" stroke="#ffffff" stroke-opacity="0.06"/>
  <text x="56" y="382" fill="{DIM}" font-family="{MONO}" font-size="11.5">read down = which channel earned it · read across = how much the answer depends on the model</text>
</svg>
"""


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, builder in (("hero.svg", hero), ("pipeline.svg", pipeline), ("system.svg", system), ("diff.svg", diff)):
        path = OUT / name
        path.write_text(builder(), encoding="utf-8")
        print(f"wrote {path.relative_to(OUT.parent)} ({path.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
