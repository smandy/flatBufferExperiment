# automatically generated by the FlatBuffers compiler, do not modify

# namespace: argo

import flatbuffers

class Thing(object):
    __slots__ = ['_tab']

    # Thing
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Thing
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return ""

def ThingStart(builder): builder.StartObject(1)
def ThingAddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def ThingEnd(builder): return builder.EndObject()
