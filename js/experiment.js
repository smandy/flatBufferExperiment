$.get( "things.fb" , function( xs ) {
    console.log( "Load was performed." );
    console.log( "Length is " + xs.length);
    //var d = new Uint8Array(xs, 0, xs.length);
    var buf = new flatbuffers.ByteBuffer(xs);
    //var sec = new argo.Security();
    var thingList = argo.ThingList.getRootAsSecurityList(buf);

    console.log("Name is " + thingList.name());
    
    console.log( "Length is " + thingList.securitiesLength() );
    
    var i;
    for (i = 0;i<thingList.securitiesLength();++i) {
        var sec = thingList.securities(i,sec);
        console.log("Ric is " + sec.ric() + " ticker is " + sec.ticker() );
    };
    console.log("Woot " + thingList);
} ).fail( function(err) {
    console.log("Failed")
});
