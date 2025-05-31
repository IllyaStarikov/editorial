# Easter Egg Hunt 🥚
> Eggs Marks the Spot.

Easter Eggs began as real eggs hidden on holiday mornings, but in tech and media the term has a twist: it means a hidden surprise tucked into the content.  In fact, the phrase was coined in 1979 at Atari’s *Adventure* game.  There, developers hid a secret credit (“Created by Warren Robinett”) in an invisible room.  Today an Easter egg is any deliberate secret – a concealed feature or message in software, games, movies or websites.  In practice this can be anything from a hidden function in an app to a sly visual reference in a film.

Iconic examples include:

* **Atari (*Adventure*, 1979)** Finding a tiny invisible dot in *Adventure* opens a hidden room that reads “Created by Warren Robinett”.  This was one of the first video-game Easter eggs, and Atari loved the idea – it even adopted “Easter egg” as the official term for hidden dev signatures.
* **Google tricks:** Google search is full of Easter eggs.  For example, typing **“do a barrel roll”** makes the results page spin 360°.  (Try it – in modern browsers the page will flip once.)
* **Video games** Beyond *Adventure*, many classic games hide secrets. Famous examples include Metal Gear Solid’s [Psycho Mantis reading your memory card](https://www.youtube.com/watch?v=t0oHnGM_iQw), Hitman 3’s [Alien abduction](https://www.youtube.com/watch?v=n3ftW7Nq9WU), or Doom 2’s [“To win the game you must kill me, John Romero”](https://www.youtube.com/watch?v=oKOuOteJn2Q).
* **Movies and TV** Filmmakers pepper Easter eggs throughout their work.  Marvel movies famously include clues to future films in almost every scene.  Fans also love spotting recurring motifs (like *Star Wars* homages or Pixar cameos) as “Easter eggs” for the observant.

![](https://starikov.co/content/images/2025/05/easter_egg_hunt.png)


## #EasterEgg-straction

On this site, any page tagged `#EasterEgg` hides a secret page behind it.  These secrets aren’t obvious – you have to sniff them out.  For example, the **Zero-Width Space** page cheekily begins with “Nothing to see here”.  In fact, that line (and the tiny translucent dot next to it) is the clue: clicking the invisible bit reveals a hidden page.  The key is literally an invisible character (a zero-width space) placed in the HTML.  In short, a `#EasterEgg` tag signals that a playful secret is buried in the code or content, discoverable only by a curious visitor.

## Hints
### [The Zero-Width Space-Place](https://starikov.co/zero-width-space/)


<!-- SPOILER‑IN‑A‑LIST (grid‑centred overlay) -->
<style>
/* ── Spoiler core ───────────────────────────── */
:where(.spoiler-box){
  display:inline-grid;          /* one‑cell grid for perfect overlap */
  position:relative;            /* keeps list numbers untouched */
}

:where(.spoiler-text){
  grid-area:1/1;                /* shares the same cell as the overlay */
  filter:blur(8px) contrast(.6);
  transition:filter .4s ease;
}

:where(.spoiler-toggle){
  all:unset;
  grid-area:1/1;                /* full‑cell overlay */
  display:flex; align-items:center; justify-content:center;
  cursor:pointer;
  background:rgba(0,0,0,.55);
  backdrop-filter:blur(3px);
  color:#fff; font:700 .9em/1 sans-serif;
  text-transform:uppercase; letter-spacing:.05em;
  transition:opacity .4s ease, transform .4s ease;
}

:where(.spoiler-box.revealed) .spoiler-text{filter:none;}
:where(.spoiler-box.revealed) .spoiler-toggle{
  opacity:0; transform:scale(1.1); pointer-events:none;
}
</style>

<ol>
  <li>
    <span class="spoiler-box">
      <span class="spoiler-text">This is a page about zero-width spaces...</span>
      <button class="spoiler-toggle" aria-label="Reveal spoiler">Show</button>
    </span>
  </li>
  <li>
    <span class="spoiler-box">
      <span class="spoiler-text">”Nothing to see here.”</span>
      <button class="spoiler-toggle" aria-label="Reveal spoiler">Show</button>
    </span>
  </li>
  <li>
    <span class="spoiler-box">
      <span class="spoiler-text"> To inspect Right-click anywhere and choose **Inspect** (or press Ctrl + Shift + I) to open the Developer Tools. Hidden elements (like a zero-width space or transparent button) will appear in the DOM.</span>
      <button class="spoiler-toggle" aria-label="Reveal spoiler">Show</button>
    </span>
  </li>
</ol>

<script>
/* single delegated listener handles every spoiler on the page */
document.addEventListener('click', e=>{
  if(e.target.matches('.spoiler-toggle')){
    e.target.closest('.spoiler-box')?.classList.add('revealed');
  }
});
</script>
