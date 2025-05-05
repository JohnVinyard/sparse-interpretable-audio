Most widely-used modern audio codecs, such as Ogg Vorbis and MP3, as well as more recent “neural” codecs like Meta’s Encodec or Descript’s are based on block-coding; audio is divided into overlapping, fixed-size “frames” which are then compressed. While they can result in excellent reproduction quality and can be used for downstream tasks such
as text-to-audio, they do not produce an intuitive, directly-interpretable
representation. In this work, we introduce a proof-of-concept audio
encoder that represents audio as a sparse set of events and their times-of-
occurrence. Rudimentary physics-based assumptions are used to model
attack and the physical resonance of both the instrument being played
and the room in which a performance occurs, hopefully encouraging a
sparse, parsimonious, and easy-to-interpret representation.





Most widely-used modern audio codecs, such as Ogg Vorbis and MP3, as well as more recent "neural" codecs like Meta's Encodec or the Descript codec are based on block-coding;  audio is divided into overlapping, fixed-size "frames" which are then compressed.  While they can result in excellent reproduction quality and impressive compression rates, they do not produce an intuitive representation that is directly interpretable or easy to manipulate.  In this work, we introduce a proof-of-concept audio encoder that represents audio as a sparse set of events and their times-of-occurrence.  The encoder works in an iterative fashion, removing information at each step, akin to the matching pursuit algorithm.  Rudimentary physics-based assumptions are used in the decoder, modeling attack and the physical resonances of instruments and rooms, hopefully encouraging a sparse, parsimonious and easy-to-interpret representation.