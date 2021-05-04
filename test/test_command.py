from command import *
from game import Game


def test_command_parse_none():
    assert Command.parse("NONE:").type == CommandType.NONE


def test_command_parse_hello():
    assert Command.parse("HELLO:").type == CommandType.HELLO


def test_command_parse_state():
    assert Command.parse("STATE:").type == CommandType.STATE


def test_command_parse_wait():
    assert Command.parse("WAIT:").type == CommandType.WAIT


def test_command_parse_step():
    assert Command.parse("STEP:").type == CommandType.STEP


def test_command_parse_ping():
    assert Command.parse("PING:").type == CommandType.PING


def test_command_construct_none():
    assert Command().type == CommandType.NONE


def test_command_construct_hello():
    assert HelloCommand().type == CommandType.HELLO


def test_command_construct_state():
    assert GameStateCommand(Game()).type == CommandType.STATE


def test_command_construct_wait():
    assert WaitCommand().type == CommandType.WAIT


def test_command_construct_step():
    assert StepCommand().type == CommandType.STEP


def test_command_construct_ping():
    assert PingCommand().type == CommandType.PING
