var emmet = require("./emmet/emmet.js");

function do_extract(text) {
    return emmet.utils.action.extractAbbreviation(text);
}

function do_expand(text, syntax, profile) {
    try {
        return emmet.expandAbbreviation(text, syntax, profile) || '';
    }
    catch (e) {
        return '?';
    }
}

var _mode = process.argv[2];
var _text = process.argv[3];

if (_mode=="extract") {
    _text = do_extract(_text);
    process.stdout.write(_text);
}

if (_mode=="expand") {
    var _syntax = process.argv[4];
    var _profile = process.argv[5];
    _text = do_expand(_text, _syntax, _profile);
    process.stdout.write(_text);
}
