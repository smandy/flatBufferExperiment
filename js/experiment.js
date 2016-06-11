$.get( "things.fb" , function( xs ) {
    console.log( "Load was performed." );
    console.log( "Length is " + xs.length);
    //var d = new Uint8Array(xs, 0, xs.length);
    var buf = new flatbuffers.ByteBuffer(xs);
    //var sec = new argo.Security();
    var thingList = argo.ThingList.getRootAsThingList(buf);

    console.log("Name2 is " + thingList.title());
    
    console.log( "Length2 is " + thingList.thingsLength() );
    
    var i;
    for (i = 0;i<thingList.thingsLength();++i) {
        var thing = thingList.things(i);
        console.log("Ric is " + thing.name);
    };
    console.log("Woot " + thingList);
} ).fail( function(err) {
    console.log("Failed");
});
