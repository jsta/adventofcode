program example_loadtxt
   use stdlib_io, only: loadtxt
   implicit none

   ! INTEGER, PARAMETER                :: M = 10, N = 2000
   ! REAL, DIMENSION(0:N-1)            :: vector
   ! LOGICAL, DIMENSION(M)             :: idx

   real, allocatable  :: x(:, :)
   real, dimension(0:10)  :: x_sub
   integer            :: j
   integer :: t
   integer, dimension(1)             :: j_max
   integer, dimension(0:1) :: gap_locs
   integer, dimension(1) :: gap_loc

   call loadtxt('input_small', x)
   !    print *, x
   !    print *, sum(x)
   ! print *, x(2,:)

   ! vector(:) = 0
   ! idx(1:) = (/ (x(j,:) == 0, j=1,10)/)
   ! print *, idx
   ! print *, size(vector)

   ! get gap location
   gap_locs = 0
   gap_locs = findloc(x, 0)
   gap_loc = gap_locs(0)
   print *, gap_loc
   ! print *, gap_locs

   ! print *, gap_loc - 1
   j_max = gap_loc-1
   ! print *, j_max

   do j=1, j_max(1)
      ! print *, j
      ! print *, x(j,1)
      x_sub(j) = x(j,1)
   enddo

   print *, sum(x_sub)

   ! print *, x
   ! print *, x(gap_loc-1,:)
   ! print *, sum(x(gap_loc-1,:))

end program example_loadtxt
