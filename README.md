# scanParser
### Concept
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
 - Remove need for .xml extension for input
 - Increase parsing data points

### Introduction
scanParser uses SQLite3 and lxml to take a given scan XML, and convert it to something more quantifiable when performing research on large sets of scan data.  In addition to its visualization techniques, it also has a prettifier function that takes XMLs and makes them way more readable than the raw output typically found.  This helps when it comes to writing a parser for an unknown or untried combination on a scan.

#### Visualization performed on an xml
```
./scanParser -v <your-scan.xml>
```
Visualization creates the following SQL:
  - `by_addr`
    - Group the results by IP address, GROUP_CONCAT and DISTINCT everything else
  - `by_port`
    - Group the results by port, GROUP_CONCAT and DISTINCT everything else
  - `by_svc`
    - Group the results by service, GROUP_CONCAT and DISTINCT everything else
  - `ip_list`
    - IP/Port results
  - `svc_list`
    - nmap-services data points

Visualization creates the following html pages:
  - byAddr
    - `by_addr` in a GUI layout
  - byPort
    - `by_port` in a GUI layout
  - bySvc
    - `by_svc` in a GUI layout

#### Prettify an unknown XML
```
./scanParser -p <your-scan.xml>
```
Remove extra tabs and empty lines.  Tab out the XML to where children are 4 spaces to the right of their parent and on the next line.
