#!/usr/bin/rdmd --shebang -I/home/andy/repos/d_flatbuffers/d/source

import argo;

import std.file;
import std.stdio;
import flatbuffers : ByteBuffer;

void main() {
    auto buf = cast(ubyte[]) read("../things.fb");
    writefln("Buf is %s", buf.length);
    auto f = ThingList.getRootAsThingList( new ByteBuffer( buf ));
    writefln("title is " , f.title());
    writefln("Length is %s" , f.thingsLength());
    writefln("Title is %s", f.title());
    auto things = f.things();
    foreach( t ; things) {
        writefln("t is %s" , t.name());
    };
};
