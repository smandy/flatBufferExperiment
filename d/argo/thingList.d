// automatically generated, do not modify

module argo.thingList;

import std.typecons;
import flatbuffers;

import argo.thing;

struct ThingList {
  mixin Table!ThingList;

  static ThingList getRootAsThingList(ByteBuffer _bb) { return getRootAsThingList(_bb, ThingList()); }
  static ThingList getRootAsThingList(ByteBuffer _bb, ThingList obj) { return (obj.__init(_bb.getInt(_bb.position()) + _bb.position(), _bb)); }
  ThingList __init(int _i, ByteBuffer _bb) { bb_pos = _i; bb = _bb; return this; }

  Nullable!string title() { int o = __offset(4); return o != 0 ? Nullable!string(__string(o + bb_pos)) : Nullable!string(); }
  auto things() { return FlatBufferIterator!(ThingList, Thing, "things")(this); }
  Nullable!Thing things(int j) { return things(Thing(), j); }
  Nullable!Thing things(Thing obj, int j) { int o = __offset(6); return o != 0 ? Nullable!Thing(obj.__init(__indirect(__dvector(o) + j * 4), bb)) : Nullable!Thing(); }
  int thingsLength() { int o = __offset(6); return o != 0 ? __vector_len(o) : 0; }

  static int createThingList(FlatBufferBuilder builder,
      int title = 0,
      int things = 0) {
    builder.startObject(2);
    ThingList.addThings(builder, things);
    ThingList.addTitle(builder, title);
    return ThingList.endThingList(builder);
  }

  static void startThingList(FlatBufferBuilder builder) { builder.startObject(2); }
  static void addTitle(FlatBufferBuilder builder, int titleOffset) { builder.addOffset(0, titleOffset, 0); }
  static void addThings(FlatBufferBuilder builder, int thingsOffset) { builder.addOffset(1, thingsOffset, 0); }
  static int createThingsVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, cast(int)data.length, 4); for (int i = cast(int)data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  static void startThingsVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  static int endThingList(FlatBufferBuilder builder) {
    int o = builder.endObject();
    return o;
  }
  static void finishThingListBuffer(FlatBufferBuilder builder, int offset) { builder.finish(offset); }
}

