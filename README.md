# DuplicateRemoval
最近在携程碰到了一个大文件的去重问题。
从数据库里拿出了近两年半的酒店的订单数据，但这个表居然没有主键！
前面的机票订单数据是按orderID作为主键的，并且不重复记录。酒店没
有主键且数据重复，按partitions拿出来分成了七个文件，每个大概10G左右，八千万条记录。
每个文件本身不含重复记录，但是任意两个文本之间大量记录重复。（后来去重的时候也得到验证）
一开始想按orderID直接作为hash来做，但是该类型是8*2^64byte太大，内存开不了。
后来再想就是分治法去做，整个的文本来做hash不行，就只拿其中的一部分进来。
所有的文本按照orderID的大小分块，若记录重复则是在orderID相同大小的块中重复，不同的orderID块是不会有重复记录的