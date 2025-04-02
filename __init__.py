import os
import webbrowser
from .node_proc import *
from .profiles_list import *
from .proc_snip_insert import *
from cudatext import *
import cudax_lib as appx

fn_script = os.path.join(os.path.dirname(__file__), 'runner.js')
fn_ini = os.path.join(app_path(APP_DIR_SETTINGS), 'cuda_emmet.ini')
ini_section = 'setup'
ini_key_profile = 'profile'
text_quote = '%Q%'

lexers_xml = ['XML', 'XSL', 'XSLT']
lexers_css = ['CSS', 'SCSS', 'SASS', 'Sass', 'Stylus', 'LESS']

HELP_URL = 'http://docs.emmet.io/cheat-sheet/'

def get_syntax():
    lexer = ed.get_prop(PROP_LEXER_CARET)
    if lexer in lexers_xml:
        return 'xsl'
    elif lexer in lexers_css:
        return 'css'
    else:
        return 'html'

def get_profile():
    return ini_read(fn_ini, ini_section, ini_key_profile, profiles[0])


def do_find_expand():
    x, y, x1, y1 = ed.get_carets()[0]
    text = ed.get_text_line(y)
    if not text: return
    text = text[:x]
    if not text: return

    try:
        return run_node('', [fn_script, 'find_expand', text, get_syntax(), get_profile() ])
    except Exception as e:
        msg_box(str(e), MB_OK+MB_ICONERROR)
        return


def do_insert_result(x0, y0, x1, y1, text, text_insert):
    if text_insert:
        for i in [1,2,3,4,5,6,7,8,9,0]:
            text_rep = '${'+str(i)+'}'
            if text_rep in text:
                text = text.replace(text_rep, '${'+str(i)+':'+text_insert+'}', 1)
                break

    ed.delete(x0, y0, x1, y1)
    ed.set_caret(x0, y0)

    lines = text.splitlines()
    insert_snip_into_editor(ed, lines)


def do_expand_abbrev(text_ab):
    msg_status('Expanding: %s (profile %s)' % (text_ab, get_profile()))

    try:
        text = run_node('', [fn_script, 'expand', text_ab, get_syntax(), get_profile() ])
    except Exception as e:
        msg_box(str(e), MB_OK+MB_ICONERROR)
        return

    if not text or text=='?':
        msg_status('Cannot expand Emmet abbreviation: '+text_ab)
        return

    return text


class Command:
    def profiles(self):
        n = dlg_menu(DMENU_LIST, profiles, caption='Profiles')
        if n is None: return
        item = profiles[n]
        ini_write(fn_ini, ini_section, ini_key_profile, item)

    def help(self):
        appx.safe_open_url(HELP_URL)
        msg_status('Opened browser')

    def wrap_abbrev(self):
        x0, y0, x1, y1 = ed.get_carets()[0]
        #sort coords
        if (y1>y0) or ((y1==y0) and (x1>x0)):
            pass
        else:
            x0, y0, x1, y1 = x1, y1, x0, y0

        text_sel = ed.get_text_sel()
        if not text_sel:
            msg_status('Text not selected')
            return

        text_ab = dlg_input('Emmet abbreviation:', 'div')
        if not text_ab:
            return

        text = do_expand_abbrev(text_ab)
        if not text: return

        do_insert_result(x0, y0, x1, y1, text, text_sel)


    def expand_abbrev(self):
        text = do_find_expand()
        if not text or ';' not in text:
            msg_status('Cannot find Emmet abbreviation')
            return

        slen, text = text.split(';', maxsplit=2)
        nlen = int(slen)
        x0, y0, x1, y1 = ed.get_carets()[0]
        xstart = max(0, x0-nlen)

        do_insert_result(xstart, y0, x0, y0, text, '')
