import struct


def read_control_file(filename):
    with open(filename, "rb") as f:
        # Read Version
        version = struct.unpack(">H", f.read(2))[0]
        print(f"Version: {version}")

        # Read EXT (Extension)
        ext = struct.unpack(">I", f.read(4))[0]
        print(f"EXT (Extension): {ext}")

        # Read Info Hash Length
        info_hash_length = struct.unpack(">I", f.read(4))[0]
        print(f"Info Hash Length: {info_hash_length}")

        # Read Info Hash
        info_hash = f.read(info_hash_length)
        print(f"Info Hash: {info_hash.hex()}")

        # Read Piece Length
        piece_length = struct.unpack(">I", f.read(4))[0]
        print(f"Piece Length: {piece_length}")

        # Read Total Length
        total_length = struct.unpack(">Q", f.read(8))[0]
        print(f"Total Length: {total_length} bytes")

        # Read Upload Length
        upload_length = struct.unpack(">Q", f.read(8))[0]
        print(f"Upload Length: {upload_length} bytes")

        # Read Bitfield Length
        bitfield_length = struct.unpack(">I", f.read(4))[0]
        print(f"Bitfield Length: {bitfield_length}")

        # Read Bitfield
        bitfield = f.read(bitfield_length)
        print(f"Bitfield: {bitfield.hex()}")

        # Calculate downloaded bytes based on bitfield
        downloaded_bytes = 0
        for byte in bitfield:
            for i in range(8):
                if byte & (1 << i):
                    downloaded_bytes += piece_length

        print(f"Downloaded Bytes: {downloaded_bytes} bytes")

        # Read Num In-Flight Piece
        num_in_flight_piece = struct.unpack(">I", f.read(4))[0]
        print(f"Num In-Flight Piece: {num_in_flight_piece}")

        # Read In-Flight Pieces
        for _ in range(num_in_flight_piece):
            index = struct.unpack(">I", f.read(4))[0]
            length = struct.unpack(">I", f.read(4))[0]
            piece_bitfield_length = struct.unpack(">I", f.read(4))[0]
            piece_bitfield = f.read(piece_bitfield_length)

            print(f"In-Flight Piece Index: {index}")
            print(f"In-Flight Piece Length: {length}")
            print(f"In-Flight Piece Bitfield Length: {piece_bitfield_length}")
            print(f"In-Flight Piece Bitfield: {piece_bitfield.hex()}")


if __name__ == "__main__":
    read_control_file("download.aria2")
