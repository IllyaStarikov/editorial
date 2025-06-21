# Color Clipper
<h2 style="font-size: 2.5rem; line-height: 1.4; text-align: center; font-weight: 700; margin: 2rem auto; max-width: 800px;">
  <span style="background: linear-gradient(135deg, #00f5ff 0%, #ff0099 25%, #ffea00 50%, #00ff88 75%, #00f5ff 100%); background-size: 400% 400%; -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; animation: gradient-shift 4s ease infinite; filter: brightness(1.2);">Drag, hover, click</span>
  <span style="color: #e0e0e0;"> a </span>
  <span style="display: inline-block; background: linear-gradient(45deg, #ff006e, #00f5ff, #ffea00, #00ff88, #ff006e); background-size: 600% 100%; -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; animation: pixel-rainbow 3s linear infinite; filter: brightness(1.3); font-weight: 800;">pixel</span><span style="color: #e0e0e0;">.</span>
  <br>
  <span style="background: linear-gradient(90deg, #00f5ff, #ff0099, #ffea00, #00f5ff); background-size: 200% 100%; -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; animation: wave 2s ease-in-out infinite; filter: brightness(1.1);">Color's copied</span>
  <span style="color: #e0e0e0;"> to your </span>
  <span style="color: #00f5ff; font-weight: 800; text-shadow: 0 0 20px rgba(0, 245, 255, 0.5), 0 0 40px rgba(0, 245, 255, 0.3);">clipboard!</span>

  <style>
    @keyframes gradient-shift {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    @keyframes pixel-rainbow {
      0% { background-position: 0% 50%; }
      100% { background-position: 100% 50%; }
    }

    @keyframes wave {
      0%, 100% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
    }
  </style>
</h2>


Drop an image, hover any pixel, click once to copy its HEX. Four more formats (RGB, RGBA, HSL, HSV) are ready if you need them.
---


What is this?
A self‑contained, browser‑side colour inspector that:
Accepts JPG, PNG, GIF, WebP.
Magnifies 10× under the cursor so you never miss the right pixel.
Shows five colour formats in real time.
Copies any value to your clipboard with a single click.
Stays entirely client‑side—images never leave your machine.---


Why might I care?
Design QA: Verify that exported assets match the brand palette.
Accessibility audits: Check contrast hotspots.
Development shortcuts: Skip the screenshot → Photoshop loop.
Palette mining: Turn vintage posters into modern UI themes.---


How might I use this?
1  Load an image
Drop a file anywhere inside the dashed zone, or
Click the zone to open a file picker.
Tip: Huge RAWs are fine—the script auto‑scales them to fit your viewport.
2  Hover to inspect
The circular loupe follows your cursor and zooms 10×. A crosshair marks the exact pixel.
3  Click to lock
Click anywhere on the image. The current HEX value is copied straight to your clipboard, and the button flashes a confirmation.
4  Grab any format
Need RGBA for CSS or HSL for Tailwind? Just click the label beside the value—copied.
5  Start over
Load another image and repeat. No refresh needed.
