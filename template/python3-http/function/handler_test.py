from handler import handle
from handler_types import Event, Context

# Test your handler here

# To disable testing, you can set the build_arg `TEST_ENABLED=false` on the CLI or in your stack.yml
# https://docs.openfaas.com/reference/yaml/#function-build-args-build-args


def test_handle() -> None:
    # assert handle(Event(b'', '', '', '', ''), Context('', 200, '', '')).statusCode == 200
    pass
