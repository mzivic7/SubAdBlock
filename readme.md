# SubAdBlock
Adblocker for movie subtitles.
## Usage
Place "main.py" and "config.conf" in directory with subtitles and run "main.py". 
It will automatically open all subtitles and delete all lines containing keywords that are set in "config.conf".

Open "config.conf" in text editor to configure settings.
Only first 4 lines are used for config:
 - First line: Encoding type
 - Second line: Also delete lines bellow one where is detected keyword (True/False)
 - Third line: File extensions whitelist
 - Fourth line: Keywords to detect in subtitle lines

File extensions and keywords must be separated with comma and space: ", "

Set first line to "auto" to try auto-detect encoding type. If it fails, try to manually set encoding type.
See [encoding list](encoding.md).

## Building:
1. Install pyinstaller python module: `pip install pyinstaller`
2. Run: `pyinstaller -yFcn "SubAdBlock" "main.py"`
3. Built aplication is located in "dist" directory.
4. To use it just place it with "config.conf" file in directory with subtitles and run executable.
