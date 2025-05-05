# Header
```
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-H5ERFVZRFB"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-H5ERFVZRFB');
</script>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tocbot/4.12.3/tocbot.css">

<style>
    .gh-content {
        position: relative;
    }

    .gh-toc > .toc-list {
        position: relative;
    }

    .toc-list {
        overflow: hidden;
        list-style: none;
    }

    @media (min-width: 1300px) {
        .gh-sidebar {
            position: absolute; 
            top: 0;
            bottom: 0;
            margin-top: 4vmin;
            margin-left: 20px;
            grid-column: wide-end / main-end; /* Place the TOC to the right of the content */
            width: inline-block;
            white-space: nowrap;
        }

        .gh-toc-container {
            position: sticky; /* On larger screens, TOC will stay in the same spot on the page */
            top: 4vmin;
        }
    }

    .gh-toc .is-active-link::before {
        background-color: var(--ghost-accent-color); /* Defines TOC accent color based on Accent color set in Ghost Admin */
    } 
</style>
```