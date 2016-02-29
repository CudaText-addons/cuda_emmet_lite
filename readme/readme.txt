Emmet Lite plugin for CudaText.
See www.emmet.io for info.

Plugin gives 2 basic commands: "expand abbreviation", "wrap with abbreviation".
Uses WindowsScriptHost, so don't work on Linux.


Emmet profile can be changed using menu. Supported:
 - html    - default output profile. 
 - xhtml   - the same as "html", but outputs empty elements with closed slash: <br />. 
 - xml     - default for XML and XSL syntaxes: outputs each tag on a new line with indentation, empty elements are outputted with closing slash: <br/>. 
 - xml_zen - the same as "xml", but outputs leaf tags (i.e. tags without nested tags) with additional newline (e.g. <td> is leaf tag in table>tr>td). 
 - line    - used to output expanded abbreviation without any indentation and newlines. 
 - plain   - the same as "line", but doesn't move caret. 

Emmet syntax detected automatically:
for lexers CSS/LESS/SCSS/SASS/Stylus it's "css"; 
for lexers XML/XSLT it's "xsl"; 
for others it's "html".

Author: Alexey (CudaText)
License: MIT
