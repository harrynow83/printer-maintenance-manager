import time
from moonraker.components.printer_maintenance_manager import (
    PrinterMaintenanceManager
)

class MockServer:
    def register_endpoint(self, *args, **kwargs): pass
    def register_event_handler(self, *args, **kwargs): pass

class MockConfig:
    def get_server(self):
        return MockServer()
    def get_name(self):
        return "test_printer"

def test_plugin_loads():
    config = MockConfig()
    plugin = PrinterMaintenanceManager(config)
    assert plugin is not None

def test_print_time_tracking(tmp_path, monkeypatch):
    from moonraker.components import printer_maintenance_manager as pmm

    monkeypatch.setattr(pmm, "DB_PATH", tmp_path / "test.db")

    config = MockConfig()
    plugin = PrinterMaintenanceManager(config)

    plugin.on_print_start()
    time.sleep(1)
    plugin.on_print_end()

    stats = plugin.handle_get(None)
    assert stats["print_hours"] > 0
