from command import *
from game import Game


def test_command_parse():
    assert Command.parse("NONE:").type == CommandType.NONE
    assert Command.parse("HELLO:").type == CommandType.HELLO
    assert Command.parse("STATE:").type == CommandType.STATE
    assert Command.parse("WAIT:").type == CommandType.WAIT
    assert Command.parse("STEP:").type == CommandType.STEP
    assert Command.parse("PING:").type == CommandType.PING


def test_command_construct():
    assert Command().type == CommandType.NONE
    assert HelloCommand().type == CommandType.HELLO
    assert GameStateCommand(Game()).type == CommandType.STATE
    assert WaitCommand().type == CommandType.WAIT
    assert StepCommand().type == CommandType.STEP
    assert PingCommand().type == CommandType.PING
