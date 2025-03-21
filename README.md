# Test Model Component

This is a small stub of FORTRAN code which is used to simulate a model component for testing purposes.

## Compilation

### Spack compilation

Follow instructions to set up to use the [ACCESS-NRI spack configuration](https://access-hive.org.au/getting_started/spack/).

Install using spack:
```bash
spack install access-test-component %intel@2021.10.0
```
In this case the compiler and version are specified, but they can be changed.

### Direct compilation

On `gadi` this can be compiled like so

```bash
module load openmpi/4.1.7
module load intel-compiler/2021.10.0 

cd stub && CMAKE_PREFIX_PATH=/apps/openmpi/4.1.7/include/Intel cmake . && make
```

Note that `CMAKE_PREFIX_PATH` is specified in the `spack-config` so this is required to be specified explicitly to mimic what is done when built inside `spack`.

## Sample Run

### Spack

```bash
$ spack load access-test-component
$ mpirun -n 6 $(which hello_world.exe)
 Hello World from process:            1 of            6
 Hello World from process:            2 of            6
 Hello World from process:            3 of            6
 Hello World from process:            4 of            6
 Hello World from process:            5 of            6
 Hello World from process:            0 of            6
```

### Direct
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

