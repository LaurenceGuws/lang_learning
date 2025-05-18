import marshmallow as ma
import sys
import flask.views

def apply_patch():
    """
    Apply patches to fix compatibility issues between libraries.
    """
    # Fix marshmallow __version__ attribute
    if not hasattr(ma, '__version__'):
        # Add __version__ attribute to marshmallow module
        # Using the actual version from marshmallow.__version_info__
        if hasattr(ma, '__version_info__'):
            version_info = ma.__version_info__
            ma.__version__ = '.'.join(str(x) for x in version_info)
        else:
            # Fallback to a safe version if __version_info__ is not available
            ma.__version__ = '3.19.0'
        
        print(f"Applied marshmallow version patch: {ma.__version__}")
    
    # Fix flask.views.MethodViewType issue
    if not hasattr(flask.views, 'MethodViewType'):
        # In newer Flask versions, MethodView is a class, not a metaclass
        # Let's create a compatible MethodViewType
        flask.views.MethodViewType = type(flask.views.MethodView)
        print("Applied Flask MethodViewType patch") 