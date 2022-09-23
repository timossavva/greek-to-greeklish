__all__ = ['toGreeklish']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['toGreeklish'])
@Js
def PyJsHoisted_toGreeklish_(text, this, arguments, var=var):
    var = Scope({'text':text, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'engLetters', 'grLetters', 'stringToSet', 'replacement', 'text', 'greekSet', 'viSet', 'grCaps', 'fixCase', 'expression', 'replacements'])
    @Js
    def PyJsHoisted_fixCase_(text, mirror, this, arguments, var=var):
        var = Scope({'text':text, 'mirror':mirror, 'this':this, 'arguments':arguments}, var)
        var.registers(['text', 'mirror'])
        if var.get('grCaps').get(var.get('mirror').callprop('charAt', Js(0.0))):
            if ((var.get('mirror').get('length')==Js(1.0)) or var.get('grCaps').get(var.get('mirror').callprop('charAt', Js(1.0)))):
                return var.get('text').callprop('toUpperCase')
            else:
                return (var.get('text').callprop('charAt', Js(0.0)).callprop('toUpperCase')+var.get('text').callprop('substr', Js(1.0)))
        else:
            return var.get('text')
    PyJsHoisted_fixCase_.func_name = 'fixCase'
    var.put('fixCase', PyJsHoisted_fixCase_)
    @Js
    def PyJsHoisted_stringToSet_(s, this, arguments, var=var):
        var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
        var.registers(['i', 'o', 's'])
        var.put('o', Js({}))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('s').get('length')):
            try:
                var.get('o').put(var.get('s').callprop('charAt', var.get('i')), Js(1.0))
            finally:
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        return var.get('o')
    PyJsHoisted_stringToSet_.func_name = 'stringToSet'
    var.put('stringToSet', PyJsHoisted_stringToSet_)
    var.put('grCaps', var.get('stringToSet')(Js('ΑΆΒΓΔΕΈΖΗΉΘΙΊΪΚΛΜΝΞΟΌΠΡΣΤΥΎΫΦΧΨΩΏ')))
    var.put('replacements', Js([Js({'greek':Js('αι'),'greeklish':Js('ai')}), Js({'greek':Js('αί'),'greeklish':Js('ai')}), Js({'greek':Js('οι'),'greeklish':Js('oi')}), Js({'greek':Js('οί'),'greeklish':Js('oi')}), Js({'greek':Js('ου'),'greeklish':Js('ou')}), Js({'greek':Js('ού'),'greeklish':Js('ou')}), Js({'greek':Js('ει'),'greeklish':Js('ei')}), Js({'greek':Js('εί'),'greeklish':Js('ei')}), Js({'greek':Js('αυ'),'fivi':Js(1.0)}), Js({'greek':Js('αύ'),'fivi':Js(1.0)}), Js({'greek':Js('ευ'),'fivi':Js(1.0)}), Js({'greek':Js('εύ'),'fivi':Js(1.0)}), Js({'greek':Js('ηυ'),'fivi':Js(1.0)}), Js({'greek':Js('ηύ'),'fivi':Js(1.0)}), Js({'greek':Js('ντ'),'greeklish':Js('nt')}), Js({'greek':Js('μπ'),'bi':Js(1.0)}), Js({'greek':Js('τσ'),'greeklish':Js('ts')}), Js({'greek':Js('τς'),'greeklish':Js('ts')}), Js({'greek':Js('ΤΣ'),'greeklish':Js('ts')}), Js({'greek':Js('τζ'),'greeklish':Js('tz')}), Js({'greek':Js('γγ'),'greeklish':Js('ng')}), Js({'greek':Js('γκ'),'greeklish':Js('gk')}), Js({'greek':Js('θ'),'greeklish':Js('th')}), Js({'greek':Js('χ'),'greeklish':Js('ch')}), Js({'greek':Js('ψ'),'greeklish':Js('ps')})]))
    if var.get('replacements').get((var.get('replacements').get('length')-Js(1.0))).neg():
        var.get('replacements').callprop('pop')
    #for JS loop
    var.put('i', Js(0.0))
    while var.put('replacement', var.get('replacements').get(var.get('i'))):
        try:
            var.get('replacements').put(var.get('replacement').get('greek'), var.get('replacement'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('grLetters', Js('αάβγδεέζηήθιίϊΐκλμνξοόπρσςτυύϋΰφχψωώ'))
    var.put('engLetters', Js('aavgdeezii.iiiiklmnxooprsstyyyyf..oo'))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('grLetters').get('length')):
        try:
            if var.get('replacements').get(var.get('grLetters').callprop('charAt', var.get('i'))).neg():
                var.get('replacements').callprop('push', Js({'greek':var.get('grLetters').callprop('charAt', var.get('i')),'greeklish':var.get('engLetters').callprop('charAt', var.get('i'))}))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('expression', Js([]))
    #for JS loop
    var.put('i', Js(0.0))
    while var.put('replacement', var.get('replacements').get(var.get('i'))):
        try:
            var.get('replacements').put(var.get('replacement').get('greek'), var.get('replacement'))
            var.get('expression').put(var.get('i'), var.get('replacement').get('greek'))
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    var.put('expression', var.get('RegExp').create(var.get('expression').callprop('join', Js('|')), Js('gi')))
    var.put('greekSet', var.get('stringToSet')(var.get('grLetters')))
    var.put('viSet', var.get('stringToSet')(Js('αβγδεζηλιmμνορω')))
    @Js
    def PyJs_anonymous_0_(PyJsArg_2430_, index, this, arguments, var=var):
        var = Scope({'$0':PyJsArg_2430_, 'index':index, 'this':this, 'arguments':arguments}, var)
        var.registers(['c2', 'replacement', '$0', 'c1', 'index', 'bi'])
        var.put('replacement', var.get('replacements').get(var.get('$0').callprop('toLowerCase')))
        if var.get('replacement').get('bi'):
            var.put('bi', (Js('mp') if (var.get('greekSet').get(var.get('text').callprop('charAt', (var.get('index')-Js(1.0))).callprop('toLowerCase')) and var.get('greekSet').get(var.get('text').callprop('charAt', (var.get('index')+Js(2.0))).callprop('toLowerCase'))) else Js('b')))
            return var.get('fixCase')(var.get('bi'), var.get('$0'))
        else:
            if var.get('replacement').get('fivi'):
                var.put('c1', var.get('replacements').get(var.get('$0').callprop('charAt', Js(0.0)).callprop('toLowerCase')).get('greeklish'))
                var.put('c2', (Js('v') if var.get('viSet').get(var.get('text').callprop('charAt', (var.get('index')+Js(2.0))).callprop('toLowerCase')) else Js('f')))
                return var.get('fixCase')((var.get('c1')+var.get('c2')), var.get('$0'))
            else:
                return var.get('fixCase')(var.get('replacement').get('greeklish'), (var.get('$0')+var.get('text').callprop('charAt', (var.get('index')+var.get('$0').get('length')))))
    PyJs_anonymous_0_._set_name('anonymous')
    var.put('text', var.get('text').callprop('replace', var.get('expression'), PyJs_anonymous_0_))
    return var.get('text')
    pass
    pass
PyJsHoisted_toGreeklish_.func_name = 'toGreeklish'
var.put('toGreeklish', PyJsHoisted_toGreeklish_)
pass
pass


# Add lib to the module scope
toGreeklish = var.to_python()