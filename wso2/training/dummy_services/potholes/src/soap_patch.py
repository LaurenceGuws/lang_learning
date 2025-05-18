"""
This module patches the spyne library to fix issues with:
1. six.moves imports
2. cgi module dependency (removed in Python 3.11+)

Apply this patch before importing any spyne modules.
"""

import sys
import six.moves.collections_abc
import importlib.util
import email.parser
import http.cookies
import urllib.parse

# Add the six.moves to sys.modules to make it importable
sys.modules['spyne.util.six.moves'] = six.moves
sys.modules['spyne.util.six.moves.collections_abc'] = six.moves.collections_abc
sys.modules['spyne.util.six.moves.http_cookies'] = http.cookies
sys.modules['spyne.util.six.moves.urllib'] = urllib
sys.modules['spyne.util.six.moves.urllib.parse'] = urllib.parse

# Create a replacement for the cgi module's parse_header function
class CGIReplacement:
    @staticmethod
    def parse_header(line):
        """Parse a Content-type like header.
        
        Return the main content-type and a dictionary of parameters.
        """
        if not line:
            return "", {}
            
        # Use email.parser to parse the header
        parser = email.parser.HeaderParser()
        header = parser.parsestr(f'Content-Type: {line}')
        content_type = header.get_content_type()
        
        # Extract parameters
        params = {}
        for key, value in header.get_params()[1:]:  # Skip the first one, which is the content type
            params[key] = value
            
        return content_type, params

# Create a fake cgi module
cgi_module = type('cgi', (), {'parse_header': CGIReplacement.parse_header})
sys.modules['cgi'] = cgi_module

def apply_patch():
    """Apply the patch to spyne."""
    print("Spyne patch applied for six.moves compatibility and cgi module replacement") 