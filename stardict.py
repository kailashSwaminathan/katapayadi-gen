import os
import gzip
import struct

class StarDictReader(object):
    """ Class to reader StarDict format dictionary.
    """
    def __init__(self, dirpath):
        self._words = {}
        self._fdict = None
        for root, dirs, files in os.walk(dirpath):
            for f in files:
                filename = os.path.join(dirpath,f)
                ext = os.path.splitext(f)[1]
                if ext == '.idx':
                    self._read_idx(filename)
                elif ext == '.syn':
                    pass
                elif ext == '.ifo':
                    pass
                elif ext == '.dz':
                    if f.endswith('.dict.dz'):
                        self._fdict = gzip.open(filename,'rb')
                else:
                    pass
            break

    def _read_idx(self, fname):
        """ The .idx contains the word and offset (4 bytes)
            and length(4 bytes) of the entry in the .dict file.
        """
        with open(fname, 'rb') as fidx:
            w = b''
            while ch := fidx.read(1):
                if ch == b'\x00': # Denotes end of a word
                    offset = struct.unpack('>L', fidx.read(4))[0]
                    entrylen = struct.unpack('>L',fidx.read(4))[0]
                    #offset = fidx.read(4)
                    #entrylen = fidx.read(4)
                    nw = w.decode('utf-8')                    
                    if nw in self._words:
                        self._words[nw].append((offset, entrylen))
                    else:
                        self._words[nw] = [(offset, entrylen)]
                    w = b''
                else:
                    w += ch
                    
    def get_meaning(self, w):
        """ Read the dictionary entry for 
            word
        """
        if not self._fdict:
            print('Error: Missing *.dict.dz file')
            return
        if w not in self._words:
            print('Word now found in the dictionary')
            return
        # For a word with many (offset, length)
        # pairs, use the first offset and sum of
        # all the length(s)
        offset, length = -1, 0
        for o,l in self._words[w]:
            offset = o if offset == -1 else offset
            length += l
        print(offset, length)
        self._fdict.seek(offset, 0)
        m = self._fdict.read(length)
        return m.decode('utf-8')
        
if __name__ == "__main__":
    sd = StarDictReader('D:\\kailash\\courses\\iisc\\202008\\compThinkIndic\\project\\dict\\apte-1890')
