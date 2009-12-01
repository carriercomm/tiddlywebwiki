"""
A TiddlyWeb plugin providing a multi-user TiddlyWiki environment.
"""

__version__ = '0.14.0'


def init(config):
    # These imports must be in init otherwise getting
    # the version number causes cyclic imports to happen.
    import tiddlywebwiki.manage
    from tiddlyweb.config import merge_config
    from tiddlywebwiki.config import config as twwconfig
    merge_config(config, twwconfig)
    tiddlywebwiki.manage.init(config)
    # XXX and add selector for POST a wiki
