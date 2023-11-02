import struct
import sys
from typing import BinaryIO

def read_short(file: BinaryIO) -> int:
    """Read 2 bytes from the file and return as a short integer."""
    return struct.unpack(">H", file.read(2))[0]

def read_int(file: BinaryIO) -> int:
    """Read 4 bytes from the file and return as an integer."""
    return struct.unpack(">I", file.read(4))[0]

def read_long(file: BinaryIO) -> int:
    """Read 8 bytes from the file and return as a long integer."""
    return struct.unpack(">Q", file.read(8))[0]

def read_bytes(file: BinaryIO, length: int) -> bytes:
    """Read 'length' bytes from the file."""
    return file.read(length)

def read_control_file(filename: str) -> None:
    """
    Read and parse a binary control file.

    Parameters:
        filename (str): The name of the file to read.
    """
    try:
        with open(filename, "rb") as f:
            print(f"Version: {read_short(f)}")
            print(f"EXT (Extension): {read_int(f)}")
            info_hash_length = read_int(f)
            print(f"Info Hash Length: {info_hash_length}")
            print(f"Info Hash: {read_bytes(f, info_hash_length).hex()}")
            piece_length = read_int(f)
            print(f"Piece Length: {piece_length}")
            print(f"Total Length: {read_long(f)} bytes")
            print(f"Upload Length: {read_long(f)} bytes")
            bitfield_length = read_int(f)
            print(f"Bitfield Length: {bitfield_length}")
            print(f"Bitfield: {read_bytes(f, bitfield_length).hex()}")

            # Additional logic (e.g., calculating downloaded bytes) can go here.

    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    except struct.error:
        print("Error: Unexpected end of file or unpacking error.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main() -> None:
    """Main function to execute the script."""
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        read_control_file(filename)
    else:
        print("Usage: python script.py <filename>")

if __name__ == "__main__":
    main()
