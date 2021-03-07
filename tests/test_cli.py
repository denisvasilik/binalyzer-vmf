import pytest
import os

from click.testing import CliRunner

from binalyzer import Template, TemplateAutoCompletion, cli

TESTS_ABS_PATH = os.path.dirname(os.path.abspath(__file__))


def test_vmf_without_arguments():
    result = CliRunner().invoke(cli, ["vmf"])

    assert (
        result.output
        == 'Usage: binalyzer vmf [OPTIONS]\nTry "binalyzer vmf --help" for help.\n\n'
           'Error: Missing option "--input-file" / "-i".\n'
    )
    assert result.exit_code == 2


def test_vmf_help():
    result = CliRunner().invoke(cli, ["vmf", "--help"])
    assert (
        result.output
        == 'Usage: binalyzer vmf [OPTIONS]\n\n  Convert a binary file to a VMF '
           'file.\n\nOptions:\n  -i, --input-file FILENAME   The binary file to '
           'convert.  [required]\n  -o, --output-file FILENAME  The VMF file to '
           'create.  [required]\n  -s, --start-offset INTEGER  Specifes the start '
           'offset  [default: 0x00]\n  --help                      Show this '
           'message and exit.\n'
    )
    assert result.exit_code == 0


def test_vmf_missing_input_file():
    result = CliRunner().invoke(
        cli, ["vmf", "--input-file", "resources/WasmFpgaModule.wasm"])
    assert(
        result.output ==
        'Usage: binalyzer vmf [OPTIONS]\nTry "binalyzer vmf --help" for help.\n\n'
        'Error: Missing option "--output-file" / "-o".\n'
    )
    assert result.exit_code == 2


def test_vmf_default_offset():
    result = CliRunner().invoke(cli, [
        "vmf",
        "--input-file",
        "resources/WasmFpgaModule.wasm",
        "--output-file",
        "/tmp/WasmFpgaModule.vmf",
    ])
    assert result.output == ""
    assert result.exit_code == 0


def test_vmf_offset_hex():
    result = CliRunner().invoke(cli, [
        "vmf",
        "--input-file",
        "resources/WasmFpgaModule.wasm",
        "--output-file",
        "/tmp/WasmFpgaModule.vmf",
        "--start-offset",
        "0x300000",
    ])
    assert result.output == ""
    assert result.exit_code == 0


def test_vmf_offset_decimal():
    result = CliRunner().invoke(cli, [
        "vmf",
        "--input-file",
        "resources/WasmFpgaModule.wasm",
        "--output-file",
        "/tmp/WasmFpgaModule.vmf",
        "--start-offset",
        "256",
    ])
    assert result.output == ""
    assert result.exit_code == 0
