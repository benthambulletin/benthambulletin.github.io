"""From the Group Chat (Garret, Nov 27: the text-bubble look was "too hard to follow"; back to the
original quote-then-Margo format, "spruce it up a little").
    from chat_box import chat_box
    html = chat_box([
        ([("Gregg", "Thanks Margo 😃")], "You're welcome..."),
        ([("Kaylani", "Tree is up!"), ("Tom", "Yessss")], "Tree up before..."),
    ])
Each exchange: the family's lines (name in small caps, the words in quotes), then Margo's answer set off
with a rust rule. Text is HTML-ready (&rsquo; etc.)."""

LBL = "font-family:Archivo,Arial,sans-serif;font-size:.62rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase"

def chat_box(exchanges, title="From the Group Chat"):
    out = [f'<h2 class="sec">{title}</h2>',
           '<div style="border:1px solid var(--rule,#d3b88f);border-radius:8px;padding:.3rem .95rem;margin:.4rem 0 1.1rem;background:rgba(255,255,255,.35)">']
    for i, (quotes, reply) in enumerate(exchanges):
        top = '' if i == 0 else 'border-top:1px dashed var(--rule,#d3b88f);'
        out.append(f'<div style="{top}padding:.65rem 0">')
        for who, text in quotes:
            out.append(f'<div style="margin:.1rem 0 .25rem"><span style="{LBL};color:var(--teal,#2f5e3e)">{who}</span> '
                       f'<span style="font-size:1rem">&ldquo;{text}&rdquo;</span></div>')
        out.append(f'<div style="border-left:3px solid var(--rust,#9c3216);padding:.1rem 0 .1rem .65rem;margin-top:.4rem">'
                   f'<span style="{LBL};color:var(--rust,#9c3216)">Margo</span> '
                   f'<span style="font-style:italic">{reply}</span></div>')
        out.append('</div>')
    out.append('</div>')
    return '\n'.join(out)
