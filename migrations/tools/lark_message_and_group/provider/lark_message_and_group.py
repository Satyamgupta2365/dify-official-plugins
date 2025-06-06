from dify_plugin import ToolProvider
from core.tools.utils.lark_api_utils import lark_auth


class LarkMessageAndGroupProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict) -> None:
        lark_auth(credentials)
