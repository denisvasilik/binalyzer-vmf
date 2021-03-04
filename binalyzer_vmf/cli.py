"""
    binalyzer_vmf.cli
    ~~~~~~~~~~~~~~~~~

    CLI extension for the *binalyzer* command.
"""
import click
import io

from binalyzer import (
    Binalyzer,
    ExpandedFile,
    BasedIntParamType,
)


@click.command()
@click.option('--input-file', '-i', type=ExpandedFile("rb"), help='The binary file to convert.')
@click.option('--output-file', '-o', type=ExpandedFile("wb"), help='The VMF file to create.')
@click.option('--start-offset', '-s', type=BasedIntParamType(), help='The VMF file to create.')
def vmf(input_file, output_file, start_offset):
    """Convert a binary file to a VMF file.
    """
    binalyzer = Binalyzer(data=input_file)

    print(f"@{start_offset:06X}")
    for data_byte in binalyzer.template.value:
        print(f"{data_byte:02X}")