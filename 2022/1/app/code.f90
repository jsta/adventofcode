module procedures
   implicit none

contains

end module procedures

program example_loadtxt
   use stdlib_io, only: loadtxt
   implicit none

   real, allocatable       :: x(:, :)
   real, dimension(0:40)   :: x_sub
   real, dimension(1:2)    :: res
   integer                 :: i
   integer                 :: j
   integer, dimension(1)   :: k
   integer, dimension(1)   :: j_max
   integer, dimension(0:1) :: test
   integer, dimension(0:1) :: gap_locs
   integer, dimension(1)   :: gap_loc

   call loadtxt('input_small', x)

   ! initial calculation
   i = 1
   gap_locs = findloc(x, 0)
   gap_loc = gap_locs(0)
   j_max = gap_loc-1
   k(1) = 1
   do j=k(1), j_max(1)
      x_sub(j) = x(j,1)
   enddo
   res(i) = sum(x_sub, dim=1)
   print *, res(i)


   ! start iteration
   ! do while (all(findloc(x,0) /= 0))
   i = i + 1

   k = gap_loc + 1
   gap_locs = findloc(x(k(1):,1:), 0)
   gap_loc = gap_locs(0)
   j_max = k+gap_loc-2
   do j=k(1), j_max(1)
      x_sub(j) = x(j,1)
   enddo
   res(i) = sum(x_sub, dim=1)
   ! print *, x_sub
   print *, res


   ! print *, k
   ! print *, j_max(1)


   ! ---

   ! print *, x
   ! print *, x(gap_loc-1,:)
   ! print *, sum(x(gap_loc-1,:))

   ! k = gap_loc+1
   ! print *, k
   ! ! print *, x(k,1:)

end program example_loadtxt
