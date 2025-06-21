# wordle_solver
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wordle Helper - Injectable</title>
    <style>
        /* Basic structural styles - can be overridden by host page */
        /* It's generally better to let the host page control all styling */
        .wordle-helper-container {
            margin: 20px auto; /* Example margin */
            padding: 20px;
            max-width: 600px; /* Example max-width */
            /* Consider adding a border or background if your site doesn't provide one for embedded content */
            /* border: 1px solid #ccc; */
            /* background-color: #f9f9f9; */
        }
        .wordle-letter-inputs-container {
            display: flex;
            justify-content: center;
            margin-bottom: 10px;
        }
        .wordle-letter-input {
            width: 40px; /* Basic width */
            height: 40px; /* Basic height */
            text-align: center;
            font-size: 1.2em; /* Relative font size */
            margin: 0 3px; /* Spacing between inputs */
            text-transform: uppercase;
            border: 1px solid #ccc; /* Basic border */
            border-radius: 4px; /* Basic rounded corners */
        }
        .wordle-input-group {
            margin-bottom: 15px;
        }
        .wordle-input-group label {
            display: block;
            margin-bottom: 5px;
        }
        .wordle-input-group input[type="text"] {
            width: 100%;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box; /* Important for width: 100% */
        }
        .wordle-button {
            padding: 10px 15px;
            /* Add your site's button styling or leave it to inherit */
            /* background-color: #007bff; */
            /* color: white; */
            border: 1px solid #ccc;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
            margin-top: 10px;
        }
        .wordle-result-area {
            margin-top: 20px;
            text-align: center;
        }
        .wordle-suggested-word {
            font-size: 1.5em; /* Larger font for the word */
            font-weight: bold;
            min-height: 1.5em; /* Prevent layout shift */
        }
        .wordle-message-box {
            /* This will be harder to style universally without fixed positioning */
            /* Consider integrating messages more directly into the flow or using browser alerts if appropriate for your site */
            padding: 10px;
            margin: 10px 0;
            border-radius: 4px;
            text-align: center;
            display: none; /* Hidden by default */
        }
        .wordle-message-box.success {
            background-color: #e6ffed;
            color: #006622;
            border: 1px solid #c3e6cb;
        }
        .wordle-message-box.error {
            background-color: #ffe6e6;
            color: #cc0000;
            border: 1px solid #f5c6cb;
        }
        .wordle-message-box.info {
            background-color: #e6f7ff;
            color: #005c99;
            border: 1px solid #b8daff;
        }
        .wordle-footer-text {
            margin-top: 20px;
            text-align: center;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div id="wordleMessageBox" class="wordle-message-box">
        <span id="wordleMessageText"></span>
        <button onclick="hideWordleMessage()" style="margin-left: 15px; background: none; border: none; font-weight: bold; cursor: pointer;">&times;</button>
    </div>

    <div class="wordle-helper-container">
        <h1>Wordle Helper</h1>

        <div class="wordle-input-group">
            <label>Known Letters (Greens):</label>
            <div id="letter-inputs-container" class="wordle-letter-inputs-container">
                </div>
            <p style="font-size: 0.8em; text-align: center;">Enter letters in their correct positions. Leave blank if unknown.</p>
        </div>

        <div style="display: grid; grid-template-columns: 1fr; gap: 10px;">
            <div class="wordle-input-group">
                <label for="yellow-letters">Yellow Letters (present, wrong spot):</label>
                <input type="text" id="yellow-letters" placeholder="e.g., TRA">
                <p style="font-size: 0.8em;">Letters in word, but not in green spots. No spaces.</p>
            </div>
            <div class="wordle-input-group">
                <label for="gray-letters">Gray Letters (not in word):</label>
                <input type="text" id="gray-letters" placeholder="e.g., XYZEI">
                <p style="font-size: 0.8em;">Letters confirmed absent. No spaces.</p>
            </div>
        </div>
        
        <button id="find-word-btn" class="wordle-button">
            Find Best Word
        </button>

        <div id="result-area" class="wordle-result-area">
            <p>Suggested Word:</p>
            <p id="suggested-word" class="wordle-suggested-word">&nbsp;</p>
        </div>
    </div>

    <footer class="wordle-footer-text">
        <p>Enter green, yellow, and gray letters to get a strategic suggestion. The internal word list is curated; more extensive lists might yield different results.</p>
    </footer>

    <script>
        // Word list (curated for common 5-letter English words)
        const wordList = [
            "ABOUT", "ALERT", "ARGUE", "BEACH", "BRAIN", "BREAD", "BRING", "BROWN", "BUILD", "CHAIR", 
            "CHANT", "CHARM", "CLEAN", "CLEAR", "CLOCK", "CLOUD", "COAST", "COULD", "COUNT", "CRANE", 
            "CREAM", "DANCE", "DEATH", "DREAM", "DRINK", "DRIVE", "EARLY", "EARTH", "ENJOY", "EQUAL", 
            "EVERY", "EXACT", "FAITH", "FIGHT", "FINAL", "FIRST", "FLAME", "FLOOR", "FOCUS", "FORCE", 
            "FORTH", "FOUND", "FRAME", "FRESH", "FRONT", "FRUIT", "GHOST", "GIANT", "GLASS", "GRACE", 
            "GRADE", "GRAND", "GRASS", "GREAT", "GREEN", "GROUP", "GUARD", "GUESS", "GUIDE", "HEART", 
            "HEAVY", "HORSE", "HOTEL", "HOUSE", "HUMAN", "IDEAL", "IMAGE", "INPUT", "ISSUE", "JUICE", 
            "LARGE", "LAUGH", "LEARN", "LEAST", "LEAVE", "LEGAL", "LEVEL", "LIGHT", "LOCAL", "LOGIN",
            "LUCKY", "LUNCH", "MAGIC", "MAJOR", "MARCH", "MATCH", "METAL", "MODEL", "MONEY", "MONTH", 
            "MORAL", "MORPH", "MOUSE", "MOUTH", "MUSIC", "NEVER", "NIGHT", "NOBLE", "NOISE", "NORTH", 
            "NOVEL", "NURSE", "OCEAN", "OFFER", "OFTEN", "ORDER", "OTHER", "OUGHT", "PAINT", "PANIC",
            "PAPER", "PARTY", "PEACE", "PHONE", "PHOTO", "PIECE", "PILOT", "PLACE", "PLAIN", "PLANE", 
            "PLANT", "PLATE", "POINT", "POUND", "POWER", "PRESS", "PRICE", "PRIDE", "PRIME", "PRINT", 
            "PRIOR", "PRIZE", "PROOF", "PROUD", "QUIET", "QUITE", "RADIO", "RAISE", "RANGE", "RAPID", 
            "RATIO", "REACH", "REACT", "READY", "REALM", "RELAX", "REPLY", "RIGHT", "RIVER", "ROUND", 
            "ROUTE", "ROYAL", "RURAL", "SCALE", "SCARE", "SCOPE", "SCORE", "SENSE", "SERVE", "SHADE", 
            "SHAKE", "SHALL", "SHAPE", "SHARE", "SHARK", "SHARP", "SHEET", "SHELF", "SHIFT", "SHINE", 
            "SHIRT", "SHOCK", "SHOOT", "SHORT", "SHOWS", "SIGHT", "SILK", "SINCE", "SKILL", "SLEEP", 
            "SLICE", "SLIDE", "SLOPE", "SMALL", "SMART", "SMILE", "SMOKE", "SOLID", "SOLVE", "SOUND", 
            "SOUTH", "SPACE", "SPARE", "SPEAK", "SPEED", "SPEND", "SPICY", "SPIKE", "SPLIT", "SPORT", 
            "SQUAD", "SQUARE", "STACK", "STAFF", "STAGE", "STAND", "STARE", "START", "STATE", "STAY", 
            "STEAM", "STEEL", "STICK", "STILL", "STOCK", "STONE", "STORE", "STORM", "STORY", "STUDY", 
            "STUFF", "STYLE", "SUGAR", "SUITE", "SUPER", "SWEET", "TABLE", "TASTE", "TEACH", "THANK", 
            "THEIR", "THEME", "THERE", "THESE", "THING", "THINK", "THIRD", "THREE", "THROW", "TIDAL",
            "TIGER", "TIMER", "TIMES", "TIRED", "TITLE", "TODAY", "TONES", "TOPIC", "TOTAL", "TOUCH", 
            "TOUGH", "TRACE", "TRACK", "TRADE", "TRAIL", "TRAIN", "TRASH", "TREAT", "TREND", "TRIAL", 
            "TRIBE", "TRICK", "TRUCK", "TRULY", "TRUST", "TRUTH", "TWICE", "UNCLE", "UNDER", "UNION", 
            "UNIQUE", "UNITY", "UNTIL", "UPPER", "UPSET", "URBAN", "USAGE", "USUAL", "VALID", "VALUE", 
            "VIDEO", "VIRUS", "VISIT", "VITAL", "VOICE", "VOTED", "WASTE", "WATCH", "WATER", "WEARY",
            "WEIGH", "WHEAT", "WHEEL", "WHERE", "WHICH", "WHILE", "WHITE", "WHOLE", "WHOSE", "WOMAN", 
            "WORLD", "WORRY", "WORSE", "WOULD", "WRITE", "WRONG", "YACHT", "YIELD", "YOUNG", "YOUTH"
        ];
        const ALL_POSSIBLE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        // --- Message Box Logic ---
        // Renamed IDs to be more specific to this tool to avoid conflicts
        function showWordleMessage(text, type = 'info', duration = 3000) {
            const messageBox = document.getElementById('wordleMessageBox');
            const messageText = document.getElementById('wordleMessageText');
            
            if (!messageBox || !messageText) return; // Guard against missing elements

            messageText.textContent = text;
            messageBox.className = 'wordle-message-box'; // Reset classes
            messageBox.classList.add(type); 
            messageBox.style.display = 'block';

            if (duration) {
                setTimeout(() => {
                    hideWordleMessage();
                }, duration);
            }
        }

        function hideWordleMessage() {
            const messageBox = document.getElementById('wordleMessageBox');
            if (messageBox) {
                messageBox.style.display = 'none';
            }
        }

        // --- Letter Input Logic (for Green letters) ---
        const letterInputsContainer = document.getElementById('letter-inputs-container');
        const numInputs = 5;
        const letterInputs = [];

        if (letterInputsContainer) { // Check if container exists before trying to populate
            for (let i = 0; i < numInputs; i++) {
                const input = document.createElement('input');
                input.type = 'text';
                input.maxLength = 1;
                // Add a general class for styling via host CSS if needed
                input.classList.add('wordle-letter-input'); 
                input.dataset.index = i;

                input.addEventListener('input', (e) => {
                    e.target.value = e.target.value.toUpperCase().replace(/[^A-Z]/g, '');
                    const nextInput = letterInputs[i + 1];
                    if (e.target.value && nextInput) {
                        nextInput.focus();
                    }
                });

                input.addEventListener('keydown', (e) => {
                    if (e.key === 'Backspace' && !e.target.value) {
                        const prevInput = letterInputs[i - 1];
                        if (prevInput) {
                            prevInput.focus();
                        }
                    } else if (e.key.length === 1 && e.key.match(/[a-z]/i)) {
                        if (e.target.value) { 
                             e.target.value = ''; 
                        }
                    } else if (e.key === 'ArrowLeft') {
                        const prevInput = letterInputs[i - 1];
                        if (prevInput) prevInput.focus();
                    } else if (e.key === 'ArrowRight') {
                        const nextInput = letterInputs[i + 1];
                        if (nextInput) nextInput.focus();
                    }
                });
                letterInputs.push(input);
                letterInputsContainer.appendChild(input);
            }
        }


        // --- Word Finding Logic ---
        const findWordBtn = document.getElementById('find-word-btn');
        const suggestedWordEl = document.getElementById('suggested-word');
        const yellowLettersInput = document.getElementById('yellow-letters');
        const grayLettersInput = document.getElementById('gray-letters');

        if (findWordBtn) { // Check if button exists
            findWordBtn.addEventListener('click', () => {
                // Ensure elements exist before trying to access their values
                if (!suggestedWordEl || !yellowLettersInput || !grayLettersInput || letterInputs.length !== 5) {
                    console.error("Wordle Helper: Missing critical HTML elements.");
                    showWordleMessage("Initialization error. Required elements missing.", "error");
                    return;
                }

                const greenPatternArray = letterInputs.map(input => input.value.toUpperCase());
                
                const yellowLettersRaw = yellowLettersInput.value.toUpperCase().replace(/[^A-Z]/g, '');
                const grayLettersRaw = grayLettersInput.value.toUpperCase().replace(/[^A-Z]/g, '');

                yellowLettersInput.value = yellowLettersRaw; // Update input with sanitized value
                grayLettersInput.value = grayLettersRaw;   // Update input with sanitized value

                const yellowLettersSet = new Set(yellowLettersRaw.split(''));
                const grayLettersSet = new Set(grayLettersRaw.split(''));

                if (greenPatternArray.some(l => l.length > 1)) { // Check each green letter input
                     showWordleMessage("Green letter inputs can only be one letter.", "error"); return;
                }
                for (const letter of yellowLettersSet) {
                    if (grayLettersSet.has(letter)) {
                        showWordleMessage(`Letter '${letter}' cannot be both yellow and gray.`, "error");
                        suggestedWordEl.textContent = "-";
                        return;
                    }
                }
                for (const letter of greenPatternArray) {
                    if (letter && grayLettersSet.has(letter)) {
                         showWordleMessage(`Letter '${letter}' cannot be both green and gray.`, "error");
                         suggestedWordEl.textContent = "-";
                         return;
                    }
                }

                let bestWord = findBestWord(greenPatternArray, yellowLettersSet, grayLettersSet);

                if (bestWord) {
                    suggestedWordEl.textContent = bestWord;
                    showWordleMessage(`Suggested word: ${bestWord}`, "success");
                } else {
                    suggestedWordEl.textContent = "No match";
                    showWordleMessage("No matching words found with the given criteria. Try broadening your letter inputs.", "info", 5000);
                }
            });
        }


        function findBestWord(greenPatternArray, yellowLettersSet, grayLettersSet) {
            const candidateWords = [];

            for (const word of wordList) { 
                let isPossible = true;

                for (let char of word) {
                    if (grayLettersSet.has(char)) {
                        isPossible = false;
                        break;
                    }
                }
                if (!isPossible) continue;

                for (let i = 0; i < 5; i++) {
                    const greenChar = greenPatternArray[i];
                    if (greenChar !== '' && greenChar !== word[i]) {
                        isPossible = false;
                        break;
                    }
                }
                if (!isPossible) continue;

                for (const yellowChar of yellowLettersSet) {
                    if (!word.includes(yellowChar)) {
                        isPossible = false;
                        break;
                    }
                }
                if (!isPossible) continue;
                
                // Yellow letter cannot be in a position where it was *already tried* and was yellow.
                // The current UI doesn't explicitly track "tried positions for yellow letters".
                // However, we must ensure a yellow letter is NOT in a green position if that green position is for a DIFFERENT letter.
                // And a yellow letter also cannot be in its own position if that position is marked green (it would then be green, not yellow).
                for (let i = 0; i < 5; i++) {
                    // If the current position in the word (word[i]) is a yellow letter,
                    // AND that position is marked as green (greenPatternArray[i] !== ''),
                    // AND the green letter is DIFFERENT from the yellow letter at word[i], then it's impossible.
                    if (yellowLettersSet.has(word[i]) && greenPatternArray[i] !== '' && greenPatternArray[i] !== word[i]) {
                        isPossible = false;
                        break;
                    }
                    // Additionally, if a letter is yellow, it cannot be in the *same position* as itself if that position is *not* green.
                    // This is tricky. Wordle tells you 'A' is yellow if you guess 'APPLE' and 'A' is in the word but not at pos 0.
                    // If you then guess 'TRAIL' and 'A' is yellow again (not at pos 2),
                    // the helper shouldn't suggest 'A' at pos 0 or pos 2 for yellow 'A'.
                    // The current UI doesn't capture this "tried yellow positions" info.
                    // The existing logic: "yellow letter must be in the word" and "not in a conflicting green spot" is the main filter here.
                }
                if (!isPossible) continue;
                
                candidateWords.push(word);
            }

            if (candidateWords.length === 0) {
                return null;
            }

            const scoredCandidates = [];
            const lettersForDiscovery = new Set(ALL_POSSIBLE_LETTERS.split(''));
            grayLettersSet.forEach(l => lettersForDiscovery.delete(l));
            greenPatternArray.forEach(l => { if (l) lettersForDiscovery.delete(l); });
            yellowLettersSet.forEach(l => lettersForDiscovery.delete(l));


            for (const word of candidateWords) {
                const distinctLettersInWordForDiscovery = new Set();
                for (const char of word) {
                    if (lettersForDiscovery.has(char)) {
                        distinctLettersInWordForDiscovery.add(char);
                    }
                }
                const discoveryScore = distinctLettersInWordForDiscovery.size;
                const uniqueOverallScore = new Set(word).size;

                scoredCandidates.push({ 
                    word: word, 
                    discoveryScore: discoveryScore, 
                    uniqueOverallScore: uniqueOverallScore 
                });
            }
            
            scoredCandidates.sort((a, b) => {
                if (b.discoveryScore !== a.discoveryScore) {
                    return b.discoveryScore - a.discoveryScore;
                }
                if (b.uniqueOverallScore !== a.uniqueOverallScore) {
                    return b.uniqueOverallScore - a.uniqueOverallScore;
                }
                return a.word.localeCompare(b.word); 
            });
            
            return scoredCandidates.length > 0 ? scoredCandidates[0].word : null;
        }

        // Initial call to ensure elements are available or to set up if loaded dynamically
        // document.addEventListener('DOMContentLoaded', () => { /* any setup if needed */ });
    </script>
</body>
</html>
