# YourTube History
> Like and subscribe to find out what you've subscribed to!

yourtube_history.md

## What This Tool Does

This parser processes your YouTube watch history to reveal:
- Your most-watched videos with play counts
- Favorite channels based on total views
- Viewing statistics (total videos watched, daily average, estimated hours)
- Peak viewing hours
- Date range of your watch history

## Requirements

- A web browser (Chrome, Firefox, Safari, or Edge)
- Your YouTube watch history file from Google Takeout

## Getting Your YouTube History

### Step 1: Access Google Takeout
1. Go to [`https://takeout.google.com`](https://takeout.google.com)
2. Sign in to your Google account if not already signed in

### Step 2: Select YouTube Data
1. Scroll down and find "YouTube and YouTube Music"
2. Check the box next to it (if not already selected)
3. Click "All YouTube data included" to customize
4. Ensure "history" is selected
5. Click "OK"

### Step 3: Configure Export
1. Click "Next step"
2. Choose delivery method: "Send download link via email"
3. Choose frequency: "Export once"
4. Choose file type: ".zip"
5. Choose file size: 2 GB should be sufficient
6. Click "Create export"

### Step 4: Download Your Data
1. Wait for an email from Google (may take minutes to hours)
2. Click the download link in the email
3. Extract the ZIP file
4. Navigate to: `Takeout/YouTube and YouTube Music/history/`
5. Locate the file named `watch-history.html`

## Using the Parser

### Step 1: Upload Your File
1. Open the YouTube History Parser webpage
2. Click the upload area or drag your `watch-history.html` file onto it
3. The file will be validated automatically

### Step 2: Configure Analysis Parameters
- **Number of Top Videos**: How many videos to display (default: 100)
- **Minimum Play Count**: Filter out videos watched fewer times
- **Date Range**: Analyze specific time periods (optional)
- **Channel Filter**: Search for specific channels
- **Sort By**: Choose ordering method
- **Exclude YouTube Music**: Toggle to filter out music content

### Step 3: Analyze
1. Click "Analyze History"
2. Wait for processing to complete
3. Review your statistics and top videos

### Step 4: Export Results (Optional)
- **Export CSV**: Download spreadsheet-compatible file
- **Export JSON**: Download structured data file

## Understanding Your Results

### Statistics Section
- **Data Period**: Date range of your watch history
- **Total Watch Events**: Number of times you've watched any video
- **Unique Videos**: Different videos you've watched
- **Unique Channels**: Different channels you've watched
- **Estimated Hours**: Rough viewing time (assumes 10-minute average)
- **Daily Average**: Videos watched per day
- **Favorite Channel**: Most-watched channel by play count
- **Most Rewatched**: Single video with highest play count
- **Peak Viewing Hour**: When you watch most videos

### Top Videos Table
- **Rank**: Position by play count
- **Video Title**: Name of the video with link
- **Channel**: Creator's channel name
- **Plays**: Number of times watched
- **First Watched**: Earliest viewing date

## Privacy Notice

All processing occurs locally in your browser. Your watch history file never leaves your device. No data is uploaded to any server.

## Troubleshooting

### File Won't Upload
- Ensure file is named `watch-history.html` or has `.html` extension
- Verify file is from Google Takeout YouTube export
- Check file isn't corrupted (should open in browser)

### No Data Showing
- Confirm you selected the correct date range
- Check minimum play count isn't too high
- Verify YouTube history was included in your Takeout export

### Missing Videos
- Some deleted videos may not display properly
- YouTube Music content is excluded by default (toggle setting to include)
- Very old entries might have incomplete data

## Tips

- Use the search box to find specific videos or channels
- Click column headers to sort differently
- Adjust date filters to analyze specific periods
- Export data for further analysis in spreadsheet software
