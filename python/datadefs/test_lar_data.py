__author__ = 'matthias'

import lar_data as ld

filename = "../data/testdata.root"


data = ld.LarData(filename)

data.read_laser()
data.read_hits()

print data.get_laser(1)
print data.get_hits(1)
print data.n_entries