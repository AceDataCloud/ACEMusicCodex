import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PluginContract(unittest.TestCase):
    def test_service_and_credential_binding(self):
        manifest = json.loads((ROOT / ".codex-plugin/plugin.json").read_text())
        market = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text())
        entry, = market["plugins"]
        self.assertEqual(entry["name"], manifest["name"])
        config = json.loads((ROOT / manifest["mcpServers"]).read_text())
        server = config["mcpServers"]["acemusic"]
        self.assertEqual(server["bearer_token_env_var"], "ACEDATACLOUD_API_TOKEN")
        self.assertEqual(server['url'], "https://acemusic.mcp.acedata.cloud/mcp")

        names = server['enabled_tools']
        self.assertEqual(set(names), {"acemusic_" + name for name in (
            "list_models", "get_capabilities", "generate_music", "generate_custom_music",
            "generate_lyrics", "upload_audio", "cover_audio", "mashup_audio", "get_task",
            "get_tasks_batch", "list_tasks",
        )})
