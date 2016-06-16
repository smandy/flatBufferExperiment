var assert = require('assert');
var fs = require('fs');

var flatbuffers = require('../js/flatbuffers').flatbuffers;
var argo = require('./thing_generated').argo;

console.log("Woot");

var f = fs.readFileSync( "../things.fb");

console.log("F is " + f );
console.log("F is " + typeof f );

var d = new Uint8Array(f);
console.log("Length of f is " + f.length);

var j;
for (j = 0;j<f.length;++j) {
    console.log( j + " is " + f[j]);
};

var buf = new flatbuffers.ByteBuffer(d);
var thingList = argo.ThingList.getRootAsThingList(buf);

console.log("ThingList is " + thingList);
console.log("Title is " + thingList.title());
console.log( "Length is " + thingList.thingsLength() );

var i;

for (i = 0;i<thingList.thingsLength();++i) {
    console.log("thing is " + thingList.things(i));
    console.log( thingList.things(i).name('utf-8') );
};


