import random, math
random.seed(7)
INK="#24170c"; PAPER="#f8eedb"; RUST="#9c3216"
# Profile silhouette facing right, in a 300x360 box: back of head -> bun -> crown -> forehead -> nose -> lips -> chin -> neck -> collar
P = ("M 96 300 C 92 270 88 248 78 232 C 62 214 54 190 58 166 "   # nape / back of head
     "C 36 168 22 146 30 124 C 40 100 72 96 86 112 "               # bun
     "C 92 80 116 62 150 60 C 186 58 210 74 220 98 "               # crown to brow
     "C 224 110 224 120 226 130 C 230 140 238 150 246 160 "        # forehead, bridge
     "C 250 166 248 171 240 172 C 236 173 234 176 236 180 "        # nose tip, underside
     "C 240 184 238 188 232 190 C 238 194 236 200 230 202 "        # upper lip, lower lip
     "C 232 212 231 222 223 230 C 215 239 205 245 194 246 "        # chin, jaw
     "C 192 258 194 272 202 286 C 222 294 246 302 262 318 "        # throat, collar line
     "L 262 360 L 40 360 C 46 334 66 312 96 300 Z")
def stipple(n):
    # dot field inside the silhouette, denser toward the back of the head (shading)
    dots=[]
    for _ in range(n):
        x=random.uniform(30,265); y=random.uniform(55,360)
        w=1-(x-30)/235
        if random.random()<0.25+0.75*w: dots.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{random.uniform(.7,1.6):.2f}"/>')
    return "".join(dots)
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 380" width="300" height="380">
<defs><clipPath id="s"><path d="{P}"/></clipPath><clipPath id="o"><ellipse cx="150" cy="200" rx="128" ry="160"/></clipPath></defs>
<ellipse cx="150" cy="200" rx="138" ry="170" fill="none" stroke="{INK}" stroke-width="2"/>
<ellipse cx="150" cy="200" rx="131" ry="163" fill="none" stroke="{INK}" stroke-width=".8"/>
<g clip-path="url(#o)">
 <rect width="300" height="380" fill="{PAPER}"/>
 <g stroke="{INK}" stroke-width=".55" opacity=".35">{"".join(f'<line x1="0" y1="{y}" x2="300" y2="{y-60}"/>' for y in range(0,460,7))}</g>
 <path d="{P}" fill="{INK}"/>
 <g clip-path="url(#s)" fill="{PAPER}" opacity=".10">{stipple(1400)}</g>

 <path d="M 58 166 C 36 168 22 146 30 124 C 40 100 72 96 86 112 C 92 80 116 62 150 60 C 186 58 210 74 220 98 C 214 96 200 90 186 92 C 160 96 132 104 118 118 C 104 132 96 150 92 170 C 80 172 66 170 58 166 Z" fill="#7a6a58"/>
 <g fill="none" stroke="#8a7a66" stroke-width="1.3" opacity=".8">
  <path d="M 40 128 C 52 118 66 116 80 124"/><path d="M 120 76 C 150 66 184 70 206 86"/><path d="M 110 96 C 140 82 176 82 200 94"/>
 </g>
 <ellipse cx="215" cy="133" rx="9.5" ry="7" fill="none" stroke="{PAPER}" stroke-width="2"/>
 <path d="M 205 133 C 186 144 168 156 152 192" fill="none" stroke="{PAPER}" stroke-width="1" stroke-dasharray="1.5 2.5" opacity=".9"/>
 <rect x="234" y="193" width="28" height="5" rx="1" fill="#efe3c8" stroke="{INK}" stroke-width=".8" transform="rotate(-7 234 195)"/>
 <rect x="258" y="193" width="5" height="5" rx="1" fill="{RUST}" transform="rotate(-7 234 195)"/>
 <path d="M 262 188 C 256 176 270 168 262 156 C 254 146 268 136 260 124 C 254 116 262 108 258 100" fill="none" stroke="{INK}" stroke-width="1.6" stroke-linecap="round" opacity=".45"/>
 <path d="M 202 286 C 222 294 246 302 262 318 L 262 332 C 240 320 214 306 198 302 Z" fill="{RUST}"/>
</g>
</svg>'''
open('margo.svg','w').write(svg)
