# The Zero-Width Space-Place

> Nothing to​​ see here<a href="https://starikov.co/4O4">&#8203</a>.

​<!-- Zero‑Width‑Space generator – larger pill & button with padded label -->
<div class="zws-generator">
  <style>
    /* base colours */
    .zws-generator{
      --accent: var(--ghost-accent-color, #ffab40);
      --bg:     var(--color-bg, #111);
      --fg:     var(--color-text, #eee);
      --border: var(--color-border, rgba(255,255,255,.16));
      --marker: #16a4ff;

      font-family: system-ui, sans-serif;
      color: var(--fg);
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: .75rem;
      padding: 2.25rem 2.5rem;
      max-width: 480px;
      margin: 1.8rem auto;
      text-align: center;
      box-shadow: 0 5px 18px rgba(0,0,0,.45);
    }

    /* layout */
    .zws-form{display:flex; gap:1.2rem; justify-content:center; flex-wrap:wrap;}

    /* shared sizes */
    .pill-w {width: 110px;}
    .btn-w  {width: 260px;}   /* outer size still large */
    .elem-h {height: 56px;}

    /* blue‑dot wrapper */
    .zws-wrapper{position:relative;}
    .zws-wrapper::after{
      content:''; position:absolute; top:50%; left:50%;
      transform:translate(-50%,-50%);
      width:12px; height:12px; border-radius:50%; background:var(--marker);
      pointer-events:none;
    }

    /* input pill */
    .zws-field{
      border:1px dashed var(--border);
      border-radius:.7rem;
      background:rgba(255,255,255,.06);
      backdrop-filter:blur(4px);
      color:transparent; caret-color:var(--marker);
      user-select:all; cursor:text;
      font-size:1.05rem; line-height:56px; padding:0; text-align:center;
    }
    .zws-field:focus{outline:2px solid var(--marker); outline-offset:2px;}

    /* copy button – now padded */
    .zws-btn{
      all:unset;
      display:flex; align-items:center; justify-content:center;
      border-radius:.7rem;
      background:var(--accent); color:#000;
      font-weight:700; font-size:1.05rem;
      cursor:pointer;
      width:260px; height:56px;               /* keeps outer size */
      padding:0 2rem;                         /* horizontal padding */
      box-sizing:border-box;                  /* include padding in width */
      transition:transform .15s, box-shadow .15s;
    }
    .zws-btn:hover  {transform:translateY(-2px); box-shadow:0 4px 8px rgba(0,0,0,.35);}
    .zws-btn:active {transform:none;            box-shadow:none;}

    /* feedback */
    .zws-notice{margin-top:1rem; font-size:.95rem; opacity:0; transition:opacity .25s;}
    .zws-notice.show{opacity:1;}
  </style>

  <h3 style="margin-top:0">Zero‑Width Space</h3>
  <p style="margin:.35rem 0 1.25rem">
    Click the translucent pill (blue dot marks it) or the big Copy button.
  </p>

  <form class="zws-form" onsubmit="return false;">
    <span class="zws-wrapper pill-w elem-h">
      <input class="zws-field pill-w elem-h" id="zwsField" value="&#8203;" readonly>
    </span>

    <button type="button" class="zws-btn" id="zwsCopy">Copy</button>
  </form>

  <div class="zws-notice" id="zwsMsg" aria-live="polite"></div>

  <script>
  (()=>{                    /* scoped to this widget only */
    const zws  = "\u200B";
    const field = document.getElementById("zwsField");
    const btn   = document.getElementById("zwsCopy");
    const msg   = document.getElementById("zwsMsg");

    ["focus","click"].forEach(e=>field.addEventListener(e,()=>field.select()));
    btn.addEventListener("click", copyZWS);

    async function copyZWS(){
      try{ await navigator.clipboard.writeText(zws); flash("Copied 👍"); }
      catch{ fallback(zws)? flash("Copied 👍 (fallback)") : flash("Failed 😢"); }
    }

    function fallback(txt){
      const ta = Object.assign(document.createElement("textarea"),{value:txt, style:"position:fixed;opacity:0"});
      document.body.appendChild(ta); ta.select();
      const ok = document.execCommand("copy");
      document.body.removeChild(ta); return ok;
    }

    function flash(text){
      msg.textContent = text; msg.classList.add("show");
      clearTimeout(flash.t); flash.t = setTimeout(()=>msg.classList.remove("show"), 2800);
    }
  })();
  </script>
</div>


## What’s Zero-Width Space?
The zero‑width space (U+200B) is a Unicode glyph that renders nothing and occupies zero width. In the right hands, this “invisible ink” changes how software treats text. 


## Example
Below are seven tricks I actually use, each with a quick demo.

1. **Anchor an Alphabetical List**
Prefix one or more ZWS characters to push an item *ahead* of "A".

```txt
​Newsletter  ← with ZWS
Apple
Zucchini
```

2. **Break Auto‑Linking**
Drop a ZWS into a URL or email to foil scrapers while leaving it human‑readable.

```txt
hello​@starikov.co
https://starikov​.co
```

3. **Duplicate C++ Identifiers**
ZWS is a valid identifier character in many compilers.

```cpp
int total = 1;    // normal
int tota​l = 2;    // looks the same, compiles fine
std::cout << total + tota​l; // prints 3
```

4. **Python Indentation Gremlins**
Slip a ZWS into leading spaces; code *looks* aligned but crashes.

```python
def hello():
print("ok")   # four spaces
​    print("boom") # four + ZWS → IndentationError
```

5. **Hide Easter‑Egg Text**
Insert a binary watermark every 100 characters; humans never see it, diff tools do.

6. **Zero‑Length Social Forms**
Some platforms allow a username, bios, and other forms that is literally just ZWS. Pure minimalism.

7. **Control word‑wrapping**
Add ZWS inside a super‑long URL to let browsers break the line without inserting a visible hyphen.

```html   
<span style="word-break:break-all">
https://example.com/superlong​paththatneverends
</span>
```