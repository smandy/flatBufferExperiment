// automatically generated by the FlatBuffers compiler, do not modify

package argo;

import java.nio.*;
import java.lang.*;
import java.util.*;
import com.google.flatbuffers.*;

@SuppressWarnings("unused")
public final class SecurityList extends Table {
  public static SecurityList getRootAsSecurityList(ByteBuffer _bb) { return getRootAsSecurityList(_bb, new SecurityList()); }
  public static SecurityList getRootAsSecurityList(ByteBuffer _bb, SecurityList obj) { _bb.order(ByteOrder.LITTLE_ENDIAN); return (obj.__init(_bb.getInt(_bb.position()) + _bb.position(), _bb)); }
  public SecurityList __init(int _i, ByteBuffer _bb) { bb_pos = _i; bb = _bb; return this; }

  public String name() { int o = __offset(4); return o != 0 ? __string(o + bb_pos) : null; }
  public ByteBuffer nameAsByteBuffer() { return __vector_as_bytebuffer(4, 1); }
  public Security securities(int j) { return securities(new Security(), j); }
  public Security securities(Security obj, int j) { int o = __offset(6); return o != 0 ? obj.__init(__indirect(__vector(o) + j * 4), bb) : null; }
  public int securitiesLength() { int o = __offset(6); return o != 0 ? __vector_len(o) : 0; }

  public static int createSecurityList(FlatBufferBuilder builder,
      int nameOffset,
      int securitiesOffset) {
    builder.startObject(2);
    SecurityList.addSecurities(builder, securitiesOffset);
    SecurityList.addName(builder, nameOffset);
    return SecurityList.endSecurityList(builder);
  }

  public static void startSecurityList(FlatBufferBuilder builder) { builder.startObject(2); }
  public static void addName(FlatBufferBuilder builder, int nameOffset) { builder.addOffset(0, nameOffset, 0); }
  public static void addSecurities(FlatBufferBuilder builder, int securitiesOffset) { builder.addOffset(1, securitiesOffset, 0); }
  public static int createSecuritiesVector(FlatBufferBuilder builder, int[] data) { builder.startVector(4, data.length, 4); for (int i = data.length - 1; i >= 0; i--) builder.addOffset(data[i]); return builder.endVector(); }
  public static void startSecuritiesVector(FlatBufferBuilder builder, int numElems) { builder.startVector(4, numElems, 4); }
  public static int endSecurityList(FlatBufferBuilder builder) {
    int o = builder.endObject();
    return o;
  }
  public static void finishSecurityListBuffer(FlatBufferBuilder builder, int offset) { builder.finish(offset); }
};

