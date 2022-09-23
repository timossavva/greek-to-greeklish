function toGreeklish(text) {
    let grCaps = stringToSet('ΑΆΒΓΔΕΈΖΗΉΘΙΊΪΚΛΜΝΞΟΌΠΡΣΤΥΎΫΦΧΨΩΏ'),
        replacements = [
            {greek: 'αι', greeklish: 'ai'},
            {greek: 'αί', greeklish: 'ai'},
            {greek: 'οι', greeklish: 'oi'},
            {greek: 'οί', greeklish: 'oi'},
            {greek: 'ου', greeklish: 'ou'},
            {greek: 'ού', greeklish: 'ou'},
            {greek: 'ει', greeklish: 'ei'},
            {greek: 'εί', greeklish: 'ei'},
            {greek: 'αυ', fivi: 1},
            {greek: 'αύ', fivi: 1},
            {greek: 'ευ', fivi: 1},
            {greek: 'εύ', fivi: 1},
            {greek: 'ηυ', fivi: 1},
            {greek: 'ηύ', fivi: 1},
            {greek: 'ντ', greeklish: 'nt'},
            {greek: 'μπ', bi: 1},
            {greek: 'τσ', greeklish: 'ts'},
            {greek: 'τς', greeklish: 'ts'},
            {greek: 'ΤΣ', greeklish: 'ts'},
            {greek: 'τζ', greeklish: 'tz'},
            {greek: 'γγ', greeklish: 'ng'},
            {greek: 'γκ', greeklish: 'gk'},
            {greek: 'θ', greeklish: 'th'},
            {greek: 'χ', greeklish: 'ch'},
            {greek: 'ψ', greeklish: 'ps'},
        ];

    // Remove extraneous array element
    if (!replacements[replacements.length - 1]) replacements.pop();

    // Enhance replacements
    for (let i = 0, replacement; replacement = replacements[i]; i++) {
        replacements[replacement.greek] = replacement;
    }

    // Append single letter replacements
    let grLetters = 'αάβγδεέζηήθιίϊΐκλμνξοόπρσςτυύϋΰφχψωώ',
        engLetters = 'aavgdeezii.iiiiklmnxooprsstyyyyf..oo';
    for (let i = 0; i < grLetters.length; i++) {
        if (!replacements[grLetters.charAt(i)]) {
            replacements.push({greek: grLetters.charAt(i), greeklish: engLetters.charAt(i)})
        }
    }
    // Enhance replacements, build expression
    let expression = [];
    for (let i = 0, replacement; replacement = replacements[i]; i++) {
        replacements[replacement.greek] = replacement;
        expression[i] = replacement.greek;
    }

    expression = new RegExp(expression.join('|'), 'gi');
    // Replace greek with greeklish.
    let greekSet = stringToSet(grLetters),
        viSet = stringToSet('αβγδεζηλιmμνορω');
    text = text.replace(expression, function ($0, index) {
        let replacement = replacements[$0.toLowerCase()];
        if (replacement.bi) {
            let bi = (greekSet[text.charAt(index - 1).toLowerCase()] && greekSet[text.charAt(index + 2).toLowerCase()]) ? 'mp' : 'b';
            return fixCase(bi, $0);
        } else if (replacement.fivi) {
            let c1 = replacements[$0.charAt(0).toLowerCase()].greeklish,
                c2 = viSet[text.charAt(index + 2).toLowerCase()] ? 'v' : 'f';
            return fixCase(c1 + c2, $0);
        } else {
            return fixCase(replacement.greeklish, $0 + text.charAt(index + $0.length));
        }
    })
    return text;

    function fixCase(text, mirror) {
        if (grCaps[mirror.charAt(0)]) {
            if (mirror.length == 1 || grCaps[mirror.charAt(1)]) {
                return text.toUpperCase();
            } else {
                return text.charAt(0).toUpperCase() + text.substr(1);
            }
        } else {
            return text;
        }
    }

    function stringToSet(s) {
        let o = {};
        for (let i = 0; i < s.length; i++) {
            o[s.charAt(i)] = 1;
        }
        return o;
    }
}