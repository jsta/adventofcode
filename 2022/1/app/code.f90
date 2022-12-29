program example_loadtxt
   use stdlib_io, only: loadtxt
   implicit none
   real, allocatable :: x(:, :)
   call loadtxt('input', x)
   print *, x
end program example_loadtxt
