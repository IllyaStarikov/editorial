# Sortable List

## Header

<style>
/* Floating Toggle Button */
.list-toggle-button {
  position: fixed;
  bottom: 30px;
  right: 30px;
  width: 56px;
  height: 56px;
  background-color: var(--color-text, #000);
  color: var(--color-background, #fff);
  border: none;
  border-radius: 50%;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-family-sans-serif);
  font-size: 14px;
  font-weight: 600;
  transition: all 0.3s ease;
  overflow: hidden;
}

.list-toggle-button.at-footer {
  position: absolute;
}

.list-toggle-button:hover {
  transform: scale(1.1);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2);
}

.list-toggle-button:active {
  transform: scale(0.95);
}

/* Button Icons - Swapped */
.list-toggle-button::before {
  content: "ABC";
  position: absolute;
  transition: all 0.3s ease;
}

.list-toggle-button.sorted-mode::before {
  content: "•••";
  font-size: 20px;
  letter-spacing: 2px;
}

/* Tooltip - Updated text */
.list-toggle-button::after {
  content: "Sort alphabetically";
  position: absolute;
  bottom: 100%;
  right: 0;
  margin-bottom: 10px;
  padding: 8px 12px;
  background-color: var(--color-text, #000);
  color: var(--color-background, #fff);
  font-size: 12px;
  white-space: nowrap;
  border-radius: 4px;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s ease;
}

.list-toggle-button.sorted-mode::after {
  content: "Show original order";
}

.list-toggle-button:hover::after {
  opacity: 1;
}

/* Sortable List Container - Transparent wrapper */
.sortable-list {
  /* Completely transparent container */
  margin: 0;
  padding: 0;
  background: transparent;
}

/* Direct lists in sortable container */
.sortable-list > ol,
.sortable-list > ul {
  /* Inherit all default list styling from your theme */
  transition: opacity 0.3s ease;
}

/* CRITICAL FIX: Ensure sortable lists match your site exactly */

/* Force sortable lists to have MORE space from the left */
.sortable-list > ul {
  /* Added 5 pixels more for bullet lists */
  margin-left: calc(var(--space-100) + 5px) !important;
  padding-left: 0 !important;
}

/* Ordered lists need extra space for three-digit numbers */
.sortable-list > ol {
  /* Reduced from 2.5em to 1em - just enough for 3-digit numbers */
  margin-left: calc(var(--space-100) + 1em) !important;
  padding-left: 0 !important;
}

/* Content area direct child lists need special handling */
.c-content > .sortable-list > ul {
  /* Added 5 pixels more for bullet lists */
  padding-left: calc(var(--space-100) + 5px) !important;
  margin-left: 0 !important;
}

/* Content area ordered lists need more space */
.c-content > .sortable-list > ol {
  /* Reduced from 2.5em to 1em */
  padding-left: calc(var(--space-100) + 1em) !important;
  margin-left: 0 !important;
}

/* Add spacing between list items */
.sortable-list li {
  /* Add 3-4 pixels between each bullet/item */
  margin-bottom: 4px !important;
}

/* Remove margin from last item to prevent extra space at bottom */
.sortable-list li:last-child {
  margin-bottom: 0 !important;
}

/* Nested lists maintain standard margin */
.sortable-list li > ul {
  /* Nested bullet lists keep the standard margin */
  margin-left: var(--space-100) !important;
  padding-left: 0 !important;
  /* Add a tiny bit of spacing above nested lists */
  margin-top: 3px !important;
}

/* Nested ordered lists also need extra space */
.sortable-list li > ol {
  /* No indentation - flush with the left edge */
  margin-left: 0 !important;
  padding-left: 0 !important;
  /* Add a tiny bit of spacing above nested lists */
  margin-top: 3px !important;
}

/* Mobile specific adjustments to prevent clipping */
@media (max-width: 768px) {
  /* 4 pixels of extra padding on mobile */
  .sortable-list {
    padding-left: 4px;
  }

  /* Ordered lists - reduced from 3em to 1.2em on mobile */
  .sortable-list > ol {
    margin-left: calc(var(--space-100) + 1.2em) !important;
  }

  .c-content > .sortable-list > ol {
    padding-left: calc(var(--space-100) + 1.2em) !important;
  }

  /* Very small screens */
  @media (max-width: 480px) {
    .sortable-list {
      padding-left: 6px;
    }

    /* Reduced from 3.5em to 1.5em on tiny screens */
    .sortable-list > ol {
      margin-left: calc(var(--space-100) + 1.5em) !important;
    }

    .c-content > .sortable-list > ol {
      padding-left: calc(var(--space-100) + 1.5em) !important;
    }
  }
}

/* Typography inheritance */
.sortable-list,
.sortable-list ol,
.sortable-list ul,
.sortable-list li {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
  font-weight: inherit;
  color: inherit;
  letter-spacing: inherit;
  word-break: inherit;
}

/* Let links inherit normal behavior from your theme */
.sortable-list a {
  color: inherit;
}

/* Links should inherit underline behavior from your theme */
/* Your theme underlines links in content areas by default */

/* Content area specific typography */
.c-content .sortable-list,
.c-content .sortable-list ol,
.c-content .sortable-list ul,
.c-content .sortable-list li {
  font-family: var(--font-family-serif);
  font-size: var(--font-size-150);
  line-height: var(--line-height-150);
  word-break: break-word;
}

/* Transition state */
.sortable-list.transitioning ol,
.sortable-list.transitioning ul {
  opacity: 0.7;
}

/* Content flow spacing - only between different content types */
.c-content > * + .sortable-list {
  /* Increased from 6px to 12px for more top spacing */
  margin-top: 12px;
}

.c-content .sortable-list + *:not(.sortable-list) {
  margin-top: var(--content-flow);
}

/* Increased spacing when sortable list follows headings */
.c-content > :is(h1, h2, h3, h4, h5) + .sortable-list {
  margin-top: 10px;
}

/* No margin between sortable wrapper and its list */
.sortable-list > ol:first-child,
.sortable-list > ul:first-child {
  margin-top: 0 !important;
}

/* Mobile adjustments */
@media (max-width: 768px) {
  .list-toggle-button {
    bottom: 20px;
    right: 20px;
    width: 48px;
    height: 48px;
    font-size: 12px;
  }
}

/* IMPORTANT: Don't override any list positioning or spacing */
/* Let your theme's existing CSS handle all the layout */
</style>


## Footer

<script>
(function() {
  // Wait for DOM to be fully loaded
  document.addEventListener('DOMContentLoaded', function() {
    // Check if there are any sortable lists on the page
    const sortableLists = document.querySelectorAll('.sortable-list');
    if (sortableLists.length === 0) return;

    // Create the floating button
    const toggleButton = document.createElement('button');
    toggleButton.className = 'list-toggle-button';
    toggleButton.setAttribute('aria-label', 'Toggle list format');
    document.body.appendChild(toggleButton);

    // State tracking - now starts as false (unordered/manual)
    let isSorted = false;

    // Function to extract text content for sorting (ignoring HTML and emoji)
    function getTextForSorting(element) {
      // Clone the element to avoid modifying the original
      const clone = element.cloneNode(true);

      // Remove all nested lists to get just the item's own text
      const nestedLists = clone.querySelectorAll('ol, ul');
      nestedLists.forEach(el => el.remove());

      // Remove all images, icons, and other non-text elements
      const nonTextElements = clone.querySelectorAll('img, svg, picture, video, audio, iframe, object, embed');
      nonTextElements.forEach(el => el.remove());

      // Get the text content
      let text = clone.textContent || clone.innerText || '';

      // Remove emoji and special characters from the beginning for sorting
      text = text.replace(/^[\u{1F300}-\u{1F9FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}\u{1F000}-\u{1F02F}\u{1F0A0}-\u{1F0FF}\u{1F100}-\u{1F64F}\u{1F680}-\u{1F6FF}\u{1F900}-\u{1F9FF}\u{1FA70}-\u{1FAFF}\s\u{2190}-\u{21FF}\u{2300}-\u{23FF}\u{2460}-\u{24FF}\u{25A0}-\u{25FF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}\u{2900}-\u{297F}\u{2B00}-\u{2BFF}\u{3000}-\u{303F}]+/gu, '');

      // Also remove common icon fonts and special characters
      text = text.replace(/^[\s\W]+/, '');

      return text.trim();
    }

    // Function to process a list recursively
    function processListRecursively(list, shouldSort) {
      // Get all direct child list items
      const items = Array.from(list.children);

      // Create array of item data with sort text
      const itemData = items.map(item => ({
        element: item,
        sortText: getTextForSorting(item)
      }));

      // Sort if needed
      if (shouldSort) {
        itemData.sort((a, b) => {
          const textA = a.sortText.toLowerCase();
          const textB = b.sortText.toLowerCase();
          return textA.localeCompare(textB);
        });
      }

      // Clear the list
      list.innerHTML = '';

      // Re-add items in the correct order
      itemData.forEach(data => {
        const item = data.element;

        // Process any nested lists within this item
        const nestedLists = item.querySelectorAll('ol, ul');
        nestedLists.forEach(nestedList => {
          processListRecursively(nestedList, shouldSort);
        });

        list.appendChild(item);
      });
    }

    // Function to clone and process entire list structure
    function cloneAndProcessList(originalList, newType, shouldSort) {
      // Deep clone the entire list
      const clonedList = originalList.cloneNode(true);

      // Change the list type
      const newList = document.createElement(newType);

      // Copy attributes
      Array.from(clonedList.attributes).forEach(attr => {
        if (attr.name !== 'style') {
          newList.setAttribute(attr.name, attr.value);
        }
      });

      // Move all children to new list
      while (clonedList.firstChild) {
        newList.appendChild(clonedList.firstChild);
      }

      // Process the new list recursively (sorts all levels if needed)
      processListRecursively(newList, shouldSort);

      // Change all nested list types based on current mode
      if (shouldSort) {
        // When sorted, change all ul to ol (numbered)
        const allULs = newList.querySelectorAll('ul');
        allULs.forEach(ul => {
          const ol = document.createElement('ol');
          Array.from(ul.attributes).forEach(attr => {
            ol.setAttribute(attr.name, attr.value);
          });
          while (ul.firstChild) {
            ol.appendChild(ul.firstChild);
          }
          ul.parentNode.replaceChild(ol, ul);
        });
      } else {
        // When unsorted, change all ol to ul (bulleted)
        const allOLs = newList.querySelectorAll('ol');
        allOLs.forEach(ol => {
          const ul = document.createElement('ul');
          Array.from(ol.attributes).forEach(attr => {
            ul.setAttribute(attr.name, attr.value);
          });
          while (ol.firstChild) {
            ul.appendChild(ol.firstChild);
          }
          ol.parentNode.replaceChild(ul, ol);
        });
      }

      return newList;
    }

    // Store original lists
    const originalLists = new Map();
    sortableLists.forEach((wrapper, index) => {
      const list = wrapper.querySelector('ol, ul');
      if (list) {
        originalLists.set(index, {
          element: list.cloneNode(true),
          type: list.tagName.toLowerCase()
        });
      }
    });

    // Function to toggle all lists
    function toggleLists() {
      // Store current scroll position
      const scrollY = window.scrollY;
      const scrollX = window.scrollX;

      sortableLists.forEach((wrapper, index) => {
        wrapper.classList.add('transitioning');

        const currentList = wrapper.querySelector('ol, ul');
        if (!currentList) return;

        const originalData = originalLists.get(index);
        if (!originalData) return;

        let newList;

        if (!isSorted) {
          // Switching to sorted - create ordered list and sort
          newList = cloneAndProcessList(originalData.element, 'ol', true);
        } else {
          // Switching back to original - restore original as unordered
          newList = originalData.element.cloneNode(true);
          // Make sure it's unordered
          if (newList.tagName.toLowerCase() !== 'ul') {
            const ul = document.createElement('ul');
            Array.from(newList.attributes).forEach(attr => {
              ul.setAttribute(attr.name, attr.value);
            });
            while (newList.firstChild) {
              ul.appendChild(newList.firstChild);
            }
            newList = ul;
          }
        }

        // Replace the list
        currentList.parentNode.replaceChild(newList, currentList);

        // Remove transition class after animation
        setTimeout(() => {
          wrapper.classList.remove('transitioning');
        }, 300);
      });

      // Toggle state
      isSorted = !isSorted;
      toggleButton.classList.toggle('sorted-mode', isSorted);

      // Restore scroll position
      window.scrollTo(scrollX, scrollY);
    }

    // Handle button position relative to footer
    function handleButtonPosition() {
      const footer = document.querySelector('.c-footer') || document.querySelector('footer');
      if (!footer) return;

      const footerRect = footer.getBoundingClientRect();
      const windowHeight = window.innerHeight;
      const buttonHeight = 86; // 56px height + 30px bottom margin

      if (footerRect.top < windowHeight) {
        // Footer is visible
        const bottomPosition = windowHeight - footerRect.top + 30;
        toggleButton.style.bottom = bottomPosition + 'px';
        toggleButton.classList.add('at-footer');
      } else {
        // Footer is not visible
        toggleButton.style.bottom = '30px';
        toggleButton.classList.remove('at-footer');
      }
    }

    // Add scroll listener for button positioning
    let scrollTimeout;
    window.addEventListener('scroll', function() {
      clearTimeout(scrollTimeout);
      scrollTimeout = setTimeout(handleButtonPosition, 10);
    });

    // Initial position check
    handleButtonPosition();

    // Add click event to button
    toggleButton.addEventListener('click', toggleLists);

    // Optional: Keyboard shortcut (Alt + L)
    document.addEventListener('keydown', function(e) {
      if (e.altKey && e.key === 'l') {
        e.preventDefault();
        toggleLists();
      }
    });

    // Handle resize events
    window.addEventListener('resize', handleButtonPosition);
  });
})();
</script>

## Example

<div class="sortable-list">
  <ul>
    <li><strong><a href="https://starikov.co/about/">⭐ About</a></strong></li>
    <li><strong><a href="https://starikov.co/elsewhere/">🔗 Elsewhere</a></strong></li>
    <li><strong><a href="https://starikov.co/contact/">💬 Contact</a></strong></li>
    <li><strong><a href="https://starikov.co/citations/">🔖 Citations</a></strong></li>
    <li><strong><a href="https://starikov.co/resume/">🎓 Resume</a></strong></li>
    <li><strong><a href="https://starikov.co/milestones/">🏆 Milestones</a></strong></li>
    <li><strong><a href="https://starikov.co/balance/">⚖️ Work/Life Balance</a></strong></li>
    <li><strong><a href="https://starikov.co/feedback/">📝 Feedback</a></strong></li>
  </ul>
</div>
