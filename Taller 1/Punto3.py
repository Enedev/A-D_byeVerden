F zigzag(n)
   F compare(xy)
      V (x, y) = xy
      R (x + y, I (x + y) % 2 {-y} E y)
   V xs = 0 .< n
   R Dict(enumerate(sorted((multiloop(xs, xs, (x, y) -> (x, y))), key' compare)), (n, index) -> (index, n))

F printzz(myarray)
   V n = Int(myarray.len ^ 0.5 + 0.5)
   V xs = 0 .< n
   print((xs.map(y -> @xs.map(x -> ‘#3’.format(@@myarray[(x, @y)])).join(‘’))).join("\n"))

printzz(zigzag(6))