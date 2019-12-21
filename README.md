# safelinks
 
***Yet Another Microsoft ATP Safe Link decoder/descrambler/deobfuscator***


Why write one?  
I needed something which would accept multiple URL's through copy/paste as simple as possible

The program accepts one SafeLink URL as argument,  
or multiple URLs via STDIN; so the following works:

`./safelinks.py https://atp-safelink-url`  
`./safelinks.py < file-with-atp-safelinks.txt`  
`cat file-with-atp-safelinks.txt | ./safelinks.py`

or copy/paste from commandline and end with CTRL-D  
`cat | ./safelinks.py`
