

var assert = require('assert');
var fs = require('fs');

var flatbuffers = require('../js/flatbuffers').flatbuffers;
var argo = require('./thing_generated').argo;

console.log("Woot");

var f = fs.readFileSync( "../things.fb");

console.log("F is " + f );

var d = new Uint8Array(f);
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


