
var text2ua = function(s) {
    var ua = new Uint8Array(s.length);
    for (var i = 0; i < s.length; i++) {
        ua[i] = s.charCodeAt(i);
    }
    return ua;
};

$.ajax( { url: "things.fb",
          type: "GET" } )
    .done( function( xs,b,c ) {
        console.log( "Load was performed." );
        console.log( "Length is " + xs.length);
        var d = text2ua(xs);
        var buf = new flatbuffers.ByteBuffer(d);
        var thingList = argo.ThingList.getRootAsThingList(buf);
        console.log("Name2 is " + thingList.title());
        console.log( "Length2 is " + thingList.thingsLength() );
        var t = new argo.Thing();
        var i;
        for (i = 0;i<thingList.thingsLength();i++) {
            thingList.things(i, t);
            console.log("Name " + i + " is " + t.name() );
        };
        console.log("Woot " + thingList);
    } ).fail( function(err) {
        console.log("Error " + err);
    });

