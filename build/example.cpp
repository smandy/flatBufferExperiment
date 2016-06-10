
#include "thing_generated.h"

#include <fstream>
#include <iostream>

using namespace argo;

// Example how to use FlatBuffers to create and read binary buffers.

int main(int /*argc*/, const char * /*argv*/ []) {
  flatbuffers::FlatBufferBuilder builder;

  auto barney  = CreateThing(builder, builder.CreateString("Barney") );
  auto fred = CreateThing(builder, builder.CreateString("Fred") );
  
  std::vector<flatbuffers::Offset<Thing> > sec_vector;
  sec_vector.push_back(fred);
  sec_vector.push_back(barney);
  
  auto securities = builder.CreateVector(sec_vector);
  
  auto title = builder.CreateString("flintstones");
  auto orc = CreateThingList(builder, title, securities);
  builder.Finish(orc);

  // We now have a FlatBuffer we can store on disk or send over a network.
  // ** file/network code goes here :) **
  // access builder.GetBufferPointer() for builder.GetSize() bytes
  // Instead, we're going to access it right away (as if we just received it).
  {
    std::cout << "Writing" << std::endl;
    std::ofstream ofs("../things.fb");
    ofs.write( reinterpret_cast<const char *>(builder.GetBufferPointer()), builder.GetSize());
    std::cout << "Written" << std::endl;
  };

}
