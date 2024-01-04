const CryptoJS = require('./crypto-js');
function v(t) {
    return function (t, e) {
        d.includes(e) && (y.error = !0);
        e = e.startsWith("/") ? "".concat(t).concat(e) : "".concat(t, "/").concat(e);
        return e
    }(function () {
        if (window.location.host.startsWith("localhost") || window.location.host.startsWith("127."))
            return h;
        return ""
    }(), t)
}
function t() {
    !function (t, e) {
        if (!(t instanceof e))
            throw new TypeError("Cannot call a class as a function")
    }(this, t)
}
function g() {
    return !0
}
function _u_e(t) {
    if (null == t)
        return null;
    t = t.replace(/\r\n/g, "\n");
    for (var e = "", r = 0; r < t.length; r++) {
        var n = t.charCodeAt(r);
        n < 128 ? e += String.fromCharCode(n) : n > 127 && n < 2048 ? (e += String.fromCharCode(n >> 6 | 192),
            e += String.fromCharCode(63 & n | 128)) : (e += String.fromCharCode(n >> 12 | 224),
                e += String.fromCharCode(n >> 6 & 63 | 128),
                e += String.fromCharCode(63 & n | 128))
    }
    return e
}
var n = 1;
var _keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
    , _p = "W5D80NFZHAYB8EUI2T649RT2MNRMVE2O";
var t = ",7WB:d`ym{1L$'=n";
function e1(t) {
    if (null == t)
        return null;
    for (var e, r, n, o, i, a, c, u = "", s = 0; s < t.length;)
        o = (e = t.charCodeAt(s++)) >> 2,
            i = (3 & e) << 4 | (r = t.charCodeAt(s++)) >> 4,
            a = (15 & r) << 2 | (n = t.charCodeAt(s++)) >> 6,
            c = 63 & n,
            isNaN(r) ? a = c = 64 : isNaN(n) && (c = 64),
            u = u + _keyStr.charAt(o) + _keyStr.charAt(i) + _keyStr.charAt(a) + _keyStr.charAt(c);
    return u
}
function e2(t) {
    if (null == (t = _u_e(t)))
        return null;
    for (var e = "", r = 0; r < t.length; r++) {
        var n = _p.charCodeAt(r % _p.length);
        e += String.fromCharCode(t.charCodeAt(r) ^ n)
    }
    return e
}
function sig(t) {
    // return md5(t + _p).toUpperCase()
    return CryptoJS.MD5(t + _p).toString().toUpperCase()
}
function n(t, e, r) {
    ("production".startsWith("next") || "production".startsWith("dev")) && (r > 500 ? console.log("========== ".concat(r, " ===========")) : console.log("".concat(r)))
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

var aa = function (e, r, o) {
    e = "/api2/service/x_service/person_industry_list/list_industries_by_sort";
    var i = !1;
    (e.indexOf("/api2/service/x_service/system_") >= 0 || e.indexOf("/api/company") >= 0 || e.indexOf("/api/search/deal") >= 0) && (i = !0,
        n = null);
    console.log(r)
    var s = JSON.stringify(r)
        , l = JSON.parse(s);
    if (!i) {
        if (g()) {
            null == n && (n = 1);
            const payloadObj = new e1();
            const payloadStr = JSON.stringify(l.payload);
            const result = new e2(payloadStr);
            var f = result;
            let result1 = sig(t); // 假设sig(t)返回一个函数
            l.payload = f,
                l.sig = p
        } else
            null == n && (n = -20180620);
        l.v = Number(n)
    }
    var h = new Date;
    Date.now();
    // (function () {
        var C = 1904
        var w = "visibilityState"
        var A = "hidden"

        function a() {
            clearTimeout(C);
            var b;
            w && (b = "visible" == 'visible');
            A && (b = !false);
            l = "undefined" == typeof b ? t : b;
            g = true
            r = true
            l = true
            p = true
            m = +new Date;
            // if ((!g || !r) && l && p)
            //     v = t,
            //     m = +new Date;
            // else if (g && r && (!l || !p))
            //     v = x,
            //     q += +new Date - m;
            g = true;
            r = true;
            C = setTimeout(a, 100)
        }
        function e() {
            return function () {
                h.b.a.et = 3;
                h.b.a.ep = h.T.Va() + "," + h.T.Ra();
                h.b.a.hca = c.hca;
                h.b.m()
            }
        }
        function m(a) {
            return new Date;
        }
    // })();
    return a(e, m(1)).then(function (t) {
        return t.json()
    }).then(function (n) {
        if (i)
            return b(n.code),
                n;
        if (g()) {
            var a, s = n.v, l = n.d;
            if (2 === s) {
                var f = new B
                    , p = f.d1(l);
                a = f.d2(p)
            } else if (1 === s) {
                var d = d1(l)
                    , y = d2(d)
                    , v = JSON.parse(y);
                "function" == typeof o && o(v),
                    a = v
            } else
                a = n;
            var m = (new Date).getTime() - h.getTime();
            return n(e, r, m),
                t.error || b(a.code),
                a
        }
        t.error || b(n.code);
        Date.now();
        return n
    }).catch(function (t) {
        return {
            code: -999
        }
    })
}

aa('/api2/service/x_service/person_industry_list/list_industries_by_sort', '{"sort":1,"start":20,"limit":20}');
// console.log(e1(t));
// const payloadObj = new e1();
// const payloadStr = JSON.stringify(l.payload);
// const result = new e2(payloadStr);
// console.log(result);