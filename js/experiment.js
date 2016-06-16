
var text2ua = function(s) {
    var ua = new Uint8Array(s.length);
    for (var i = 0; i < s.length; i++) {
        ua[i] = s.charCodeAt(i);
        //console.log( i + " is " + s.charCodeAt(i));
    }
    return ua;
};

// $.ajax( { url: "things.fb",
//           type: "GET" } )
//     .done( function( xs,b,c ) {
//         console.log( "Load was performed." );
//         console.log( "Length is " + xs.length);
//         var d = text2ua(xs);
//         var buf = new flatbuffers.ByteBuffer(d);
//         var thingList = argo.ThingList.getRootAsThingList(buf);
//         console.log("Name2 is " + thingList.title());
//         console.log( "Length2 is " + thingList.thingsLength() );
//         var i;
//         for (i = 0;i<thingList.thingsLength();++i) {
//             console.log("Name " + i + " is " + thingList.things(i).name() );
//         };
//         console.log("Woot " + thingList);
//     }).fail( function(err) {
//         console.log("Error " + err);
//     });

var ws = new WebSocket( 'ws://localhost:8889/ws');
//var ws = new WebSocket( 'ws://localhost:8889/ws');
ws.binaryType = 'arraybuffer';

ws.onopen = function() {
    console.log("Open");
    this.send("Hello");
};

ws.onmessage = function(msg) {
    console.log("Woot");
    //var decoded = JSON.parse(msg.data);
    var ary = new Uint8Array(msg.data);
    var buf = new flatbuffers.ByteBuffer(ary);
    var thingList = argo.ThingList.getRootAsThingList(buf);
    console.log("Name2 is " + thingList.title());
    console.log( "Length2 is " + thingList.thingsLength() );
    var i;
    for (i = 0;i<thingList.thingsLength();++i) {
        console.log("Name " + i + " is " + thingList.things(i).name() );
    };
    console.log("Woot " + thingList);
};
