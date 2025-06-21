# Boilerplate

[//]: # --------------------------------------------------- Custom Callout

<div class="custom-callout custom-callout-note">
  <strong>NOTE 📜</strong> This is a page that talks about my work, please review my <a href="https://starikov.co/disclosures/"><strong>Disclosures</strong></a>.
</div>


<div class="custom-callout custom-callout-note">
  <strong>NOTE</strong> This is a helpful piece of information that you should pay attention to. It's not critical, but good to know.
</div>

<div class="custom-callout custom-callout-warning">
  <strong>WARNING</strong> Be careful! This action could have unintended consequences or lead to data loss if not handled correctly.
</div>

<div class="custom-callout custom-callout-info">
  <strong>INFO</strong> Just an informational update. For example, a new feature has been released or a system maintenance is scheduled.
</div>
</div>


[//]: # --------------------------------------------------- Remove Post Footer

<script>
document.addEventListener('DOMContentLoaded', function() {
    // Hide the post footer section
    const postFooter = document.querySelector('.c-post__footer');
    if (postFooter) {
        postFooter.style.display = 'none';
    }

    // Also remove the padding from the parent post element to eliminate extra space
    const postElement = document.querySelector('.c-post');
    if (postElement) {
        postElement.style.paddingBottom = '0';
    }
});
</script>


[//]: # --------------------------------------------------- Header Inline Image

<!-- Self-contained H2 with inline image -->
<div style="
  width: 100%;
  margin: 0;
  padding: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
">
  <h2 style="
    color: #ffffff;
    font-size: 2rem;
    font-weight: 700;
    line-height: 1.2;
    margin: 0 0 1.5rem 0;
    padding: 0;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    flex-wrap: wrap;
  ">
    <span>Your Header Text</span>
    <img
      src="https://via.placeholder.com/32x32/ffffff/000000?text=★"
      alt="Header icon"
      style="
        height: 1em;
        width: auto;
        display: inline-block;
        vertical-align: middle;
        object-fit: contain;
      "
    />
    <span>More Text</span>
  </h2>
</div>

<!-- Alternative version with image in the middle of text -->
<div style="
  width: 100%;
  margin: 2rem 0 0 0;
  padding: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
">
  <h2 style="
    color: #ffffff;
    font-size: 2rem;
    font-weight: 700;
    line-height: 1.2;
    margin: 0 0 1.5rem 0;
    padding: 0;
  ">
    Text with
    <img
      src="https://via.placeholder.com/32x32/ffffff/000000?text=✦"
      alt="Inline icon"
      style="
        height: 0.9em;
        width: auto;
        display: inline;
        vertical-align: baseline;
        margin: 0 0.25rem;
        object-fit: contain;
      "
    />
    inline image
  </h2>
</div>

<!-- Version with image at the beginning -->
<div style="
  width: 100%;
  margin: 2rem 0 0 0;
  padding: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
">
  <h2 style="
    color: #ffffff;
    font-size: 2rem;
    font-weight: 700;
    line-height: 1.2;
    margin: 0 0 1.5rem 0;
    padding: 0;
  ">
    <img
      src="https://via.placeholder.com/32x32/ffffff/000000?text=◆"
      alt="Header decoration"
      style="
        height: 1em;
        width: auto;
        display: inline;
        vertical-align: text-bottom;
        margin-right: 0.5rem;
        object-fit: contain;
      "
    />
    Header with Leading Icon
  </h2>
</div>

