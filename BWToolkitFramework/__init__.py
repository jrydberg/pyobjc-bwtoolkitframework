'''
Python mapping for the BWToolkit framework.
'''

import objc as _objc

__bundle__ = _objc.initFrameworkWrapper("BWToolkitFramework",
    frameworkIdentifier="com.brandonwalkin.BWToolkitFramework",
    frameworkPath=_objc.pathForFramework(
        "/System/Library/Frameworks/BWToolkitFramework.framework"),
    globals=globals())
