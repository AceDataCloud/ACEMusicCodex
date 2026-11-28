# ACE Music for Codex

[简体中文](readme/README_zh_Hans.md)

Create ACE Music songs and lyrics, upload reference audio, cover one owned track, blend two, and retrieve the original task. This Codex integration connects to the [hosted ACE Music MCP](https://platform.acedata.cloud/documents/mcp-acemusic?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=acemusiccodex_readme_tool_reference). You can use the plugin independently of other music integrations.

## Install

```sh
codex plugin marketplace add AceDataCloud/ACEMusicCodex --ref v0.1.1
codex plugin add ace-music@acedatacloud-ace-music
```

Set `ACEDATACLOUD_API_TOKEN` in the environment of the Codex process using your secret manager and start a fresh session. The plugin reads the variable when connecting to the MCP. Get a general or service API key with ACE Music access from [Applications](https://platform.acedata.cloud/console/applications?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=acemusiccodex_readme_api_key). Enter the raw key through the client configuration. Keep it out of prompts and repositories.

## First use

Ask “List the ACE Music models and capabilities.” This only reads service information. To make a song, describe the idea or provide the title, lyrics and style. A successful song task returns two candidates. Uploading a reference and generating lyrics are separate billable actions. For a cover, supply one owned audio ID; for a mashup, two different compatible IDs. Keep the returned task ID and query it after reconnecting. [Pricing](https://platform.acedata.cloud/services/acemusic?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=acemusiccodex_readme_pricing) · [MCP tool reference](https://platform.acedata.cloud/documents/mcp-acemusic?utm_source=github&utm_medium=referral&utm_campaign=evergreen&utm_content=acemusiccodex_readme_tool_reference)
