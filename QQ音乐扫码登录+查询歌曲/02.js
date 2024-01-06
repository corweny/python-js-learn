var cheng;
window = global;
document = {}
location = {
    "ancestorOrigins": {},
    "href": "https://y.qq.com/n/ryqq/search?w=%E4%BA%BA%E5%95%8A",
    "origin": "https://y.qq.com",
    "protocol": "https:",
    "host": "y.qq.com",
    "hostname": "y.qq.com",
    "port": "",
    "pathname": "/n/ryqq/search",
    "search": "?w=%E4%BA%BA%E5%95%8A",
    "hash": ""
}
navigator = {
    appCodeName: "Mozilla",
    appName: "Netscape",
    appVersion: "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    userAgent:"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}
navigation = {

    currentEntry: {
        id: "57041d94-1c57-4739-9da8-4593c98704e9",
        index: 4,
        key: "7d6c13d7-458e-4888-a702-796fd4cf22f3",
        ondispose: null,
        sameDocument: true,
        url: "https://y.qq.com/n/ryqq/search?w=%E4%BA%BA%E5%95%8A"
    }
}
require('./01')
!function (e) {
    function t(t) {
        for (var n, a, f = t[0], c = t[1], i = t[2], l = 0, b = []; l < f.length; l++)
            a = f[l],
                Object.prototype.hasOwnProperty.call(o, a) && o[a] && b.push(o[a][0]),
                o[a] = 0;
        for (n in c)
            Object.prototype.hasOwnProperty.call(c, n) && (e[n] = c[n]);
        for (u && u(t); b.length;)
            b.shift()();
        return d.push.apply(d, i || []),
            r()
    }
    function r() {
        for (var e, t = 0; t < d.length; t++) {
            for (var r = d[t], n = !0, a = 1; a < r.length; a++) {
                var c = r[a];
                0 !== o[c] && (n = !1)
            }
            n && (d.splice(t--, 1),
                e = f(f.s = r[0]))
        }
        return e
    }
    var n = {}
        , a = {
            20: 0
        }
        , o = {
            20: 0
        }
        , d = [];
    function f(t) {
        if (n[t])
            return n[t].exports;
        var r = n[t] = {
            i: t,
            l: !1,
            exports: {}
        };
        return e[t].call(r.exports, r, r.exports, f),
            r.l = !0,
            r.exports
    }
    f.e = function (e) {
        var t = [];
        a[e] ? t.push(a[e]) : 0 !== a[e] && {
            1: 1,
            3: 1,
            4: 1,
            5: 1,
            6: 1,
            7: 1,
            8: 1,
            9: 1,
            10: 1,
            11: 1,
            12: 1,
            13: 1,
            14: 1,
            15: 1,
            16: 1,
            17: 1,
            18: 1,
            19: 1,
            21: 1,
            22: 1,
            23: 1,
            24: 1,
            25: 1
        }[e] && t.push(a[e] = new Promise((function (t, r) {
            for (var n = "css/" + ({
                1: "common",
                3: "album",
                4: "albumDetail",
                5: "album_mall",
                6: "category",
                7: "cmtpage",
                8: "index",
                9: "msg_center",
                10: "mv",
                11: "mvList",
                12: "mv_toplist",
                13: "notfound",
                14: "player",
                15: "player_radio",
                16: "playlist",
                17: "playlist_edit",
                18: "profile",
                19: "radio",
                21: "search",
                22: "singer",
                23: "singer_list",
                24: "songDetail",
                25: "toplist"
            }[e] || e) + "." + {
                1: "2e3d715e72682303d35b",
                3: "5cf0d69eaf29bcab23d2",
                4: "798353db5b0eb05d5358",
                5: "df4c243f917604263e58",
                6: "20d532d798099a44bc88",
                7: "e3bedf2b5810f8db0684",
                8: "ea0adb959fef9011fc25",
                9: "020422608fe8bfb1719a",
                10: "8bdb1df6c5436b790baa",
                11: "47ce9300786df1b70584",
                12: "4aee33230ba2d6b81dce",
                13: "e6f63b0cf57dd029fbd6",
                14: "1d2dbefbea113438324a",
                15: "d893492de07ce97d8048",
                16: "9484fde660fe93d9f9f0",
                17: "67fb85e7f96455763c83",
                18: "5e8c651e74b13244f7cf",
                19: "3befd83c10b19893ec66",
                21: "b2d11f89ea6a512a2302",
                22: "c7a38353c5f4ebb47491",
                23: "df0961952a2d3f022894",
                24: "4c080567e394fd45608b",
                25: "8edb142553f97482e00f"
            }[e] + ".chunk.css?max_age=2592000", o = f.p + n, d = document.getElementsByTagName("link"), c = 0; c < d.length; c++) {
                var i = (u = d[c]).getAttribute("data-href") || u.getAttribute("href");
                if ("stylesheet" === u.rel && (i === n || i === o))
                    return t()
            }
            var l = document.getElementsByTagName("style");
            for (c = 0; c < l.length; c++) {
                var u;
                if ((i = (u = l[c]).getAttribute("data-href")) === n || i === o)
                    return t()
            }
            var b = document.createElement("link");
            b.rel = "stylesheet",
                b.type = "text/css",
                b.onload = t,
                b.onerror = function (t) {
                    var n = t && t.target && t.target.src || o
                        , d = new Error("Loading CSS chunk " + e + " failed.\n(" + n + ")");
                    d.code = "CSS_CHUNK_LOAD_FAILED",
                        d.request = n,
                        delete a[e],
                        b.parentNode.removeChild(b),
                        r(d)
                }
                ,
                b.href = o,
                0 !== b.href.indexOf(window.location.origin + "/") && (b.crossOrigin = "anonymous"),
                document.getElementsByTagName("head")[0].appendChild(b)
        }
        )).then((function () {
            a[e] = 0
        }
        )));
        var r = o[e];
        if (0 !== r)
            if (r)
                t.push(r[2]);
            else {
                var n = new Promise((function (t, n) {
                    r = o[e] = [t, n]
                }
                ));
                t.push(r[2] = n);
                var d, c = document.createElement("script");
                c.charset = "utf-8",
                    c.timeout = 120,
                    f.nc && c.setAttribute("nonce", f.nc),
                    c.src = function (e) {
                        return f.p + "js/" + ({
                            1: "common",
                            3: "album",
                            4: "albumDetail",
                            5: "album_mall",
                            6: "category",
                            7: "cmtpage",
                            8: "index",
                            9: "msg_center",
                            10: "mv",
                            11: "mvList",
                            12: "mv_toplist",
                            13: "notfound",
                            14: "player",
                            15: "player_radio",
                            16: "playlist",
                            17: "playlist_edit",
                            18: "profile",
                            19: "radio",
                            21: "search",
                            22: "singer",
                            23: "singer_list",
                            24: "songDetail",
                            25: "toplist"
                        }[e] || e) + ".chunk." + {
                            1: "980f2070e7573755d59c",
                            3: "6f355307b2cd93d84763",
                            4: "fa75412685d138dcee03",
                            5: "ba904bcfb557caf1e2d5",
                            6: "f6698bcdfe688972088b",
                            7: "9163bde468afbb8d391d",
                            8: "9982204a0cc5e3c91c08",
                            9: "d0a14e5e1117e13d5fdb",
                            10: "b1b11110edb8763c18b8",
                            11: "ebcbc289f8de994bead2",
                            12: "f9c874d47d9bf469977f",
                            13: "e0d4e37a3bc8d2858707",
                            14: "59d55f320606138bce79",
                            15: "fe70d872eae2f4f00170",
                            16: "3de74dd547c7a2651f27",
                            17: "a0bab70e9cfcd1d8a344",
                            18: "801a044c8ea659ae2e8c",
                            19: "ed7e91726ce90f0711eb",
                            21: "85caee30f1963ce0fa97",
                            22: "50f54c7a599df2216aed",
                            23: "195d10ae915dea5fe9d8",
                            24: "4ec2b0002905ee3f5f02",
                            25: "854d3dd0bf0eb2a4f78b"
                        }[e] + ".js?max_age=2592000"
                    }(e),
                    0 !== c.src.indexOf(window.location.origin + "/") && (c.crossOrigin = "anonymous");
                var i = new Error;
                d = function (t) {
                    c.onerror = c.onload = null,
                        clearTimeout(l);
                    var r = o[e];
                    if (0 !== r) {
                        if (r) {
                            var n = t && ("load" === t.type ? "missing" : t.type)
                                , a = t && t.target && t.target.src;
                            i.message = "Loading chunk " + e + " failed.\n(" + n + ": " + a + ")",
                                i.name = "ChunkLoadError",
                                i.type = n,
                                i.request = a,
                                r[1](i)
                        }
                        o[e] = void 0
                    }
                }
                    ;
                var l = setTimeout((function () {
                    d({
                        type: "timeout",
                        target: c
                    })
                }
                ), 12e4);
                c.onerror = c.onload = d,
                    document.head.appendChild(c)
            }
        return Promise.all(t)
    }
        ,
        f.m = e,
        f.c = n,
        f.d = function (e, t, r) {
            f.o(e, t) || Object.defineProperty(e, t, {
                enumerable: !0,
                get: r
            })
        }
        ,
        f.r = function (e) {
            "undefined" !== typeof Symbol && Symbol.toStringTag && Object.defineProperty(e, Symbol.toStringTag, {
                value: "Module"
            }),
                Object.defineProperty(e, "__esModule", {
                    value: !0
                })
        }
        ,
        f.t = function (e, t) {
            if (1 & t && (e = f(e)),
                8 & t)
                return e;
            if (4 & t && "object" === typeof e && e && e.__esModule)
                return e;
            var r = Object.create(null);
            if (f.r(r),
                Object.defineProperty(r, "default", {
                    enumerable: !0,
                    value: e
                }),
                2 & t && "string" != typeof e)
                for (var n in e)
                    f.d(r, n, function (t) {
                        return e[t]
                    }
                        .bind(null, n));
            return r
        }
        ,
        f.n = function (e) {
            var t = e && e.__esModule ? function () {
                return e.default
            }
                : function () {
                    return e
                }
                ;
            return f.d(t, "a", t),
                t
        }
        ,
        f.o = function (e, t) {
            return Object.prototype.hasOwnProperty.call(e, t)
        }
        ,
        f.p = "/ryqq/",
        f.oe = function (e) {
            throw e
        }
        ;
    var c = window.webpackJsonp = window.webpackJsonp || []
        , i = c.push.bind(c);
    c.push = t,
        c = c.slice();
    for (var l = 0; l < c.length; l++)
        t(c[l]);
    var u = i;
    r()
    cheng = f;
}([]);

function main(data) {

    i = cheng(351).default;
    return i(data)

}