
# n = number of dimensions = number of for loops
# m = size (in every dimensions) = loop variable maximum
def dim( n, m=None ):
  if m is None:
    m = n
  if n > 0:
    for i in range(0, m):
      dim( n-1, m )
    print "\n"
  else: # n == 0
    print ".",

# (simple) cube
print "\n-----";
dim( 0, 2 )
print "\n-----";
dim( 1, 2 )
print "\n-----";
dim( 2, 2 )
print "\n-----";
dim( 3, 2 )
print "\n-----";
dim( 4, 2 )

# double cube
print "\n-----";
dim( 0, 3 )
print "\n-----";
dim( 1, 3 )
print "\n-----";
dim( 2, 3 )
print "\n-----";
dim( 3, 3 )
print "\n-----";
dim( 4, 3 )

# n^n
print "\n-----";
dim( 1 )
print "\n-----";
dim( 2 )
print "\n-----";
dim( 3 )
print "\n-----";
dim( 4 )
print "\n-----";

