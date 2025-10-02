## How to run:

this task is made to be run inside of docker:

```bash
docker run --rm --platform linux/amd64 -v $(pwd):/code -w /code ubuntu \
bash -c "apt update && apt install -y build-essential && \
gcc -fPIC -shared a_function.c more_functions.c -o libfunctions.so && \
gcc -L. -o c_example main.c -lfunctions && \
LD_LIBRARY_PATH=. ./c_example"
```

### Testing dynamic libs

If you want to test dynamic library functionality, you can run:

```bash
docker run --rm -it --platform linux/amd64 -v $(pwd):/code -w /code ubuntu bash
```

You can then install dependencies and tweak the code inside a docker ubuntu image:

```bash
apt update && apt install -y build-essential nano
```

Build the dynamic library:

```bash
gcc -fPIC -shared a_function.c more_functions.c -o libfunctions.so
```

Build the executable

```bash
gcc -L. -o c_example main.c -lfunctions
```

Run the executable

```bash
LD_LIBRARY_PATH=. ./c_example
```

Change `another_function` in `more_functions.c` to `another_functon` to have a spelling mistake:

```bash
nano more_functions.c
```

Rebuild the dynamic library

```bash
gcc -fPIC -shared a_function.c more_functions.c -o libfunctions.so
```

Rerun the executable without building it:

```bash
LD_LIBRARY_PATH=. ./c_example
```

You now get an error as dynamic libraries are imported runtime. If you revert this change and rebuild the dynamic library, it will run as expected.
