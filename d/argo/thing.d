// automatically generated, do not modify

module argo.thing;

import std.typecons;
import flatbuffers;

struct Thing {
  mixin Table!Thing;

  static Thing getRootAsThing(ByteBuffer _bb) { return getRootAsThing(_bb, Thing()); }
  static Thing getRootAsThing(ByteBuffer _bb, Thing obj) { return (obj.__init(_bb.getInt(_bb.position()) + _bb.position(), _bb)); }
  Thing __init(int _i, ByteBuffer _bb) { bb_pos = _i; bb = _bb; return this; }

  Nullable!string name() { int o = __offset(4); return o != 0 ? Nullable!string(__string(o + bb_pos)) : Nullable!string(); }

  static int createThing(FlatBufferBuilder builder,
      int name = 0) {
    builder.startObject(1);
    Thing.addName(builder, name);
    return Thing.endThing(builder);
  }

  static void startThing(FlatBufferBuilder builder) { builder.startObject(1); }
  static void addName(FlatBufferBuilder builder, int nameOffset) { builder.addOffset(0, nameOffset, 0); }
  static int endThing(FlatBufferBuilder builder) {
    int o = builder.endObject();
    return o;
  }
}

