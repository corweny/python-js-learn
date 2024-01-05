const CryptoJS = require('./crypto-js')


function txEfS(_0x4b232d, _0x216d43) {
    return _0x4b232d / _0x216d43;
}

function rBJcW(_0x30580b, _0x2ca935) {
    return txEfS(_0x30580b, _0x2ca935);
}
function getResCode() {
    var _0x57da4f = CryptoJS['AES']['encrypt'](CryptoJS['enc']['Utf8']['parse'](Math['floor'](rBJcW(new Date()['getTime'](), 1000))), CryptoJS['enc']['Utf8']['parse'](1234567887654321 || 1234567887654321), {
        'iv': CryptoJS['enc']['Utf8']['parse'](1234567887654321),
        'mode': CryptoJS['mode']['CBC'],
        'padding': CryptoJS['pad']['Pkcs7']
    });
    return CryptoJS['enc']['Base64']['stringify'](_0x57da4f['ciphertext']);
}