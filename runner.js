var emmet = require("./emmet/emmet.js");

function do_expand(text, syntax, profile) {
    try {
        return emmet.expandAbbreviation(text, syntax, profile) || '';
    }
    catch (e) {
        return '?';
    }
}

function do_find_expand(text, syntax, profile) {
    s = emmet.utils.action.extractAbbreviation(text);
    if (s=='') {
        return '';
    }
    res = do_expand(s, syntax, profile);
    if (res=='?') {
        return '';
    }
    return s.length.toString() + ';' + res;
}

var _mode = process.argv[2];
var _text = process.argv[3];
var _syntax = process.argv[4];
var _profile = process.argv[5];

if (_mode=="find_expand") {
    s = do_find_expand(_text, _syntax, _profile);
    process.stdout.write(s);
    return;
}

if (_mode=="expand") {
    s = do_expand(_text, _syntax, _profile);
    process.stdout.write(s);
}
