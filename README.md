# scanParser
- Useful for visualizing port scans
- Creates statistics based off service --> port commonalities
  - Uses browser for GUI visualization
  - Uses SQL for text visualization

### Summary
 - Parse and sort the XML results given from masscan or nmap
   - GUI visualization provided by Plotly Bubble chart
    - Bubble charts are the default right now
   - SQL visualization provided by sqlite3
 - Visualize the data in interesting ways as to find quirks and commonalities
 - Uses the services list from Nmap for visualization points
 - Expandable to use other datasets as well
 - Interchangable with Python3 || Python2

### Future plans
 - Increase parsing data points
