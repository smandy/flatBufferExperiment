// automatically generated by the FlatBuffers compiler, do not modify

package argo;

import java.nio.*;
import java.lang.*;
import java.util.*;
import com.google.flatbuffers.*;

@SuppressWarnings("unused")
public final class ThingList extends Table {
  public static ThingList getRootAsThingList(ByteBuffer _bb) { return getRootAsThingList(_bb, new ThingList()); }
  public static ThingList getRootAsThingList(ByteBuffer _bb, ThingList obj) { _bb.order(ByteOrder.LITTLE_ENDIAN); return (obj.__init(_bb.getInt(_bb.position()) + _bb.position(), _bb)); }
  public ThingList __init(int _i, ByteBuffer _bb) { bb_pos = _i; bb = _bb; return this; }

  public String title() { int o = __offset(4); return o != 0 ? __string(o + bb_pos) : null; }
  public ByteBuffer titleAsByteBuffer() { return __vector_as_bytebuffer(4, 1); }
  public Thing things(int j) { return things(new Thing(), j); }
  public Thing things(Thing obj, int j) { int o = __offset(6); return o != 0 ? obj.__init(__indirect(__vector(o) + j * 4), bb) : null; }
  public int thingsLength() { int o = __offset(6); return o != 0 ? __vector_len(o) : 0; }

  public static int createThingList(FlatBufferBuilder builder,
      int titleOffset,
      int thingsOffset) {
    builder.startObject(2);
    ThingList.addThings(builder, thingsOffset);
    ThingList.addTitle(builder, titleOffset);
    return ThingList.endThingList(builder);
  }

  public static void startThingList(FlatBufferBuilder builder) { builder.startObject(2); }
  public static void addTitle(FlatBufferBuilder builder, int titleOffset) { builder.addOffset(0, titleOffset, 0); }
  public static void addThings(FlatBufferBuilder builder, int thingsOffset) { builder.addOffset(1, thingsOffset, 0); }
  public static int createThingsVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, data.length, 4); for (int i = data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  public static void startThingsVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  public static int endThingList(FlatBufferBuilder builder) {
    int o = builder.endObject();
    return o;
  }
  public static void finishThingListBuffer(FlatBufferBuilder builder, int offset) { builder.finish(offset); }
};

