from pandocfilters import toJSONFilter, attributes, Math, Span, RawInline, RawBlock
from environment_list import environments

blatex = lambda x: RawBlock('latex', x)
ilatex = lambda x: RawInline('latex', x)
imath = lambda x: Math({'t': 'InlineMath'}, x)
answer = lambda x, c: [ilatex('\\answer[{}]{{'.format(c))] + x + [ilatex('}')]

envcount = 1
first_env = True

def environment(ident, env, keyvals, contents, count):
    data = environments[env]
    title = '{}: {}'.format(data['title'], keyvals['t'] if 't' in keyvals else '')
    pause = '\\onslide<{}->{{'.format(count)
    begin = '\\begin{{{0}}}{{{1}\ {2}}}'.format(data['env'], data['prefix'], title)
    end = '\\end{{{0}}}}}'.format(data['env'])
    return [blatex(pause + begin)] + contents + [blatex(end)]

def main(key, value, fmt, meta):
    global envcount, first_env, environments
    if key == 'Span':
        [[ident, classes, keyvals], contents] = value
        if 'gap' in classes:
            return ilatex('\\vspace{' + contents[0]['c'] + '}')
        elif 'answer' in classes and 'fmt' == 'beamer':
            envcount += 1
            return answer(contents, envcount)
    if key == 'Header' and value[0] == 1:
        envcount = 1
        first_env = True
    if key == 'Div':
        [[ident, classes, keyvals], contents] = value
        keyvals = dict(keyvals)
        if len(set(classes) & set(environments.keys())) > 0:
            if not first_env and not 'show' in keyvals:
                envcount += 1
            first_env = False
            count = keyvals['show'] if 'show' in keyvals else envcount
            return environment(ident, classes[0], dict(keyvals), contents, count)

if __name__ == '__main__':
    toJSONFilter(main)
