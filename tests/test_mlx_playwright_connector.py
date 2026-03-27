import pytest
import asyncio
from enterprise_modules.mlx_playwright_connector import launch_stealth_browser

@pytest.mark.asyncio
async def test_launch_stealth_browser(monkeypatch):
    async def fake_launch(proxy):
        assert proxy == "user:pass@1.2.3.4:1080"
        return True
    monkeypatch.setattr('enterprise_modules.mlx_playwright_connector.launch_stealth_browser', fake_launch)
    await launch_stealth_browser("user:pass@1.2.3.4:1080")
