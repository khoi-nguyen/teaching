from pandocfilters import toJSONFilter, attributes, Math, Span, RawInline, RawBlock, Div
from environment_list import environments
import re

blatex = lambda x: RawBlock('latex', x)
bhtml = lambda x: RawBlock('html', x)
ilatex = lambda x: RawInline('latex', x)
imath = lambda x: Math({'t': 'InlineMath'}, x)
answer = lambda x, c: [ilatex('\\answer[{}]{{'.format(c))] + x + [ilatex('}')]

envcount = 1
first_env = True

def add_transition(m):
    global envcount
    envcount += 1
    return f"\\onslide<{envcount}->{{{m.group(1)}}}"

def environment(ident, classes, keyvals, contents, count):
    env = list(set(classes) & set(environments.keys()))
    env = env[0]
    classes.remove(env)
    data = environments[env]
    title = '{}: {}'.format(data['title'], keyvals['t'] if 't' in keyvals else '')
    pause = '\\onslide<{}->{{'.format(count)
    begin = f"\\begin{{colorenv}}[{data['bgcolor']}]{{{data['tcolor']}}}"
    begin += f"{{{data['prefix']}\  {data['title']}}}{{{keyvals['t'] if 't' in keyvals else ''}}}"
    end = '\\end{colorenv}}'
    keyvals = [[k, v] for k, v in keyvals.items()]
    return [blatex(pause + begin)] + [Div([ident, classes, keyvals], contents)] + [blatex(end)]

def main(key, value, fmt, meta):
    global envcount, first_env, environments
    if key == 'Span':
        [[ident, classes, keyvals], contents] = value
        if 'gap' in classes:
            return ilatex('\\vspace{' + contents[0]['c'] + '}')
        elif 'answer' in classes and fmt == 'beamer':
            envcount += 1
            return answer(contents, envcount)
    elif key == 'Header' and value[0] == 1:
        envcount = 1
        first_env = True
    elif key == 'Div':
        [[ident, classes, keyvals], contents] = value
        keyvals = dict(keyvals)
        if len(set(classes) & set(environments.keys())) > 0:
            if fmt == 'revealjs':
                return [bhtml(f'<div><h4>{environments[classes[0]]["title"]}</h4>')] + contents + [bhtml('</div>')]
            if not first_env and not 'show' in keyvals:
                envcount += 1
            first_env = False
            count = keyvals['show'] if 'show' in keyvals else envcount
            return environment(ident, classes, keyvals, contents, count)
    elif key == 'RawBlock' and value[0] == 'latex':
        [fmt, code] = value
        regex = re.compile(r'(\\plotfunction.*|\\draw.*\\draw.*)$', re.MULTILINE)
        code = re.sub(regex, add_transition, code)
        return RawBlock(fmt, code)

if __name__ == '__main__':
    toJSONFilter(main)
