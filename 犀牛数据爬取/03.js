var _keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    , _p = "W5D80NFZHAYB8EUI2T649RT2MNRMVE2O";
function _u_d(t) {
    for (var e = "", r = 0, n = 0, o = 0, i = 0; r < t.length;)
        (n = t.charCodeAt(r)) < 128 ? (e += String.fromCharCode(n),
            r++) : n > 191 && n < 224 ? (o = t.charCodeAt(r + 1),
                e += String.fromCharCode((31 & n) << 6 | 63 & o),
                r += 2) : (o = t.charCodeAt(r + 1),
                    i = t.charCodeAt(r + 2),
                    e += String.fromCharCode((15 & n) << 12 | (63 & o) << 6 | 63 & i),
                    r += 3);
    return e
}
function d1(t) {
    var e, r, n, o, i, a, c = "", u = 0;
    for (t = t.replace(/[^A-Za-z0-9\+\/\=]/g, ""); u < t.length;)
        e = _keyStr.indexOf(t.charAt(u++)) << 2 | (o = _keyStr.indexOf(t.charAt(u++))) >> 4,
            r = (15 & o) << 4 | (i = _keyStr.indexOf(t.charAt(u++))) >> 2,
            n = (3 & i) << 6 | (a = _keyStr.indexOf(t.charAt(u++))),
            c += String.fromCharCode(e),
            64 != i && (c += String.fromCharCode(r)),
            64 != a && (c += String.fromCharCode(n));
    return c
}
function d2(t) {
    for (var e = "", r = 0; r < t.length; r++) {
        var n = _p.charCodeAt(r % _p.length);
        e += String.fromCharCode(t.charCodeAt(r) ^ n)
    }
    return e = _u_d(e)
}

function decode1(l) {
    var a = d2(d1(l))
    return {
        "a": a,
    }
}
function a(s){
    return s
}