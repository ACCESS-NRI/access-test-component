# Test Model Component

This is a small stub of FORTRAN code which is used to simulate a model component for testing purposes.

## Compilation

On `gadi` this can be compiled like so

```bash
module load openmpi
FC=mpif90 ccmake -B build
FC=mpif90 cmake --build build
```

## Sample Run

```bash
$ mpirun -n 6 build/hello_world.exe 
 Hello World from process:            0 of            6
 Hello World from process:            1 of            6
 Hello World from process:            2 of            6
 Hello World from process:            3 of            6
 Hello World from process:            4 of            6
 Hello World from process:            5 of            6
$
```

