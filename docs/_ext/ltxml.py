from docutils import nodes
from sphinx import addnodes


def parse_nodevar(env, sig, signode):
    nodevar, t, default = sig.split(" ", 2)
    nodevar = nodevar.strip()
    if nodevar.startswith('[') and nodevar.endswith(']'):
        nodevar = nodevar.strip('[]')
        optional = True
    else:
        optional = False
    t = "类型: %s" % t.strip(" <>").lower()
    d = "%s" % default.strip(" ()")

    signode += addnodes.desc_name(nodevar, nodevar)
    signode += nodes.Text(' ')
    signode += addnodes.desc_type(t, t)
    if d:
        signode += nodes.Text(', ')
        default = "默认值: %s" % d
        signode += addnodes.desc_annotation(default, default)
    if optional:
        signode += nodes.Text(', ')
        signode += addnodes.desc_annotation("可选项", "可选项")
    return nodevar + '; ' + env.docname


def setup(app):
    """Sphinx-doc callback."""

    app.add_object_type(
        'nodevar',
        'nodevar',
        objname='variable value',
        indextemplate='triple: %s; node variable value',
        parse_node=parse_nodevar,
    )
