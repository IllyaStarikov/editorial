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
/* Table of Contents */
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

/* Tables */
table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 20px;
  font-family: Arial, sans-serif;
  color: #E0E0E0; /* Light text color for dark background */
  /* box-shadow: 0 2px 8px rgba(0,0,0,0.5); /* Optional: A darker shadow for dark themes */
}

caption {
  font-size: 1.8em;
  margin-bottom: 15px;
  font-weight: bold;
  text-align: left;
  color: #F5F5F5; /* Very light caption color */
}

th, td {
  border: 1px solid #333333; /* Darker borders that are still visible */
  padding: 10px 15px;
  text-align: left;
}

th { /* Styles for header cells */
  background-color: #252525; /* Dark background for headers, slightly different from rows */
  font-weight: bold;
  color: #F0F0F0; /* Light header text */
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* Assuming a very dark base for rows */
tbody tr {
  background-color: #1A1A1A; /* Your default very dark row background */
}

/* Optional: Zebra striping for dark themes (can be very subtle or omitted) */
tbody tr:nth-child(even) {
  background-color: #161616; /* Slightly different dark shade for even rows, if desired */
}

tbody tr:hover {
  background-color: #222222; /* VERY slightly less dark than #1A1A1A for hover */
  /* If your base is pure black (#000000), you might use something like #0A0A0A or #101010 */
  color: #FFFFFF; /* Optionally make text pure white on hover for a slight emphasis */
  cursor: default;
}

td:first-child, th:first-child {
  /* Optional: styling for the first column if needed */
}

table.wrappable-table {
  width: 100%; /* Or a specific width */
  border-collapse: collapse;
  table-layout: fixed; /* Helps with predictable wrapping */
}
table.wrappable-table th,
table.wrappable-table td {
  border: 1px solid black; /* Optional: for visibility */
  padding: 8px;           /* Optional: for spacing */
  word-wrap: break-word;  /* For older browsers */
  overflow-wrap: break-word; /* Standard property */
  white-space: normal;    /* Ensures text wraps normally */
}

</style>
```
