## How to run:

Assembly code is based on linux x86 and has to be emulated on mac / arm.

I use this docker command: 

`
docker run --rm --platform linux/amd64 -v $(pwd):/code -w /code ubuntu \
  bash -c "apt update && apt install -y nasm build-essential && nasm -f elf64 assembly.s -o assembly.o && ld assembly.o -o assembly && ./assembly"
`
