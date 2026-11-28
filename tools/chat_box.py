"""From the Group Chat, drawn as a text thread (Garret, Nov 27: "make it look more of a text message style").
    from chat_box import chat_box
    html = chat_box([("Gregg", "Thanks Margo 😃"), ("Margo", "You're welcome...")])
Family lines are gray bubbles on the left with the sender's name above; Margo's are blue on the right.
Consecutive lines from the same sender group under one name. Text is HTML-ready (use &rsquo; etc.)."""

def chat_box(lines, title="From the Group Chat"):
    out = [f'<h2 class="sec">{title}</h2>',
           '<div style="background:#f4f1ea;border:1px solid var(--rule,#d3b88f);border-radius:14px;padding:.8rem .7rem .6rem;margin:.4rem 0 1.1rem;font-family:-apple-system,BlinkMacSystemFont,\'Helvetica Neue\',Arial,sans-serif">']
    prev = None
    for who, text in lines:
        me = who == "Margo"
        if who != prev:
            out.append(f'<div style="font-size:.68rem;color:#8e8e93;margin:{".55rem" if prev else "0"} {".35rem" if me else "0"} .15rem {"0" if me else ".55rem"};text-align:{"right" if me else "left"}">{who}</div>')
        bubble = ('background:#0b84ff;color:#fff;border-bottom-right-radius:5px' if me
                  else 'background:#e5e5ea;color:#111;border-bottom-left-radius:5px')
        out.append(f'<div style="display:flex;justify-content:{"flex-end" if me else "flex-start"}"><div style="{bubble};max-width:78%;padding:.45rem .75rem;border-radius:18px;font-size:.95rem;line-height:1.3;margin:.12rem 0">{text}</div></div>')
        prev = who
    out.append('</div>')
    return '\n'.join(out)
