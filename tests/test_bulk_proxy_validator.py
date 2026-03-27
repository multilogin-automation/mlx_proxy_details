import pytest
import asyncio
from enterprise_modules.bulk_proxy_validator import validate_proxies

@pytest.mark.asyncio
async def test_validate_proxies_all_invalid():
    proxies = ["invalid:proxy@0.0.0.0:1234"] * 5
    valid, invalid = await validate_proxies(proxies, concurrency=5)
    assert len(valid) == 0
    assert len(invalid) == 5

@pytest.mark.asyncio
async def test_validate_proxies_mixed(monkeypatch):
    async def fake_check_proxy(session, proxy):
        return proxy, proxy.endswith('good:1080')
    import enterprise_modules.bulk_proxy_validator as bpv
    monkeypatch.setattr(bpv, 'check_proxy', fake_check_proxy)
    proxies = ["user:pass@1.2.3.4:good:1080", "user:pass@5.6.7.8:bad:1080"]
    valid, invalid = await validate_proxies(proxies, concurrency=2)
    assert len(valid) == 1
    assert len(invalid) == 1
